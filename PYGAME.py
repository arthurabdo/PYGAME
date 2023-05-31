import pygame  
import os
import random 
pygame.init()

#TELA
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#IMAGENS:
#Lista com as duas imagens do Otavio correndo:
CORRER = [pygame.image.load(os.path.join("images", "OtavioRun1.png")),
           pygame.image.load(os.path.join("images", "OtavioRun2.png"))]
#imagem pulando
PULAR = pygame.image.load(os.path.join("images", "OtavioJump.png"))
#imagens do bafometro, agua e policia usados como obstáculos
BAFOMETRO = [pygame.image.load(os.path.join("images", "Bafometro.png")),
            pygame.image.load(os.path.join("images", "policia.png")),
            pygame.image.load(os.path.join("images", "agua.png"))]
#logo do quata que é usado como nuvem:              
QUATA = pygame.image.load(os.path.join("images", "logoQuata.png"))
#Imagem de fundo
BG = pygame.image.load(os.path.join("images", "Chao.png"))

#Upload da música usada como fundo: 
pygame.mixer.music.load('snd/Musica_fundo_otavio.wav')
pygame.mixer.music.set_volume(0.4)

#Fontes dos textos:
font_g = pygame.font.SysFont(None, 48)
font_m = pygame.font.SysFont(None, 30)


#CLASSES:
# Classe do Oatvio (personagem principal):  
class Otavio:
    #Define pósições
    X_POS = 200
    Y_POS = 270
    #define velocidade do pulo
    JUMP_VEL = 8.5

    #Cria os selfs
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

    #Cria o update do Otavio no jogo:
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
        elif not (self.otavio_jump):
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





def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
      
    clock = pygame.time.Clock()
    player = Otavio()
    cloud = Quata()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    run = True
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

    pygame.mixer.music.play(loops=-1)
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
    username = ''
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Pressione qualquer tecla para começar", True, (0, 0, 0))
            text = font.render("OTAVIO GAME", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Pressione ENTER para recomeçar", True, (0, 0, 0))
            score = font.render("Sua pontuação: " + str(points), True, (0, 0, 0))
            text = font_g.render('Digite o seu username!', True, (0, 0, 0))
            SCREEN.blit(text, (300, 200))
                        
            text = font_m.render('Depois pressione ENTER para recomeçar', True, (0, 0, 0))
            SCREEN.blit(text, (300, 250))

            text = font_g.render(f'{username}', True, (0, 0, 0))
            

            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if death_count == 0 :
                    main()
                else:
                    if event.key == pygame.K_RETURN:
                        with open('score.txt', 'a') as arquivo:
                                conteudo = f'{username} - {points}\n'
                                arquivo.write(conteudo)

                        main()
                    elif event.key == pygame.K_BACKSPACE and len(username) > 0:
                        # Quando usuário aperta a tecla para apagar o texto
                        username = username[:len(username)-1]                    
                    else:
                        # Concatena a letra digitada pelo jogador
                        username += event.unicode

      
                

    pygame.quit()

menu(death_count=0)
