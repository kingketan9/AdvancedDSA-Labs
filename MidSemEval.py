import pygame
import sys

pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Letter Collision")

# Set up the fonts
font = pygame.font.SysFont(None, 50)

# Set up the letters
letter_a = font.render('A', True, (255, 0, 0))
letter_b = font.render('B', True, (0, 0, 255))

# Set up the letter positions
letter_a_pos = [0, 0]
letter_b_pos = [0, 400 - letter_b.get_height()]

# Set up the letter velocities
letter_a_vel = [1, 1]
letter_b_vel = [1, -1]

# Set up the clock
clock = pygame.time.Clock()

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            letter_b_vel = [1, -1]

    # Move the letters
    letter_a_pos[0] += letter_a_vel[0]
    letter_a_pos[1] += letter_a_vel[1]
    letter_b_pos[0] += letter_b_vel[0]
    letter_b_pos[1] += letter_b_vel[1]

    # Check for collision
    if letter_a_pos[0] + letter_a.get_width() >= letter_b_pos[0] and \
       letter_a_pos[1] + letter_a.get_height() >= letter_b_pos[1]:
        break

    # Draw the letters
    screen.fill((255, 255, 255))
    screen.blit(letter_a, letter_a_pos)
    screen.blit(letter_b, letter_b_pos)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(60)

# Quit pygame
pygame.quit()
