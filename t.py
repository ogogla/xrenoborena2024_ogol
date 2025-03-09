import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("15 кнопок с прозрачным фоном")

# Загрузка изображения кнопки (предположим, что у всех кнопок одинаковое изображение)
button_image = pygame.image.load("button.png").convert_alpha()

# Создание списка кнопок
buttons = []
for i in range(15):
    # Случайное положение кнопки
    x = random.randint(0, screen_width - button_image.get_width())
    y = random.randint(0, screen_height - button_image.get_height())
    rect = button_image.get_rect(topleft=(x, y))
    # Создание маски для кнопки
    mask = pygame.mask.from_surface(button_image)
    # Добавление кнопки в список
    buttons.append({"image": button_image, "rect": rect, "mask": mask, "name": f"Кнопка {i + 1}"})

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