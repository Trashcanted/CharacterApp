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
    parts = re.split(r"([+\-*/])", notation.replace(" ", ""))
    parsed_rolls = []
    current_op = "+"

    for part in parts:
        if part in "+-*/":
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
    match = re.match(r"(?:(\d*)[dfrce](\d+)|(\d+)ce(\d+))", notation)

    if not match:
        raise ValueError("Invalid dice notation")

    if match.group(3):  # Handling "{number1}ce{number2}"
        num_dice = int(match.group(3))
        sides = int(match.group(4))
        roll_type = "ce"
    else:
        num_dice = int(match.group(1) or 1)
        sides = int(match.group(2))

        if "c" in notation:
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
    # Parse the notation for multiple rolls
    match = re.match(r"(\d+)\^(.+)", notation)
    if match:
        times = int(match.group(1))
        dice_notation = match.group(2)
    else:
        times = 1
        dice_notation = notation

    results = []

    for _ in range(times):
        parsed_rolls = parse_notation(dice_notation)
        result = 0
        all_rolls = []
        modifiers = []
        multipliers = []

        for parsed in parsed_rolls:
            op = parsed[0]
            if len(parsed) == 2:
                number = parsed[1]
                match op:
                    case "+":
                        result += number
                        modifiers.append(number)
                    case "-":
                        result -= number
                        modifiers.append(-number)
                    case "*":
                        result *= number
                        multipliers.append(number)
                    case "/":
                        result = math.floor(result / number)
                        multipliers.append(f"1 / {number}")
                    case _:
                        messagebox.showerror(
                            "Error", f"Unknown operator: {op}"
                        )

            elif len(parsed) == 4:  # Handling dice rolls with an operator
                num_dice, sides, roll_type = parsed[1], parsed[2], parsed[3]

                match roll_type:
                    case "d":
                        rolls = xdy(num_dice, sides)
                    case "f":
                        rolls = xfy(num_dice, sides)
                    case "r":
                        rolls = xry(num_dice, sides)
                    case "c":
                        rolls = xcy(num_dice, sides)
                    case "e":
                        rolls = xey(num_dice, sides)
                    case "ce":
                        rolls = xcey(num_dice, sides)
                    case _:
                        messagebox.showerror(
                            "Error", f"Unknown roll type: {roll_type}"
                        )

                match op:
                    case "+":
                        result += sum(rolls)
                    case "-":
                        result -= sum(rolls)
                    case "*":
                        result *= sum(rolls)
                    case "/":
                        result /= sum(rolls)
                    case _:
                        messagebox.showerror(
                            "Error", f"Unknown operator: {op}"
                        )

                all_rolls.extend(rolls)

        results.append((result, all_rolls, modifiers, multipliers))

    return results


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
        self.entry.bind("<KP_Enter>", self.roll_dice)
        self.entry.bind("<Return>", self.roll_dice)  # Bind Enter key to roll dice

        # Button
        self.roll_button = tk.Button(self, text="Roll", command=self.roll_dice)
        self.roll_button.pack(pady=10)

        # Result Text
        self.result_text = tk.Text(self, height=10, width=40)
        self.result_text.pack(pady=10)
        self.result_text.configure(state="disabled")

    def roll_dice(self, event=None):
        """
        Handles the roll button click event, rolls the dice, and displays the result.
        Implements a rolling animation before showing the result.
        """
        self.show_rolling(1)  # Start the rolling animation with the first dot

    def show_rolling(self, step):
        """
        Displays the rolling animation step-by-step with a delay.
        """
        self.result_text.configure(state="normal")
        self.result_text.delete(1.0, tk.END)

        if step == 1:
            self.result_text.insert(tk.END, "Rolling .")
        elif step == 2:
            self.result_text.insert(tk.END, "Rolling ..")
        elif step == 3:
            self.result_text.insert(tk.END, "Rolling ...")
        else:
            self.result_text.delete(1.0, tk.END)  # Clear the rolling text
            self.display_result()  # Show the final dice roll result
            return

        self.result_text.configure(state="disabled")
        self.after(
            500, self.show_rolling, step + 1
        )  # Schedule the next step after 500ms

    def display_result(self):
        """
        Rolls the dice and displays the result in the text widget.
        """
        notation = self.entry.get()
        try:
            results = roll_dice_expression(notation)
            self.result_text.configure(state="normal")
            self.result_text.delete(1.0, tk.END)
            for i, (
                result,
                rolls,
                modifiers,
                multipliers,
            ) in enumerate(results):
                self.result_text.insert(
                    tk.END, f"Result of roll set {i + 1}: {result}\n"
                )
                self.result_text.insert(tk.END, f"All rolls: {rolls}\n")
                if modifiers:
                    self.result_text.insert(
                        tk.END,
                        f"Modifier(s): {' + '.join(map(str, modifiers))}\n"
                    )
                if multipliers:
                    self.result_text.insert(
                        tk.END,
                        f"Multiplier(s): {' * '.join(map(str, multipliers))}\n"
                    )
                self.result_text.insert(tk.END, "\n")
            self.result_text.configure(state="disabled")
        except ValueError as e:
            self.display_error(str(e))

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
