# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 12:22:12 2019

@author: Fab-Tour
"""

import pygame
from pygame.locals import *
Largeur=800 
Hauteur=600


if __name__=="__main__" :


#### Initialisation de Pygame
    pygame.init()
    #fenetre est une variable qui contient l'affichage ( display)
    fenetre = pygame.display.set_mode((Largeur, Hauteur))
    continuer=True
    while continuer :
       for evenement in pygame.event.get() :
            if evenement.type == QUIT :
                continuer=False
            if evenement.type==KEYDOWN and evenement.key==K_F10 :
                pass
pygame.display.quit()
                