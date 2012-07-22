import pygame

class Wall(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
    def collide(self, ball):
        return 0

class LeftWall(Wall):
    def __init__(self,color,surface):
        Wall.__init__(self,color,1,surface.screen_height)
        self.surface = surface
    def collide(self,ball):
        return 180

class RightWall(LeftWall):
    pass

class LowerWall(Wall):
    def __init__(self,color,surface):
        Wall.__init__(self,color,surface.screen_width,1)
        self.surface = surface
    def collide(self, ball):
        pygane.quit()
class UpperWall(Wall):
    def __init__(self,color,surface):
        Wall.__init__(self,color,surface.screen_width,1)
        self.surface = surface

class Walls:

    def __init__(self,surface):
        self.surface = surface
        self.rightWall, self.leftWall = RightWall((255,0,0),surface),LeftWall((255,0,0),surface) #change color
        self.leftWall.rect.x, self.leftWall.rect.y = 1, 1
        self.rightWall.rect.x, self.rightWall.rect.y = surface.screen_width-1, 1
        self.lowerWall , self.upperWall = LowerWall((255,0,0),surface),UpperWall((255,0,0),surface)
        self.upperWall.rect.x, self.upperWall.rect.y = 1,1
        self.lowerWall.rect.x, self.lowerWall.rect.y = 1, surface.screen_height-1
    #    self.addInGroup([self.leftWall, self.rightWall, self.upperWall, self.lowerWall])
    
    #def addInGroup(self,spriteList):
        for sprite in [self.leftWall, self.rightWall, self.upperWall, self.lowerWall]:
            surface.all_sprites_list.add(sprite)
