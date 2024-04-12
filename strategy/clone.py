import random

# Function to move the robot
def move_robot(current_pos):
    x, y = current_pos
    direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
    new_pos = (x + direction[0], y + direction[1])

    return new_pos