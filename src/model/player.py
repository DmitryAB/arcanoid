from  model.block import *
from  controller.move import *

class Player(Block, Move):

    def __init__(self, color, width, height,surface):
        Block.__init__(self, color, width, height,surface)
        self.width = width
        self.height = height
        self.rect.y = surface.screen_height-height
        surface.all_sprites_list.add(self)

    def collide(self, ball):
        diff = (self.rect.left + self.width/2) - (ball.rect.left+ball.width/2)
        return diff
#    def move(self):
#        self.rect.x = pygame.mouse.get_pos()[0]
