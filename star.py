import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    def __init__(self, ai_settings, screen):
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/zuo.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = randint(self.rect.width, 20*self.rect.width)
        self.rect.y = self.rect.height
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)


