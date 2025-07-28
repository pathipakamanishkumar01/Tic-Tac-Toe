# Tic-Tac-Toe
HI, This project is a classic Tic Tac Toe game implemented using Python's tkinter module, providing a graphical user interface for easy two-player interaction. The program allows two players to enter their names, player 1 to choose a symbol (X or O), while player 2 is assigned the remaining symbol. Players take alternate turns clicking on the cells in a 3x3 grid. The game checks for a winner (three marks in a horizontal, vertical or diagonal sequence) or a draw (when all cells are filled without a winner). Upon game completion, the result is shown via a pop-up message box, and the board resets dynamically for a new game.

THE ALGORITHM I USED TO BUILD THIS PROJECT:
Import tkinter and necessary dialog/messagebox modules.

Initialize the main window with title "Tic Tac Toe".

Get player names via input dialog boxes. If no input is entered, assign default names.

Ask Player 1 to select their symbol (X or O), and assign the other symbol to Player 2.

Create a 3x3 grid of buttons to act as the Tic Tac Toe board.

On button click, update the board state and disable the clicked button.

Check if the current player has won by verifying all rows, columns, and diagonals.

If a player wins, show a message box declaring the winner and reset the game board.

If all cells are clicked without a winner, declare a draw and reset the board.

Switch the current player after every valid move.

Reset the board by enabling all buttons and clearing the game state for a fresh game.


OUTPUT OF THE PROGRAM GOES LIKE:
The program runs a tkinter GUI window where:

Two dialog boxes appear to enter player names.

Player 1 is prompted to choose their symbol (X/O).

A 3x3 grid of buttons is displayed representing the board.

Players click empty squares alternately to place their mark.

After each move, the game checks for a winner.

Upon winning, a popup message declares the winner, and the board resets for a new game.

If all squares fill without a winner, a tie is declared and the board resets.
