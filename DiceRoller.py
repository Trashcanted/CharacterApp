import math
import random
import re
import tkinter as tk
from tkinter import messagebox


def roll_die(sides):
    return random.randint(1, sides)


def xdy(num_dice, sides, use_crit=False, reroll_1s=False, use_elevation=False, explode_threshold=None, explode_inline=False):
    rolls = []
    threshold = 8 if use_elevation else None

    def single_die():
        roll = roll_die(sides)
        total = roll

        if reroll_1s and sides != 20:
            while roll == 1:
                roll = roll_die(sides)
                total = roll

        if use_crit and sides == 20:
            if roll == sides:
                total = 2 * sides
            elif roll == 1:
                total = -sides

        if use_elevation and sides == 20 and 2 <= roll <= threshold:
            total = threshold

        return total

    dice_queue = [1] * num_dice
    while dice_queue:
        _ = dice_queue.pop()
        roll = single_die()
        rolls.append(roll)
        if explode_threshold is not None and roll >= explode_threshold and explode_inline:
            dice_queue.append(1)

    return rolls


# Remaining logic unchanged for notation parsing
def parse_notation(notation):
    parts = re.split(r'([+\-*/])', notation.replace(" ", ""))
    parsed = []
    current_op = '+'

    for part in parts:
        if part in '+-*/':
            current_op = part
        elif 'd' in part:
            match = re.match(r'(\d*)d(\d+)', part)
            if not match:
                raise ValueError(f"Invalid dice notation: {part}")
            num_dice = int(match.group(1)) if match.group(1) else 1
            sides = int(match.group(2))
            parsed.append((current_op, num_dice, sides))
        else:
            parsed.append((current_op, int(part)))

    return parsed


def roll_dice_expression(notation, use_crit=False, reroll_1s=False, use_elevation=False, explode_threshold=None, explode_inline=False):
    match = re.match(r'(\d+)\^(.+)', notation)
    if match:
        times = int(match.group(1))
        dice_expr = match.group(2)
    else:
        times = 1
        dice_expr = notation

    results = []

    for _ in range(times):
        parsed = parse_notation(dice_expr)
        result = 0
        rolls = []
        modifiers = []
        multipliers = []

        for item in parsed:
            op = item[0]
            if len(item) == 2:
                number = item[1]
                match op:
                    case '+': result += number; modifiers.append(number)
                    case '-': result -= number; modifiers.append(-number)
                    case '*': result *= number; multipliers.append(number)
                    case '/': result = math.floor(result / number); multipliers.append(f"1/{number}")
            elif len(item) == 3:
                num_dice, sides = item[1], item[2]
                roll_set = xdy(num_dice, sides, use_crit, reroll_1s, use_elevation, explode_threshold, explode_inline)
                match op:
                    case '+': result += sum(roll_set)
                    case '-': result -= sum(roll_set)
                    case '*': result *= sum(roll_set)
                    case '/': result = math.floor(result / sum(roll_set))
                rolls.append(roll_set)

        results.append((result, rolls, modifiers, multipliers))

    return results


