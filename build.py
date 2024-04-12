import pygame
import random
from values import *



# Function to create the board
def create_board():
    return [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]



# Function to check if position is valid on the board
def isvalid(current_pos):
    if current_pos == None:
        return None
    return 0 <= current_pos[0] < BOARD_SIZE and 0 <= current_pos[1] < BOARD_SIZE



# Function to generate starting positions for all robots
def get_random_valid_position(all_positions):
    valid_positions = [(x, y) for x in range(BOARD_SIZE) for y in range(BOARD_SIZE) if (x, y) not in all_positions]
    return random.choice(valid_positions)



# Function to place all robots on their starting positions
def initialize_robots(robots):

    robots = []
    for i in range(RCNT):
        robots.append(get_random_valid_position(robots))
    
    return robots




# Function to draw the board
def draw_board(screen):
    screen.fill(GRAY)
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            rect = pygame.Rect(BOARD_OFFSET_X + x * TILE_SIZE, BORDER_SIZE + y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)
    pygame.draw.rect(screen, BLACK, (BOARD_OFFSET_X, BORDER_SIZE, TILE_SIZE * BOARD_SIZE, TILE_SIZE * BOARD_SIZE), 3)



# Function to draw the robot
def draw_robot(screen, pos, col):

    if (pos == None):
        return

    x, y = pos
    pygame.draw.circle(screen, col, (BOARD_OFFSET_X + x * TILE_SIZE + TILE_SIZE // 2, BORDER_SIZE + y * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 3)