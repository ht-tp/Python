import unittest

from hello_world import hello

class TestHelloFunction(unittest.TestCase):
    def test_hello_returns_correct_string(self):

        msg = "\n\nThis test expects a return of the string 'Hello, World!' \nDid you use print('Hello, World!') by mistake?"
        self.assertEqual(hello(), "Hello, World!", msg=msg)

if __name__ == '__main__':
    unittest.main()