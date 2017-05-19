import pygame
import time
#pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
#pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("C:\\Users\\rickr\\projects\\ricklon\\etudes\\01-opening-demo.mp3")
pygame.mixer.music.play()
time.sleep(5)

pygame.mixer.music.load('C:\\Users\\rickr\\projects\\ricklon\\etudes\\hadouryu.wav')
pygame.mixer.music.play()
# repeat forever: pygame.mixer.music.play(-1)

time.sleep(5)
pygame.mixer.music.load('C:\\Users\\rickr\\projects\\ricklon\\etudes\\02-player-select.mp3')
pygame.mixer.music.play()
