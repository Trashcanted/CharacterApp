import random
import tkinter as tk
from tkinter import messagebox, ttk


class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")

        self.diceTypeCount = tk.IntVar()
        self.forcePointTypeCount = tk.IntVar()
        self.addRolls = tk.BooleanVar(value=True)
        self.applyReliableBoon = tk.BooleanVar(value=False)
        self.dice_info = []
        self.force_point_info = []
        self.diceRollTotal = []

        # Style configuration
        style = ttk.Style()
        style.configure(
            "TLabel", background="black", foreground="green", font=("monospace", 10)
        )
        style.configure("TEntry", foreground="green", font=("monospace", 10))
        style.configure(
            "TCheckbutton",
            background="black",
            foreground="green",
            font=("monospace", 10),
        )
        style.configure(
            "TButton", background="black", foreground="green", font=("monospace", 10)
        )

        self.root.configure(background="black")

        self.create_widgets()

    def create_widgets(self):
        self.entries = []
        ttk.Label(
            self.root, text="How many different types of dice are you rolling?"
        ).grid(column=0, row=0, padx=10, pady=5)
        dice_count_entry = ttk.Entry(self.root, textvariable=self.diceTypeCount)
        dice_count_entry.grid(column=1, row=0, padx=10, pady=5)
        self.entries.append(dice_count_entry)
        dice_count_entry.bind("<Return>", self.focus_next_widget)

        ttk.Label(
            self.root, text="How many different types of force points are you using?"
        ).grid(column=0, row=1, padx=10, pady=5)
        force_point_count_entry = ttk.Entry(
            self.root, textvariable=self.forcePointTypeCount
        )
        force_point_count_entry.grid(column=1, row=1, padx=10, pady=5)
        self.entries.append(force_point_count_entry)
        force_point_count_entry.bind("<Return>", self.focus_next_widget)

        ttk.Button(self.root, text="Submit", command=self.setup_dice_inputs).grid(
            column=2, row=0, padx=10, pady=5, rowspan=2
        )

    def setup_dice_inputs(self):
        for widget in self.root.winfo_children():
            widget.grid_forget()

        self.entries = []

        for i in range(self.diceTypeCount.get()):
            dice_info = {}
            ttk.Label(self.root, text=f"Dice {i+1} Sides:").grid(
                column=0, row=i * 5, padx=10, pady=5
            )
            sides_entry = ttk.Entry(self.root)
            sides_entry.grid(column=1, row=i * 5, padx=10, pady=5)
            self.entries.append(sides_entry)
            dice_info["sides"] = sides_entry

            ttk.Label(self.root, text=f"Dice {i+1} Count:").grid(
                column=0, row=i * 5 + 1, padx=10, pady=5
            )
            count_entry = ttk.Entry(self.root)
            count_entry.grid(column=1, row=i * 5 + 1, padx=10, pady=5)
            self.entries.append(count_entry)
            dice_info["count"] = count_entry

            ttk.Label(self.root, text=f"Dice {i+1} Modifier:").grid(
                column=0, row=i * 5 + 2, padx=10, pady=5
            )
            modifier_entry = ttk.Entry(self.root)
            modifier_entry.grid(column=1, row=i * 5 + 2, padx=10, pady=5)
            self.entries.append(modifier_entry)
            dice_info["modifier"] = modifier_entry

            exceptional_skill = tk.BooleanVar(value=False)
            ttk.Checkbutton(
                self.root, text="Exceptional Skill", variable=exceptional_skill
            ).grid(column=1, row=i * 5 + 3, padx=10, pady=5)
            dice_info["exceptional_skill"] = exceptional_skill

            crit = tk.BooleanVar(value=False)
            ttk.Checkbutton(self.root, text="Critical", variable=crit).grid(
                column=1, row=i * 5 + 4, padx=10, pady=5
            )
            dice_info["crit"] = crit

            self.dice_info.append(dice_info)

        for i in range(self.forcePointTypeCount.get()):
            force_point_info = {}
            ttk.Label(self.root, text=f"Force Point {i+1} Sides:").grid(
                column=0, row=self.diceTypeCount.get() * 5 + i * 2, padx=10, pady=5
            )
            sides_entry = ttk.Entry(self.root)
            sides_entry.grid(
                column=1, row=self.diceTypeCount.get() * 5 + i * 2, padx=10, pady=5
            )
            self.entries.append(sides_entry)
            force_point_info["sides"] = sides_entry

            ttk.Label(self.root, text=f"Force Point {i+1} Count:").grid(
                column=0, row=self.diceTypeCount.get() * 5 + i * 2 + 1, padx=10, pady=5
            )
            count_entry = ttk.Entry(self.root)
            count_entry.grid(
                column=1, row=self.diceTypeCount.get() * 5 + i * 2 + 1, padx=10, pady=5
            )
            self.entries.append(count_entry)
            force_point_info["count"] = count_entry

            self.force_point_info.append(force_point_info)

        ttk.Button(self.root, text="Roll Dice", command=self.roll_dice).grid(
            column=0,
            row=self.diceTypeCount.get() * 5 + self.forcePointTypeCount.get() * 2 + 2,
            padx=10,
            pady=5,
        )
        ttk.Button(self.root, text="Reset", command=self.reset).grid(
            column=1,
            row=self.diceTypeCount.get() * 5 + self.forcePointTypeCount.get() * 2 + 2,
            padx=10,
            pady=5,
        )
        ttk.Checkbutton(
            self.root, text="Add Rolls Together", variable=self.addRolls
        ).grid(
            column=0,
            row=self.diceTypeCount.get() * 5 + self.forcePointTypeCount.get() * 2 + 3,
            padx=10,
            pady=5,
        )
        ttk.Checkbutton(
            self.root,
            text="Apply Reliable Boon to Force Points",
            variable=self.applyReliableBoon,
        ).grid(
            column=1,
            row=self.diceTypeCount.get() * 5 + self.forcePointTypeCount.get() * 2 + 3,
            padx=10,
            pady=5,
        )

    def focus_next_widget(self, event):
        event.widget.tk_focusNext().focus()
        return "break"

    def roll_dice(self):
        self.diceRollTotal = []

        for dice in self.dice_info:
            for _ in range(int(dice["count"].get())):
                roll = random.randint(1, int(dice["sides"].get()))
                roll_mod = int(dice["modifier"].get())

                if dice["exceptional_skill"].get() and roll in [2, 3, 4, 5, 6, 7]:
                    roll = 8

                if dice["crit"].get():
                    if roll == 20:
                        roll = 40
                    elif roll == 1:
                        roll = -20

                self.diceRollTotal.append(roll)
                self.diceRollTotal.append(roll_mod)

        for force_point in self.force_point_info:
            for _ in range(int(force_point["count"].get())):
                force_point_roll = random.randint(1, int(force_point["sides"].get()))

                if self.applyReliableBoon.get() and force_point_roll == 1:
                    force_point_roll = random.randint(
                        1, int(force_point["sides"].get())
                    )

                self.diceRollTotal.append(force_point_roll)

        self.show_results()

    def show_results(self):
        result = f"Dice Rolls: {self.diceRollTotal}"
        if self.addRolls.get():
            result += f"\nSum of Rolls: {sum(self.diceRollTotal)}"

        messagebox.showinfo("Results", result)

    def reset(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.dice_info.clear()
        self.force_point_info.clear()
        self.create_widgets()


if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()
