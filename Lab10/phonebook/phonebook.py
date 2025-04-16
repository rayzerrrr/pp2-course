import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="1234"
    )

def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS PhoneBook (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) NOT NULL,
                    phone VARCHAR(15) NOT NULL
                );
            """)

def insert_console():
    username = input("Введите имя: ")
    phone = input("Введите телефон: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)", (username, phone))
    print("Контакт добавлен.")

def insert_csv(path):
    with connect() as conn:
        with conn.cursor() as cur:
            with open(path, newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    cur.execute("INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
    print("Данные из CSV загружены.")

def update_user():
    name = input("Введите имя пользователя для обновления: ")
    new_phone = input("Введите новый номер телефона: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE PhoneBook SET phone = %s WHERE username = %s", (new_phone, name))
    print("Телефон обновлён.")

def query_users():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM PhoneBook")
            users = cur.fetchall()
            print("\nСписок всех контактов:")
            for row in users:
                print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
            print()

def delete_user():
    name = input("Введите имя пользователя для удаления: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM PhoneBook WHERE username = %s", (name,))
    print("Пользователь удалён (если был найден).")

def delete_all():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM PhoneBook")
    print("База очищена")

def menu():
    create_table()
    while True:
        print("\n--- Меню ---")
        print("1. Добавить контакт вручную")
        print("2. Загрузить контакты из CSV")
        print("3. Обновить номер телефона")
        print("4. Показать всех пользователей")
        print("5. Удалить пользователя")
        print("6. Очистить базу ")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            insert_console()
        elif choice == "2":
            path = input("Введите путь к CSV-файлу ")
            insert_csv(path)
        elif choice == "3":
            update_user()
        elif choice == "4":
            query_users()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            delete_all()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    menu()
