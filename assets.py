import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR, SCREEN_WIDTH, SCREEN_HEIGHT

BG = 'Chao'
CORRER = ['OtavioRun1', 'OtavioRun2']
PULAR = 'OtavioJump'
BAFOMETRO = ['Bafometro', 'policia', 'agua']
QUATA = 'logoQuata'
FUNDO_SOUND = 'musicafundo_otavio'
def load_assets():
    assets = {}
    assets[BG] = pygame.image.load(os.path.join("images", "Chao.png"))
    assets[CORRER] = [pygame.image.load(os.path.join("images", "OtavioRun1.png")),
           pygame.image.load(os.path.join("images", "OtavioRun2.png"))]
    assets[PULAR] = pygame.image.load(os.path.join("images", "OtavioJump.png"))
    assets[BAFOMETRO] = [pygame.image.load(os.path.join("images", "Bafometro.png")),
            pygame.image.load(os.path.join("images", "policia.png")),
            pygame.image.load(os.path.join("images", "agua.png"))]
    assets[QUATA] = pygame.image.load(os.path.join("images", "logoQuata.png"))
    run_anim = []
    for i in range(2):
        filename = os.path.join(IMG_DIR, 'OtavioRun1{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        run_anim.append(img)
    assets[CORRER] = run_anim

    #carrega sons:
    pygame.mixer.music.load(os.path.join(SND_DIR))
    pygame.mixer.music.set_volume(0.4)
    assets[FUNDO_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'musicafundo_otavio.wav'))