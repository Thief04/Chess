import pygame
import os
import random
import math
import sys
import neat

# Initializing Pygame
pygame.init()
  
# Initializing surface
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
# Initialing RGB Color 
color = (0,0,255)
  
# Changing surface color
SCREEN.fill(color)
pygame.display.flip()

