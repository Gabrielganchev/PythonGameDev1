import pygame , sys
import math
from classes import *
from process import *
pygame.init()
SCREENWIDTH,SCREENHEIGHT=640,360 # so if we change the screen size we do it from here not from all the down screen sizes
#sets the display
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT),0,32)# fast change
clock = pygame.time.Clock()
FPS =60
total_frames = 0

background = pygame.image.load("images/forest.png")
bug = Bug(0,SCREENHEIGHT-70,     "images/hero2.png")
enemy1 = Enemy(40,100, "images/enemybug1.png")
#fivesecondinterval = FPS * 5



while True:
    #how to close the window
# the closing crap
    process(bug, FPS, total_frames)

    bug.motion(SCREENWIDTH ,SCREENHEIGHT)# the motion for the bug
    enemy1.fly(SCREENWIDTH)# writes the enemy 1
    BugProjectile.movement() # movement of the bug
    Enemy.update_all(SCREENWIDTH,SCREENHEIGHT)
    total_frames += 1 # the frame for the while



    screen.blit(background, (0,0)) # displays the background image
    BaseClass.allsprites.draw(screen)
    BugProjectile.List.draw(screen)# drawns the bug
    pygame.display.flip()

    clock.tick(FPS)


