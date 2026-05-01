import unittest


class TestCubeFunction(unittest.TestCase):

  def test_that_cube_function_exists(self):
     functionplayground.cube(10)
  
  def test_that_cub_function_return_correct_result_(self):
   actual=functionplayground.cube(10)
    expected=1000
    self.assertEquale(actual, expected)
