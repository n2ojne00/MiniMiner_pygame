import pygame
	
pygame.init()

#window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('GAMENAME')

#start Game loop
run = True
while run == True:
    
    #stop Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()    

#framerate
FPS = pygame.time.Clock()
FPS.tick(60)