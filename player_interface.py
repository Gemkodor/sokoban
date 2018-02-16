import pygame
import constants as SOKOBAN

class PlayerInterface:
    def __init__(self, player, level):
        self.player = player
        self.level = level
        self.mouse_pos = (-1,-1)
        self.font_menu = pygame.font.Font('assets/fonts/FreeSansBold.ttf', 18)
        self.txtLevel = "Niveau 1"
        self.colorTxtLevel = SOKOBAN.BLACK
        self.txtCancel = "Annuler le dernier coup"
        self.colorTxtCancel = SOKOBAN.GREY
        self.txtReset = "Recommencer le niveau"
        self.colorTxtReset = SOKOBAN.BLACK

    def click(self, pos_click, level, game):
        x = pos_click[0]
        y = pos_click[1]

        # Cancel last move
        if x > self.posTxtCancel[0] and x < self.posTxtCancel[0] + self.txtCancelSurface.get_width() \
         and y > self.posTxtCancel[1] and y < self.posTxtCancel[1] + self.txtCancelSurface.get_height():
            level.cancel_last_move(self.player, self)
            self.colorTxtCancel = SOKOBAN.GREY

        # Reset level
        if x > self.posTxtReset[0] and x < self.posTxtReset[0] + self.txtResetSurface.get_width() \
        and y > self.posTxtReset[1] and y < self.posTxtReset[1] + self.txtResetSurface.get_height():
            game.load_level()

    def setTxtColors(self):
        pass

    def render(self, window, level):
        self.txtLevel = "Niveau " + str(level)
        self.txtLevelSurface = self.font_menu.render(self.txtLevel, True, self.colorTxtLevel, SOKOBAN.WHITE)
        window.blit(self.txtLevelSurface, (10, 10))

        self.txtCancelSurface = self.font_menu.render(self.txtCancel, True, self.colorTxtCancel, SOKOBAN.WHITE)
        self.posTxtCancel = (SOKOBAN.WINDOW_WIDTH - self.txtCancelSurface.get_width() - 10, 10)
        window.blit(self.txtCancelSurface, self.posTxtCancel)

        self.txtResetSurface = self.font_menu.render(self.txtReset, True, self.colorTxtReset, SOKOBAN.WHITE)
        self.posTxtReset = ((SOKOBAN.WINDOW_WIDTH / 2) - (self.txtResetSurface.get_width() / 2), 10)
        window.blit(self.txtResetSurface, self.posTxtReset)
