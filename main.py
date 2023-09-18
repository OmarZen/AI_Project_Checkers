from time import sleep
import tkinter as tk
from tkinter import ttk

from Game import Game


class Window:
    def __init__(self):
        # Window Creation by tkinter
        self.window = tk.Tk()
        self.window.title("Checkers")
        self.window.geometry("600x600")
        self.window.configure(background="#FFEAD4")  # window background
        self.Frame1 = tk.Frame(self.window, background="#CC9544", pady=10)
        # config
        self.Frame1.columnconfigure(0, weight=1)
        self.Frame1.columnconfigure(1, weight=1)
        self.Frame1.columnconfigure(2, weight=1)

        label = tk.Label(self.Frame1,
                         text="Algorithm Type:", font=('Calibri', 10),
                         background="#361500", foreground="White")
        label.grid(row=0, column=0, sticky="w", padx=10)

        label = tk.Label(self.Frame1,
                         text="Difficulty Level:", font=('Calibri', 10),
                         background="#361500", foreground="White")
        label.grid(row=1, column=0, sticky="w", padx=10)

        def onceSelected(value):
            print("Selected:", value)

        AlgorithmOptions = ["Minimax", "AlphaBeta"]
        Algorithm = tk.StringVar(self.Frame1)
        Algorithm.set(AlgorithmOptions[0])

        def algorithmSelected(event):
            selected_value = Algorithm.get()
            onceSelected(selected_value)

        Dropdown = ttk.Combobox(self.Frame1, textvariable=Algorithm, values=AlgorithmOptions, state="readonly")
        Dropdown.grid(row=0, column=1, padx=10)
        Dropdown.bind("<<ComboboxSelected>>", algorithmSelected)

        DifficultyOptions = ['3', '5', '10', '15']
        Difficulty = tk.StringVar(self.Frame1)
        Difficulty.set(DifficultyOptions[0])

        def difficultySelected(event):
            selected_value = Difficulty.get()
            onceSelected(selected_value)

        Dropdown = ttk.Combobox(self.Frame1, textvariable=Difficulty, values=DifficultyOptions, state="readonly")
        Dropdown.grid(row=1, column=1, padx=10)
        Dropdown.bind("<<ComboboxSelected>>", difficultySelected)

        ResetButton = tk.Button(self.Frame1,
                                text="Reset", border=0,
                                background="#1C0A00", foreground="White", width=15,
                                command=lambda: self.Game.ResetButton())
        ResetButton.grid(row=0, column=2, padx=10)

        BackButton = tk.Button(self.Frame1,
                               text="Back", border=0,
                               background="#E5E5CB", foreground="Black", width=15,
                               command=lambda: self.Game.getPreviousBoard())
        BackButton.grid(row=1, column=2, padx=10)

        NextButton = tk.Button(self.Frame1,
                               text="Next", border=0,
                               background="#E5E5CB", foreground="White",
                               command=lambda: self.Game.Play(), width=25, highlightthickness=2)
        NextButton.grid(row=0, column=3, padx=10)
        label = tk.Label(self.Frame1,
                         text="Computer is White - AI is Black", font=('Calibri', 10),
                         background="#613100", foreground="White", width=25, highlightthickness=1)
        label.grid(row=1, column=3, sticky="w", padx=10)

        self.Frame1.pack(fill="both", side="top")

        self.Frame2 = tk.Frame(self.window, background="#a39898")
        self.Frame2.pack(expand=True)  # Window size

        # sleep(0.75)
        self.Game = Game(self.Frame2, NextButton, Algorithm, Difficulty)

        self.window.mainloop()


if __name__ == "__main__":
    Run = Window()
