import tkinter as tk
from multiprocessing import Process
from time import sleep

from CharacterSheet import CharacterSheetApp
from NotationDiceRoller import DiceRollerApp as NotationDiceRollerApp
from Roll import DiceRollerApp


def run_dice_roller_app():
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()


def run_character_sheet_app():
    root = tk.Tk()
    app = CharacterSheetApp(root)
    root.mainloop()


def run_notation_dice_roller_app():
    app = NotationDiceRollerApp()
    app.mainloop()


if __name__ == "__main__":
    # Create separate processes for each Tkinter application
    p1 = Process(target=run_dice_roller_app)
    p2 = Process(target=run_character_sheet_app)
    p3 = Process(target=run_notation_dice_roller_app)

    # Start both processes
    p2.start()

    sleep(0.2)
    p1.start()
    p3.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()
    p3.join()
