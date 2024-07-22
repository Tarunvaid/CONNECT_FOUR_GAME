# Connect Four Game

This Python script creates a colorful Connect Four game using `tkinter` for the GUI. Players take turns clicking columns to drop their pieces, with the board updating dynamically. It includes vibrant colors, custom fonts, and intuitive controls, making for an engaging, visually appealing gameplay experience.

## Features

- Two-player mode.
- Colorful and styled buttons for each player.
- Dynamic board updates.
- Win detection with an alert.
- Automatic board reset after a win.

## Requirements

- Python 3.x

## Usage

1. Run the script using Python.

   ```sh
   python connect_four_game.py
   ```

2. The game window will appear. Players take turns clicking the columns to drop their pieces.

## How to Play

1. **Starting the Game**: The game starts with Player X.
2. **Making a Move**: Click on a column to drop your piece into the lowest available row.
3. **Alternating Turns**: Players alternate turns. Player X's pieces are red, and Player O's pieces are yellow.
4. **Winning the Game**: The game checks for a winner after each move. If a player connects four pieces horizontally, vertically, or diagonally, they win, and an alert appears.
5. **Resetting the Board**: Click "OK" in the alert to reset the board and play again.

## Code Overview

### ConnectFourGUI Class

- **Initialization**: Sets up the game window and initializes the game board.
- **create_board()**: Creates a 6x7 grid of buttons for the game board.
- **make_move(row, col)**: Handles the logic for placing a piece in the lowest available row of the chosen column.
- **check_winner()**: Checks for horizontal, vertical, and diagonal connections of four pieces.
- **switch_player()**: Changes the current player after each move.
- **reset_board()**: Clears the board and GUI buttons after a win.

### Main Function

- Creates an instance of `ConnectFourGUI` and starts the Tkinter main loop.


## Customization

- **Button Styles**: Customize button styles (font, color, size) in the `create_board()` method.
- **Win Detection**: Modify the win detection logic in the `check_winner()` method for different winning conditions.


## Acknowledgments

- The `tkinter` library for GUI elements.
- Python Software Foundation for Python.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
