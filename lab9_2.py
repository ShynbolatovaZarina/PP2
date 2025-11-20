import pygame
import random
import sys

pygame.init()

cell_size = 20
g_w = 30
g_h = 20
width = cell_size * g_w
height = cell_size * g_h
fps = 5

bg = (18, 18, 18)
s_color = (0, 200, 0)
f_color = (200, 0, 0)
t_color = (220, 220, 220)

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

food_timer = 0        
food_lifetime = 50    
food_value = 1      

def draw_rect(pos, color):
    x, y = pos
    rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, color, rect)

def random_food(snake):
    global food_value, food_timer
    while True:
        p = (random.randrange(g_w), random.randrange(g_h))
        if p not in snake:
            food_value = random.choice([1, 2, 3])
            food_timer = 0
            return p

def game_loop():
    global food_timer
    snake = [(g_w // 2, g_h // 2)]
    direction = (1, 0)  
    food = random_food(snake)
    grow = False
    score = 0
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key in (pygame.K_w, pygame.K_UP) and direction != (0, 1):
                        direction = (0, -1)
                    elif event.key in (pygame.K_s, pygame.K_DOWN) and direction != (0, -1):
                        direction = (0, 1)
                    elif event.key in (pygame.K_a, pygame.K_LEFT) and direction != (1, 0):
                        direction = (-1, 0)
                    elif event.key in (pygame.K_d, pygame.K_RIGHT) and direction != (-1, 0):
                        direction = (1, 0)
                else:
                    if event.key == pygame.K_r:
                        return True
                    if event.key in (pygame.K_q, pygame.K_ESCAPE):
                        pygame.quit()
                        sys.exit()

        if not game_over:
            food_timer += 1
            if food_timer > food_lifetime:
                food = random_food(snake)

            head = snake[0]
            new_head = ((head[0] + direction[0]) % g_w, (head[1] + direction[1]) % g_h)


            if not (0 <= new_head[0] < g_w and 0 <= new_head[1] < g_h):
                game_over = True
            else:
                if new_head in snake:
                    game_over = True
                else:
                    snake.insert(0, new_head)
                    if new_head == food:
                        score += food_value
                        food = random_food(snake)
                    else:
                        snake.pop()

        screen.fill(bg)
        for segment in snake:
            draw_rect(segment, s_color)
        draw_rect(food, f_color)

        score_surf = font.render(f"Score: {score}", True, t_color)
        screen.blit(score_surf, (10, 10))

        if game_over:
            over_surf = font.render("Game Over", True, t_color)
            rect = over_surf.get_rect(center=(width // 2, height // 2))
            screen.blit(over_surf, rect)

        pygame.display.flip()
        clock.tick(fps)

    return False
    
while True:
    try:
        restart = game_loop()
        if not restart:
            break
    except SystemExit:
        pygame.quit()
        raise
pygame.quit()
