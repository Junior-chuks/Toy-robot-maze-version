# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------
import random


def create_random_obstacles():
    """
    Generates a list that stores a random number tuples that store randomly generated co_ordinates x,y.
    returns a list of tuples that store co_ordinates. 
    """
    num_coord = random.randint(0,10)
    
    co_ordinates = [(random.randint(-100,100),random.randint(-200,200)) for i in range(num_coord)]
    
    return [num for num in co_ordinates[:num_coord]]


def is_position_blocked(x, y):
    """
    Checks if the position is blocked.
    """
    
    obstacles = get_obstacles()
    return True if (x,y) in obstacles else False


def is_path_blocked(x1, y1, x2, y2):
    """Checks if the path-way is blocked
        returns True.
    """
    
    side = (x2[0] + 4)
    top =  (y2[0] + 4)
    
    # Checks which side of the obstacle the robot is and if it wishes to pass through the obstacle
    if (x2[0] < x1 < (x2[0] + 4)) and (y2[0] <= y1 or y1 >= (y2[0] + 4) ) and (y2[1] <= y2[0])  :
        return True
    elif (x2[0] < x1 < (x2[0] + 4)) and ( y2[0] >= y1 or y1 <= (y2[0] + 4)) and  (top <= y2[1]) :
        return True
    elif y2[0] < y1 < (y2[0] + 4) and (x2[0] <= x1  or x1 >= (x2[0] + 4)) and (x2[0] >= x2[1]):
        return True
    elif y2[0] < y1 < (y2[0] + 4) and ( x2[0] >= x1  or x1 <= (x2[0] + 4)) and  (side <= x2[1]):
        return True


def get_obstacles():
    obstacles = create_random_obstacles()
    return obstacles