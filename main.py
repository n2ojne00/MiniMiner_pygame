import pygame
	
pygame.init()

#window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('GAMENAME')

player = pygame.Rect((400, 350, 50, 80))

#start Game loop
run = True
while run == True:
    
    #background color
    screen.fill((0, 20, 0))
    
    pygame.draw.rect(screen, (80, 130, 100), player)
    
    
    #keybinds and coordinates
    key = pygame.key.get_pressed()
        #UP
    if key[pygame.K_w] == True and player[1] >= 0: 
        player.move_ip(0, -1)
        #DOWN
    elif key[pygame.K_s] == True and player[1] <= SCREEN_HEIGHT - player[3]:
        player.move_ip(0, 1)    
        #LEFT
    elif key[pygame.K_a] == True and player[0] >= 0: 
        player.move_ip(-1, 0) 
        #RIGHT
    elif key[pygame.K_d] == True and player[0] <= SCREEN_WIDTH - player[2]: 
        player.move_ip(1, 0)
    


    #stop Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
            
pygame.quit()    

#framerate
FPS = pygame.time.Clock()
FPS.tick(60)