import pygame
import sys
from pygame.locals import *
import constants as SOKOBAN
from level import *
from player import *
from scores import *

class Game:
    def __init__(self, window):
        self.window = window
        self.font_menu = pygame.font.Font('assets/fonts/FreeSansBold.ttf', 18)
        self.load_textures()
        self.player = None
        self.index_level = 1
        self.load_level()
        self.play = True
        self.scores = Scores(self)

    def load_textures(self):
       self.textures = {
           SOKOBAN.WALL: pygame.image.load('assets/images/wall.png').convert_alpha(),
           SOKOBAN.BOX: pygame.image.load('assets/images/box.png').convert_alpha(),
           SOKOBAN.TARGET: pygame.image.load('assets/images/target.png').convert_alpha(),
           SOKOBAN.TARGET_FILLED: pygame.image.load('assets/images/valid_box.png').convert_alpha(),
           #SOKOBAN.PLAYER: pygame.image.load('assets/images/player.png').convert_alpha()

           SOKOBAN.PLAYER: pygame.image.load('assets/images/player_sprites.png').convert_alpha()
       }

    def load_level(self):
        self.level = Level(self.index_level)
        self.board = pygame.Surface((self.level.width, self.level.height))
        if self.player:
            self.player.pos = self.level.position_player
        else:
            self.player = Player(self.level)

    def start(self):
        while self.play:
            self.process_event(pygame.event.wait())
            self.update_screen()

    def process_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                # Quit game
                self.play = False
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT, K_z, K_s, K_q, K_d]:
                # Move player
                self.player.move(event.key, self.level)
                if self.has_win():
                    self.index_level += 1
                    self.scores.save()
                    self.load_level()
            if event.key == K_r:
                # Restart current level
                self.load_level()

    def update_screen(self):
        pygame.draw.rect(self.board, SOKOBAN.WHITE, (0,0, self.level.width * SOKOBAN.SPRITESIZE, self.level.height * SOKOBAN.SPRITESIZE))
        pygame.draw.rect(self.window, SOKOBAN.WHITE, (0,0,SOKOBAN.WINDOW_WIDTH,SOKOBAN.WINDOW_HEIGHT))

        self.level.render(self.board, self.textures)
        self.player.render(self.board, self.textures)

        pox_x_board = (SOKOBAN.WINDOW_WIDTH / 2) - (self.board.get_width() / 2)
        pos_y_board = (SOKOBAN.WINDOW_HEIGHT / 2) - (self.board.get_height() / 2)
        self.window.blit(self.board, (pox_x_board, pos_y_board))

        txt = "Niveau " + str(self.index_level)
        txtLevel = self.font_menu.render(txt, True, (0,0,0), (255,255,255))
        self.window.blit(txtLevel, (10, 10))

        pygame.display.flip()

    def has_win(self):
        nb_missing_target = 0
        for y in range(len(self.level.structure)):
            for x in range(len(self.level.structure[y])):
                if self.level.structure[y][x] == SOKOBAN.TARGET:
                    nb_missing_target += 1

        return nb_missing_target == 0
