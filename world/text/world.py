# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------
# list of coordinates
from import_helper import dynamic_import
obstacles =  dynamic_import(None)

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0


# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def the_obstacles(co_ordinates,text):
    """
    Displays where the obstacls are displayed as text
    param : co_ordinates
    param : text
    """
    
    position_text=""
    for i in co_ordinates:
        x,y = i[0]+4,i[1]+4
        if i == co_ordinates[-1]:
            position_text+=f"- At position {i[0]},{i[1]} (to {x},{y})"
        else:
            position_text+=f"- At position {i[0]},{i[1]} (to {x},{y})"+"\n"
    if len(position_text)>0:
        print("There are some obstacles:")
        print(position_text)


def show_position(robot_name,command,arg,bool):
    """
    Displays  the current position of the robot.
    param : robot_name
    param : command
    param : arg
    param : bool 
    """
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def update_position(steps,co_ordinates):
    """
    Update the current x and y positions given the current direction, and specific number of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps


    for i in co_ordinates:
        if obstacles.is_path_blocked(new_x,new_y,(i[0],position_x),(i[1],position_y)) == True:
            return False,"Sorry, there is an obstacle in the way."

    if obstacles.is_position_blocked(new_x,new_y) == True:
        return False,"Sorry, there is an obstacle in the way."

    if is_position_allowed(new_x,new_y):
        position_x = new_x
        position_y = new_y
        return True ,"correct"
    return False ,"distance"


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def position():
    return position_x,position_y