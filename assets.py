import pygame
import os
from config import *

# BG = 'Chao'
# CORRER = 'OtavioRun'
# PULAR = 'OtavioJump'
# BAFOMETRO = 'Obstaculos'
# QUATA = 'logoQuata'

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
    return assets
