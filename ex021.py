# Faça um programa em python que abra e reproduza o áudio de um arquiv mp3.

import pygame 
import time

pygame.init()
pygame.mixer.init()

musica_fundo = pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(-1)

while True:
    time.sleep(1)