class DiceRollerApp(tk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        self.last_results = []

        self.label = tk.Label(self, text="Enter Dice Notation (e.g. 2d6+3):")
        self.label.pack(pady=5)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.roll_dice)

        self.use_crit = tk.BooleanVar()
        self.reroll_1s = tk.BooleanVar()
        self.use_elevation = tk.BooleanVar()
        self.use_exploding = tk.BooleanVar()
        self.use_repeat = tk.BooleanVar()
        self.explode_inline = tk.BooleanVar()

        explode_frame = tk.Frame(self)
        explode_frame.pack(anchor="w", pady=2, padx=5, fill="x")

        tk.Checkbutton(explode_frame, text="Exploding Dice", variable=self.use_exploding, command=self.toggle_explode_entry).pack(side=tk.LEFT)
        tk.Label(explode_frame, text="Threshold:").pack(side=tk.LEFT)
        self.explode_threshold_entry = tk.Entry(explode_frame, width=5)
        self.explode_threshold_entry.insert(0, "20")
        self.explode_threshold_entry.pack(side=tk.LEFT, padx=5)
        self.explode_threshold_entry.configure(state="disabled")

        tk.Label(explode_frame, text="Explode Gives:").pack(side=tk.LEFT)
        self.explode_multiplier_entry = tk.Entry(explode_frame, width=3)
        self.explode_multiplier_entry.insert(0, "1")
        self.explode_multiplier_entry.pack(side=tk.LEFT)
        self.explode_multiplier_entry.configure(state="disabled")

        self.explode_inline_check = tk.Checkbutton(explode_frame, text="Exploding damage (vs fortunes's favor)", variable=self.explode_inline)
        self.explode_inline_check.pack(side=tk.LEFT)

        repeat_frame = tk.Frame(self)
        repeat_frame.pack(anchor="w", pady=2, padx=5, fill="x")
        tk.Checkbutton(repeat_frame, text="Repeat Notation", variable=self.use_repeat, command=self.toggle_repeat_entry).pack(side=tk.LEFT)
        tk.Label(repeat_frame, text="Times:").pack(side=tk.LEFT)
        self.repeat_times_entry = tk.Entry(repeat_frame, width=5)
        self.repeat_times_entry.insert(0, "1")
        self.repeat_times_entry.pack(side=tk.LEFT, padx=5)
        self.repeat_times_entry.configure(state="disabled")

        tk.Checkbutton(self, text="Critical", variable=self.use_crit).pack()
        tk.Checkbutton(self, text="Reliable Boon (force points only)", variable=self.reroll_1s).pack()
        tk.Checkbutton(self, text="Exceptional Skill", variable=self.use_elevation).pack()

        self.roll_button = tk.Button(self, text="Roll", command=self.roll_dice)
        self.roll_button.pack(pady=5)

        self.result_text = tk.Text(self, height=12, width=60)
        self.result_text.pack(pady=10)
        self.result_text.configure(state="disabled")

        filter_frame = tk.Frame(self)
        filter_frame.pack(anchor="w", pady=2, padx=5, fill="x")
        tk.Label(filter_frame, text="Min Total:").pack(side=tk.LEFT)
        self.min_filter_entry = tk.Entry(filter_frame, width=5)
        self.min_filter_entry.pack(side=tk.LEFT, padx=5)
        tk.Label(filter_frame, text="Max Total:").pack(side=tk.LEFT)
        self.max_filter_entry = tk.Entry(filter_frame, width=5)
        self.max_filter_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(filter_frame, text="Filter Results", command=self.filter_results).pack(side=tk.LEFT, padx=10)

    def toggle_explode_entry(self):
        state = "normal" if self.use_exploding.get() else "disabled"
        self.explode_threshold_entry.configure(state=state)
        self.explode_multiplier_entry.configure(state=state)
        self.explode_inline_check.configure(state=state)

    def toggle_repeat_entry(self):
        if self.use_repeat.get():
            self.repeat_times_entry.configure(state="normal")
        else:
            self.repeat_times_entry.configure(state="disabled")

    def roll_dice(self, event=None):
        notation = self.entry.get()

        try:
            explode_threshold = None
            explode_multiplier = 1
            if self.use_exploding.get():
                try:
                    explode_threshold = int(self.explode_threshold_entry.get())
                    explode_multiplier = int(self.explode_multiplier_entry.get())
                    if explode_multiplier < 1:
                        raise ValueError
                except ValueError:
                    self.display_error("Exploding threshold and multiplier must be valid integers.")
                    return

            repeat_times = 1
            if self.use_repeat.get():
                try:
                    repeat_times = int(self.repeat_times_entry.get())
                    if repeat_times < 1:
                        raise ValueError
                except ValueError:
                    self.display_error("Repeat times must be a positive integer.")
                    return

            explode_inline = self.explode_inline.get()
            results = []
            queue = [1] * repeat_times
            explosion_count = 0
            max_explosions = 1000
            explosion_limit_reached = False

            while queue:
                queue.pop()
                result_set = roll_dice_expression(
                    notation,
                    use_crit=self.use_crit.get(),
                    reroll_1s=self.reroll_1s.get(),
                    use_elevation=self.use_elevation.get(),
                    explode_threshold=explode_threshold,
                    explode_inline=explode_inline
                )
                results.extend(result_set)

                if explode_threshold is not None and not explode_inline and explosion_count < max_explosions:
                    for _, roll_sets, *_ in result_set:
                        for roll_set in roll_sets:
                            for roll in roll_set:
                                if roll >= explode_threshold:
                                    to_add = min(explode_multiplier, max_explosions - explosion_count)
                                    queue.extend([1] * to_add)
                                    explosion_count += to_add
                                    if explosion_count >= max_explosions:
                                        explosion_limit_reached = True
                                        break
                            if explosion_limit_reached:
                                break
                        if explosion_limit_reached:
                            break

            self.last_results = results
            self.render_results(results, explosion_limit_reached)

        except ValueError as e:
            self.display_error(str(e))

    def render_results(self, results, explosion_limit_reached=False):
        self.result_text.configure(state="normal")
        self.result_text.delete(1.0, tk.END)

        for i, (result, rolls, modifiers, multipliers) in enumerate(results):
            self.result_text.insert(tk.END, f"Result of roll set {i + 1}: {result}\n")
            for j, roll_set in enumerate(rolls):
                self.result_text.insert(tk.END, f"  Roll {j + 1}: {roll_set}\n")
            if modifiers:
                self.result_text.insert(tk.END, f"Modifiers: {' + '.join(map(str, modifiers))}\n")
            if multipliers:
                self.result_text.insert(tk.END, f"Multipliers: {' * '.join(map(str, multipliers))}\n")
            self.result_text.insert(tk.END, "\n")

        if explosion_limit_reached:
            self.result_text.insert(tk.END, f"[!] Explosion limit of 1000 reached. Some rolls were skipped.\n\n")

        self.result_text.configure(state="disabled")

    def filter_results(self):
        try:
            min_val = int(self.min_filter_entry.get()) if self.min_filter_entry.get() else None
            max_val = int(self.max_filter_entry.get()) if self.max_filter_entry.get() else None

            filtered = []
            for result in self.last_results:
                total = result[0]
                if min_val is not None and total < min_val:
                    continue
                if max_val is not None and total > max_val:
                    continue
                filtered.append(result)

            self.render_results(filtered)

        except ValueError:
            self.display_error("Filter values must be valid integers.")

    def display_error(self, message):
        self.result_text.configure(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Error: {message}\n")
        self.result_text.configure(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dice Roller")
    app = DiceRollerApp(parent=root)
    app.mainloop()
