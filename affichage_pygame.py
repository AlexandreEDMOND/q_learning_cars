
import pygame
from obstacles import *
from car import *
from ligne_arrivee import *

def init_screen(width=400, height=400):

    pygame.init()
    WINDOW_SIZE = (width, height)
    screen = pygame.display.set_mode(WINDOW_SIZE)

    return screen

def main_loop_pygame(screen):

    level = 1

    list_obstacle = init_obstacle()
    ligne_arrivee = init_ligne_arrivee(level)
    car = init_car()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Récupérer les touches enfoncées
        keys = pygame.key.get_pressed()

        # Mettre à jour les vitesses en fonction des touches enfoncées
        x_speed = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * car.coef_acceleration
        y_speed = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * car.coef_acceleration

        car.change_speed(x_speed, y_speed)

        car.apply_friction()
        car.move_car()
        car.detect_collision(list_obstacle)
        car.detect_finish(ligne_arrivee)

        screen.fill((0, 0, 0))

        display_obstacle(screen, list_obstacle)
        display_ligne_arrivee(screen, ligne_arrivee)
        display_car(screen, car)

        pygame.display.flip()