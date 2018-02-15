import pygame
import constants as SOKOBAN

class PlayerInterface:
    def __init__(self, player, level):
        self.player = player
        self.level = level
        self.font_menu = pygame.font.Font('assets/fonts/FreeSansBold.ttf', 18)
        self.txtLevel = "Niveau 1"
        self.txtCancel = "Annuler le dernier coup"

    def click(self, pos_click, level):
        x = pos_click[0]
        y = pos_click[1]

        if x > self.posTxtCancel[0] and x < self.posTxtCancel[0] + self.txtCancelSurface.get_width() \
         and y > self.posTxtCancel[1] and y < self.posTxtCancel[1] + self.txtCancelSurface.get_height():
            level.cancel_last_move(self.player)

    def render(self, window, level):
        self.txtLevel = "Niveau " + str(level)
        self.txtLevelSurface = self.font_menu.render(self.txtLevel, True, SOKOBAN.BLACK, (255,255,255))
        window.blit(self.txtLevelSurface, (10, 10))

        if self.level.last_state_index > 0:
            colorTxtCancel = SOKOBAN.BLACK
        else:
            colorTxtCancel = SOKOBAN.GREY

        self.txtCancelSurface = self.font_menu.render(self.txtCancel, True, colorTxtCancel, (255,255,255))
        self.posTxtCancel = (SOKOBAN.WINDOW_WIDTH - self.txtCancelSurface.get_width() - 10, 10)
        window.blit(self.txtCancelSurface, self.posTxtCancel)
