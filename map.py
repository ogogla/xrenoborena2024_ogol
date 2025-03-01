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
md_button = pygame.image.load("cell.png")
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

    # Отрисовка фона и текущего изображения
    screen.blit(bg, (0, 0))
    screen.blit(md_button, (20, 40))
    screen.blit(current_image, (800, 70))

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
sys.exit()