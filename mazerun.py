import heapq
import sys
from import_helper import dynamic_import


if  len(sys.argv) == (3) or (len(sys.argv) == (2) and sys.argv[-1] != "text" ):
    if sys.argv[-1] == "turtle" or sys.argv[1] == "turtle" :
        from world.turtle import world
else:
    from world.text import world


# imports the correct module according to the user's input
b = dynamic_import(None)

obstacle = b.get_obstacles()

def get_shortest_path(direc):
    global obstacle

    text = ""
    start = (0,0)
    #get the end point
    end = get_end_point(direc)
    # Create a priority queue to store the next nodes to visit
    heap = [(0, start)]
    # Create a dictionary to store the cost of visiting each node
    cost = {start: 0}
    # Create a dictionary to store the parent of each node
    parent = {start: None}
    # Create a set to store the visited nodes
    visited = []
    # Create a list of directions (up, down, left, right)
    dirs = [(0, 5), (0, -5), (5, 0), (-5, 0)]

    # checks the direction of mazerun to return the correct text
    if direc.lower() == "bottom":
        text += 'I am at the bottom edge'

    elif direc.lower() == "left":
        text += 'I am at the left edge'

    elif direc.lower() == "right":
        text += 'I am at the right edge'

    else:
        text += 'I am at the top edge'
    
    while heap:
        # Get the node with the lowest cost
        curr_cost, curr_pos = heapq.heappop(heap)

        # If the current position is equivalent the end, return the path
        if  curr_pos[1] == 200 or curr_pos[1] == -200 or curr_pos[0] == 100 or curr_pos[0] == -100 :
            end = curr_pos
            return path(parent, end)[-1::-1],end,text

        # If the current position has been visited, skip it
        if curr_pos in visited:
            continue

        visited.append(curr_pos)

        # Check the neighboring nodes
        for dx, dy in dirs:
            n = False
            x, y = curr_pos
            new_x, new_y = x + dx, y + dy

            # If the new x and y position is out of bounds or blocked, skip it
            if not (-100 <= new_x < 101 and -200 <= new_y < 201):
                continue
            
            if b.is_position_blocked(new_x,new_y):
                    continue
            # Calculate the new cost
            new_cost = cost[curr_pos] + 1
            # If the new cost is lower than the existing cost, update it
            if new_cost < cost.get((new_x, new_y), float("inf")):
                cost[(new_x, new_y)] = new_cost
                priority = new_cost + manhattan_distance(end, (new_x, new_y))
                heapq.heappush(heap, (priority, (new_x, new_y)))
                parent[(new_x, new_y)] = curr_pos
    
    # If the heap is empty, return None (no path was found)
    return 


# Function helps to calculate the Manhattan distance (heuristic)
def manhattan_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)


# Function helps to construct the path from the parent dictionary
def path(parent, end):
    curr = end
    path = []
    while curr:
        path.append(curr)
        curr = parent[curr]
    return path


def get_y_path_end(obstacle,direc):
    y = ...
    #finding the axis end point with  a constant y value
    if direc == "bottom":y= -200
    elif direc == "top" or len(direc) == 0: y = 200
    end = None
    for x in range(-100,101,5):
        if not (x+5,y) in obstacle:
            end = (x+5,y)
            break
    return end


def get_x_path_end(obstacle,direc):
    x = ...
    #finding the axis end point with a constant x value
    if direc == "left":x= -100
    elif direc == "right": x = 100
    end = None
    for y in range(-200,201,5):
        if not (x,y+5) in obstacle:
            end = (x,y+5)
            break
    return end

       
def get_end_point(direct):
    global obstacle
    
    if direct == "left" or direct =="right":
        return get_x_path_end(obstacle,direct)
    elif direct == "top" or direct == "bottom" or len(direct) == 0 :
        return get_y_path_end(obstacle,direct)
    

# Function finds the shortest path
def solve_maze_path(path,end,direc):
    
    for i in path:
        
        world.t.setheading(90)
        world.t.shape("turtle")
        world.t.shapesize(0.3)
        world.t.speed(1)
        if i[0] ==end[0] and end[1] == i[1]:
            break 
        
        if i == (0,0):
            world.t.penup()
        else:world.t.pendown()
        world.t.goto(i)
        world.position_x ,world.position_y = i

    if direc == "left" :
        world.t.left(90)
        world.current_direction_index -= 1
        if world.current_direction_index < 0:
            world.current_direction_index = 3

    elif direc == "right":
        world.t.right(90)
        world.current_direction_index += 1
        if world.current_direction_index > 3:
            world.current_direction_index = 0

    for m in range(2):
        if direc == "bottom":
            world.t.left(90)
            world.current_direction_index += 1
            if world.current_direction_index > 3:
                world.current_direction_index = 0
    

