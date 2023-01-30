import unittest
from test_base import StringIO
from test_base import captured_io
from world.text import world as text
from maze import obstacles


class MyFunction (unittest.TestCase):
    def test_show_obstacles(self):
        with captured_io(StringIO()) as (out,err):
            obstacles.random.randint = lambda a,b : 2
            coord = obstacles.get_obstacles()
            text.the_obstacles(coord, None)

        output = out.getvalue().strip()
        self.assertEqual("""There are some obstacles:
- At position 2,2 (to 6,6)- At position 2,2 (to 6,6)""",output)


    def test_show_position(self):
        with captured_io(StringIO()) as (out,err):
            text.position_x = 0
            text.position_y = 0
            text.show_position('Jarvis',None,None,None)
        output = out.getvalue().strip()
        self.assertEqual("""> Jarvis now at position (0,0).""",output)
    

    def test_update_position(self):
        
        obstacles.random.randint = lambda a,b : 1
        coord = obstacles.get_obstacles()
        self.assertEqual(text.update_position(1,coord),(True,"correct"))
                    
        
    def test_position_allowed(self):
        
        allowed = text.is_position_allowed(9,10)
        not_allowed = text.is_position_allowed(102,90)
        self.assertTrue(allowed)
        self.assertFalse(not_allowed)
        

if __name__ == "__main__":
    unittest.main()