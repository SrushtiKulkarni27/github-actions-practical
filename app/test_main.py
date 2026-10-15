import unittest
from main import greeting


class GreetingTests(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(greeting(), "Hello again from automated CI")


if __name__ == "__main__":
    unittest.main()
