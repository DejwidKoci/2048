import tkinter as tk
import colors as c
import random

class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("2048")
        self.window.resizable(0,0)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = Game()
    game.run()
