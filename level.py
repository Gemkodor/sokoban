import pygame
import constants as SOKOBAN

class Level:
    def __init__(self, level_to_load):
        self.last_structure_state = []
        self.last_state_index = len(self.last_structure_state)
        self.load(level_to_load)

    def load(self, level):
        self.structure = []
        max_width = 0
        with open("assets/levels/level_" + str(level) + ".txt") as level_file:
            rows = level_file.read().split('\n')

            for y in range(len(rows)):
                level_row = []
                if len(rows[y]) > max_width:
                    max_width = len(rows[y])

                for x in range(len(rows[y])):
                    if rows[y][x] == ' ':
                        level_row.append(SOKOBAN.AIR)
                    elif rows[y][x] == 'X':
                        level_row.append(SOKOBAN.WALL)
                    elif rows[y][x] == '*':
                        level_row.append(SOKOBAN.BOX)
                    elif rows[y][x] == '.':
                        level_row.append(SOKOBAN.TARGET)
                    elif rows[y][x] == '@':
                        level_row.append(SOKOBAN.AIR)
                        self.position_player = [x,y]
                self.structure.append(level_row)

        self.width = max_width * SOKOBAN.SPRITESIZE
        self.height = (len(rows) - 1) * SOKOBAN.SPRITESIZE

    def cancel_last_move(self, player):
        if self.last_structure_state and self.last_state_index > 0:
            self.structure = self.last_structure_state[self.last_state_index - 1]['previous_level_structure']
            player.pos = self.last_structure_state[self.last_state_index - 1]['previous_player_pos']
            self.last_state_index -= 1
        else:
            print("No previous state to load")

    def render(self, window, textures):
        for y in range(len(self.structure)):
            for x in range(len(self.structure[y])):
                if self.structure[y][x] in textures:
                    window.blit(textures[self.structure[y][x]], (x * SOKOBAN.SPRITESIZE, y * SOKOBAN.SPRITESIZE))
                else:
                    if self.structure[y][x] == SOKOBAN.TARGET_FILLED:
                        pygame.draw.rect(window, (0,255,0), (x * SOKOBAN.SPRITESIZE, y * SOKOBAN.SPRITESIZE, SOKOBAN.SPRITESIZE, SOKOBAN.SPRITESIZE))
                    else:
                        pygame.draw.rect(window, SOKOBAN.WHITE, (x * SOKOBAN.SPRITESIZE, y * SOKOBAN.SPRITESIZE, SOKOBAN.SPRITESIZE, SOKOBAN.SPRITESIZE))
