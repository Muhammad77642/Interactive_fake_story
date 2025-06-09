import unittest
from unittest.mock import patch
import main

class TestGameFunctions(unittest.TestCase):

    def setUp(self):
        main.SWITCHER = True
        main.USER_SCORE = 0
        main.NO_OF_TURNS = 0

    def test_switch_on_off(self):
        main.switch_off()
        self.assertFalse(main.SWITCHER)
        main.switch_on()
        self.assertTrue(main.SWITCHER)

    def test_increase_turns(self):
        main.NO_OF_TURNS = 0
        main.increse_no_of_turns()
        self.assertEqual(main.NO_OF_TURNS, 1)

    def test_print_sleep(self):
        # just test it doesn't raise error
        try:
            main.print_sleep("test message")
        except Exception as e:
            self.fail(f"print_sleep raised exception: {e}")

    @patch('builtins.input', return_value='  Yes ')
    def test_removing_spaces_lower(self, mock_input):
        main.USER_INPUT = "  Yes "
        main.removing_spaces_lower()
        self.assertEqual(main.USER_INPUT, "yes")

    @patch('builtins.input', return_value='Y')
    def test_bring_input_and_cleaning(self, mock_input):
        main.bring_input("Do you want to play? (Y/N): ")
        self.assertEqual(main.USER_INPUT, 'y')

