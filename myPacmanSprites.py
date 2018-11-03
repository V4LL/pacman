import pygame, random

class Cherry(pygame.sprite.Sprite):
    
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load ("cherries.gif")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0,screen.get_width())
        self.rect.centery = random.randrange(0,screen.get_height())
        
class Pacman (pygame.sprite.Sprite):
    
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
    
        self.pacman_right = pygame.image.load ("pacman-right.png")
        self.pacman_left = pygame.image.load ("pacman-left.png")
        self.pacman_up = pygame.image.load ("pacman-up.png")
        self.pacman_down = pygame.image.load ("pacman-down.png")
        
        self.image = self.pacman_right.convert()
        self.rect = self.image.get_rect()
        self.rect.left = 320
        self.rect.top = 240
        self.__dx = 5
        self.__dy = 5
        self.__move = "right"
 
    def go_left(self):
        self.image = self.pacman_left
        self.image.convert()
        self.__move = "left"

    def go_right(self):
        self.image = self.pacman_right
        self.image.convert()
        self.__move = "right"

    def go_up(self):
        self.image = self.pacman_up
        self.image.convert()
        self.__move = "up"

    def go_down(self):
        self.image = self.pacman_down
        self.image.convert()
        self.__move = "down"
        
    def update (self):        
        if self.__move == "left":
            self.__dx = -5
            self.__dy = 0
            self.rect.left += self.__dx
            self.rect.top += self.__dy
            if self.rect.centerx < 0:
                self.rect.centerx = 640
                
        elif self.__move == "right":
            self.__dx = 5
            self.__dy = 0
            self.rect.left += self.__dx
            self.rect.top += self.__dy
            if self.rect.centerx > 640:
                self.rect.centerx = 0
                
        elif self.__move == "up":
            self.__dx = 0
            self.__dy = -5
            self.rect.left += self.__dx
            self.rect.top += self.__dy
            if self.rect.centery < 0:
                self.rect.centery = 480
                
        elif self.__move == "down":
            self.__dx = 0
            self.__dy = 5
            self.rect.left += self.__dx
            self.rect.top += self.__dy
            if self.rect.centery > 480:
                self.rect.centery = 0