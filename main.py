import pygame
from random import randint

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (180, 0, 0)

# Подгружаем шрифты
font = pygame.font.Font(None, 80)
win_text = font.render('YOU WIN!', True, WHITE)
lose_text = font.render('YOU LOSE!', True, RED)
font_small = pygame.font.Font(None, 36)

# Загрузка изображений
img_bita = pygame.image.load("bita.png")
img_bita = pygame.transform.scale(img_bita, (10, 100))  # Размер ракетки
img_pig = pygame.image.load("pig.png")
img_pig = pygame.transform.scale(img_pig, (20, 20))  # Размер мяча

# Параметры игры
paddle_speed = 10
ball_speed_x = 7
ball_speed_y = 7

# Инициализация объектов
paddle1 = pygame.Rect(30, HEIGHT // 2 - 50, 10, 100)
paddle2 = pygame.Rect(WIDTH - 40, HEIGHT // 2 - 50, 10, 100)
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)

# Игровые переменные
score1 = 0
score2 = 0
running = True
game_over = False

# Основной игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= paddle_speed
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += paddle_speed
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += paddle_speed

    # Движение мяча
    if not game_over:
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Отскок от верхней и нижней границ
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1

        # Отскок от ракеток
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ball_speed_x *= -1

        # Проверка на гол
        if ball.left <= 0:
            score2 += 1
            if score2 == 5:
                game_over = True
            ball.x, ball.y = WIDTH // 2 - 10, HEIGHT // 2 - 10
            ball_speed_x *= -1

        if ball.right >= WIDTH:
            score1 += 1
            if score1 == 5:
                game_over = True
            ball.x, ball.y = WIDTH // 2 - 10, HEIGHT // 2 - 10
            ball_speed_x *= -1

    # Отрисовка объектов
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Отображение счета
    score_display = font_small.render(f"{score1} : {score2}", True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - 50, 20))

    # Проверка окончания игры
    if game_over:
        if score1 == 5:
            screen.blit(win_text, (WIDTH // 2 - 150, HEIGHT // 2 - 40))
        else:
            screen.blit(lose_text, (WIDTH // 2 - 150, HEIGHT // 2 - 40))

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
