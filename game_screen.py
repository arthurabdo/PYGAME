import pygame
from config import FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from assets import load_assets, FUNDO_SOUND, BG
from sprites import Otavio, Quata, Obstaculo, Bafometro
def GAME():
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
            text = font.render("Pressione qualquer tecla para começar", True, (0, 0, 0))
            text = font.render("OTAVIO GAME", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Pressione qualquer tecla para recomeçar", True, (0, 0, 0))
            score = font.render("Sua pontuação: " + str(points), True, (0, 0, 0))
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
                GAME()

    #guardando score
    with open('score.json', 'a') as arquivo_json:
        texto = arquivo_json.write(str(points))
