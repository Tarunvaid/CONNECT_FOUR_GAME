import tkinter as tk
from tkinter import messagebox

class ConnectFourGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'
        self.buttons = []
        self.create_board()

    def create_board(self):
        for row in range(6):
            button_row = []
            for col in range(7):
                button = tk.Button(self.root, text=' ', width=10, height=3,
                                   font=('Helvetica', 20, 'bold'),
                                   fg='white', bg='blue',
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

    def make_move(self, row, col):
        if self.board[0][col] != ' ':
            return

        for r in reversed(range(6)):
            if self.board[r][col] == ' ':
                self.board[r][col] = self.current_player
                self.buttons[r][col].config(text=self.current_player, bg='red' if self.current_player == 'X' else 'yellow')
                break

        if self.check_winner():
            messagebox.showinfo("Connect Four", f"Player {self.current_player} wins!")
            self.reset_board()
            return

        self.switch_player()

    def check_winner(self):
        # Check horizontal
        for row in self.board:
            for col in range(4):
                if row[col] == self.current_player and all(row[col + i] == self.current_player for i in range(4)):
                    return True

        # Check vertical
        for col in range(7):
            for row in range(3):
                if self.board[row][col] == self.current_player and all(self.board[row + i][col] == self.current_player for i in range(4)):
                    return True

        # Check diagonal (bottom-left to top-right)
        for col in range(4):
            for row in range(3, 6):
                if self.board[row][col] == self.current_player and all(self.board[row - i][col + i] == self.current_player for i in range(4)):
                    return True

        # Check diagonal (top-left to bottom-right)
        for col in range(4):
            for row in range(3):
                if self.board[row][col] == self.current_player and all(self.board[row + i][col + i] == self.current_player for i in range(4)):
                    return True

        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_board(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        for row in range(6):
            for col in range(7):
                self.buttons[row][col].config(text=' ', bg='blue')

if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFourGUI(root)
    root.mainloop()


