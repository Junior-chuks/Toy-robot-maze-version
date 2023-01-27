import heapq
from import_helper import dynamic_import
from world.turtle import world
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
def solve_maze_path(path,end):
    for pair in path:
        continue

    for i in path:
    
        world.t.shape("turtle")
        world.t.shapesize(0.3)
        world.t.speed(1)
        if i[0] ==end[0] and end[1] == i[1]:
            break 
        
        if i == (0,0):
            world.t.penup()
        else:world.t.pendown()
        world.t.goto(i)
        

# Function follows the exact path to the end   
def follow_path(name,direction):

    print("> "+name+" starting maze run..")
    path ,end ,text = get_shortest_path(direction)
    solve_maze_path(path,end)
    return True,text
        
