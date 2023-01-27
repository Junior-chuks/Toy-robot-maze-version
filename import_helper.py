import sys
from importlib import import_module

  
# dynamic import  
def dynamic_import(name):

    if len(sys.argv) == 2:
        if sys.argv[-1] == "turtle" or sys.argv[-1] == "text":
            name = "maze.obstacles"
            return import_module(name)
        
    elif len(sys.argv) == 3 :
        if sys.argv[2] == "simple_maze":
            name = "maze.the_worlds_most_crazy_maze"
            return import_module(name)

    else:
        name = "maze.obstacles"
        return import_module(name)