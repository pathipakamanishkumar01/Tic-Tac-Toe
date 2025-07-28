import tkinter as tk
from tkinter import simpledialog, messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.players = [None, None]
        self.symbols = ["X", "O"]
        self.current_player = 0
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.get_player_info()
        self.create_board()

    def get_player_info(self):
        # Get player names
        self.players[0] = simpledialog.askstring("Player 1", "Enter name for Player 1:")
        self.players[1] = simpledialog.askstring("Player 2", "Enter name for Player 2:")
        if not self.players[0]: self.players[0] = "Player 1"
        if not self.players[1]: self.players[1] = "Player 2"

        # Player 1 chooses symbol
        symbol = simpledialog.askstring("Symbol", f"{self.players[0]}, choose your symbol (X/O):", initialvalue="X")
        if symbol and symbol.upper() == "O":
            self.symbols = ["O", "X"]
        else:
            self.symbols = ["X", "O"]

    def create_board(self):
        frame = tk.Frame(self.master)
        frame.pack()
        for i in range(3):
            for j in range(3):
                button = tk.Button(frame, text="", width=5, height=2, font=("Arial", 24),
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.symbols[self.current_player]
            self.buttons[row][col].config(text=self.symbols[self.current_player], state="disabled")
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"{self.players[self.current_player]} wins!")
                self.reset_game()
            elif all(self.board[i][j] != "" for i in range(3) for j in range(3)):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = 1 - self.current_player

    def check_winner(self):
        b = self.board
        for i in range(3):
            # Rows & columns
            if b[i][0] == b[i][1] == b[i][2] != "":
                return True
            if b[0][i] == b[1][i] == b[2][i] != "":
                return True
        # Diagonals
        if b[0][0] == b[1][1] == b[2][2] != "":
            return True
        if b[0][2] == b[1][1] == b[2][0] != "":
            return True
        return False

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="", state="normal")
        self.current_player = 0

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window while getting player info
    app = TicTacToe(root)
    root.deiconify() # Show main window after dialogs
    root.mainloop()
