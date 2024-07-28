import tkinter as tk
from multiprocessing import Process

from CharacterSheet import CharacterSheetApp
from Roll import DiceRollerApp


def run_dice_roller_app():
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()


def run_character_sheet_app():
    root = tk.Tk()
    app = CharacterSheetApp(root)
    root.mainloop()


if __name__ == "__main__":
    # Create separate processes for each Tkinter application
    p1 = Process(target=run_dice_roller_app)
    p2 = Process(target=run_character_sheet_app)

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()
