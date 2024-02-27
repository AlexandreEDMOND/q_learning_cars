import pygame

def init_obstacle():
    list_obstacle = []

    # Ajout des contours en rouge
    list_obstacle.append(pygame.Rect(0, 0, 1000, 10))
    list_obstacle.append(pygame.Rect(0, 0, 10, 700))
    list_obstacle.append(pygame.Rect(990, 0, 10, 700))
    list_obstacle.append(pygame.Rect(0, 690, 1000, 10))

    # Ajout du obstacle niveau 1
    list_obstacle = obstacle_niveau_1(list_obstacle)

    return list_obstacle


def obstacle_niveau_1(list_obstacle):
    list_obstacle.append(pygame.Rect(470, 300, 60, 400))

    return list_obstacle


def display_obstacle(screen, list_obstacle):
    for obstacle in list_obstacle:
        pygame.draw.rect(screen, (255, 0, 0), obstacle)