def solve_maze_path_text_v(name,path,end):
    for pair in path:
        continue

    x,y=0,0
    n = "N"
    q = 0
    no_steps = 0


    for i in path:
    
        if i[0] < x  and i[1] == y and n == "N" and q == 0:
            do_left_turn(name)
            print(' > '+name+' moved forward by '+str(no_steps*5)+' steps.')
            world.show_position(name,"","","")
            n = "W"
            q -=1
            no_steps = 0
                    
        elif i[0] > x and i[1] == y and n == "N" and q == 0:
            do_right_turn(name)
            print(' > '+name+' moved forward by '+str(no_steps*5)+' steps.')
            world.show_position(name,"","","")
            n = "E"
            q+=1
            no_steps = 0

        elif i[1] < y and i[0] == x and n == "E" and q == 1:
            do_right_turn(name)
            print(' > '+name+' moved forward by '+str(no_steps*5)+' steps.')
            world.show_position(name,"","","")
            n = "S"
            q += 1
            no_steps = 0

        elif i[1] > y and i[0] == x and n == "E" and  q == 1:
            do_left_turn(name)
            print(' > '+name+' moved forward by '+str(no_steps*5)+' steps.')
            world.show_position(name,"","","")
            n = "N"
            q-=1
            no_steps = 0

        elif i[1] > y and i[0] == x and n == "W" and (q == -1 or q == 3 ):
            do_right_turn(name)
            print(' > '+name+' moved forward by '+str(no_steps*5)+' steps.')
            world.show_position(name,"","","")
            n = "N"
            q+=1
            no_steps = 0

        elif i[1] < y and i[0] == x and n == "W" and (q == -1 or q == 3 ) :
            do_left_turn(name)
            print(' > '+name+' moved forward by '+str(no_steps*5)+' steps.')
            world.show_position(name,"","","")
            n = "S"
            q -=1
            no_steps = 0

        elif i[0] > x  and i[1] == y and n == "S" and (q == 2 or q == -3):
            do_left_turn(name)
            print(' > '+name+' moved forward by '+str(no_steps*5)+' steps.')
            world.show_position(name,"","","")
            n = "E"
            q-=1
            no_steps = 0
                    
        elif i[0] < x and i[1] == y and n == "S" and (q == 2 or q == 3):
            do_right_turn(name)
            print(' > '+name+' moved forward by '+str(no_steps*5)+' steps.')
            world.show_position(name,"","","")
            n = "W"
            q+=1
            no_steps = 0

        else:
            no_steps +=1

        x,y = i

        world.position_x = x
        world.position_y = y

        if  x == end[0] and y == end[1]:
            print(' > '+name+' moved forward by '+str(no_steps*5)+' steps.')
            world.show_position(name,"","","")
            print(''+name+': Sorry, I cannot go outside my safe zone.')


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """

    world.current_direction_index -= 1
    if world.current_direction_index < 0:
        world.current_direction_index = 3

    print(' > '+robot_name+' turned left.')


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """

    world.current_direction_index += 1
    if world.current_direction_index > 3:
        world.current_direction_index = 0

    print(' > '+robot_name+' turned right.')


# Function follows the exact path to the end   
def follow_path(name,direction):

    print(" > "+name+" starting maze run..")
    path ,end ,text = get_shortest_path(direction)
    if  len(sys.argv) == (3) or (len(sys.argv) == (2) and sys.argv[-1] != "text" ):
        if sys.argv[-1] == "turtle" or sys.argv[1] == "turtle" :
            solve_maze_path(path,end,direction)
            
    else:
        solve_maze_path_text_v(name,path,end)
    return True,text


if __name__ == "__main__":
    paths ,end ,text = get_shortest_path("left")
    solve_maze_path(paths,end,"left")
    paths ,end ,text = get_shortest_path("bottom")
    solve_maze_path(paths,end,"bottom")
    paths ,end ,text = get_shortest_path("top")
    solve_maze_path(paths,end,"top")
    # print(paths)