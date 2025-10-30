import pygame
import sys
import datetime

pygame.init()
WIDTH, HEIGHT = 777, 777
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("clock")
clock = pygame.time.Clock()

mickey = pygame.image.load("base_micky.jpg")
min_hand = pygame.image.load("minute.png")
sec_hand = pygame.image.load("second.png")

center = (WIDTH // 2, HEIGHT // 2)

def strelka(image, angle):
    rotated = pygame.transform.rotate(image, angle)
    rect = rotated.get_rect(center=center)
    screen.blit(rotated, rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.datetime.now()
    second_angle = -now.second * 6
    minute_angle = -(now.minute * 6 + now.second * 0.1)

    screen.fill((255,255,255))
    screen.blit(mickey, mickey.get_rect(center=center))
    strelka(sec_hand, second_angle)
    strelka(min_hand, minute_angle)

    pygame.display.flip()
    clock.tick(60)

