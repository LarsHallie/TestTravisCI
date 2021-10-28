import Main
import unittest

check = Main.algorithm()

class TestAlg(unittest.TestCase):

    def test_add(self):
        self.assertEqual(check.run(5), 25)

if __name__ == '__main__':
    unittest.main()
