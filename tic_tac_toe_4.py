"""
Tic-Tac-Toe Version 4: The GUI & AI Upgrade
Upgrade: Graphical User Interface using tkinter with a Random AI opponent.
UX: Centers a large window, minimizes others, and adds a 3s delay for AI moves.
"""

import tkinter as tk
from tkinter import messagebox
import random
import os
import ctypes

class TicTacToeGUI:
    def __init__(self):
        # Attempt to minimize other windows (Windows specific)
        try:
            ctypes.windll.user32.ShowCursor(True)
            ctypes.windll.shell32.ShellExecuteW(None, "find", "shell:::{3080BE0D-D7AD-11D9-BD98-0000947B0257}", None, None, 0)
        except:
            pass

        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe V4: Human vs AI")
        
        # Window sizing and centering logic
        width, height = 600, 600
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        self.window.geometry(f'{width}x{height}+{int(sw/2-width/2)}+{int(sh/2-height/2)}')

        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.create_widgets()

    def create_widgets(self):
        """Creates the 3x3 grid of buttons."""
        for r in range(3):
            self.window.grid_rowconfigure(r, weight=1)
            self.window.grid_columnconfigure(r, weight=1)
            for c in range(3):
                btn = tk.Button(self.window, text="", font=('Arial', 50, 'bold'),
                                command=lambda r=r, c=c: self.human_move(r, c))
                btn.grid(row=r, column=c, sticky="nsew")
                self.buttons[r][c] = btn

    def toggle_buttons(self, state):
        """Enable or disable all empty buttons."""
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "":
                    self.buttons[r][c].config(state=state)

    def human_move(self, r, c):
        if self.board[r][c] == "" and not self.game_over:
            self.process_move(r, c, "X")
            
            if not self.game_over:
                # Disable buttons and wait for AI
                self.toggle_buttons("disabled")
                self.window.after(3000, self.ai_move)

    def ai_move(self):
        if self.game_over: return
        
        # Level 1 AI: Randomly pick an empty spot
        empty_spots = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ""]
        if empty_spots:
            r, c = random.choice(empty_spots)
            self.process_move(r, c, "O")
            self.toggle_buttons("normal")

    def process_move(self, r, c, player):
        self.board[r][c] = player
        self.buttons[r][c].config(text=player, state="disabled", disabledforeground="black")
        
        if self.check_win(player):
            messagebox.showinfo("Game Over", f"Player {player} wins! 🎉")
            self.reset_game()
        elif all(cell != "" for row in self.board for cell in row):
            messagebox.showinfo("Game Over", "It's a draw! 🤝")
            self.reset_game()

    def check_win(self, p):
        # Check rows, cols, and diagonals
        for i in range(3):
            if all(self.board[i][j] == p for j in range(3)): return True
            if all(self.board[j][i] == p for j in range(3)): return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == p: return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == p: return True
        return False

    def reset_game(self):
        self.game_over = False
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", state="normal")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    TicTacToeGUI().run()