import pygame, sys, asyncio
from settings import *
from background import Background
from spawnlogic import Spawn
from pygame import mixer

pygame.init()
mixer.init()

mixer.music.load('ES_Crowned Kings - Dream Cave.mp3')
mixer.music.set_volume(0.2)

async def main():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Dino")
    clock = pygame.time.Clock()
    FPS = 60
    # Initialize level
    background = Background()
    ground_rect = pygame.Rect(0, screen_height - 30, screen_width, 30)
    scroll_speed = 3
    # Score counter
    font = pygame.font.Font(None, 36)
    start_time = pygame.time.get_ticks() / 1000.0
    logic = Spawn()
    lost = False
    mixer.music.play()



    # Music 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and lost:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                restart_button_rect = pygame.Rect(screen_width // 2 - 50, screen_height // 2 -200, 100, 50)
                if restart_button_rect.collidepoint(mouse_x, mouse_y):
                    reset_game_state( ground_rect, scroll_speed)
                    lost = False
                    start_time = pygame.time.get_ticks() / 1000.0
                    logic = Spawn()
                    mixer.music.play()

                    

        if lost:
            mixer.music.stop()
            loss_bg = pygame.image.load('./images/background/loss_screen.png').convert()
            loss_rect = loss_bg.get_rect(topleft=(0,0))
            screen.blit(loss_bg, loss_rect)
            finalTime = elapsed_time / 10
            score_text = font.render(f'Time lasted: {finalTime*10:.2f} s', True, (0,0,0))
            screen.blit(score_text, (screen_width-250, 10))
            pygame.draw.rect(screen, "green", (screen_width // 2 - 50, screen_height // 2 - 200, 100, 50))
            restart_text = font.render("Restart", True, (0, 0, 0))
            screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2 - 190))
        else:
            # Background and floor
            background.update(screen, scroll_speed)
            pygame.draw.rect(screen, 'white', ground_rect)

            current_time = pygame.time.get_ticks() / 1000.0
            elapsed_time = current_time - start_time
            level = round(elapsed_time) / 10

            # Setting Score
            score_text = font.render(f'Time lasted: {elapsed_time:.2f} s', True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            gameplay = logic.update(screen, level, ground_rect)
            if gameplay:
                lost = True

        pygame.display.flip()

        clock.tick(FPS)
        await asyncio.sleep(0)

def reset_game_state( ground_rect, scroll_speed):
    # Reset all variables and objects to their initial state
    ground_rect = pygame.Rect(0, screen_height - 30, screen_width, 30)
    scroll_speed = 3

asyncio.run(main())