import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    radius = min(200, radius + 1)
                elif event.button == 3: 
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()


def enhanced_main():
    screen = pygame.display.get_surface() or pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    mode = 'pen'
    color_mode = 'blue'
    color_map = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
    }
    width = 5

    drawing = False
    start_pos = None
    last_pos = None

    font = pygame.font.Font(None, 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
                ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
                if event.key == pygame.K_ESCAPE or (event.key == pygame.K_w and ctrl_held) or (event.key == pygame.K_F4 and alt_held):
                    return

                if event.key == pygame.K_1:
                    mode = 'pen'
                elif event.key == pygame.K_2:
                    mode = 'rect'
                elif event.key == pygame.K_3:
                    mode = 'circle'
                elif event.key == pygame.K_4:
                    mode = 'eraser'

                elif event.key == pygame.K_r:
                    color_mode = 'red'
                elif event.key == pygame.K_g:
                    color_mode = 'green'
                elif event.key == pygame.K_b:
                    color_mode = 'blue'
                elif event.key == pygame.K_w:
                    color_mode = 'white'
                elif event.key == pygame.K_k:
                    color_mode = 'black'

                elif event.key in (pygame.K_EQUALS, pygame.K_PLUS, pygame.K_KP_PLUS):
                    width = min(200, width + 1)
                elif event.key in (pygame.K_MINUS, pygame.K_KP_MINUS):
                    width = max(1, width - 1)

                elif event.key == pygame.K_c:
                    screen.fill((0, 0, 0))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos
                    if mode == 'pen':
                        pygame.draw.circle(screen, color_map[color_mode], event.pos, width)
                elif event.button == 3:  
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, width * 8)

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if mode == 'pen':
                        pygame.draw.line(screen, color_map[color_mode], last_pos, event.pos, width * 2)
                        last_pos = event.pos
                    elif mode == 'eraser':
                        pygame.draw.circle(screen, (0, 0, 0), event.pos, width * 2)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and start_pos:
                    end_pos = event.pos
                    col = color_map[color_mode]
                    if mode == 'rect':
                        left = min(start_pos[0], end_pos[0])
                        top = min(start_pos[1], end_pos[1])
                        w = abs(end_pos[0] - start_pos[0])
                        h = abs(end_pos[1] - start_pos[1])
                        rect = pygame.Rect(left, top, w, h)
                        if width == 0:
                            pygame.draw.rect(screen, col, rect)
                        else:
                            pygame.draw.rect(screen, col, rect, width)
                    elif mode == 'circle':
                        dx = end_pos[0] - start_pos[0]
                        dy = end_pos[1] - start_pos[1]
                        r = int(math.hypot(dx, dy))
                        if width == 0:
                            pygame.draw.circle(screen, col, start_pos, r)
                        else:
                            pygame.draw.circle(screen, col, start_pos, r, width)
                    elif mode == 'pen':
                        pygame.draw.circle(screen, col, end_pos, width)
                    elif mode == 'eraser':
                        pygame.draw.circle(screen, (0, 0, 0), end_pos, width * 2)

                    drawing = False
                    start_pos = None
                    last_pos = None

        info = f"Mode:{mode}  Color:{color_mode}  Width:{width}  Keys:1=pen 2=rect 3=circle 4=eraser  R/G/B/W/K colors  +/- width  C=clear"
        text_surf = font.render(info, True, (255, 255, 255))
        bg_rect = text_surf.get_rect(topleft=(4, 4))
        pygame.draw.rect(screen, (0, 0, 0), bg_rect)  
        screen.blit(text_surf, (4, 4))

        pygame.display.flip()
        clock.tick(60)

enhanced_main()