# test_main.py
import unittest
from unittest.mock import patch
from main import valid_arg

class TestMain(unittest.TestCase):
    @patch('builtins.input', return_value='ROCK')
    def test_valid_user_choice_rock(self, input):
        self.assertIn(input().upper(), valid_arg)

    @patch('builtins.input', return_value='PAPER')
    def test_valid_user_choice_paper(self, input):
        self.assertIn(input().upper(), valid_arg)

    @patch('builtins.input', return_value='SCISSORS')
    def test_valid_user_choice_scissors(self, input):
        self.assertIn(input().upper(), valid_arg)

    @patch('builtins.input', return_value='SPOCK')
    def test_valid_user_choice_spock(self, input):
        self.assertIn(input().upper(), valid_arg)

    @patch('builtins.input', return_value='LIZARD')
    def test_valid_user_choice_lizard(self, input):
        self.assertIn(input().upper(), valid_arg)

    @patch('builtins.input', return_value='invalid_choice')
    def test_invalid_user_choice(self, input):
        self.assertNotIn(input().upper(), valid_arg)

if __name__ == '__main__':
    unittest.main()