import pygame
from pygame.locals import *
import constants as SOKOBAN
from level import *
from player import *

class Game:
    def __init__(self, window):
        self.window = window
        self.player = None

    def prepare(self):
        self.index_level = 1
        self.load_textures()
        self.load_level()
        self.play = True

    def load_level(self):
        self.level = Level(self.index_level)
        self.board = pygame.Surface((self.level.width, self.level.height))
        if self.player:
            self.player.pos = self.level.position_player
        else:
            self.player = Player(self.level)

    def load_textures(self):
       self.textures = {
           SOKOBAN.WALL: pygame.image.load('assets/images/wall.png').convert_alpha(),
           SOKOBAN.BOX: pygame.image.load('assets/images/box.png').convert_alpha(),
           SOKOBAN.TARGET: pygame.image.load('assets/images/target.png').convert_alpha(),
           SOKOBAN.TARGET_FILLED: pygame.image.load('assets/images/valid_box.png').convert_alpha(),
           SOKOBAN.PLAYER: pygame.image.load('assets/images/player.png').convert_alpha()
       }

    def process_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.play = False
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT, K_z, K_s, K_q, K_d]:
                self.player.move(event.key, self.level)
                if self.has_win():
                    self.index_level += 1
                    self.load_level()

    def has_win(self):
        nb_missing_target = 0
        for y in range(len(self.level.structure)):
            for x in range(len(self.level.structure[y])):
                if self.level.structure[y][x] == SOKOBAN.TARGET:
                    nb_missing_target += 1

        return nb_missing_target == 0

    def update_screen(self):
        pygame.draw.rect(self.board, SOKOBAN.WHITE, (0,0, self.level.width * SOKOBAN.SPRITESIZE, self.level.height * SOKOBAN.SPRITESIZE))
        pygame.draw.rect(self.window, SOKOBAN.WHITE, (0,0,SOKOBAN.WINDOW_WIDTH,SOKOBAN.WINDOW_HEIGHT))

        self.level.render(self.board, self.textures)
        self.player.render(self.board, self.textures)

        pox_x_board = (SOKOBAN.WINDOW_WIDTH / 2) - (self.board.get_width() / 2)
        pos_y_board = (SOKOBAN.WINDOW_HEIGHT / 2) - (self.board.get_height() / 2)
        self.window.blit(self.board, (pox_x_board, pos_y_board))

        pygame.display.flip()

    def start(self):
        self.prepare()
        while self.play:
            self.process_event(pygame.event.wait())
            self.update_screen()
