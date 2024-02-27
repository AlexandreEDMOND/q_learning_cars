import pygame

def init_ligne_arrivee(niveau):

    if niveau == 1:
        return arrivee_niveau_1()
    
    print("Problème dans la fonction init_ligne_arrivee")
    exit(1)


def display_ligne_arrivee(screen, ligne_arrivee):
    pygame.draw.rect(screen, (0, 255, 0), ligne_arrivee)


def arrivee_niveau_1():
    return pygame.Rect(530, 500, 460, 20)