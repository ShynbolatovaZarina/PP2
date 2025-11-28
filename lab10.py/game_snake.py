# game_snake.py
import pygame
import random
import sys

from snakee import (
    create_snake_tables,
    get_or_create_user,
    get_current_level,
    save_score,
)

pygame.init()

cell_size = 20
g_w = 30
g_h = 20
width = cell_size * g_w
height = cell_size * g_h

bg = (18, 18, 18)
s_color = (0, 200, 0)
f_color = (200, 0, 0)
t_color = (220, 220, 220)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)


def draw_rect(pos, color):
    x, y = pos
    rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, color, rect)


def random_food(snake, walls):
    while True:
        p = (random.randrange(g_w), random.randrange(g_h))
        if p not in snake and p not in walls:
            return p


def make_walls_for_level(level, snake):
    """generate lvls 1-7"""
    walls = []

    #1 
    if level <= 1:
        return walls

    #2 
    if level >= 2:
        y = g_h // 2
        for x in range(3, g_w - 3):
            walls.append((x, y))

    #3
    if level >= 3:
        x = g_w // 4
        for y in range(3, g_h - 3):
            walls.append((x, y))

    #4
    if level >= 4:
        x = 3 * g_w // 4
        for y in range(3, g_h - 3):
            walls.append((x, y))

    #5 
    if level >= 5:
        cx, cy = g_w // 2, g_h // 2
        for x in range(cx - 3, cx + 4):
            walls.append((x, cy))
        for y in range(cy - 3, cy + 4):
            walls.append((cx, y))

    #6 
    if level >= 6:
        for x in range(0, g_w):
            if x not in (g_w // 3, 2 * g_w // 3):
                walls.append((x, 0))
                walls.append((x, g_h - 1))
        for y in range(0, g_h):
            if y not in (g_h // 3, 2 * g_h // 3):
                walls.append((0, y))
                walls.append((g_w - 1, y))

    #7 
    if level >= 7:
        for i in range(3, min(g_w, g_h) - 3):
            walls.append((i, i))

    
    walls = [w for w in walls if w not in snake]
    return walls


def game_loop(user_id, start_level):
    snake = [(g_w // 2, g_h // 2)]
    direction = (1, 0)
    score = 0
    level = start_level

    walls = make_walls_for_level(level, snake)
    food = random_food(snake, walls)

    game_over = False
    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_q, pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        save_score(user_id, level, score)

                if not game_over and not paused:
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

        if not game_over and not paused:
            head = snake[0]

            new_head = (
                (head[0] + direction[0]) % g_w,
                (head[1] + direction[1]) % g_h
            )

            if new_head in snake or new_head in walls:
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    score += 1
                    # lvl
                    level = min(7, 1 + score // 3)
                    walls = make_walls_for_level(level, snake)
                    food = random_food(snake, walls)
                else:
                    snake.pop()

        screen.fill(bg)

        for w in walls:
            draw_rect(w, (120, 120, 120))

        for segment in snake:
            draw_rect(segment, s_color)

        
        draw_rect(food, f_color)

        score_surf = font.render(f"Score: {score}", True, t_color)
        level_surf = font.render(f"Level: {level}", True, t_color)
        screen.blit(score_surf, (10, 10))
        screen.blit(level_surf, (10, 40))

        if paused:
            pause_surf = font.render("PAUSED (P)", True, t_color)
            rect = pause_surf.get_rect(center=(width // 2, height // 2))
            screen.blit(pause_surf, rect)

        if game_over:
            over_text = "Game Over, press R to restart"
            over_surf = font.render(over_text, True, t_color)
            rect = over_surf.get_rect(center=(width // 2, height // 2))
            screen.blit(over_surf, rect)
            save_score(user_id, level, score)

        pygame.display.flip()

        base_fps = 10
        extra = (level - 1) * 2
        clock.tick(base_fps + extra)

    return False


def main():
    create_snake_tables()

    username = input("Enter your username: ").strip()
    user_id = get_or_create_user(username)
    current_level = get_current_level(user_id)
    print(f"Your current level: {current_level}")

    restart = True
    while restart:
        restart = game_loop(user_id, current_level)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
