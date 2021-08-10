"""Unit tests of functions in hog."""
import unittest
from unittest.mock import Mock
from hog import roll_dice  # function to test


class HogTest(unittest.TestCase):
    """Unit tests of functions in the hog game."""

    def test_roll_one_die(self):
        """Test roll_dice for a single roll."""
        # mock dice that always returns the same value (dice.return_value)
        dice = Mock()
        dice.return_value = 5
        result = roll_dice(1, dice=dice)
        self.assertEqual(5, result)
        self.assertEqual(1, dice.call_count)
        dice.return_value = 1
        dice.call_count = 0
        result = roll_dice(1, dice=dice)
        self.assertEqual(1, result)
        self.assertEqual(1, dice.call_count)

    def test_roll_many_dice_no_ones(self):
        """Roll two or more simulated dice, but don't roll any ones."""
        # use a mock object so we can "program" what the rolled values are.
        dice = Mock()
        # specify the return values for the mock object.
        # each time you call dice() it returns the next value in this list.
        dice.side_effect = [5, 6, 2, 2, 6, 3, 4, 6, 5, 0]
        # syntax: assertEqual(expected_result, actual_result)
        self.assertEqual(11, roll_dice(2, dice=dice))
        # mock.call_count returns how many times a mock function was called
        self.assertEqual( 2, dice.call_count, 'should have rolled 2 dice')
        self.assertEqual( 4, roll_dice(2, dice=dice))
        # the call_count keeps accumulating unless you write mock.call_count = 0
        self.assertEqual( 4, dice.call_count)
        self.assertEqual(13, roll_dice(3, dice=dice))
        self.assertEqual( 7, dice.call_count) 

    def test_roll_dice_with_ones(self):
        """Roll dice but have one."""
        # use a mock object so we can "program" what the rolled values are.
        dice = Mock()
        # specify the return values for the mock object.
        # each time you call dice() it returns the next value in this list.
        dice.side_effect = [2, 4, 2, 1, 2, 6, 3, 4, 5, 0]
        # syntax: assertEqual(expected_result, actual_result)
        self.assertEqual(6, roll_dice(2, dice=dice))
        # mock.call_count returns how many times a mock function was called
        self.assertEqual(2, dice.call_count, 'rolled 2 dice')
        self.assertEqual(1, roll_dice(3, dice=dice))
        self.assertEqual(5, dice.call_count)
        self.assertEqual(18, roll_dice(4, dice=dice))
        self.assertEqual(9, dice.call_count)

    def test_roll_dice_with_ones_everytime(self):
        """Roll dice but have only ones."""
        # use a mock object so we can "program" what the rolled values are.
        dice = Mock()
        # specify the return values for the mock object.
        # each time you call dice() it returns the next value in this list.
        list_of_ones = []
        for _ in range(1000):
            list_of_ones.append(1)
        dice.side_effect = list_of_ones
        self.assertEqual(1, roll_dice(2, dice=dice))
        # mock.call_count returns how many times a mock function was called
        self.assertEqual(2, dice.call_count, 'rolled 2 dice')
        self.assertEqual(1, roll_dice(32, dice=dice))
        self.assertEqual(34, dice.call_count, 'rolled 34 dice')
        self.assertEqual(1, roll_dice(47, dice=dice))
        self.assertEqual(81, dice.call_count, 'rolled 81 dice')
        self.assertEqual(1, roll_dice(342, dice=dice))
        self.assertEqual(423, dice.call_count, 'rolled 423 dice')
