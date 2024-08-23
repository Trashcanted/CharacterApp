import math
import random
import re
import tkinter as tk
from tkinter import messagebox


# Dice rolling logic
def parse_notation(notation):
    """
    Parses the dice notation and returns a list of dice rolls and integers with their respective operations.
    """
    parts = re.split(r"([+-])", notation.replace(" ", ""))
    parsed_rolls = []
    current_op = "+"

    for part in parts:
        if part in "+-":
            current_op = part
        else:
            if re.match(r"^\d+$", part):
                parsed_rolls.append((current_op, int(part)))
            else:
                num_dice, sides, roll_type = parse_single_notation(part)
                parsed_rolls.append((current_op, num_dice, sides, roll_type))

    return parsed_rolls


def parse_single_notation(notation):
    """
    Parses a single dice notation and returns the number of dice, the number of sides, and the type of roll.
    """
    match = re.match(r"(?:(\d*)[dfrce](\d+))", notation)

    if not match:
        raise ValueError("Invalid dice notation")

    num_dice = int(match.group(1) or 1)
    sides = int(match.group(2))

    if "ce" in notation:
        roll_type = "ce"
    elif "c" in notation:
        roll_type = "c"
    elif "e" in notation:
        roll_type = "e"
    elif "r" in notation:
        roll_type = "r"
    elif "f" in notation:
        roll_type = "f"
    else:
        roll_type = "d"

    return num_dice, sides, roll_type


def roll_die(sides):
    """
    Rolls a single die with the given number of sides.
    """
    return random.randint(1, sides)


def xdy(num_dice, sides):
    """
    Rolls num_dice y-sided dice.
    """
    return [roll_die(sides) for _ in range(num_dice)]


def xcy(num_dice, sides):
    """
    Rolls num_dice y-sided dice with custom rules for critical success and critical failure.
    """
    rolls = []
    for _ in range(num_dice):
        roll = roll_die(sides)
        if roll == sides:
            rolls.append(2 * sides)
        elif roll == 1:
            rolls.append(-sides)
        else:
            rolls.append(roll)
    return rolls


def xey(num_dice, sides):
    """
    Rolls num_dice y-sided dice with custom rule: if roll is between 2 and threshold, set to threshold.
    """
    rolls = []
    threshold = math.ceil((2 * sides) / 5)
    for _ in range(num_dice):
        roll = roll_die(sides)
        if 2 <= roll <= threshold:
            rolls.append(threshold)
        else:
            rolls.append(roll)
    return rolls


def xcey(num_dice, sides):
    """
    Rolls num_dice y-sided dice applying both xcy and xey rules.
    """
    rolls = []
    threshold = math.ceil((2 * sides) / 5)
    for _ in range(num_dice):
        roll = roll_die(sides)
        if roll == sides:
            rolls.append(2 * sides)
        elif roll == 1:
            rolls.append(-sides)
        elif 2 <= roll <= threshold:
            rolls.append(threshold)
        else:
            rolls.append(roll)
    return rolls


def xfy(num_dice, sides):
    """
    Rolls num_dice y-sided dice. Same as xdy.
    """
    return xdy(num_dice, sides)


def xry(num_dice, sides):
    """
    Rolls num_dice y-sided dice and rerolls any 1s.
    """
    rolls = []
    for _ in range(num_dice):
        roll = roll_die(sides)
        while roll == 1:
            roll = roll_die(sides)
        rolls.append(roll)
    return rolls


def roll_dice_expression(notation):
    """
    Interprets the dice notation with addition, subtraction, and integers, and performs the rolls.
    """
    parsed_rolls = parse_notation(notation)
    total_result = 0
    all_rolls = []
    modifiers = []

    for parsed in parsed_rolls:
        op = parsed[0]
        if len(parsed) == 2:
            number = parsed[1]
            if op == "+":
                total_result += number
                modifiers.append(number)
            elif op == "-":
                total_result -= number
                modifiers.append(-number)
        else:
            num_dice, sides, roll_type = parsed[1], parsed[2], parsed[3]
            if roll_type == "d":
                rolls = xdy(num_dice, sides)
            elif roll_type == "f":
                rolls = xfy(num_dice, sides)
            elif roll_type == "r":
                rolls = xry(num_dice, sides)
            elif roll_type == "c":
                rolls = xcy(num_dice, sides)
            elif roll_type == "e":
                rolls = xey(num_dice, sides)
            elif roll_type == "ce":
                rolls = xcey(num_dice, sides)
            else:
                raise ValueError(f"Unknown roll type: {roll_type}")

            if op == "+":
                total_result += sum(rolls)
            elif op == "-":
                total_result -= sum(rolls)

            all_rolls.extend(rolls)

    return total_result, all_rolls, modifiers


# Tkinter Interface
class DiceRollerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notation Dice Roller")
        self.geometry("400x300")

        # Label
        self.label = tk.Label(self, text="Enter Dice Notation:")
        self.label.pack(pady=10)

        # Entry
        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        # Button
        self.roll_button = tk.Button(self, text="Roll", command=self.roll_dice)
        self.roll_button.pack(pady=10)

        # Result Text
        self.result_text = tk.Text(self, height=10, width=40)
        self.result_text.pack(pady=10)
        self.result_text.configure(state="disabled")

    def roll_dice(self):
        """
        Handles the roll button click event, rolls the dice, and displays the result.
        """
        notation = self.entry.get()
        try:
            result, rolls, modifiers = roll_dice_expression(notation)
            self.display_result(result, rolls, modifiers)
        except ValueError as e:
            self.display_error(str(e))

    def display_result(self, result, rolls, modifiers):
        """
        Displays the result of the dice roll in the text widget.
        """
        self.result_text.configure(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(
            tk.END, f"Result of rolling {self.entry.get()}: {result}\n"
        )
        self.result_text.insert(tk.END, f"All rolls: {rolls}\n")
        if modifiers:
            self.result_text.insert(
                tk.END, f"Modifier(s): {' + '.join(map(str, modifiers))}\n"
            )
        self.result_text.configure(state="disabled")

    def display_error(self, error_message):
        """
        Displays an error message in the text widget.
        """
        self.result_text.configure(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Error: {error_message}\n")
        self.result_text.configure(state="disabled")


if __name__ == "__main__":
    app = DiceRollerApp()
    app.mainloop()
