import pygame
import sys
import time
import random

# Инициализация pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 1400, 793
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BioStudy Quiz")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
GRAY = (200, 200, 200)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (255, 200, 200)

# Шрифты
try:
    title_font = pygame.font.Font("arial.ttf", 48)
    question_font = pygame.font.Font("arial.ttf", 32)
    timer_font = pygame.font.Font("arial.ttf", 28)
    button_font = pygame.font.Font("arial.ttf", 24)
    feedback_font = pygame.font.Font("arial.ttf", 28)  # Уменьшен размер шрифта
except:
    # Если шрифты не найдены, используем системные
    title_font = pygame.font.SysFont("Arial", 48, bold=True)
    question_font = pygame.font.SysFont("Arial", 32)
    timer_font = pygame.font.SysFont("Arial", 28, bold=True)
    button_font = pygame.font.SysFont("Arial", 24)
    feedback_font = pygame.font.SysFont("Arial", 28, bold=True)  # Уменьшен размер шрифта

# Загрузка изображений
try:
    bg = pygame.image.load("background_map.png").convert()
    mit_inf = pygame.image.load("mit.png").convert_alpha()
    plaz_inf = pygame.image.load("plaz_m.png").convert_alpha()
    rib_inf = pygame.image.load("s_rib.png").convert_alpha()
    plazm_inf = pygame.image.load("plazm.png").convert_alpha()
    appar_inf = pygame.image.load("appar.png").convert_alpha()
    s_yad_inf = pygame.image.load("s_yad.png").convert_alpha()
    ger_inf = pygame.image.load("ger.png").convert_alpha()
    kst_inf = pygame.image.load("k_st.png").convert_alpha()
    hlor_inf = pygame.image.load("hlor.png").convert_alpha()
    vak_inf = pygame.image.load("vak.png").convert_alpha()
    sit_inf = pygame.image.load("sitoplaz.png").convert_alpha()
    gger_inf = pygame.image.load("gger.png").convert_alpha()
    yadk_inf = pygame.image.load("yadrk.png").convert_alpha()
    yad_inf = pygame.image.load("yadro.png").convert_alpha()
    lis_inf = pygame.image.load("liz.png").convert_alpha()
except pygame.error as e:
    print(f"Ошибка загрузки изображений: {e}")
    sys.exit()

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
        image = pygame.image.load(f"{name}.png").convert_alpha()
        rect = image.get_rect(topleft=pos)
        mask = pygame.mask.from_surface(image)
        buttons.append({"image": image, "rect": rect, "mask": mask, "name": name})
    except FileNotFoundError:
        print(f"Ошибка: файл {name}.png не найден.")

# Вопросы и ответы
questions = [
    {"question": "Где находится цитоплазма?", "answer": "цитоплазма"},
    {"question": "Какой органоид отвечает за выработку энергии?", "answer": "митохондрии"},
    {"question": "Какой органоид осуществляет фотосинтез?", "answer": "хлоропласты"},
    {"question": "Какой органоид синтезирует белки?", "answer": "рибосомы"},
    {"question": "Какой органоид содержит клеточный сок?", "answer": "вакуоль"},
    {"question": "Какой органоид участвует в сортировке белков?", "answer": "гольджи"},
    {"question": "Какой органоид синтезирует липиды?", "answer": "ГЭР"},
    {"question": "Какой органоид ограничивает клетку снаружи?", "answer": "плазм_мембрана"},
    {"question": "Какой органоид содержит генетическую информацию?", "answer": "ядро"},
    {"question": "Какой органоид разрушает поврежденные структуры?", "answer": "лизосомы"},
    {"question": "Какой органоид участвует в образовании рибосом?", "answer": "ядрышко"},
    {"question": "Какой органоид обеспечивает связь между клетками?", "answer": "плазмодесма"},
    {"question": "Какой органоид придает форму растительной клетке?", "answer": "стенка"},
    {"question": "Какой органоид участвует в транспорте веществ?", "answer": "ГлЭР"}
]

random.shuffle(questions)

# Игровые переменные
current_question_index = 0
current_question = questions[current_question_index]
start_time = time.time()
time_limit = 15
feedback = None
feedback_time = 0
score = 0
total_questions = len(questions)
game_over = False
click_processed = False  # Флаг для обработки клика


