import pygame
import sys
from pygame.locals import * 

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Paint v1.0 Simplifed")
clock = pygame.time.Clock()


def draw_line(surface, start_pos, end_pos, color, width):
        if start_pos and end_pos:
            pygame.draw.line(surface, color, start_pos, end_pos, width)
            pygame.draw.circle(surface, color, end_pos, width // 2)


shapes = []       
current_color = BLUE    
brush_radius = 5        
tool = 'brush'          

drawing_shape = False  
shape_start = None      
last_pos = None         

canvas = pygame.Surface(SCREEN_SIZE)
canvas.fill(BLACK) 


running = True
while running:
    
    current_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
    
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False
            
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            
            elif event.key == K_b: tool = 'brush'
            elif event.key == K_1: tool = 'rect'
            elif event.key == K_2: tool = 'circle'
            elif event.key == K_3: tool = 'eraser'
            elif event.key == K_4: tool = 'picker'
            elif event.key == K_c: canvas.fill(BLACK)
            
            elif event.key == K_r: current_color = RED
            elif event.key == K_g: current_color = GREEN
            elif event.key == K_l: current_color = BLUE 
            elif event.key == K_w: current_color = WHITE 

            elif event.key == K_5: tool = 'square'
            elif event.key == K_6: tool = 'right_triangle'
            elif event.key == K_7: tool = 'equilateral_triangle'
            elif event.key == K_8: tool = 'rhombus'

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  
                if tool in ('rect', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus'):
                    drawing_shape = True
                    shape_start = event.pos
                elif tool in ('brush', 'eraser'):
                    last_pos = event.pos
                elif tool == 'picker':
                    if 0 <= event.pos[0] < SCREEN_WIDTH and 0 <= event.pos[1] < SCREEN_HEIGHT:
                        current_color = canvas.get_at(event.pos)[:3] 
                        tool = 'brush'

            elif event.button == 3:  
                brush_radius = max(1, brush_radius + 2)
        
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                if drawing_shape and shape_start:
                    x0, y0 = shape_start
                    x1, y1 = event.pos
                    
                    left = min(x0, x1)
                    top = min(y0, y1)
                    w = abs(x1 - x0)
                    h = abs(y1 - y0)

                    if tool == 'rect':
                        shapes.append(('rect', (left, top, w, h), current_color))
                    elif tool == 'circle':
                        shapes.append(('circle', (left, top, w, h), current_color))
                    elif tool == 'square':
                        size = max(w, h)
                        shapes.append(('square', (left, top, size, size), current_color))
                    elif tool == 'right_triangle':
                        shapes.append(('right_triangle', (left, top, w, h), current_color))
                    elif tool == 'equilateral_triangle':
                        size = max(w, h)
                        shapes.append(('equilateral_triangle', (left, top, size), current_color))
                    elif tool == 'rhombus':
                        shapes.append(('rhombus', (left, top, w, h), current_color))
                        
                    drawing_shape = False
                    shape_start = None
                
                last_pos = None 

        if event.type == MOUSEMOTION:
            if mouse_buttons[0] and tool in ('brush', 'eraser'):
                color = current_color
                if tool == 'eraser':
                    color = BLACK 
                    
                draw_line(canvas, last_pos, current_pos, color, brush_radius * 2)
                last_pos = current_pos
            
    
    screen.blit(canvas, (0, 0))

    for type, rect_data, color in shapes:
        if type == 'rect':
            pygame.draw.rect(screen, color, rect_data, 0)
        elif type == 'circle':
            pygame.draw.ellipse(screen, color, rect_data, 0) 
        elif type == 'square':
            pygame.draw.rect(screen, color, rect_data, 0)
        elif type == 'right_triangle':
            x, y, w, h = rect_data
            points = [(x, y+h), (x, y), (x+w, y+h)]
            pygame.draw.polygon(screen, color, points, 0)
        elif type == 'equilateral_triangle':
            x, y, size = rect_data
            points = [(x+size//2, y), (x, y+size), (x+size, y+size)]
            pygame.draw.polygon(screen, color, points, 0)
        elif type == 'rhombus':
            x, y, w, h = rect_data
            points = [(x + w//2, y), (x+w, y+h//2), (x + w//2, y+h), (x, y+h//2)]
            pygame.draw.polygon(screen, color, points, 0)

    if drawing_shape and shape_start and tool in ('rect', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus'):
        x0, y0 = shape_start
        x1, y1 = current_pos
        
        left = min(x0, x1)
        top = min(y0, y1)
        w = abs(x1 - x0)
        h = abs(y1 - y0)
        
        if tool == 'rect':
            pygame.draw.rect(screen, current_color, (left, top, w, h), 2)
        elif tool == 'circle':
            pygame.draw.ellipse(screen, current_color, (left, top, w, h), 2)
        elif tool == 'square':
            size = max(w, h)
            pygame.draw.rect(screen, current_color, (left, top, size, size), 2)
        elif tool == 'right_triangle':
            points = [(left, top+h), (left, top), (left+w, top+h)]
            pygame.draw.polygon(screen, current_color, points, 2)
        elif tool == 'equilateral_triangle':
            size = max(w, h)
            points = [(left+size//2, top), (left, top+size), (left+size, top+size)]
            pygame.draw.polygon(screen, current_color, points, 2)
        elif tool == 'rhombus':
            points = [(left + w//2, top), (left+w, top+h//2), (left + w//2, top+h), (left, top+h//2)]
            pygame.draw.polygon(screen, current_color, points, 2)
            
    pygame.display.flip()
    clock.tick(660)

pygame.quit()
sys.exit()
