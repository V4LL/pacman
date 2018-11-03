import pygame, myPacmanSprites
pygame.init()
screen = pygame.display.set_mode((640, 480))

def main():
    '''This function defines the 'mainline logic' for our game.'''
    
    # Display
    pygame.display.set_caption ("pacman")
    
    # Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    chomp = pygame.mixer.Sound("pacman_chomp.ogg")
    chomp.set_volume (0.5)
    
    # Create 10 random bricks
    cherries = []
    for i in range(10):
        cherries.append(myPacmanSprites.Cherry(screen))
         
    pacman = myPacmanSprites.Pacman(screen)
    cherryGroup = pygame.sprite.Group(cherries)
    allSprites = pygame.sprite.Group(cherries, pacman)
    
    # ACTION
         
    # Assign 
    keepGoing = True
    clock = pygame.time.Clock()
        
    # Loop
    while keepGoing:
         
        # Time
        clock.tick(30)
         
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    pacman.go_left()
                elif event.key == pygame.K_RIGHT :
                    pacman.go_right()
                elif event.key == pygame.K_UP :
                    pacman.go_up()
                elif event.key == pygame.K_DOWN :
                    pacman.go_down()
                
        if pygame.sprite.spritecollide(pacman, cherryGroup, True):
            chomp.play()
            
        # Refresh screen
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
             
        pygame.display.flip()
     
    # Close the game window
    pygame.quit()     
           
# Call the main function
main()        