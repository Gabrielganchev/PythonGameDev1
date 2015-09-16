import pygame , sys
pygame.init()

print "it worked !"
#sets the display
screen = pygame.display.set_mode((640, 360),0,32)

#clock = pygame.time.Clock()
#FPS = 24
#fivesecondinterval = FPS * 5
#totalframes = 0


clr1 = (22,122,221)
clr2 = (0, 44 , 166)
clr3 = (34,55,245)
color_change = 0
#Processes , always runs the game

while True:
        #how to close the window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        color_change +=1 # loop so we change the color for the background
        if color_change >255:
                color_change%=255

        #totalframes += 1

        screen.fill((color_change,color_change,color_change)) # changes the background color with the loop above

        pygame.draw.line(screen, clr2, (0,0),(640, 360))
        pygame.draw.rect(screen, clr3,(40,40,300,45))
        pygame.draw.circle(screen, clr1,(350,200),80, 40 )

        pygame.display.flip()

        #clock.tick(FPS)
