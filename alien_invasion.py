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
    aliens = Group()
    alien = Alien(ai_settings, screen)
    stars = Group()

    gf.create_star(ai_settings, screen, stars)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while 1:
        gf.check_events(ai_settings, screen, ship, bullets)  
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, stars, bullets)
        

run_game()


