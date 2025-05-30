# Tic Tac Toe Game

A simple command-line implementation of the classic Tic Tac Toe game in Python.

## Description

This is a two-player game where players take turns marking spaces in a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Features

- Clean command-line interface
- Input validation
- Automatic player switching
- Win detection
- Draw detection
- Option to play again
- Cross-platform compatibility (Windows/Linux)

## Requirements

- Python 3.x
- No additional packages required

## How to Play

1. Run the game:
   ```bash
   python3 tictactoe.py
   ```

2. Game Rules:
   - The game is played on a 3x3 grid
   - Players take turns placing their mark (X or O) in an empty cell
   - First player to get 3 marks in a row (horizontally, vertically, or diagonally) wins
   - If all cells are filled and no player has won, the game is a draw

3. Making a Move:
   - When prompted, enter the row number (1-3)
   - Then enter the column number (1-3)
   - The grid positions are numbered as follows:
     ```
     1,1 | 1,2 | 1,3
     ---------------
     2,1 | 2,2 | 2,3
     ---------------
     3,1 | 3,2 | 3,3
     ```

4. Game Controls:
   - Enter numbers 1-3 for row and column positions
   - Press Ctrl+C to exit the game at any time
   - After a game ends, choose 'y' to play again or 'n' to quit

## Example

```
Tic Tac Toe
-------------
   |   |   
-----------
   |   |   
-----------
   |   |   

Player X's turn
Enter row (1-3): 2
Enter column (1-3): 2
```

## Contributing

Feel free to fork this repository and submit pull requests with improvements.

## License

This project is open source and available under the MIT License. 
