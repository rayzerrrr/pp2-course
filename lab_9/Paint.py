import pygame
import math

pygame.init()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GFG Paint")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

screen.fill(WHITE)

# Кнопки выбора цветов
COLOR_BUTTONS = [
    {"color": RED, "rect": pygame.Rect(10, 10, 50, 50)},
    {"color": YELLOW, "rect": pygame.Rect(70, 10, 50, 50)},
    {"color": GREEN, "rect": pygame.Rect(130, 10, 50, 50)},
    {"color": BLUE, "rect": pygame.Rect(190, 10, 50, 50)},
    {"color": BLACK, "rect": pygame.Rect(250, 10, 50, 50)}
]

# Загрузка изображения ластика
eraser_img = pygame.image.load('Lab9/picandsound/eraser.png')
eraser_img = pygame.transform.scale(eraser_img, (50, 50))

# Кнопки выбора фигур с изображениями
TOOLS = [
    {"name": "Линия", "rect": pygame.Rect(320, 10, 60, 60), "type": "pencil", "shape": "line"},
    {"name": "Прямоугольник", "rect": pygame.Rect(380, 10, 60, 60), "type": "rectangle", "shape": "rectangle"},
    {"name": "Круг", "rect": pygame.Rect(440, 10, 60, 60), "type": "circle", "shape": "circle"},
    {"name": "Квадрат", "rect": pygame.Rect(500, 10, 60, 60), "type": "square", "shape": "square"},
    {"name": "Прямоуг. треугольник", "rect": pygame.Rect(560, 10, 60, 60), "type": "right_triangle", "shape": "right_triangle"},
    {"name": "Равносторонний треугольник", "rect": pygame.Rect(620, 10, 60, 60), "type": "equilateral_triangle", "shape": "equilateral_triangle"},
    {"name": "Ромб", "rect": pygame.Rect(680, 10, 60, 60), "type": "rhombus", "shape": "rhombus"}
]

# Кнопка выбора ластика
eraser_button = pygame.Rect(740, 10, 50, 50)

# Текущие настройки
current_color = BLACK
current_tool = "pencil"
drawing = False
start_pos = None
last_pos = None

# Оригинальные функции для рисования
def draw_pencil(surface, color, start, end, width=3):
    pygame.draw.line(surface, color, start, end, width)

def draw_rectangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    pygame.draw.rect(surface, color, (min(x1, x2), min(y1, y2), width, height), 3)

def draw_circle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    radius = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    pygame.draw.circle(surface, color, start, radius, 3)

def draw_square(surface, color, start, end):
    """Рисует квадрат, основываясь на координатах двух противоположных углов"""
    side_length = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    pygame.draw.rect(surface, color, (start[0], start[1], side_length, side_length), 3)

def draw_right_triangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.polygon(surface, color, [(x1, y1), (x1, y2), (x2, y2)], 3)

def draw_equilateral_triangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    side = abs(x2 - x1)
    h = (math.sqrt(3) / 2) * side
    pygame.draw.polygon(surface, color, [(x1, y2), (x1 + side, y2), (x1 + side / 2, y2 - h)], 3)


def draw_rhombus(surface, color, start, end):
    """Рисует ромб"""
    x1, y1 = start
    x2, y2 = end
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    points = [(x1, center_y), (center_x, y1), (x2, center_y), (center_x, y2)]
    pygame.draw.polygon(surface, color, points, 3)

def erase_area(surface, position):
    pygame.draw.circle(surface, WHITE, position, 20)

