import pygame, random, math

class Ball(pygame.sprite.Sprite):
    
    def __init__(self, colorBack, colorFront, width, height):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface([width, height])
        self.image.fill(colorBack)
        self.width, self.height = width, height
        self.rect = self.image.get_rect()
        pygame.draw.ellipse(self.image, colorFront, self.rect)
    

class BallBehavior:
    
    speed = 15
    change_x = speed*random.choice((-1,1))
    change_y = speed*random.choice((-1,1))
    direction = 200
    def __init__(self,ball,surface):
        self.surface = surface
        self.ball = ball
        
        surface.balls.add(ball)
        ball.rect.x = surface.screen_width/2+random.randint(-100,100)
        ball.rect.y = surface.screen_height/3
        

    def move(self):
        direction_radians = math.radians(self.direction)
        self.ball.rect.x += self.speed * math.sin(direction_radians)
        self.ball.rect.y -= self.speed * math.cos(direction_radians)
        self.collide()
        
    def bounce(self,diff):
        self.direction = (180-self.direction)%360
        self.direction -= diff
   
    def collide(self):
        sprite = pygame.sprite.spritecollide(self.ball, self.surface.all_sprites_list, False)
        #print(self.surface.player.rect.left)
        
        if len(sprite) is not 0: 
            diff = sprite[0].collide(self.ball)
            #diff = (sprite[0].rect.left + sprite[0].width/2) - (self.ball.rect.left+self.ball.width/2)
            print(diff)
            self.bounce(diff)
        
            #if sprite[0].rect.x < self.ball.rect.x : self.change_x *=-1
