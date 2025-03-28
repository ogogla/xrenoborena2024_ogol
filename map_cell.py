import pygame
import sys

# Инициализация pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 1400, 793
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BioStudy map")

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
s_yad_inf = pygame.image.load("s_yad.png")

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

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                current_image = mit_inf
            elif event.key == pygame.K_q:
                current_image = plaz_inf
            elif event.key == pygame.K_e:
                current_image = rib_inf
            elif event.key == pygame.K_t:
                current_image = plazm_inf
            elif event.key == pygame.K_s:
                current_image = appar_inf
            elif event.key == pygame.K_b:
                current_image = s_yad_inf
            elif event.key == pygame.K_f:
                current_image = ger_inf
            elif event.key == pygame.K_w:
                current_image = hlor_inf
            elif event.key == pygame.K_r:
                current_image = vak_inf
            elif event.key == pygame.K_z:
                current_image = sit_inf
            elif event.key == pygame.K_d:
                current_image = gger_inf
            elif event.key == pygame.K_v:
                current_image = yadk_inf
            elif event.key == pygame.K_g:
                current_image = yad_inf
            elif event.key == pygame.K_a:
                current_image = lis_inf
            elif event.key == pygame.K_x:
                current_image = kst_inf
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                # Проверяем кнопки в порядке их отрисовки (сверху вниз)
                for button in reversed(buttons):
                    x, y = event.pos[0] - button["rect"].x, event.pos[1] - button["rect"].y
                    # Проверяем, попал ли клик в область кнопки
                    if 0 <= x < button["rect"].width and 0 <= y < button["rect"].height:
                        if button["mask"].get_at((x, y)):
                            print(f"Нажата {button['name']}")
                            # Изменяем текущее изображение в зависимости от нажатой кнопки
                            if button["name"] == "плазм_мембрана":
                                current_image = plaz_inf
                            elif button["name"] == "хлоропласты":
                                current_image = hlor_inf
                            elif button["name"] == "рибосомы":
                                current_image = rib_inf
                            elif button["name"] == "вакуоль":
                                current_image = vak_inf
                            elif button["name"] == "цитоплазма":
                                current_image = sit_inf
                            elif button["name"] == "плазмодесма":
                                current_image = plazm_inf
                            elif button["name"] == "гольджи":
                                current_image = appar_inf
                            elif button["name"] == "ГЭР":
                                current_image = gger_inf
                            elif button["name"] == "оболочка":
                                current_image = s_yad_inf
                            elif button["name"] == "ядрышко":
                                current_image = yadk_inf
                            elif button["name"] == "ГлЭР":
                                current_image = ger_inf
                            elif button["name"] == "ядро":
                                current_image = yad_inf
                            elif button["name"] == "стенка":
                                current_image = kst_inf
                            elif button["name"] == "лизосомы":
                                current_image = lis_inf
                            elif button["name"] == "митохондрии":
                                current_image = mit_inf
                            break  # Прекращаем проверку, если кнопка нажата

    # Отрисовка фона и текущего изображения
    screen.blit(bg, (0, 0))
    screen.blit(current_image, info_image_pos)

    # Отрисовка кнопок
    for button in buttons:
        screen.blit(button["image"], button["rect"].topleft)

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
sys.exit()
