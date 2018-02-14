import pygame
from pygame.locals import *
import constants as SOKOBAN
from level import *
from player import *

class Game:
    def __init__(self, window):
        self.window = window

    def prepare(self):
        self.index_level = 1
        self.level = Level(self.index_level)
        self.player = Player(self.level)
        self.load_textures()
        self.play = True

    def load_textures(self):
       self.textures = {
           SOKOBAN.WALL: pygame.image.load('assets/images/wall.png').convert_alpha(),
           SOKOBAN.BOX: pygame.image.load('assets/images/box.png').convert_alpha(),
           SOKOBAN.TARGET: pygame.image.load('assets/images/target.png').convert_alpha(),
        #    SOKOBAN.TARGET_FILLED: pygame.image.load('')
           SOKOBAN.PLAYER: pygame.image.load('assets/images/player.png').convert_alpha()
       }

    def process_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.play = False
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                self.player.move(event.key, self.level)
                if self.has_win():
                    self.index_level += 1
                    self.level = Level(self.index_level)
                    self.player.pos = self.level.position_player

    def has_win(self):
        nb_missing_target = 0
        for y in range(len(self.level.structure)):
            for x in range(len(self.level.structure[y])):
                if self.level.structure[y][x] == SOKOBAN.TARGET:
                    nb_missing_target += 1

        return nb_missing_target == 0

    def update_screen(self):
        pygame.draw.rect(self.window, (255,255,255), (0,0,SOKOBAN.MAPWIDTH * SOKOBAN.SPRITESIZE, SOKOBAN.MAPHEIGHT * SOKOBAN.SPRITESIZE))
        self.level.render(self.window, self.textures)
        self.player.render(self.window, self.textures)
        pygame.display.flip()


    def start(self):
        self.prepare()
        while self.play:
            self.process_event(pygame.event.wait())
            self.update_screen()
