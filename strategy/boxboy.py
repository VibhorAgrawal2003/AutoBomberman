direction = 0

# Function to move the robot
def move_robot(current_pos):
    x, y = current_pos

    global direction
    direction = (direction + 1) % 4

    if direction == 0:
      return (x, y - 2)
    
    elif direction == 1:
      return (x + 2, y)
    
    elif direction == 2:
      return (x, y + 2)
    
    elif direction == 3:
      return (x - 2, y)