import pygame
import sys
import time

# Инициализация pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 1400, 793
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BioStudy Quiz")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Шрифты
font = pygame.font.Font(None, 36)

# Загрузка изображений
bg = pygame.image.load("background_map.png")
ph_inf = pygame.image.load("start.png")
mit_inf = pygame.image.load("mit.png")
plaz_inf = pygame.image.load("plaz_m.png")
rib_inf = pygame.image.load("s_rib.png")
plazm_inf = pygame.image.load("plazm.png")
appar_inf = pygame.image.load("appar.png")
s_yad_inf = pygame.image.load("s_yad.png")
ger_inf = pygame.image.load("ger.png")
kst_inf = pygame.image.load("k_st.png")
hlor_inf = pygame.image.load("hlor.png")
vak_inf = pygame.image.load("vak.png")
sit_inf = pygame.image.load("sitoplaz.png")
gger_inf = pygame.image.load("gger.png")
yadk_inf = pygame.image.load("yadrk.png")
yad_inf = pygame.image.load("yadro.png")
lis_inf = pygame.image.load("liz.png")

# Начальное изображение
current_image = ph_inf

# Координаты информационного изображения
info_image_pos = (800, 70)  # Позиция для отображения текущего изображения

# Координаты кнопок
button_positions = {
    "цитоплазма": (145, 105),
    "плазм_мембрана": (100, 50),
    "хлоропласты": (160, 125),
    "рибосомы": (156, 125),
    "вакуоль": (190, 160),
    "гольджи": (300, 350),
    "ГЭР": (200, 390),
    "оболочка": (325, 415),
    "ГлЭР": (172, 470),
    "ядро": (228, 412),
    "стенка": (112, 42),
    "лизосомы": (185, 134),
    "митохондрии": (147, 109),
    "ядрышко": (317, 480),
    "плазмодесма": (130, 333)
}

# Список кнопок
buttons = []
for name, pos in button_positions.items():
    try:
        # Загрузка изображения
        image = pygame.image.load(f"{name}.png").convert_alpha()
        # Создание прямоугольника для кнопки
        rect = image.get_rect(topleft=pos)
        # Создание маски для кнопки
        mask = pygame.mask.from_surface(image)
        # Добавление кнопки в список
        buttons.append({"image": image, "rect": rect, "mask": mask, "name": name})
    except FileNotFoundError:
        print(f"Ошибка: файл {name}.png не найден. Убедитесь, что он находится в той же директории, что и скрипт.")

# Вопросы и ответы
questions = [
    {"question": "Где находится цитоплазма?", "answer": "цитоплазма"},
    {"question": "Какой органоид отвечает за выработку энергии?", "answer": "митохондрии"}
]

# Текущий вопрос
current_question_index = 0
current_question = questions[current_question_index]
start_time = time.time()
time_limit = 15  # 15 секунд на ответ

# Основной цикл
running = True
while running:
    screen.fill(WHITE)

    # Отрисовка фона
    screen.blit(bg, (0, 0))

    # Отображение текущего вопроса
    question_text = font.render(current_question["question"], True, BLACK)
    screen.blit(question_text, (20, 10))

    # Отображение таймера
    elapsed_time = time.time() - start_time
    remaining_time = max(0, time_limit - int(elapsed_time))
    timer_text = font.render(f"Осталось времени: {remaining_time} сек", True, RED)
    screen.blit(timer_text, (20, 50))

    # Отрисовка текущего изображения
    screen.blit(current_image, info_image_pos)

    # Отрисовка кнопок
    for button in buttons:
        screen.blit(button["image"], button["rect"].topleft)

    # Проверка времени
    if elapsed_time >= time_limit:
        print("Время вышло!")
        current_question_index += 1
        if current_question_index < len(questions):
            current_question = questions[current_question_index]
            start_time = time.time()
        else:
            print("Викторина завершена!")
            running = False

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                for button in reversed(buttons):
                    x, y = event.pos[0] - button["rect"].x, event.pos[1] - button["rect"].y
                    if 0 <= x < button["rect"].width and 0 <= y < button["rect"].height:
                        if button["mask"].get_at((x, y)):
                            if button["name"] == current_question["answer"]:
                                print("Правильно!")
                            else:
                                print("Неправильно!")
                            current_question_index += 1
                            if current_question_index < len(questions):
                                current_question = questions[current_question_index]
                                start_time = time.time()
                            else:
                                print("Викторина завершена!")
                                running = False

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
sys.exit()