from typing import Union
import unittest,sys
import quadratic_equation, assistant, vote

class TestStringMethods(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(quadratic_equation.solution(-4, 28, -49), (dict))
        self.assertIsInstance(assistant.get_name("10006"), Union[list,None])

    def test_r(self):
     with self.assertRaisesRegex(ValueError, 'literal'):
         vote.vote([1,1,1,2,3])

class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")


    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        self.assertIn('win', sys.platform.title().lower())
        pass


if __name__ == '__main__':
    pass
    # print("{description} {value}".format(**quadratic_equation.solution(-4, 28, -49)))
