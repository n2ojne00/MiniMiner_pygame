import pygame
	
pygame.init()

#window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('GAMENAME')

player = pygame.Rect((300, 250, 50, 50))

#start Game loop
run = True
while run == True:
    
    screen.fill((0, 20, 0))
    
    pygame.draw.rect(screen, (80, 130, 100), player)
    
    #keybinds and cordinates
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0) 
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    
    #stop Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
            
pygame.quit()    

#framerate
FPS = pygame.time.Clock()
FPS.tick(60)