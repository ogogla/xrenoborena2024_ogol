import pygame
import sys
import subprocess  # Импортируем модуль для запуска других скриптов

# Инициализация pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 1400, 793
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BioStudy")

# Загрузка изображений
bg = pygame.image.load("background.png")
button_map_img = pygame.image.load("button_map.png")
next_img = pygame.image.load("next.png")
prev_img = pygame.image.load("prev.png")
play_img = pygame.image.load("play.png")
all_schemes_img = pygame.image.load("all_schemes.png")
settings_img = pygame.image.load("settings.png")
statistics_img = pygame.image.load("statistics.png")
bar_img = pygame.image.load("bar.png")
medal_img = pygame.image.load("medal.png")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Шрифт
font = pygame.font.Font(None, 36)


# Функции для кнопок
def open_map():
    print("Открыть карту")
    # Запуск файла map_cell.py
    subprocess.Popen([sys.executable, "map_cell.py"])


def next_map():
    print("Следующая карта")


def prev_map():
    print("Предыдущая карта")


def play_menu():
    subprocess.Popen([sys.executable, "play_cell.py"])


def schemes():
    print("Все схемы")


def settings():
    print("Настройки")


def statistics():
    print("Статистика")


# Класс для кнопок
class Button:
    def __init__(self, x, y, image, action):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.action = action

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()


# Создание кнопок
buttons = [
    Button(428, 221, button_map_img, open_map),
    Button(998.5, 370.8, next_img, next_map),
    Button(351, 370.8, prev_img, prev_map),
    Button(546, 643, play_img, play_menu),
    Button(55, 643, all_schemes_img, schemes),
    Button(1261.3, 47.4, settings_img, settings),
    Button(1256.9, 234.3, statistics_img, statistics),
]

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                for button in buttons:
                    button.check_click(event.pos)

    # Отрисовка фона
    screen.blit(bg, (0, 0))

    # Отрисовка кнопок
    for button in buttons:
        button.draw(screen)

    # Отрисовка шкалы опыта
    screen.blit(bar_img, (462, 47.4))
    screen.blit(medal_img, (451.8, 38.5))

    # Отрисовка прогресс-бара
    pygame.draw.rect(screen, GRAY, (515, 60, 370, 20))
    pygame.draw.rect(screen, BLACK, (515, 60, 370 * 0.2, 20))  # 20% заполненности

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
sys.exit()