def draw_text_multiline(text, font, color, x, y, max_width):
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        if font.size(test_line)[0] <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (x, y + i * font.get_linesize()))


# Основной цикл
running = True
while running:
    screen.fill(WHITE)
    screen.blit(bg, (0, 0))

    # Отображение заголовка
    title_text = title_font.render("BioStudy Quiz", True, BLUE)
    screen.blit(title_text, (700, 10))

    # Отображение текущего вопроса
    draw_text_multiline(current_question["question"], question_font, BLACK, 700, 70, WIDTH - 710)

    # Отображение таймера
    elapsed_time = time.time() - start_time
    remaining_time = max(0, time_limit - int(elapsed_time))
    timer_color = RED if remaining_time < 5 else BLACK
    timer_text = timer_font.render(f"Время: {remaining_time} сек", True, timer_color)
    screen.blit(timer_text, (700, 150))

    # Отображение счета
    score_text = timer_font.render(f"Счет: {score}/{total_questions}", True, BLUE)
    screen.blit(score_text, (700, 190))

    # Отрисовка кнопок
    for button in buttons:
        screen.blit(button["image"], button["rect"].topleft)

    # Отображение обратной связи (уменьшенный размер)
    if feedback:
        feedback_width = max(300, feedback_font.size(feedback["text"])[0] + 40)
        feedback_surface = pygame.Surface((feedback_width, 50), pygame.SRCALPHA)
        feedback_color = LIGHT_GREEN if feedback["correct"] else LIGHT_RED
        feedback_surface.fill((*feedback_color[:3], 200))

        feedback_text = feedback_font.render(
            feedback["text"],
            True,
            GREEN if feedback["correct"] else RED
        )

        screen.blit(feedback_surface, (700, 240))
        screen.blit(feedback_text, (700 + (feedback_width - feedback_text.get_width()) // 2, 250))

        if time.time() - feedback_time > 1.5:
            feedback = None
            click_processed = False  # Сбрасываем флаг после скрытия feedback

    # Отображение сообщения о завершении игры
    if game_over:
        game_over_surface = pygame.Surface((500, 200), pygame.SRCALPHA)
        game_over_surface.fill((230, 230, 230, 240))
        screen.blit(game_over_surface, (450, 250))

        game_over_text = title_font.render("Игра завершена!", True, BLUE)
        final_score_text = question_font.render(f"Ваш счет: {score}/{total_questions}", True, BLACK)
        restart_text = button_font.render("Нажмите R для перезапуска", True, BLACK)

        screen.blit(game_over_text, (450 + (500 - game_over_text.get_width()) // 2, 270))
        screen.blit(final_score_text, (450 + (500 - final_score_text.get_width()) // 2, 330))
        screen.blit(restart_text, (450 + (500 - restart_text.get_width()) // 2, 380))

    # Проверка времени
    if not game_over and not feedback and elapsed_time >= time_limit:
        feedback = {"text": "Время вышло!", "correct": False}
        feedback_time = time.time()
        current_question_index += 1

        if current_question_index < len(questions):
            current_question = questions[current_question_index]
            start_time = time.time()
        else:
            game_over = True

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and not feedback and not click_processed:
            if event.button == 1:  # Левая кнопка мыши
                for button in reversed(buttons):
                    x, y = event.pos[0] - button["rect"].x, event.pos[1] - button["rect"].y
                    if 0 <= x < button["rect"].width and 0 <= y < button["rect"].height:
                        if button["mask"].get_at((x, y)):
                            click_processed = True  # Запрещаем обработку новых кликов

                            if button["name"] == current_question["answer"]:
                                feedback = {"text": "Правильно!", "correct": True}
                                score += 1
                            else:
                                feedback = {
                                    "text": f"Ошибка! Правильно: {current_question['answer']}",
                                    "correct": False
                                }
                            feedback_time = time.time()

                            current_question_index += 1
                            if current_question_index < len(questions):
                                current_question = questions[current_question_index]
                                start_time = time.time()
                            else:
                                game_over = True
                            break

        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:  # Перезапуск игры
                current_question_index = 0
                random.shuffle(questions)
                current_question = questions[current_question_index]
                start_time = time.time()
                score = 0
                feedback = None
                game_over = False
                click_processed = False

    pygame.display.flip()

pygame.quit()
sys.exit()