# Функция для рисования фигур внутри кнопок
def draw_tool_buttons():
    for button in TOOLS:
        pygame.draw.rect(screen, BLACK, button["rect"], 2)
        if button["shape"] == "line":
            pygame.draw.line(screen, BLACK, (button["rect"].x + 5, button["rect"].y + 30), 
                             (button["rect"].x + button["rect"].width - 5, button["rect"].y + 30), 3)
        elif button["shape"] == "rectangle":
            pygame.draw.rect(screen, BLACK, (button["rect"].x + 5, button["rect"].y + 5, 
                                             button["rect"].width - 10, button["rect"].height - 10), 3)
        elif button["shape"] == "circle":
            pygame.draw.circle(screen, BLACK, (button["rect"].x + button["rect"].width // 2, 
                                               button["rect"].y + button["rect"].height // 2), 25, 3)
        elif button["shape"] == "square":
            pygame.draw.rect(screen, BLACK, (button["rect"].x + 5, button["rect"].y + 5, 
                                             button["rect"].width - 10, button["rect"].width - 10), 3)
        elif button["shape"] == "right_triangle":
            pygame.draw.polygon(screen, BLACK, [(button["rect"].x + 5, button["rect"].y + button["rect"].height - 5),
                                               (button["rect"].x + button["rect"].width - 5, button["rect"].y + button["rect"].height - 5),
                                               (button["rect"].x + 5, button["rect"].y + 5)], 3)
        elif button["shape"] == "equilateral_triangle":
            pygame.draw.polygon(screen, BLACK, [(button["rect"].x + 5, button["rect"].y + button["rect"].height - 5),
                                               (button["rect"].x + button["rect"].width - 5, button["rect"].y + button["rect"].height - 5),
                                               (button["rect"].x + button["rect"].width // 2, button["rect"].y + 5)], 3)
        elif button["shape"] == "rhombus":
            pygame.draw.polygon(screen, BLACK, [(button["rect"].x + 5, button["rect"].y + button["rect"].height // 2),
                                               (button["rect"].x + button["rect"].width // 2, button["rect"].y + 5),
                                               (button["rect"].x + button["rect"].width - 5, button["rect"].y + button["rect"].height // 2),
                                               (button["rect"].x + button["rect"].width // 2, button["rect"].y + button["rect"].height - 5)], 3)

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка клика мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # ЛКМ
                # Проверяем кнопки инструментов
                for button in TOOLS:
                    if button["rect"].collidepoint(event.pos):
                        current_tool = button["type"]

                # Проверяем кнопку ластика
                if eraser_button.collidepoint(event.pos):
                    current_tool = "eraser"

                # Проверяем кнопки цветов
                for button in COLOR_BUTTONS:
                    if button["rect"].collidepoint(event.pos):
                        current_color = button["color"]

                start_pos = event.pos
                last_pos = event.pos
                drawing = True

        # Отпускание кнопки мыши
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # ЛКМ
                drawing = False
                end_pos = event.pos
                if start_pos and end_pos:
                    if current_tool == "rectangle":
                        draw_rectangle(screen, current_color, start_pos, end_pos)
                    elif current_tool == "circle":
                        draw_circle(screen, current_color, start_pos, end_pos)
                    elif current_tool == "square":
                        draw_square(screen, current_color, start_pos, end_pos)
                    elif current_tool == "right_triangle":
                        draw_right_triangle(screen, current_color, start_pos, end_pos)
                    elif current_tool == "equilateral_triangle":
                        draw_equilateral_triangle(screen, current_color, start_pos, end_pos)
                    elif current_tool == "rhombus":
                        draw_rhombus(screen, current_color, start_pos, end_pos)

        # Движение мыши для рисования
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if current_tool == "pencil":
                    draw_pencil(screen, current_color, last_pos, event.pos, 3)
                    last_pos = event.pos  # Обновляем последнюю позицию
                elif current_tool == "eraser":
                    erase_area(screen, event.pos)

    # Рисуем кнопки цветов
    for button in COLOR_BUTTONS:
        pygame.draw.rect(screen, button["color"], button["rect"])

    # Рисуем кнопки инструментов с фигурами
    draw_tool_buttons()

    # Кнопка ластика
    pygame.draw.rect(screen, BLACK, eraser_button, 2)
    screen.blit(eraser_img, (eraser_button.x, eraser_button.y))

    pygame.display.flip()

pygame.quit()
