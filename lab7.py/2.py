import pygame

pygame.init()
pygame.mixer.init()

playlist = [
    "Dasdinlovee_KETPE.mp3",
    "Kendrick Lamar - Love (Feat. Zacari).mp3",
    "Rihanna feat. Future - Loveeeeeee Song.mp3"
]
current_song = 0

def play_music():
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song
    current_song = (current_song + 1) 
    play_music()

def prev_song():
    global current_song
    current_song = (current_song - 1) 
    play_music()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("player")
font = pygame.font.Font(None, 28)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_d:
                next_song()
            elif event.key == pygame.K_a:
                prev_song()

    screen.fill((30, 30, 30))

    text = font.render(f"playing:  {playlist[current_song]}", True, (255, 255, 255))
    screen.blit(text, (20, 130))

    under_text = font.render("enter=play  s=stop  a=prev  d=next", True, (200, 200, 200))
    screen.blit(under_text, (20, 260))

    pygame.display.flip()

pygame.quit()