from os import path

#pastas com figuras e sons:
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'images')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fnt')

#dados gerais do jogo:
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000
FPS = 60

#estados para controle do fluxo da aplicação:
INIT = 0
GAME = 1
QUIT = 2