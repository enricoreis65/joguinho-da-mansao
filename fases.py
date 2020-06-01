import pygame, sys
import random
from os import path
from pygame.locals import *
from mapa import BLOCK,EMPTY,MAP1,MAP2,Tile
from imagens import *
from medidas import *
from code import blocks,all_sprites
def fases_manipula(nivel_da_fase):
    if nivel_da_fase==1:
        for row in range(len(MAP1)):
            for column in range(len(MAP1[row])):
                tile_type = MAP1[row][column]
                if tile_type == BLOCK:
                    tile = Tile(assets[tile_type], row, column)
                    all_sprites.add(tile)
                    blocks.add(tile)

    elif nivel_da_fase==2:
        for row in range(len(MAP2)):
            for column in range(len(MAP2[row])):
                tile_type = MAP2[row][column]
                if tile_type == BLOCK:
                    tile = Tile(assets[tile_type], row, column)
                    all_sprites.add(tile)
                    blocks.add(tile)
        
        
