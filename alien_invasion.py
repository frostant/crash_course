import pygame
import sys

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init();
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien_Invation")
    
    ship = Ship(ai_settings, screen)
    bullets = Group()
    alien = Alien(ai_settings, screen)

    while 1:
        gf.check_events(ai_settings, screen, ship, bullets)  
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()


