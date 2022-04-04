"""Tic Tac Game Module"""


class TicTacGame:
    """Tic Tac Game Class"""

    def __init__(self):
        """Initialization function"""

        self.board = [0 for i in range(9)]
        # 0 - empty, 1 - x, 2 - 0

    def show_board(self):
        """Function show board"""

        def field_value(val):
            if val == 0:
                return ' '
            if val == 1:
                return 'x'
            if val == 2:
                return 'o'
            raise Exception('Wrong value of board')

        print(f'\n{field_value(self.board[0])} | {field_value(self.board[1])}\
 | {field_value(self.board[2])}\n{field_value(self.board[3])}\
 | {field_value(self.board[4])} | {field_value(self.board[5])}\
 \n{field_value(self.board[6])} | {field_value(self.board[7])}\
 | {field_value(self.board[8])}\n')

    def validate_input(self, num):
        """Check valid input"""

        try:
            num = int(num)

            if not 1 <= int(num) <= 9:
                return 1
            if self.board[int(num) - 1] != 0:
                return 2
            return 0

        except ValueError:
            return 3

    def move(self, move_pos, x_flag):
        """Function move"""

        valid_num = self.validate_input(move_pos)

        if valid_num == 1:
            print('INCORRECT POSITION ENTERED - ENTER A NUMBER FROM 1 TO 9')

        elif valid_num == 2:
            print('INCORRECT POSITION ENTERED - THE POSITION IS FILLED')

        elif valid_num == 3:
            print('INCORRECT POSITION ENTERED - ENTER AN INTEGER NUMBER')

        else:
            self.board[int(move_pos) - 1] = int(not x_flag) + 1
            return 1

        return 0

    def start_game(self):
        """Function start"""

        print('START GAME')

        x_flag = True

        while True:

            print('1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9')
            self.show_board()

            if x_flag:
                print('move for x')
            else:
                print('move for o')

            move = input()

            if not self.move(move, x_flag):
                continue

            check = self.check_winner()

            if check:
                if check == 1:
                    print('x win')
                elif check == 2:
                    print('o win')
                else:
                    print('draw')

                self.show_board()
                print('0 - exit, 1 - play again')

                inp = int(input())
                if inp:
                    for i in range(9):
                        self.board[i] = 0
                    continue

                print('END GAME')
                break

            x_flag = not x_flag

    def check_winner(self):
        """Check board"""

        # 0 - no, 1 - x, 2 - o, 3 - draw
        output = 3

        for i in range(3):
            if self.board[i * 3] == self.board[i * 3 + 1]\
                    == self.board[i * 3 + 2] != 0:
                if self.board[i * 3] == 1:
                    output = 1
                    break

                output = 2
                break

            if self.board[i] == self.board[i + 3] == self.board[i + 6] != 0:
                if self.board[i] == 1:
                    output = 1
                    break

                output = 2
                break

        if self.board[0] == self.board[4] == self.board[8] != 0\
                or self.board[2] == self.board[4] == self.board[6] != 0:
            if self.board[4] == 1:
                output = 1
            else:
                output = 2

        if output == 3:
            for i in range(9):
                if self.board[i] == 0:
                    return 0

        return output


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
