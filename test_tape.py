import unittest
import tape as tape

class TestTape(unittest.TestCase):

    def setUp(self):
        self.tape = tape.Tape('t1', ['0','0','0','0'],0)
        pass

    def test_write_dash(self):
        self.tape.write('-')
        self.assertEqual(self.tape.print(), ['', '0', '000'])

    def test_print(self):
        view = self.tape.print()
        self.assertEqual(view, ['', '0', '000'])

    def test_move_and_print(self):
        self.tape.move('L')
        view = self.tape.print()
        self.assertEqual(view, ['0', '0', '00'])

    def test_move_right(self):
        self.tape.move('R')
        view = self.tape.print()
        self.assertEqual(self.tape.getHead(), 0)
        self.assertEqual(view, ['', '_', '0000'])

    def test_move_left(self):
        self.tape.move('L')
        self.tape.move('L')
        self.tape.move('L')
        self.tape.move('L')
        self.tape.move('L')
        self.assertEqual(self.tape.getHead(), 5)
        self.assertEqual(self.tape.print(), ['0000_', '_', ''])


    def test_moves(self):
        self.tape.move('L')
        self.assertEqual(self.tape.getHead(), 1)
        self.tape.move('L')
        self.assertEqual(self.tape.getHead(), 2)
        self.tape.move('L')
        self.assertEqual(self.tape.getHead(), 3)
        self.tape.move('L')
        self.assertEqual(self.tape.getHead(), 4)
        self.tape.move('L')
        self.assertEqual(self.tape.getHead(), 5)
        self.tape.move('L')
        self.assertEqual(self.tape.getHead(), 6)
        self.tape.move('L')
        self.assertEqual(self.tape.getHead(), 7)
        self.tape.move('R')
        self.assertEqual(self.tape.getHead(), 6)
        self.tape.move('R')
        view = self.tape.print()
        self.assertEqual(view, ['0000_', '_', '__'])

if __name__ == '__main__':
    unittest.main()
