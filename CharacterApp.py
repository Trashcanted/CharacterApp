import tkinter as tk
from CharacterSheet import CharacterSheetApp
from DiceRoller import DiceRollerApp as NotationDiceRollerApp

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stellar Fantasies")
        self.geometry("1200x600")  # Adjusted size to fit all apps

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        self.create_frames()

    def create_frames(self):

        character_sheet_frame = CharacterSheetApp(self.container, self)
        character_sheet_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

        notation_dice_roller_frame = NotationDiceRollerApp(self.container, self)
        notation_dice_roller_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.frames["CharacterSheetApp"] = character_sheet_frame
        self.frames["NotationDiceRollerApp"] = notation_dice_roller_frame

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_rowconfigure(1, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)

    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        app_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Apps", menu=app_menu)
        app_menu.add_command(label="Dice Roller", command=lambda: self.show_frame("DiceRollerApp"))
        app_menu.add_command(label="Character Sheet", command=lambda: self.show_frame("CharacterSheetApp"))

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
