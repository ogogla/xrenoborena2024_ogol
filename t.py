import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("15 кнопок с уникальными изображениями")

# Список названий изображений
image_names = [
    "плазм_мембрана.png", "хлоропласты.png", "рибосомы.png", "вакуоль.png",
    "цитоплазма.png", "плазмодесма.png", "гольджи.png", "ГЭР.png", "оболочка.png",
    "ядрышко.png", "ГлЭР.png", "ядро.png", "стенка.png", "лизосомы.png", "митохондрии.png"
]

# Загрузка изображений и создание кнопок
buttons = []
for i, name in enumerate(image_names):
    try:
        # Загрузка изображения
        image = pygame.image.load(name).convert_alpha()
        # Случайное положение кнопки
        x = 0
        y = 0
        rect = image.get_rect(topleft=(x, y))
        # Создание маски для кнопки
        mask = pygame.mask.from_surface(image)
        # Добавление кнопки в список
        buttons.append({"image": image, "rect": rect, "mask": mask, "name": name[:-4]})  # Убираем расширение .png
    except FileNotFoundError:
        print(f"Ошибка: файл {name} не найден. Убедитесь, что он находится в той же директории, что и скрипт.")

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                # Проверяем кнопки в порядке их отрисовки (сверху вниз)
                for button in reversed(buttons):
                    x, y = event.pos[0] - button["rect"].x, event.pos[1] - button["rect"].y
                    # Проверяем, попал ли клик в область кнопки
                    if 0 <= x < button["rect"].width and 0 <= y < button["rect"].height:
                        if button["mask"].get_at((x, y)):
                            print(f"Нажата {button['name']}")
                            break  # Прекращаем проверку, если кнопка нажата

    # Отрисовка кнопок
    screen.fill((255, 255, 255))  # Белый фон
    for button in buttons:
        screen.blit(button["image"], button["rect"])
    pygame.display.flip()

# Завершение работы
pygame.quit()
sys.exit()