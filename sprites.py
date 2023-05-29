import random
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from assets import BG, CORRER, PULAR, BAFOMETRO, QUATA, FUNDO_SOUND
#CLASSES  
class Otavio:
    X_POS = 200
    Y_POS = 270
    JUMP_VEL = 8.5

    def __init__(self):
        self.corre_img = CORRER
        self.pulo_img = PULAR

        self.otavio_run = True
        self.otavio_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.corre_img[0]
        self.otavio_rect = self.image.get_rect()
        self.otavio_rect.x = self.X_POS
        self.otavio_rect.y = self.Y_POS

    def update(self, userInput):
        if self.otavio_run:
            self.run()
        if self.otavio_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.otavio_jump:
            self.otavio_run = False
            self.otavio_jump = True
        elif not (self.otavio_jump or userInput[pygame.K_DOWN]):
            self.otavio_run = True
            self.otavio_jump = False

    
    def run(self):
        self.image = self.corre_img[self.step_index //  5]
        self.otavio_rect = self.image.get_rect()
        self.otavio_rect.x = self.X_POS
        self.otavio_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.pulo_img
        if self.otavio_jump:
            self.otavio_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.otavio_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.otavio_rect.x, self.otavio_rect.y))


class Quata:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = QUATA
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstaculo:
    def __init__(self, image, type):
        self.image = image
        print('estou printando', self.type, self.image)
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class Bafometro(Obstaculo):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

