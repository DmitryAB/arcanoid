import pygame

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height,surface):
        pygame.sprite.Sprite.__init__(self) 
        self.surface = surface
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.width, self.height = width, height
    def collide(self,ball):
        self.surface.all_sprites_list.remove(self)
        return 0

class Blocks:
   
    def __init__(self,color, surface, width=19,height=14):
        self.surface = surface
        for i in range(5):
            for j in range(20):
                block = Block(color, width, height, surface)
 
                block.rect.x = j*(width+1)
                block.rect.y = i*(height+1)

                surface.block_list.add(block) 
                surface.all_sprites_list.add(block) 
