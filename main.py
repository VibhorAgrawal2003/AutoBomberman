import pygame
import sys
import time

from values import *
from build import *
from master import *

# Initialize Pygame
pygame.init()

# Main function
def main():
    global LSTOP
    global LPAUSE
    global LKEYS
    global LCOLORS

    # Set up the screen
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(CAPTION)
    create_board()

    # Initial positions for robots
    robots = initialize_robots([])

    # Set up lives for robots
    lives = [1 for i in range(RCNT)]

    # Main loop
    running = True
    paused = False
    ended = False
    step_count = 0

    while running:

        # Draw board & robots
        screen.fill(GRAY)
        draw_board(screen)

        for i in range(RCNT):
            draw_robot(screen, robots[i], COLOR(i))



        # Display keybindings message
        lines = LKEYS.splitlines()
        font = pygame.font.SysFont('arial', 16)
        for i, line in enumerate(lines):
            text = font.render(line, True, BLACK)
            screen.blit(text, (WINDOW_WIDTH - 300, LKEYS_OFFSET_Y + i * LSPACING))

        # Display colorcoding message
        lines = LCOLORS.splitlines()
        for i, line in enumerate(lines):
            text = font.render(line, True, BLACK)
            screen.blit(text, (WINDOW_WIDTH - 300, LCOLORS_OFFSET_Y + i * LSPACING))

        # Display step count
        text = font.render("Step Count: " + str(step_count), True, BLACK)
        screen.blit(text, (WINDOW_WIDTH - 300, LSTEP_OFFSET_Y))



        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

                elif event.key == pygame.K_r:
                    ended = False
                    robots = initialize_robots([])
                    lives = [1 for i in range(RCNT)]
                    step_count = 0

                elif event.key == pygame.K_p:
                    paused = not paused

        if not paused:

            if not ended:

                # End if winner found or limit exceed
                sum = 0
                for i in range(RCNT):
                    sum += lives[i]
                if sum <= 1 or step_count > LIMIT:
                    ended = True

                # Move the robots
                for i in range(RCNT):
                    new_pos = MOVE(robots[i], i)

                    if isvalid(new_pos):
                        robots[i] = new_pos
                    else:
                        robots[i] = None
                        lives[i] = 0

                step_count += 1

            if ended:
                font = pygame.font.SysFont('arial', 16)
                text = font.render(LSTOP, True, BLACK)
                screen.blit(text, (WINDOW_WIDTH - 300, LPAUSE_OFFSET_Y))
        else:
            # Display pause message
            font = pygame.font.SysFont('arial', 16)
            text = font.render(LPAUSE, True, BLACK)
            screen.blit(text, (WINDOW_WIDTH - 300, LPAUSE_OFFSET_Y))

        pygame.display.flip()
        time.sleep(DELAY)

    # Pause the simulation until a key is pressed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    main()
                elif event.key == pygame.K_p:
                    paused = not paused

# Run the window
if __name__ == "__main__":
    main()