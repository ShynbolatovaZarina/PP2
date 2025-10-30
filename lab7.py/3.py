import pygame

pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ball_x, ball_y = WIDTH // 2, HEIGHT // 2
radius = 25
speed = 20

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (5, 255, 0), (ball_x, ball_y), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_x - radius > 0:
        ball_x -= speed
    if keys[pygame.K_RIGHT] and ball_x + radius < WIDTH:
        ball_x += speed
    if keys[pygame.K_UP] and ball_y - radius > 0:
        ball_y -= speed
    if keys[pygame.K_DOWN] and ball_y + radius < HEIGHT:
        ball_y += speed

    pygame.display.flip()
    clock.tick(30)

pygame.quit()