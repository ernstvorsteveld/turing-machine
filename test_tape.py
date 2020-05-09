import unittest
import tape as tape

class TestTape(unittest.TestCase):

    def setUp(self):
        self.tape = tape.Tape('t1', ['0','0','0','0'],0)
        pass

    def test_print(self):
        view = self.tape.print()
        self.assertEqual(view, ['', '0', '000'])

    def test_move_and_print(self):
        self.tape.left()
        view = self.tape.print()
        self.assertEqual(view, ['0', '0', '00'])


if __name__ == '__main__':
    unittest.main()
