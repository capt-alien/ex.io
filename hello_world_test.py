import unittest
import hello_world



class Test_hella_world(unittest.TestCase):
    def test_hello_world(self):
        x = hello_world.hello_world()
        assert x == "Hello World!"
