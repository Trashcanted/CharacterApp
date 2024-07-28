import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class CharacterSheetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stellar Fantasies Character Sheet")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.create_tabs()
        self.create_buttons()

    def create_tabs(self):
        self.character_info_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.character_info_tab, text="Character Info")
        self.create_info_fields(self.character_info_tab)
        self.create_language_fields(self.character_info_tab)

        self.stats_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.stats_tab, text="Stats")
        self.create_stat_fields(self.stats_tab)

        self.defenses_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.defenses_tab, text="Defenses")
        self.create_defense_fields(self.defenses_tab)

        self.damage_thresholds_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.damage_thresholds_tab, text="Damage Thresholds")
        self.create_damage_threshold_fields(self.damage_thresholds_tab)

        self.armor_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.armor_tab, text="Armor")
        self.create_armor_fields(self.armor_tab)

        self.weapons_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.weapons_tab, text="Weapons")
        self.create_weapon_fields(self.weapons_tab)

        self.skills_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.skills_tab, text="Skills")
        self.create_skill_fields(self.skills_tab)

        self.force_schools_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.force_schools_tab, text="Force Schools")
        self.create_force_school_fields(self.force_schools_tab)

        self.force_tech_secrets_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.force_tech_secrets_tab, text="Force Techs/Secrets")
        self.create_force_tech_secret_fields(self.force_tech_secrets_tab)

        self.feats_talents_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.feats_talents_tab, text="Feats/Talents")
        self.create_feats_talents_fields(self.feats_talents_tab)

        self.equipment_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.equipment_tab, text="Equipment")
        self.create_equipment_fields(self.equipment_tab)

    def create_info_fields(self, parent):
        labels = [
            "Character Name",
            "Character Level",
            "Classes",
            "Destiny",
            "Credits",
            "Species",
            "Age",
            "Height",
            "Weight",
            "Gender",
            "Species Info",
            "Force Points",
            "Base Attack Bonus",
            "Speed",
            "Destiny Points",
            "Damage Reduction",
        ]
        self.info_entries = []
        for i, label in enumerate(labels):
            lbl = tk.Label(parent, text=label)
            lbl.grid(row=i // 2, column=(i % 2) * 2, padx=5, pady=5, sticky="w")
            entry = tk.Entry(parent, width=25)
            entry.grid(row=i // 2, column=(i % 2) * 2 + 1, padx=5, pady=5)
            self.info_entries.append(entry)

    def create_language_fields(self, parent):
        self.language_entries = []
        lbl = tk.Label(parent, text="Languages:")
        lbl.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        for i in range(10):
            entry = tk.Entry(parent, width=25)
            entry.grid(row=i + 9, column=1, padx=5, pady=5)
            self.language_entries.append(entry)

    def create_stat_fields(self, parent):
        labels = [
            "Strength",
            "Dexterity",
            "Constitution",
            "Intelligence",
            "Wisdom",
            "Charisma",
            "Willpower",
        ]
        self.stat_entries = []
        for i, label in enumerate(labels):
            lbl = tk.Label(parent, text=label)
            lbl.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            score_entry = tk.Entry(parent, width=10)
            score_entry.grid(row=i, column=1, padx=5, pady=5)
            mod_entry = tk.Entry(parent, width=10)
            mod_entry.grid(row=i, column=2, padx=5, pady=5)
            self.stat_entries.extend([score_entry, mod_entry])

    def create_defense_fields(self, parent):
        labels = ["Fortitude", "Reflex", "Will"]
        self.defense_entries = []
        for i, label in enumerate(labels):
            lbl = tk.Label(parent, text=label)
            lbl.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            for j in range(5):
                entry = tk.Entry(parent, width=10)
                entry.grid(row=i, column=j + 1, padx=5, pady=5)
                self.defense_entries.append(entry)

    def create_damage_threshold_fields(self, parent):
        labels = [
            "Torso",
            "Fortitude",
            "Misc",
            "Head",
            "Head Bonus",
            "Limbs",
            "Limb Bonus",
        ]
        self.damage_threshold_entries = []
        for i, label in enumerate(labels):
            lbl = tk.Label(parent, text=label)
            lbl.grid(row=0, column=i, padx=5, pady=5, sticky="w")
            entry = tk.Entry(parent, width=10)
            entry.grid(row=1, column=i, padx=5, pady=5)
            self.damage_threshold_entries.append(entry)

    def create_armor_fields(self, parent):
        labels = [
            "Armor",
            "Fortitude Bonus",
            "Reflex Bonus",
            "Max Dex Bonus",
            "Additional Affects",
        ]
        self.armor_entries = []
        for i, label in enumerate(labels):
            lbl = tk.Label(parent, text=label)
            lbl.grid(
                row=i,
                column=0,
                padx=5,
                pady=5,
                sticky="w",
            )
            entry = tk.Entry(parent, width=50)
            entry.grid(row=i, column=1)
            self.armor_entries.append(entry)

    def create_weapon_fields(self, parent):
        labels = ["Weapon", "Hit Mod", "Damage", "Range", "CritRange"]
        self.weapon_entries = []
        for i in range(5):
            for j, label in enumerate(labels):
                lbl = tk.Label(parent, text=label)
                lbl.grid(row=i * 2, column=j, padx=5, pady=5, sticky="w")
                entry = tk.Entry(parent, width=25)
                entry.grid(row=i * 2 + 1, column=j, padx=5, pady=5)
                self.weapon_entries.append(entry)

    def create_skill_fields(self, parent):
        skill_data = [
            ("Acrobatics", "Dex", 0),
            ("Climb", "Str", 0),
            ("Deception", "Cha", 0),
            ("Endurance", "Con", 0),
            ("Gather Information", "Cha", 0),
            ("Initiative", "Dex", 0),
            ("Jump", "Str", 0),
            ("Knowledge (Bureaucracy)", "Int", 0),
            ("Knowledge (Galactic Lore)", "Int", 0),
            ("Knowledge (Life Science)", "Int", 0),
            ("Knowledge (Physical Science)", "Int", 0),
            ("Knowledge (Social Science)", "Int", 0),
            ("Knowledge (Tactics)", "Int", 0),
            ("Knowledge (Technology)", "Int", 0),
            ("Mechanics", "Int", 0),
            ("Perception", "Wis", 0),
            ("Persuasion", "Cha", 0),
            ("Pilot", "Dex", 0),
            ("Ride", "Dex", 0),
            ("Stealth", "Dex", 0),
            ("Survival", "Wis", 0),
            ("Swim", "Str", 0),
            ("Treat Injury", "Int", 0),
            ("Use Computer", "Int", 0),
            ("Use the Force", "Cha/Wil", 0),
        ]

        labels = ["Skill", "Stat", "Trained", "Focus", "Modifier"]
        self.skill_entries = []

        half = len(skill_data) // 2
        skill_columns = [skill_data[:half], skill_data[half:]]

        for col, skills in enumerate(skill_columns):
            for j, label in enumerate(labels):
                lbl = tk.Label(parent, text=label)
                lbl.grid(row=0, column=j + col * 6, padx=5, pady=5, sticky="w")

            for i, (skill, stat, trained) in enumerate(skills):
                skill_entry = tk.Entry(parent, width=25)
                skill_entry.grid(row=i + 1, column=0 + col * 6, padx=5, pady=5)
                skill_entry.insert(0, skill)
                skill_entry.config(state="readonly")
                self.skill_entries.append(skill_entry)

                stat_entry = tk.Entry(parent, width=5)
                stat_entry.grid(row=i + 1, column=1 + col * 6, padx=5, pady=5)
                stat_entry.insert(0, stat)
                stat_entry.config(state="readonly")
                self.skill_entries.append(stat_entry)

                trained_var = tk.IntVar(value=trained)
                trained_check = tk.Checkbutton(parent, variable=trained_var)
                trained_check.grid(row=i + 1, column=2 + col * 6, padx=5, pady=5)
                self.skill_entries.append(trained_var)

                focus_var = tk.IntVar()
                focus_check = tk.Checkbutton(parent, variable=focus_var)
                focus_check.grid(row=i + 1, column=3 + col * 6, padx=5, pady=5)
                self.skill_entries.append(focus_var)

                modifier_entry = tk.Entry(parent, width=5)
                modifier_entry.grid(row=i + 1, column=4 + col * 6, padx=5, pady=5)
                self.skill_entries.append(modifier_entry)

    def create_force_school_fields(self, parent):
        metalabels = [
            "Schools",
            "Training",
            "",
            "",
            "Modifier",
        ]
        labels = [
            "Alchemy",
            "Augmentation",
            "Cognition",
            "Sorcery",
            "Technokinesis",
            "Telekinesis",
            "Vitalism",
            "Force Uses",
        ]
        self.force_school_entries = []

        for i, label in enumerate(metalabels):
            lbl = tk.Label(parent, text=label)
            lbl.grid(row=0, column=i, padx=5, pady=5, sticky="w")
        for i, label in enumerate(labels):
            lbl = tk.Label(parent, text=label)
            lbl.grid(row=i + 1, column=0, padx=5, pady=5, sticky="w")
            if i != 7:
                entry = tk.Entry(parent, width=1)
                entry.grid(row=i + 1, column=1, padx=5, pady=5)
                self.force_school_entries.append(entry)
                entry = tk.Entry(parent, width=1)
                entry.grid(row=i + 1, column=2, padx=5, pady=5)
                self.force_school_entries.append(entry)
                entry = tk.Entry(parent, width=1)
                entry.grid(row=i + 1, column=3, padx=5, pady=5)
                self.force_school_entries.append(entry)
                entry = tk.Entry(parent, width=10)
                entry.grid(row=i + 1, column=4, padx=5, pady=5)
                self.force_school_entries.append(entry)
            else:
                entry = tk.Entry(parent, width=10)
                entry.grid(row=i + 1, column=1, padx=5, pady=5)
                self.force_school_entries.append(entry)

    def create_force_tech_secret_fields(self, parent):
        labels = [
            "Force Techniques",
            "Force Secrets",
        ]

        self.force_tech_entries = []
        self.force_secret_entries = []

        for i, label in enumerate(labels):
            lbl = tk.Label(parent, text=label)
            lbl.grid(row=0, column=i, padx=5, pady=5, sticky="w")
            for j in range(15):
                entry = tk.Entry(parent, width=25)
                entry.grid(row=j + 1, column=i, padx=5, pady=5)
                if i == 0:
                    self.force_tech_entries.append(entry)
                else:
                    self.force_secret_entries.append(entry)

    def create_feats_talents_fields(self, parent):
        self.feats_talents_entries = []

        lbl = tk.Label(parent, text="Feats:")
        lbl.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        lbl = tk.Label(parent, text="Talents:")
        lbl.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        for i in range(15):
            for j in range(2):
                entry = tk.Entry(parent, width=25)
                entry.grid(row=i + 1, column=j, padx=5, pady=5)
                self.feats_talents_entries.append(entry)

    def create_equipment_fields(self, parent):
        self.equipment_entries = []

        lbl = tk.Label(parent, text="Equipment:")
        lbl.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        for i in range(8):
            for j in range(4):
                entry = tk.Entry(parent, width=25)
                entry.grid(row=i + 1, column=j, padx=5, pady=5)
                self.equipment_entries.append(entry)

    def create_buttons(self):
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(fill="both", expand="yes", padx=10, pady=5)

        import_button = tk.Button(
            self.buttons_frame, text="Import from Txt", command=self.import_from_txt
        )
        import_button.pack(side="left", padx=5, pady=5)
        export_button = tk.Button(
            self.buttons_frame, text="Export to Txt", command=self.export_to_txt
        )
        export_button.pack(side="left", padx=5, pady=5)

    def import_from_txt(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                lines = file.readlines()
                entries = (
                    self.info_entries
                    + self.language_entries
                    + self.stat_entries
                    + self.defense_entries
                    + self.damage_threshold_entries
                    + self.armor_entries
                    + self.weapon_entries
                    + self.skill_entries
                    + self.force_school_entries
                    + self.force_tech_entries
                    + self.force_secret_entries
                    + self.feats_talents_entries
                    + self.equipment_entries
                )
                for entry, line in zip(entries, lines):
                    if isinstance(entry, tk.Entry):
                        entry.delete(0, tk.END)
                        entry.insert(0, line.strip())
                    elif isinstance(entry, tk.IntVar):
                        entry.set(int(line.strip()))

    def export_to_txt(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )
        if file_path:
            entries = (
                self.info_entries
                + self.language_entries
                + self.stat_entries
                + self.defense_entries
                + self.damage_threshold_entries
                + self.armor_entries
                + self.weapon_entries
                + self.skill_entries
                + self.force_school_entries
                + self.force_tech_entries
                + self.force_secret_entries
                + self.feats_talents_entries
                + self.equipment_entries
            )
            data = []
            for entry in entries:
                if isinstance(entry, tk.Entry):
                    data.append(entry.get())
                elif isinstance(entry, tk.IntVar):
                    data.append(str(entry.get()))
            with open(file_path, "w") as file:
                file.write("\n".join(data))
            messagebox.showinfo("Export Successful", f"Data exported to {file_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterSheetApp(root)
    root.mainloop()
