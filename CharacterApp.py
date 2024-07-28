import os
import subprocess
import tkinter as tk
from multiprocessing import Process

from Roll import DiceRollerApp


# Function to run the .exe file
def run_exe():
    # Relative path to the .exe file
    exe_path = os.path.join(
        os.path.dirname(__file__),
        "CharacterApp",
        "CharacterSheet",
        "CharacterSheet.exe",
    )
    # Check if the file exists
    if os.path.isfile(exe_path):
        try:
            # Open the .exe file
            subprocess.run(exe_path, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while trying to open {exe_path}: {e}")
    else:
        print(f"The file {exe_path} does not exist.")


# Function to run the Tkinter application
def run_tkinter():
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()


if __name__ == "__main__":
    # Create two separate processes
    p1 = Process(target=run_exe)
    p2 = Process(target=run_tkinter)

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()
