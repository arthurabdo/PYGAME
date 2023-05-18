import pygame  
import os
import random 
pygame.init()


SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 2000
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

CORRER = [pygame.image.load(os.path.join("images", "OtavioRun1.png")),
           pygame.image.load(os.path.join("images", "OtavioRun2.png"))]

PULAR = pygame.image.load(os.path.join("images", "OtavioJump.png"))

BAFOMETRO = [pygame.image.load(os.path.join("images", "Bafometro.png"))]
               
QUATA = pygame.image.load(os.path.join("images", "logoQuata.png"))

BG = pygame.image.load(os.path.join("images", "Chao.png"))


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





def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Otavio()
    cloud = Quata()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Pontos: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (9000, 30)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Bafometro(BAFOMETRO))
      
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.otavio_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Precione qualquer tecla para começar", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Precione qualquer tecla para recomeçar", True, (0, 0, 0))
            score = font.render("Sua pontuação: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(CORRER[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)
