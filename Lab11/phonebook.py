import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="1234"
    )

def setup_db():
    ddl = """
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        phone VARCHAR(15) NOT NULL
    );

    CREATE OR REPLACE FUNCTION search_by_pattern(p_pattern TEXT)
    RETURNS TABLE(id INT, username TEXT, phone TEXT)
    LANGUAGE plpgsql AS $$
    BEGIN
        RETURN QUERY
        SELECT pb.id, pb.username::TEXT, pb.phone::TEXT
          FROM PhoneBook AS pb
         WHERE pb.username ILIKE '%' || p_pattern || '%'
            OR pb.phone    ILIKE '%' || p_pattern || '%';
    END;
    $$;

    CREATE OR REPLACE PROCEDURE insert_or_update_user(p_username TEXT, p_phone TEXT)
    LANGUAGE plpgsql AS $$
    BEGIN
        IF EXISTS (SELECT 1 FROM PhoneBook WHERE username = p_username) THEN
            UPDATE PhoneBook
               SET phone = p_phone
             WHERE username = p_username;
        ELSE
            INSERT INTO PhoneBook(username, phone)
                 VALUES(p_username, p_phone);
        END IF;
    END;
    $$;

    CREATE OR REPLACE PROCEDURE delete_by_user_or_phone(p_username TEXT, p_phone TEXT)
    LANGUAGE plpgsql AS $$
    BEGIN
        DELETE FROM PhoneBook
         WHERE (p_username IS NULL OR username = p_username)
           AND (p_phone    IS NULL OR phone    = p_phone);
    END;
    $$;
    """
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(ddl)
        conn.commit()
    print("✅ Таблица и все функции/процедуры готовы в базе.")

def insert_csv(path):
    with connect() as conn:
        with conn.cursor() as cur:
            with open(path, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 2:
                        cur.execute(
                            "INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)",
                            (row[0], row[1])
                        )
        conn.commit()
    print("Данные из CSV загружены.")

def query_users():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM PhoneBook ORDER BY id;")
            users = cur.fetchall()
    print("\nСписок всех контактов:")
    for row in users:
        print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    print()

def delete_user():
    name = input("Введите имя пользователя для удаления (или оставьте пустым): ")
    phone = input("Введите номер телефона пользователя для удаления (или оставьте пустым): ")
    
    with connect() as conn:
        with conn.cursor() as cur:
            if name and phone:
                cur.execute("DELETE FROM PhoneBook WHERE username = %s AND phone = %s;", (name, phone))
            elif name:
                cur.execute("DELETE FROM PhoneBook WHERE username = %s;", (name,))
            elif phone:
                cur.execute("DELETE FROM PhoneBook WHERE phone = %s;", (phone,))
            else:
                print("Ошибка: необходимо указать либо имя, либо номер телефона.")
                return
        conn.commit()
    
    print("Пользователь удалён (если был найден).")

def delete_all():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM PhoneBook;")
        conn.commit()
    print("База очищена.")

def search_by_pattern():
    pat = input("Введите шаблон для поиска (часть имени или телефона): ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_by_pattern(%s);", (pat,))
            rows = cur.fetchall()
    print("\nРезультаты поиска:")
    if not rows:
        print("  Ничего не найдено.")
    else:
        for r in rows:
            print(f"  ID: {r[0]}, Имя: {r[1]}, Телефон: {r[2]}")
    print()

def insert_or_update_user_proc():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
        conn.commit()
    print("Процедура выполнена: пользователь вставлен или обновлён.")

def insert_list():
    raw = input("Введите контакты (например: Анна 12345, Иван 67890): ")
    pairs = [entry.strip() for entry in raw.split(",")]
    contacts = []
    for pair in pairs:
        parts = pair.split()
        if len(parts) >= 2:
            name = parts[0]
            phone = " ".join(parts[1:])
            contacts.append((name, phone))
        else:
            print(f"⚠️ Пропущена пара: '{pair}' (некорректный формат)")
    with connect() as conn:
        with conn.cursor() as cur:
            for name, phone in contacts:
                cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
        conn.commit()
    print("✅ Все контакты добавлены или обновлены.")

def get_paginated_users():
    limit  = int(input("Введите limit: "))
    offset = int(input("Введите offset: "))
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM PhoneBook ORDER BY id LIMIT %s OFFSET %s;", (limit, offset))
            rows = cur.fetchall()
    print(f"\nЗаписи (offset={offset}, limit={limit}):")
    for r in rows:
        print(f"  ID: {r[0]}, Имя: {r[1]}, Телефон: {r[2]}")
    print()

def menu():
    setup_db()
    while True:
        print("""
--- Меню ---
1. Загрузить контакты из CSV
2. Показать всех пользователей
3. Удалить пользователя
4. Очистить базу
5. Поиск по шаблону
6. Вставка/обновление одного (процедура)
7. Вставка списка контактов (вручную)
8. Постраничный вывод
0. Выход
""")
        choice = input("Выберите действие: ").strip()
        if   choice == "1": insert_csv(input("Путь к CSV: "))
        elif choice == "2": query_users()
        elif choice == "3": delete_user()
        elif choice == "4": delete_all()
        elif choice == "5": search_by_pattern()
        elif choice == "6": insert_or_update_user_proc()
        elif choice == "7": insert_list()
        elif choice == "8": get_paginated_users()
        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Неверный выбор, попробуйте ещё раз.")

if __name__ == "__main__":
    menu()
