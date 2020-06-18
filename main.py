import pygame
import random
from pygame.locals import *
import sys
from ship import Ship

pygame.init()

screen_info = pygame.display.Info()

#set screen
screen_size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
color = (0, 127, 255)

player = Ship((20, 100))

def main():
  while True:
    clock.tick(60)
    screen.fill(color)
    screen.blit(player.image, player.rect)
    pygame.display.flip()

if __name__ == '__main__':
  main()