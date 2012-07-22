import pygame
class Screen:
    def __init__(self,color):
         self.color = color
         self.block_list = pygame.sprite.RenderPlain()
         self.all_sprites_list = pygame.sprite.RenderPlain()
         self.balls = pygame.sprite.Group()
         self.screen_width, self.screen_height = 400,400
         self.screen=pygame.display.set_mode([self.screen_width,self.screen_height])

    def mainLoop(self,ball,player):
        self.clock=pygame.time.Clock()
        self.ball = ball
        self.player = player
        while 1:
            #another game objects & logic
            player.move()
            ball.move()
            self.quit()
            self.fillAndDraw()
            self.clock.tick(24)

    def get_height(self):
        return self.screen_height

    def quit(self):
         for event in pygame.event.get():
             if event.type == pygame.QUIT: pygame.quit()
   
    def fillAndDraw(self):
        self.screen.fill(self.color)
        self.all_sprites_list.draw(self.screen)
        self.balls.draw(self.screen)
        pygame.display.flip() 
