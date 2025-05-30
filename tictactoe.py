#!/usr/bin/python3
#! encoding: utf-8
import os
import sys

class TicTacToe:
    def __init__(self):
        self.data = [[' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']]
        self.current_player = 'X'
        self.moves_count = 0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_board(self):
        self.clear_screen()
        print("\nTic Tac Toe")
        print("-------------")
        for i in range(3):
            print(f" {self.data[i][0]} | {self.data[i][1]} | {self.data[i][2]} ")
            if i < 2:
                print("-----------")
        print("\n")

    def is_valid_move(self, row, col):
        try:
            row, col = int(row), int(col)
            if 1 <= row <= 3 and 1 <= col <= 3:
                return self.data[row-1][col-1] == ' '
            return False
        except ValueError:
            return False

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.data[int(row)-1][int(col)-1] = self.current_player
            self.moves_count += 1
            return True
        return False

    def check_win(self):
        # Check rows
        for i in range(3):
            if self.data[i][0] == self.data[i][1] == self.data[i][2] != ' ':
                return self.data[i][0]

        # Check columns
        for i in range(3):
            if self.data[0][i] == self.data[1][i] == self.data[2][i] != ' ':
                return self.data[0][i]

        # Check diagonals
        if self.data[0][0] == self.data[1][1] == self.data[2][2] != ' ':
            return self.data[0][0]
        if self.data[0][2] == self.data[1][1] == self.data[2][0] != ' ':
            return self.data[0][2]

        return None

    def is_draw(self):
        return self.moves_count == 9

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.show_board()
            
            if self.is_draw():
                print("Draw! Game Over.")
                break

            winner = self.check_win()
            if winner:
                print(f"Player {winner} wins!")
                break

            print(f"Player {self.current_player}'s turn")
            try:
                row = input("Enter row (1-3): ")
                col = input("Enter column (1-3): ")
                
                if not self.make_move(row, col):
                    print("Invalid move! Try again.")
                    continue
                
                self.switch_player()
            except KeyboardInterrupt:
                print("\nGame terminated by user.")
                sys.exit(0)

    def reset_game(self):
        self.__init__()

def main():
    game = TicTacToe()
    while True:
        game.play()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
        game.reset_game()

if __name__ == '__main__':
    main()
