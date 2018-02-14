from pygame.locals import *
import constants as SOKOBAN

class Player:
    def __init__(self, level):
        self.pos = level.position_player

    def move(self, direction, level):
        x = self.pos[0]
        y = self.pos[1]

        if direction == K_LEFT or direction == K_q:
            if x > 0 and level.structure[y][x - 1] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                # Player just move on an empty case to the left
                self.pos[0] -= 1
            elif x > 1 and level.structure[y][x - 1] in [SOKOBAN.BOX, SOKOBAN.TARGET_FILLED] and level.structure[y][x - 2] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                # Player is trying to push a box to the left
                if level.structure[y][x - 1] == SOKOBAN.TARGET_FILLED:
                    level.structure[y][x - 1] = SOKOBAN.TARGET
                else:
                    level.structure[y][x - 1] = SOKOBAN.AIR

                if level.structure[y][x - 2] == SOKOBAN.TARGET_FILLED:
                    level.structure[y][x - 2] = SOKOBAN.TARGET
                elif level.structure[y][x - 2] == SOKOBAN.TARGET:
                    level.structure[y][x - 2] = SOKOBAN.TARGET_FILLED
                else:
                    level.structure[y][x - 2] = SOKOBAN.BOX

                self.pos[0] -= 1

        if direction == K_RIGHT or direction == K_d:
            if level.structure[y][x + 1] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                self.pos[0] += 1
            elif level.structure[y][x + 1] in [SOKOBAN.BOX, SOKOBAN.TARGET_FILLED] and level.structure[y][x + 2] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                # Player is trying to push a box to the right
                if level.structure[y][x + 1] == SOKOBAN.TARGET_FILLED:
                    level.structure[y][x + 1] = SOKOBAN.TARGET
                else:
                    level.structure[y][x + 1] = SOKOBAN.AIR

                if level.structure[y][x + 2] == SOKOBAN.TARGET_FILLED:
                    level.structure[y][x + 2] = SOKOBAN.TARGET
                elif level.structure[y][x + 2] == SOKOBAN.TARGET:
                    level.structure[y][x + 2] = SOKOBAN.TARGET_FILLED
                else:
                    level.structure[y][x + 2] = SOKOBAN.BOX

                self.pos[0] += 1

        if direction == K_UP or direction == K_z:
            if y > 0 and level.structure[y - 1][x] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                self.pos[1] -= 1
            elif y > 1 and level.structure[y - 1][x] in [SOKOBAN.BOX, SOKOBAN.TARGET_FILLED] and level.structure[y - 2][x] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                # Player is trying to push a box to the left
                if level.structure[y - 1][x] == SOKOBAN.TARGET_FILLED:
                    level.structure[y - 1][x] = SOKOBAN.TARGET
                else:
                    level.structure[y - 1][x] = SOKOBAN.AIR

                if level.structure[y - 2][x] == SOKOBAN.TARGET_FILLED:
                    level.structure[y - 2][x] = SOKOBAN.TARGET
                elif level.structure[y - 2][x] == SOKOBAN.TARGET:
                    level.structure[y - 2][x] = SOKOBAN.TARGET_FILLED
                else:
                    level.structure[y - 2][x] = SOKOBAN.BOX

                self.pos[1] -= 1

        if direction == K_DOWN or direction == K_s:
            if level.structure[y + 1][x] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                self.pos[1] += 1
            elif level.structure[y + 1][x] in [SOKOBAN.BOX, SOKOBAN.TARGET_FILLED] and level.structure[y + 2][x] in [SOKOBAN.AIR, SOKOBAN.TARGET]:
                # Player is trying to push a box to the left
                if level.structure[y + 1][x] == SOKOBAN.TARGET_FILLED:
                    level.structure[y + 1][x] = SOKOBAN.TARGET
                else:
                    level.structure[y + 1][x] = SOKOBAN.AIR

                if level.structure[y + 2][x] == SOKOBAN.TARGET_FILLED:
                    level.structure[y + 2][x] = SOKOBAN.TARGET
                elif level.structure[y + 2][x] == SOKOBAN.TARGET:
                    level.structure[y + 2][x] = SOKOBAN.TARGET_FILLED
                else:
                    level.structure[y + 2][x] = SOKOBAN.BOX

                self.pos[1] += 1

    def render(self, window, textures):
        window.blit(textures[SOKOBAN.PLAYER], (self.pos[0] * SOKOBAN.SPRITESIZE, self.pos[1] * SOKOBAN.SPRITESIZE))
