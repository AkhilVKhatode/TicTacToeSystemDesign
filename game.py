class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.grid:
            print('|' + '|'.join(row) + '|')
            print('-------')

    def update(self, row, col, player):
        if self.grid[row][col] == ' ':
            self.grid[row][col] = player
            return True
        return False

    def is_full(self):
        for row in self.grid:
            if ' ' in row:
                return False
        return True

    def check_winner(self, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.grid[i][j] == player for j in range(3)) or \
               all(self.grid[j][i] == player for j in range(3)):
                return True
        if all(self.grid[i][i] == player for i in range(3)) or \
           all(self.grid[i][2 - i] == player for i in range(3)):
            return True
        return False


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self):
        while True:
            try:
                move_str = input(f"Player {self.symbol}, enter your move (row, col): ")
                row, col = map(int, move_str.split(','))
                if 0 <= row < 3 and 0 <= col < 3:
                    return row, col
                else:
                    print("Invalid move. Row and column must be between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter row and column separated by a comma.")


class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.current_player = self.player1

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def play(self):
        while True:
            self.board.display()
            row, col = self.current_player.get_move()

            if self.board.update(row, col, self.current_player.symbol):
                if self.board.check_winner(self.current_player.symbol):
                    self.board.display()
                    print(f"Player {self.current_player.symbol} wins!")
                    break
                elif self.board.is_full():
                    self.board.display()
                    print("It's a tie!")
                    break
                else:
                    self.switch_player()
            else:
                print("That position is already taken. Try again.")


if __name__ == "__main__":
    game = Game()
    game.play()
