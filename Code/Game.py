#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from Code.EntityFactory import EntityFactory
from Code.GameOver import GameOver
from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Level import Level
from Code.Menu import Menu
from Code.Menu import MENU_OPTION
from Code.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.gameover = GameOver(self.window)

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0] # [Player1, Player2]
                player = EntityFactory.get_entity('Player1')
                level = Level(self.window, 'Level1', menu_return, player_score, player)
                level_return = level.run(player_score)
                if level_return == 'game_over':
                    self.gameover.show_gameover()
                    continue
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score, player)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(menu_return, player_score)
            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pygame.quit()
                sys.exit()
