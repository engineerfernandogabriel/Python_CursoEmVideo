#Faça um programa em python que abra e reproduza o áudio de um arquivo mp3

import pygame

pygame.init()

pygame.mixer.load('desafio021.mp3')

pygame.mixer.music.play()

pygame.mixer.wait
