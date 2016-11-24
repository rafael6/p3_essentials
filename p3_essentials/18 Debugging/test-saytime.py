'''
Unit test
at the end of the module here, if __name == "__main__", instead of just calling my own main,
I call a special main that's in the unittest package. And in the unittest package,
the special main will actually open up this file and parse it and find the classes that import unittest,
and it will go ahead and run the test in that class. And so here is the class. So I can name it whatever I want.
And it has a special method called setUp. In this special method setUp, I can do any initializations that I want to
'''
import saytime
import unittest

class TestSaytime(unittest.TestCase):
    def setUp(self):
        self.nums = list(range(11))

    def test_numbers(self):  # This method will be run as a test
        # make sure the numbers translate correctly
        # These are the words that are expected
        words = (
            'oh', 'one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine', 'ten'
        )
        for i, n in enumerate(self.nums):
            self.assertEqual(saytime.numwords(n).numwords(), words[i])  # If they are equal they are fine, else error

    def test_time(self):  # This method wil run as a test
        time_tuples = (
            (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
            (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15),
            (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
        )
        # Expected results
        time_words = (
            "midnight",
            "one past midnight",
            "eleven o'clock",
            "noon",
            "one o'clock",
            "twenty-nine past noon",
            "half past noon",
            "twenty-nine til one",
            "quarter past noon",
            "half past noon",
            "quarter til one",
            "one til noon",
            "quarter past eleven",
            "one til midnight",
            "one til one",
            "one til two",
            "OOR",
            "OOR"
        )
        for i, t in enumerate(time_tuples):
            self.assertEqual(saytime.saytime(*t).words(), time_words[i]) # If they are equal fine; otherwise error

if __name__ == "__main__": unittest.main()

