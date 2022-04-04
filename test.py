"""Tests for Tic_Tac_Toe_Module"""

from unittest import TestCase
import unittest

from tic_tac_toe import TicTacGame

class TestTicTacToe(TestCase):
    """Testing class"""

    def test_validate_input(self):
        """Testing for correct function validate_input output"""

        game = TicTacGame()
        for i in range(1, 10):
            self.assertTrue(game.validate_input(str(i)) == 0)
        self.assertTrue(game.validate_input("a") == 3)
        self.assertTrue(game.validate_input("0") == 1)
        self.assertTrue(game.validate_input("10") == 1)
        self.assertTrue(game.validate_input("-1") == 1)


    def test_validate_input_again(self):
        """Testing for the correct function validate_input output when enter the same positions"""

        game = TicTacGame()
        game.move(1, True)
        self.assertEqual(game.board[0], 1)
        self.assertTrue(game.validate_input("1") == 2)

    def test_move(self):
        """Testing move function"""

        game = TicTacGame()
        self.assertEqual(game.board[0], 0)
        game.move(1, True)
        self.assertEqual(game.board[0], 1)

        self.assertEqual(game.board[1], 0)
        game.move(2, False)
        self.assertEqual(game.board[1], 2)

    def test_check_winner(self):
        """Testing check_winnew function"""

        game = TicTacGame()

        #Check vertical
        game.board = [
            1, 1, 0,
            1, 2, 2,
            1, 0, 2
        ]

        self.assertTrue(game.check_winner() == 1)

        game.board = [
            1, 2, 1,
            1, 2, 0,
            0, 2, 1
        ]

        self.assertTrue(game.check_winner() == 2)

        game.board = [
            2, 2, 1,
            2, 1, 1,
            0, 0, 1
        ]

        self.assertTrue(game.check_winner() == 1)

        #Check horizontal
        game.board = [
            2, 2, 2,
            0, 1, 1,
            1, 1, 0
        ]

        self.assertTrue(game.check_winner() == 2)

        game.board = [
            1, 2, 2,
            1, 1, 1,
            2, 0, 0
        ]

        self.assertTrue(game.check_winner() == 1)

        game.board = [
            0, 1, 0,
            0, 1, 1,
            2, 2, 2
        ]

        self.assertTrue(game.check_winner() == 2)

        #Check diagonal
        game.board = [
            1, 1, 2,
            0, 1, 0,
            2, 2, 1
        ]

        self.assertTrue(game.check_winner() == 1)

        game.board = [
            1, 1, 2,
            1, 2, 0,
            2, 0, 1
        ]

        self.assertTrue(game.check_winner() == 2)

        #Check draw
        game.board = [
            2, 2, 1,
            1, 1, 2,
            2, 1, 1
        ]

        self.assertTrue(game.check_winner() == 3)

        game.board = [
            2, 1, 2,
            1, 1, 2,
            1, 2, 1
        ]

        self.assertTrue(game.check_winner() == 3)

        #Check game continious
        game.board = [
            0, 0, 0,
            0, 1, 0,
            0, 0, 0
        ]

        self.assertFalse(game.check_winner())

        game.board = [
            0, 2, 0,
            0, 1, 0,
            0, 0, 1
        ]

        self.assertFalse(game.check_winner())

        game.board = [
            2, 2, 1,
            1, 1, 2,
            0, 2, 1
        ]

        self.assertFalse(game.check_winner())

if __name__ == "__main__":
    unittest.main()
