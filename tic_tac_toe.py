class TicTacGame:

    def __init__(self):
        self.__board = [0 for i in range(9)]
        #0 - empty, 1 - x, 2 - 0

    def show_board(self):
        def field_value(val):
            if val == 0:
                return ' '
            elif val == 1:
                return 'x'
            elif val == 2:
                return 'o'
            else:
                raise Exception('Wrong value of board')

        print('\n{0} | {1} | {2}\n{3} | {4} | {5}\n{6} | {7} | {8}\n'.format(
        field_value(self.__board[0]), field_value(self.__board[1]), 
        field_value(self.__board[2]), field_value(self.__board[3]), 
        field_value(self.__board[4]), field_value(self.__board[5]), 
        field_value(self.__board[6]), field_value(self.__board[7]), 
        field_value(self.__board[8])))

    def show_board_pos(self):
        print('1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9')

    def validate_input(self, num):
        try:
            num = int(num)

            if not (1 <= int(num) <= 9):
                return 1
            if self.__board[int(num) - 1] != 0:
                return 2
            return 0

        except ValueError:
            return 3
        
    def move(self, x_flag):

        move = input()

        valid_num = self.validate_input(move)
            
        if valid_num == 1:
            print('INCORRECT POSITION ENTERED - ENTER A NUMBER FROM 1 TO 9')
    
        elif valid_num == 2:
            print('INCORRECT POSITION ENTERED - THE POSITION IS FILLED')
        
        elif valid_num == 3:
            print('INCORRECT POSITION ENTERED - ENTER AN INTEGER NUMBER')
        
        else:
            self.__board[int(move) - 1] = int(not x_flag) + 1
            return 0

        return 1

    def start_game(self):
        print('START GAME')

        x_flag = True

        while True:

            self.show_board_pos()D
            self.show_board()

            if x_flag:
                print('move for x')
            else:
                print('move for o')

            
            if self.move(x_flag):
                continue
            
            
            check = self.check_winner()

            if check:
                if check == 1:
                    print('x win')
                elif check == 2:
                    print('o win')
                else:
                    print('draw')

                print('0 - exit, 1 - play again')
                
                inp = int(input())
                if inp:
                    for i in range(9):
                        self.__board[i] = 0
                    continue
                else:
                    print('END GAME')
                    break

            x_flag = not x_flag




    def check_winner(self):
        # 0 - no, 1 - x, 2 - o, 3 - draw
        for i in range(3):
            if (self.__board[i * 3] == self.__board[i * 3 + 1] == self.__board[i * 3 + 2] != 0):
                if self.__board[i * 3] == 1:
                    return 1
                return 2

            if (self.__board[i] == self.__board[i + 3] == self.__board[i + 6] != 0):
                if self.__board[i] == 1:
                    return 1
                return 2

        if (self.__board[0] == self.__board[4] == self.__board[8] != 0):
            if self.__board[0] == 1:
                return 1
            return 2

        if (self.__board[2] == self.__board[4] == self.__board[6] != 0):
            if self.__board[2] == 1:
                return 1
            return 2

        for i in range(9):
            if self.__board[i] == 0:
                return 0

        return 3

if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
