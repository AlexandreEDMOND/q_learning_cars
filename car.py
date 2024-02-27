import pygame

position_depart_default = (200, 500)

class Car:
    def __init__(self, position_depart):
        self.x = position_depart[0]
        self.y = position_depart[1]
        self.largeur = 50
        self.color = (0, 0, 255)
        self.x_speed = 0
        self.y_speed = 0
        self.coef_acceleration = 0.005
        self.coef_frottements = 0.001
    
    def move_car(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def change_speed(self, x_value, y_value, limit=100):
        self.x_speed += x_value
        self.y_speed += y_value
        if self.x_speed > limit:
            self.x_speed = limit
        if self.y_speed > limit:
            self.y_speed = limit

    def apply_friction(self):
        self.x_speed += -sign(self.x_speed)*self.coef_frottements
        self.y_speed += -sign(self.y_speed)*self.coef_frottements
    
    def detect_collision(self, list_obstacle):
        rect_car = pygame.Rect(self.x, self.y, self.largeur, self.largeur)
        for obstacle in list_obstacle:
            if rect_car.colliderect(obstacle):
                self.reset()
    
    def detect_finish(self, ligne_arrivee):
        rect_car = pygame.Rect(self.x, self.y, self.largeur, self.largeur)
        if rect_car.colliderect(ligne_arrivee):
            self.reset()

    def reset(self):
        self.__init__(position_depart_default)

def sign(x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

def init_car():
    return Car(position_depart_default)


def display_car(screen, car):
    pygame.draw.rect(screen, car.color, pygame.Rect(car.x, car.y, car.largeur, car.largeur))