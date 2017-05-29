# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 00:07:42 2017
@author: Gustavo Leon Sazo
"""
import sys, os
import pygame
#=================Constants====================
WIDTH = 640
HEIGHT = 480
FPS = 60
TITLE = "Prison xCape"
FONT_NAME = "m04fatalfuryblack"

#================Player properties=============
PLAYER_GRAV = 0.8
THICKNESS = 30

#=================Colors=======================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
GRAY = (27, 27, 27)
LEVEL_ONE_COLOR = (35, 21, 21)

#==============Importing images================
def load_image(nombre, dir_imagen, alpha=False):
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
    if alpha is True:
        image = image.convert_alpha()
        pass
    else:
        image = image.convert()
    return image
    
class SpriteSheet:
    sprite_sheet = None

    def __init__(self, file_name):
        ruta = os.path.join("imagenes", file_name)
        self.sprite_sheet = pygame.image.load(ruta).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height])
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(WHITE)
        return image