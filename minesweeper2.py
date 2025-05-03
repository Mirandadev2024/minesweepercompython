import tkinter as tk
from tkinter import messagebox
import random

class Minesweeper:
    def __init__(self, root, grid_size, num_mines):
        self.root = root
        self.root.title("Minesweeper")

        self.GRID_SIZE = grid_size
        self.NUM_MINES = num_mines
        self.flags = set()
        self.revealed = set()
        self.buttons = []
        self.mines = set(random.sample(range(self.GRID_SIZE * self.GRID_SIZE), self.NUM_MINES))
        self.board = [[0] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]

        self.mine_counter = tk.Button(root, text=f"Minas restantes: {self.NUM_MINES}", state='disabled', disabledforeground='black')
        self.mine_counter.grid(row=0, column=0, columnspan=self.GRID_SIZE)

        self.create_board()
        self.place_mines()
        self.calculate_numbers()

    def game_over(self):
        for r in range(self.GRID_SIZE):
            for c in range(self.GRID_SIZE):
                if self.board[r][c] == -1:
                    self.buttons[r][c].config(text="💣", bg="red")
        messagebox.showinfo("Game Over", "You hit a mine! Game Over.")
        self.root.quit()

    def check_win(self):
        if len(self.flags) == self.NUM_MINES and all((divmod(m, self.GRID_SIZE) in self.flags) for m in self.mines):
            messagebox.showinfo("You Win", "Congratulations! You found all the mines!")
            self.root.quit()

    def update_mine_counter(self):
        remaining = self.NUM_MINES - len(self.flags)
        self.mine_counter.config(text=f"Minas restantes: {remaining}")
        self.check_win()

    def create_board(self):
        for i in range(self.GRID_SIZE):
            row = []
            for j in range(self.GRID_SIZE):
                btn = tk.Button(self.root, text=" ", width=3, height=1, command=lambda r=i, c=j: self.reveal_cell(r, c))
                btn.grid(row=i + 1, column=j)
                btn.bind("<Button-3>", lambda event, r=i, c=j: self.put_flag(r, c))
                row.append(btn)
            self.buttons.append(row)

    def place_mines(self):
        for mine in self.mines:
            r, c = divmod(mine, self.GRID_SIZE)
            self.board[r][c] = -1

    def calculate_numbers(self):
        for r in range(self.GRID_SIZE):
            for c in range(self.GRID_SIZE):
                if self.board[r][c] == -1:
                    continue
                count = sum(
                    (nr * self.GRID_SIZE + nc) in self.mines
                    for nr in range(r - 1, r + 2)
                    for nc in range(c - 1, c + 2)
                    if 0 <= nr < self.GRID_SIZE and 0 <= nc < self.GRID_SIZE
                )
                self.board[r][c] = count

    def put_flag(self, r, c):
        if (r, c) in self.revealed:
            return
        if (r, c) in self.flags:
            self.buttons[r][c].config(text=" ")
            self.flags.remove((r, c))
        else:
            if len(self.flags) < self.NUM_MINES:
                self.buttons[r][c].config(text="🚩", fg="red")
                self.flags.add((r, c))
        self.update_mine_counter()

    def reveal_cell(self, r, c, depth=0):
        if (r, c) in self.revealed or (r, c) in self.flags:
            return

        self.revealed.add((r, c))
        if self.board[r][c] == -1:
            self.buttons[r][c].config(text="💣", bg="red")
            self.game_over()
        else:
            self.buttons[r][c].config(text=str(self.board[r][c]), bg="lightgray")
            if self.board[r][c] == 0 and depth < 4:
                for nr in range(r - 1, r + 2):
                    for nc in range(c - 1, c + 2):
                        if (nr, nc) != (r, c) and 0 <= nr < self.GRID_SIZE and 0 <= nc < self.GRID_SIZE:
                            self.reveal_cell(nr, nc, depth + 1)

def show_difficulty_menu():
    menu_root = tk.Tk()
    menu_root.title("Escolha a Dificuldade")

    def start_game(grid_size):
        menu_root.destroy()
        root = tk.Tk()
        Minesweeper(root, grid_size=grid_size, num_mines=40 if grid_size == 20 else 15)
        root.mainloop()

    tk.Label(menu_root, text="Selecione a dificuldade:").pack(pady=10)
    tk.Button(menu_root, text="Fácil (10x10)", width=20, command=lambda: start_game(10)).pack(pady=5)
    tk.Button(menu_root, text="Difícil (20x20)", width=20, command=lambda: start_game(20)).pack(pady=5)

    menu_root.mainloop()

if __name__ == "__main__":
    show_difficulty_menu()
