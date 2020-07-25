import unittest
import game

class TestValidImput(unittest.TestCase):
	def test_input_not_empty(self):
		self.assertFalse(game.checkChoice(''))

	def test_input_not_more_then_one(self):
		self.assertFalse(game.checkChoice('kk'))

	def test_input_one_is_ok(self):
		game.word=game.words[0]
		game.word_shown=['_']*len(game.word)
		self.assertTrue(game.checkChoice('s'))

class TestWin(unittest.TestCase):
	def test_is_not_win(self):
		game.word_shown=['_','t', '_']
		self.assertFalse(game.checkWin())
	def test_is_win(self):
		game.word_shown=['w','i', 'n']
		self.assertTrue(game.checkWin())

if __name__ == '__main__':
    unittest.main()