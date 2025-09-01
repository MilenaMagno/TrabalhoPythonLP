import pygame
import time
from pygame import Surface, Rect
from pygame.font import Font
from Code.Const import C_YELLOW, GAMEOVER_POS
from Code.Menu import Menu

class GameOver:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def show_gameover(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        start_time = time.time()
        duration = 3
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if time.time() - start_time >= duration:
                running = False
            self.window.blit(source=self.surf, dest=self.rect)
            self.gameover_text(48, 'GAME OVER!', C_YELLOW, GAMEOVER_POS['Title'])
            pygame.display.flip()
            pass
        pygame.mixer.music.stop()
        main_menu = Menu(self.window)
        main_menu.run()
