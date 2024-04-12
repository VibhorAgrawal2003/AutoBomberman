from values import *

# Import all strategies
from strategy import randumb, clone, boxboy

# Copycat strategy
class Copycat:
  def __init__(self):
      self.victim = 0

  # Function to move the robot
  def move_robot(self, current_pos):
      self.victim = (self.victim + 1) % RCNT
      return MOVE(current_pos, self.victim)
  
copycat = Copycat()


# Master functions
def MOVE(pos, k):
    
  if pos == None:
    return None

  if (k == 0):
    return randumb.move_robot(pos)
  
  elif (k == 1):
    return clone.move_robot(pos)
  
  elif (k == 2):
    return boxboy.move_robot(pos)
  
  elif (k == 3):
    return copycat.move_robot(pos)


def COLOR(k):

  if (k == 0):
    return RED
  
  elif (k == 1):
    return BLUE
  
  elif (k == 2):
    return GREEN
  
  elif (k == 3):
    return BLACK