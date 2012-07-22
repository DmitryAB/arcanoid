from view.screen import *
from model.ball import *
from model.block import *
from model.walls import *
from model.player import *

s = Screen((0,0,0))
p = Player((200,200,200),50,15,s)
ws = Walls(s)
bs = Blocks((200,200,200),s)
b = BallBehavior(Ball((0,0,0),(255,255,255),15,15),s)
s.mainLoop(b,p)

