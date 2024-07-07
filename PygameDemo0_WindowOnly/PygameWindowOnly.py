# pygame demo 0 - window only

# 1 - Import packages
import pygame
from pygame.locals import *
import sys

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s), etc.
image = pygame.image.load("space-ship-icon.png")

# Get the dimensions of the image
image_width, image_height = image.get_size()

# 5 - Initialize variables
# Calculate the x and y coordinates to position the image at the bottom center
x_position = (WINDOW_WIDTH - image_width) // 2
y_position = WINDOW_HEIGHT - image_height

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(BLACK)  # Clear the window with a black background
    
    # 10 - Draw all window elements
    window.blit(image, (x_position, y_position))
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)