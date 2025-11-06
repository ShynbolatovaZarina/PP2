import pygame, sys
from pygame.locals import *

pygame.init()

def main():
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'          
    tool = 'brush'         
    points = []            
    rects = []             
    circles = []           
    drawing_shape = False  
    shape_start = None     
    solid_color = (0, 0, 255) 

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[K_LALT] or pressed[K_RALT]
        ctrl_held = pressed[K_LCTRL] or pressed[K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            if event.type == pygame.KEYDOWN:
                if (event.key == K_w and ctrl_held) or (event.key == K_F4 and alt_held) or event.key == K_ESCAPE:
                    return

                if event.key == K_b: tool = 'brush'
                elif event.key == K_1: tool = 'rect'
                elif event.key == K_2: tool = 'circle'
                elif event.key == K_3: tool = 'eraser'
                elif event.key == K_4: tool = 'picker'

                elif event.key == K_r: mode, solid_color = 'red',   (255, 0, 0)
                elif event.key == K_g: mode, solid_color = 'green', (0, 255, 0)
                elif event.key == K_b: mode, solid_color = 'blue',  (0, 0, 255)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    if tool in ('rect', 'circle'):
                        drawing_shape = True
                        shape_start = event.pos
                    elif tool == 'brush':
                        radius = min(200, radius + 1)
                        points = points + [event.pos]
                        points = points[-256:]
                    elif tool == 'eraser':
                        points = points + [event.pos]
                        points = points[-256:]
                    elif tool == 'picker':
                        cx, cy = event.pos
                        if 0 <= cx < 640 and 0 <= cy < 480:
                            solid_color = screen.get_at((cx, cy))[:3]
                            tool = 'brush'
                elif event.button == 3:  
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if drawing_shape and shape_start and tool in ('rect', 'circle'):
                    x0, y0 = shape_start
                    x1, y1 = event.pos
                    left, top = min(x0, x1), min(y0, y1)
                    w, h = abs(x1 - x0), abs(y1 - y0)
                    if tool == 'rect':
                        rects.append((left, top, w, h, solid_color))
                    else:
                        circles.append((left, top, w, h, solid_color))
                drawing_shape = False
                shape_start = None

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if tool in ('brush', 'eraser') and pygame.mouse.get_pressed()[0]:
                    points = points + [position]
                    points = points[-256:]

        screen.fill((0, 0, 0))

        for (l, t, w, h, col) in rects:
            pygame.draw.rect(screen, col, (l, t, w, h), 0)
        for (l, t, w, h, col) in circles:
            pygame.draw.ellipse(screen, col, (l, t, w, h), 0)

        if drawing_shape and shape_start and tool in ('rect', 'circle'):
            x0, y0 = shape_start
            x1, y1 = pygame.mouse.get_pos()
            left, top = min(x0, x1), min(y0, y1)
            w, h = abs(x1 - x0), abs(y1 - y0)
            if tool == 'rect':
                pygame.draw.rect(screen, solid_color, (left, top, w, h), 2)
            else:
                pygame.draw.ellipse(screen, solid_color, (left, top, w, h), 2)

        i = 0
        while i < len(points) - 1:
            if tool == 'eraser':
                drawLineSolid(screen, points[i], points[i + 1], radius, (0, 0, 0))
            else:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1

        pygame.display.flip()
        clock.tick(60)

def drawLineSolid(screen, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    if iterations == 0:
        pygame.draw.circle(screen, color, start, width)
        return
    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    else:  
        color = (c1, c1, c2)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    if iterations == 0:
        pygame.draw.circle(screen, color, start, width)
        return
    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
