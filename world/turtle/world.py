# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------
import turtle
import sys 
from import_helper import dynamic_import
obstacles =  dynamic_import(None)

# position by quadrants
location = 0


# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0


# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


# turtles
t = turtle.Turtle()
t_2 =turtle.Turtle()
t_2.hideturtle()
s = turtle.Screen()


def turtle_display():
    """
    Creates the border on the screen.
    """

    s.bgcolor("red")
    t.left(90)
    t.penup()
    t.fd(200)
    t.left(90)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.fd(100)
    t.left(90)
    t.fd(400)
    t.left(90)
    t.fd(200)
    t.left(90)
    t.fd(400)
    t.left(90)
    t.fd(100)
    t.penup()
    t.goto(0,0)
    t.right(90)
    t.pendown()
    s.setup(250,450)
    t.end_fill()
    t.shape("arrow")


def the_obstacles_1(co_ordinates,text):
    """
    Displays the obstacle on the screen
    Param : co_ordinates
    Param : text
    """

    index=0
    style = ("Calibri", 8, "bold")
    t_2.setpos(0,200)
    t_2.write(text,font= style,align= "center")
    turtle.tracer(0)

    while len(co_ordinates) > index:

        t_2.penup()
        t_2.goto(co_ordinates[index][0],co_ordinates[index][1])
        t_2.pendown()
        t_2.color("blue")
        t_2.fillcolor("white")
        t_2.begin_fill()
        t_2.goto(co_ordinates[index][0],co_ordinates[index][1]+4)
        t_2.goto(co_ordinates[index][0]+4,co_ordinates[index][1]+4)
        t_2.goto(co_ordinates[index][0]+4,co_ordinates[index][1])
        #uncomment if you want the oblstacles closer
        t_2.goto(co_ordinates[index][0],co_ordinates[index][1])
        t_2.end_fill()
        index+=1
    turtle.tracer(1)


def the_obstacles(co_ordinates,text):
    """
    Displays the obstacle on the screen
    Param : co_ordinates
    Param : text
    """

    index=0
    style = ("Calibri", 8, "bold")
    t_2.setpos(0,200)
    t_2.write(text,font= style,align= "center")
    turtle.tracer(0)

    while len(co_ordinates) > index:

        t_2.penup()
        t_2.goto(co_ordinates[index][0],co_ordinates[index][1])
        t_2.pendown()
        t_2.fillcolor("black")
        t_2.begin_fill()
        for i in range(5):
            s = turtle.Screen()
            t_2.forward(5)
            t_2.left(90)
        t_2.end_fill()
        
        index+=1
    turtle.tracer(1)


def show_position(robot_name,command,arg_1,bool):
    """
    Moves the robot in any direction passed in by the user
    Param : robot_name
    Param : command 
    Param : arg_1
    Param : bool
    """
    
    global location
    
    # Quadrants
    n =[0,360,-360]
    s =[180,-180]
    w = [90,270]
    e =[-90,-270]

    if location == 360 or location == -360:
        location *= 0

    if (command == "forward" or command == "back") and  (location in n or location in s) and bool == True:
        if t.ycor() < 200 or t.ycor() > -200:
            if command == "forward":
                t.fd(int(arg_1))
            else:
                t.bk(int(arg_1))
    
    elif (command == "forward" or command == "back") and (location in w or location in e) and bool== True:
        if  t.xcor() < 100 or t.xcor() > -100:
            if command == "forward":
                t.fd(int(arg_1))
            else:
                t.bk(int(arg_1))
    
    elif command == "right":
        location+=90
        t.right(90)
        
    elif command == "left":
        location-=90
        t.left(90)


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


turtle_display()    


def position():
    return position_x,position_y

