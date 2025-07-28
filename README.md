# Tic-Tac-Toe
HI, This project is a classic Tic Tac Toe game implemented using Python's tkinter module, providing a graphical user interface for easy two-player interaction. The program allows two players to enter their names, player 1 to choose a symbol (X or O), while player 2 is assigned the remaining symbol. Players take alternate turns clicking on the cells in a 3x3 grid. The game checks for a winner (three marks in a horizontal, vertical or diagonal sequence) or a draw (when all cells are filled without a winner). Upon game completion, the result is shown via a pop-up message box, and the board resets dynamically for a new game.

THE ALGORITHM I USED TO BUILD THIS PROJECT:
1.Import tkinter and necessary dialog/messagebox modules.

2.Initialize the main window with title "Tic Tac Toe".

3.Get player names via input dialog boxes. If no input is entered, assign default names.

4.Ask Player 1 to select their symbol (X or O), and assign the other symbol to Player 2.

5.Create a 3x3 grid of buttons to act as the Tic Tac Toe board.

6.On button click, update the board state and disable the clicked button.

7.Check if the current player has won by verifying all rows, columns, and diagonals.

8.If a player wins, show a message box declaring the winner and reset the game board.

9.If all cells are clicked without a winner, declare a draw and reset the board.

10.Switch the current player after every valid move.

11.Reset the board by enabling all buttons and clearing the game state for a fresh game.


OUTPUT OF THE PROGRAM GOES LIKE:
The program runs a tkinter GUI window where:

1.Two dialog boxes appear to enter player names.

2.Player 1 is prompted to choose their symbol (X/O).

3.A 3x3 grid of buttons is displayed representing the board.

4.Players click empty squares alternately to place their mark.

5.After each move, the game checks for a winner.

6.Upon winning, a popup message declares the winner, and the board resets for a new game.

7.If all squares fill without a winner, a tie is declared and the board resets.
