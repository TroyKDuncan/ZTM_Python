import unittest
import unittest_exercise


class TestGame(unittest.TestCase):

    def test_guess(self):
        answer = 5
        guess = 5
        result = unittest_exercise.check_guess(guess, answer)
        self.assertTrue(result)

    def test_guess2(self):
        answer = 6
        guess = 4
        result = unittest_exercise.check_guess(guess, answer)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()