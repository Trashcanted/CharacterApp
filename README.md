# Setup Guide

Install python from python.org

## Mac or Linux

Run the character app with `python3 character_app.py` in the terminal

## Windows

the same as Mac or Linux, but `python character_app.py`

# Dice Notation Guide

## General Format
- `XdY` 
  - `X` = Number of dice (default 1 if omitted)
  - `d` = Dice
  - `Y` = Number of sides

## Notation Rules

1. **Standard Dice Roll (`d`)**
   - `XdY`: Rolls `X` dice with `Y` sides.
   - *Example*: `2d6` (Roll two 6-sided dice).

2. **Critical (`c`)**
   - `XcY`: Rolls `X` dice. Max roll (`Y`) becomes `2Y`, roll of `1` becomes `-Y`.
   - *Example*: `2c8` (Roll two 8-sided dice; 8 becomes 16, 1 becomes -8).

3. **Exceptional Skill (`e`)**
   - `XeY`: Rolls `X` dice. Rolls between 2 and `ceil((2 * Y) / 5)` become that threshold.
   - *Example*: `3e10` (Roll three 10-sided dice; results between 2 and threshold become threshold).

4. **Critical Exceptional Skill (`ce`)**
   - `XceY`: Combines Critical and Exceptional Skill rules.
   - *Example*: `2ce6` (Roll two 6-sided dice; 6 becomes 12, 1 becomes -6, results between 2 and threshold become threshold).

5. **Force Point (`f`)**
   - `XfY`: Same as standard dice roll.
   - *Example*: `2f8` (Roll two 8-sided dice).

6. **Reliable Boon (`r`)**
   - `XrY`: Rolls `X` dice. Reroll any 1s.
   - *Example*: `3r6` (Roll three 6-sided dice; reroll any 1s).

## Combining Notations and Operations
- **Addition (`+`)**: Adds results.
  - *Example*: `d20 + 4d6` (Roll one 20-sided die and four 6-sided dice, sum all results).

- **Subtraction (`-`)**: Subtracts results or integers.
  - *Example*: `2d10 - d6` (Roll two 10-sided dice, then subtract a 6-sided die result).

- **Multiplication (`*`)**: Multiplies results.
  - *Example*: `d20 * 2d6` (Roll one 20-sided die, then multiply by a two 6-sided die result).

- **Division (`/`)**: Divides results.
  - *Example*: `4d10 / 2d6` (Roll four 10-sided dice, then divide by a two 6-sided die result, then round down).

- **Modifiers**: Add or subtract integers directly.
  - *Example*: `3d8 + 5` (Roll three 8-sided dice and add 5).

- **Multipliers**: Multiply or divide integers directly.
  - *Example*: `3d8 * 2` (Roll three 8-sided dice and multiply by two).
  - *Example*: `3d8 / 2` (Roll three 8-sided dice and divide by two, then round down).

## Rolling a Dice Notation Multiple Times
- **Repetition**: Roll the same dice notation multiple times
  - *Example*: `2^d20+5` (Roll d20+5 twice).
  - *Example*: `5^3d8*2+5` (Roll 3d8*2+5 five times).

## Examples
1. `2d10 + 5`: Roll two 10-sided dice, add 5.
2. `d20 - 3`: Roll one 20-sided die, subtract 3.
3. `3c6 + 2e8 - 4`: Roll three 6-sided dice (Critical), two 8-sided dice (Exceptional Skill), subtract 4.
4. `4ce12`: Roll four 12-sided dice (Critical and Exceptional Skill).
5. `5r4 + 2`: Roll five 4-sided dice (Reliable Boon, reroll 1s), add 2.


# Character Converter Guide

Open the terminal and type `python3 character_converter.py [character name]`

The character name should be the same as the name on the txt file.

the json file will have the same name.
