import unittest
from maze import obstacles


class MyFunctions(unittest.TestCase):
    def test_obstacles(self):
        obstacles.random.randint = lambda a,b : 1
        self.assertEqual(obstacles.get_obstacles(),[(1,1)])
        self.assertEqual(type(obstacles.get_obstacles()),list)


    def test_position_blocked(self):
        obstacles.random.randint = lambda a,b : 1
        self.assertEqual(obstacles.is_position_blocked(1,1),True)


    def test_path_blocked(self):
        obstacles.random.randint = lambda a,b : 1
        self.assertEqual(obstacles.is_path_blocked(2,4,(1,0),(1,2)),True) 


if __name__ =="__main__":
    unittest.main()