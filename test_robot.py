import unittest
import robot
from io import StringIO
from test_base import captured_io
from maze import obstacles


class MyFunctions(unittest.TestCase):
    def test_history(self):
        """
        Test to see if it stores and returns a list of commands.
        """
        with captured_io(StringIO("forward 10\nback 20\nright\nright\nleft\noff\n")):
            robot.robot_start()
        self.assertEqual(robot.history,['back 20', 'right', 'right', 'left'])
            

    def test_replay(self):

        with captured_io(StringIO("Junior\nforward 10\nback 5\nleft\nright\nreplay\noff\n")) as (out,err):
            obstacles.random.randint = lambda a,b : 0
            robot.robot_start()
        output = out.getvalue().strip()
        self.maxDiff=None
        self.assertEqual("""What do you want to name your robot? Junior: Hello kiddo!
Junior: Loaded obstacles.
Junior: What must I do next?  > Junior moved forward by 10 steps.
 > Junior now at position (0,10).
Junior: What must I do next?  > Junior moved back by 5 steps.
 > Junior now at position (0,5).
Junior: What must I do next?  > Junior turned left.
 > Junior now at position (0,5).
Junior: What must I do next?  > Junior turned right.
 > Junior now at position (0,5).
Junior: What must I do next?  > Junior moved forward by 10 steps.
 > Junior now at position (0,15).
 > Junior moved back by 5 steps.
 > Junior now at position (0,10).
 > Junior turned left.
 > Junior now at position (0,10).
 > Junior turned right.
 > Junior now at position (0,10).
 > Junior replayed 4 commands.
 > Junior now at position (0,10).
Junior: What must I do next? Junior: Shutting down..""",output)


    def test_replay_silent(self):
        with captured_io(StringIO("forward 3\nleft\nforward 4\nback 2\nreplay silent\noff\n")) as (out,err):
            obstacles.random.randint = lambda a,b : 0
            robot.robot_start()
        output = out.getvalue().strip()
        self.maxDiff=None
        self.assertEqual("""What do you want to name your robot? forward 3: Hello kiddo!
forward 3: Loaded obstacles.
forward 3: What must I do next?  > forward 3 turned left.
 > forward 3 now at position (0,0).
forward 3: What must I do next?  > forward 3 moved forward by 4 steps.
 > forward 3 now at position (-4,0).
forward 3: What must I do next?  > forward 3 moved back by 2 steps.
 > forward 3 now at position (-2,0).
forward 3: What must I do next?  > forward 3 replayed 3 commands silently.
 > forward 3 now at position (-2,-2).
forward 3: What must I do next? forward 3: Shutting down..""",output)


    def test_replay_reversed(self):
        with captured_io(StringIO("James\nforward 4\nright\nback 3,replay reverse\noff\n")) as (out,err):
            obstacles.random.randint = lambda a,b : 0
            robot.robot_start()
        self.maxDiff = None
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? James: Hello kiddo!
James: Loaded obstacles.
James: What must I do next?  > James moved forward by 4 steps.
 > James now at position (0,4).
James: What must I do next?  > James turned right.
 > James now at position (0,4).
James: What must I do next? James: Sorry, I did not understand 'back 3,replay reverse'.
James: What must I do next? James: Shutting down..""",output)


    def test_replay_reversed_silent(self):
        with captured_io(StringIO("Lucky\nback 5\nleft\nforward 3\nreplay reverse silent\noff\n")) as (out,err):
            obstacles.random.randint = lambda a,b : 0
            robot.robot_start()
        output = out.getvalue().strip()
        self.maxDiff = None
        self.assertEqual("""What do you want to name your robot? Lucky: Hello kiddo!
Lucky: Loaded obstacles.
Lucky: What must I do next?  > Lucky moved back by 5 steps.
 > Lucky now at position (0,-5).
Lucky: What must I do next?  > Lucky turned left.
 > Lucky now at position (0,-5).
Lucky: What must I do next?  > Lucky moved forward by 3 steps.
 > Lucky now at position (-3,-5).
Lucky: What must I do next? Lucky: Sorry, I did not understand 'replay reverse silent'.
Lucky: What must I do next? Lucky: Shutting down..""",output)


    def test_limt_range(self):
        with captured_io(StringIO("Mel\nforward 10\nback 3\neplay 1 reversed\noff\n")) as (out,err):
            obstacles.random.randint = lambda a,b : 0
            robot.robot_start()
        output = out.getvalue().strip()
        self.maxDiff = None
        self.assertEqual("""What do you want to name your robot? Mel: Hello kiddo!
Mel: Loaded obstacles.
Mel: What must I do next?  > Mel moved forward by 10 steps.
 > Mel now at position (0,10).
Mel: What must I do next?  > Mel moved back by 3 steps.
 > Mel now at position (0,7).
Mel: What must I do next? Mel: Sorry, I did not understand 'eplay 1 reversed'.
Mel: What must I do next? Mel: Shutting down..""",output)


if __name__=="__main__":
    unittest.main()
