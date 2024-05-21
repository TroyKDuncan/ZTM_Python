# if you want to go far, you need to be an expert at testing

# generally speaking, each python module has its own tests

# try and break things in order to make it the best it can be

import unittest  # check the documentation for other assert methods
import main


class TestMain(unittest.TestCase):

    def setUp(self):  # runs before each test to set variables or something like that
        print('About to test a function')

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'asdf'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, TypeError)

    def tearDown(self):  # runs after each test, usually to reset things for the next test
        print('Cleaning up')


unittest.main()

# If you have multiple files that are unit tests, you can run python3 -m unittest and it will test all of them at the same time
