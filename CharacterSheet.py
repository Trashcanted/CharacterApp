import json
import tkinter as tk
from math import floor
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
        self.notebook.add(
            self.force_tech_secrets_tab, text="Force Techs/Secrets"
        )
        self.create_force_tech_secret_fields(self.force_tech_secrets_tab)

        self.feats_talents_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.feats_talents_tab, text="Feats/Talents")
        self.create_feats_talents_fields(self.feats_talents_tab)

        self.equipment_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.equipment_tab, text="Equipment")
        self.create_equipment_fields(self.equipment_tab)

    def create_info_fields(self, parent):
        # Labels and Entries without loop
        # Row 0
        self.lbl_name = tk.Label(parent, text="Character Name")
        self.lbl_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name = tk.Entry(parent, width=25)
        self.name.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_level = tk.Label(parent, text="Character Level")
        self.lbl_level.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.level = tk.Entry(parent, width=25)
        self.level.grid(row=0, column=3, padx=5, pady=5)

        # Row 1
        self.lbl_classes = tk.Label(parent, text="Classes")
        self.lbl_classes.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.classes = tk.Entry(parent, width=25)
        self.classes.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_destiny = tk.Label(parent, text="Destiny")
        self.lbl_destiny.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.destiny = tk.Entry(parent, width=25)
        self.destiny.grid(row=1, column=3, padx=5, pady=5)

        # Row 2
        self.lbl_credits = tk.Label(parent, text="Credits")
        self.lbl_credits.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.credits = tk.Entry(parent, width=25)
        self.credits.grid(row=2, column=1, padx=5, pady=5)

        self.lbl_species = tk.Label(parent, text="Species")
        self.lbl_species.grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.species = tk.Entry(parent, width=25)
        self.species.grid(row=2, column=3, padx=5, pady=5)

        # Row 3
        self.lbl_age = tk.Label(parent, text="Age")
        self.lbl_age.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.age = tk.Entry(parent, width=25)
        self.age.grid(row=3, column=1, padx=5, pady=5)

        self.lbl_height = tk.Label(parent, text="Height")
        self.lbl_height.grid(row=3, column=2, padx=5, pady=5, sticky="w")
        self.height = tk.Entry(parent, width=25)
        self.height.grid(row=3, column=3, padx=5, pady=5)

        # Row 4
        self.lbl_weight = tk.Label(parent, text="Weight")
        self.lbl_weight.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.weight = tk.Entry(parent, width=25)
        self.weight.grid(row=4, column=1, padx=5, pady=5)

        self.lbl_gender = tk.Label(parent, text="Gender")
        self.lbl_gender.grid(row=4, column=2, padx=5, pady=5, sticky="w")
        self.gender = tk.Entry(parent, width=25)
        self.gender.grid(row=4, column=3, padx=5, pady=5)

        # Row 5
        self.lbl_species_info = tk.Label(parent, text="Species Info")
        self.lbl_species_info.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.species_info = tk.Entry(parent, width=25)
        self.species_info.grid(row=5, column=1, padx=5, pady=5)

        self.lbl_force_points = tk.Label(parent, text="Force Points")
        self.lbl_force_points.grid(row=5, column=2, padx=5, pady=5, sticky="w")
        self.force_points = tk.Entry(parent, width=25)
        self.force_points.grid(row=5, column=3, padx=5, pady=5)

        # Row 6
        self.lbl_base_attack = tk.Label(parent, text="Base Attack Bonus")
        self.lbl_base_attack.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.base_attack = tk.Entry(parent, width=25)
        self.base_attack.grid(row=6, column=1, padx=5, pady=5)

        self.lbl_speed = tk.Label(parent, text="Speed")
        self.lbl_speed.grid(row=6, column=2, padx=5, pady=5, sticky="w")
        self.speed = tk.Entry(parent, width=25)
        self.speed.grid(row=6, column=3, padx=5, pady=5)

        # Row 7
        self.lbl_dest_point = tk.Label(parent, text="Destiny Points")
        self.lbl_dest_point.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.dest_point = tk.Entry(parent, width=25)
        self.dest_point.grid(row=7, column=1, padx=5, pady=5)

        self.lbl_dam_red = tk.Label(parent, text="Damage Reduction")
        self.lbl_dam_red.grid(row=7, column=2, padx=5, pady=5, sticky="w")
        self.dam_red = tk.Entry(parent, width=25)
        self.dam_red.grid(row=7, column=3, padx=5, pady=5)

        # Store the entries in a list if needed
        self.info_entries = [
            self.name,
            self.level,
            self.classes,
            self.destiny,
            self.credits,
            self.species,
            self.age,
            self.height,
            self.weight,
            self.gender,
            self.species_info,
            self.force_points,
            self.base_attack,
            self.speed,
            self.dest_point,
            self.dam_red,
        ]

    def create_language_fields(self, parent):
        # Label for "Languages"
        self.lbl_languages = tk.Label(parent, text="Languages:")
        self.lbl_languages.grid(row=8, column=0, padx=5, pady=5, sticky="w")

        # Manually adding 10 language Entry fields
        self.language_1 = tk.Entry(parent, width=25)
        self.language_1.grid(row=8, column=1, padx=5, pady=5)

        self.language_2 = tk.Entry(parent, width=25)
        self.language_2.grid(row=9, column=1, padx=5, pady=5)

        self.language_3 = tk.Entry(parent, width=25)
        self.language_3.grid(row=10, column=1, padx=5, pady=5)

        self.language_4 = tk.Entry(parent, width=25)
        self.language_4.grid(row=11, column=1, padx=5, pady=5)

        self.language_5 = tk.Entry(parent, width=25)
        self.language_5.grid(row=12, column=1, padx=5, pady=5)

        self.language_6 = tk.Entry(parent, width=25)
        self.language_6.grid(row=8, column=2, padx=5, pady=5)

        self.language_7 = tk.Entry(parent, width=25)
        self.language_7.grid(row=9, column=2, padx=5, pady=5)

        self.language_8 = tk.Entry(parent, width=25)
        self.language_8.grid(row=10, column=2, padx=5, pady=5)

        self.language_9 = tk.Entry(parent, width=25)
        self.language_9.grid(row=11, column=2, padx=5, pady=5)

        self.language_10 = tk.Entry(parent, width=25)
        self.language_10.grid(row=12, column=2, padx=5, pady=5)

        # Store the entries in a list if needed
        self.language_entries = [
            self.language_1,
            self.language_2,
            self.language_3,
            self.language_4,
            self.language_5,
            self.language_6,
            self.language_7,
            self.language_8,
            self.language_9,
            self.language_10,
        ]

    def create_stat_fields(self, parent):
        # Labels and Entries for stats without loop
        self.lbl_score = tk.Label(parent, text="Score")
        self.lbl_score.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.lbl_mod = tk.Label(parent, text="Mod")
        self.lbl_mod.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        # Strength
        self.lbl_str = tk.Label(parent, text="Strength")
        self.lbl_str.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.str_score = tk.Entry(parent, width=10)
        self.str_score.grid(row=1, column=1, padx=5, pady=5)
        self.str_mod = tk.Entry(parent, width=10)
        self.str_mod.grid(row=1, column=2, padx=5, pady=5)

        # Dexterity
        self.lbl_dex = tk.Label(parent, text="Dexterity")
        self.lbl_dex.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.dex_score = tk.Entry(parent, width=10)
        self.dex_score.grid(row=2, column=1, padx=5, pady=5)
        self.dex_mod = tk.Entry(parent, width=10)
        self.dex_mod.grid(row=2, column=2, padx=5, pady=5)

        # Constitution
        self.lbl_con = tk.Label(parent, text="Constitution")
        self.lbl_con.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.con_score = tk.Entry(parent, width=10)
        self.con_score.grid(row=3, column=1, padx=5, pady=5)
        self.con_mod = tk.Entry(parent, width=10)
        self.con_mod.grid(row=3, column=2, padx=5, pady=5)

        # Intelligence
        self.lbl_int = tk.Label(parent, text="Intelligence")
        self.lbl_int.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.int_score = tk.Entry(parent, width=10)
        self.int_score.grid(row=4, column=1, padx=5, pady=5)
        self.int_mod = tk.Entry(parent, width=10)
        self.int_mod.grid(row=4, column=2, padx=5, pady=5)

        # Wisdom
        self.lbl_wis = tk.Label(parent, text="Wisdom")
        self.lbl_wis.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.wis_score = tk.Entry(parent, width=10)
        self.wis_score.grid(row=5, column=1, padx=5, pady=5)
        self.wis_mod = tk.Entry(parent, width=10)
        self.wis_mod.grid(row=5, column=2, padx=5, pady=5)

        # Charisma
        self.lbl_cha = tk.Label(parent, text="Charisma")
        self.lbl_cha.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.cha_score = tk.Entry(parent, width=10)
        self.cha_score.grid(row=6, column=1, padx=5, pady=5)
        self.cha_mod = tk.Entry(parent, width=10)
        self.cha_mod.grid(row=6, column=2, padx=5, pady=5)

        # Willpower
        self.lbl_will = tk.Label(parent, text="Willpower")
        self.lbl_will.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.will_score = tk.Entry(parent, width=10)
        self.will_score.grid(row=7, column=1, padx=5, pady=5)
        self.will_mod = tk.Entry(parent, width=10)
        self.will_mod.grid(row=7, column=2, padx=5, pady=5)

        # Dark Side
        self.lbl_dark = tk.Label(parent, text="Dark Side")
        self.lbl_dark.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.dark_score = tk.Entry(parent, width=10)
        self.dark_score.grid(row=8, column=1, padx=5, pady=5)
        self.dark_mod = tk.Entry(parent, width=10)
        self.dark_mod.grid(row=8, column=2, padx=5, pady=5)

        # Store the entries in a list if needed
        self.stat_entries = [
            self.str_score,
            self.str_mod,
            self.dex_score,
            self.dex_mod,
            self.con_score,
            self.con_mod,
            self.int_score,
            self.int_mod,
            self.wis_score,
            self.wis_mod,
            self.cha_score,
            self.cha_mod,
            self.will_score,
            self.will_mod,
        ]

    def create_defense_fields(self, parent):
        # Labels and Entries for defenses without loop
        # Fortitude
        self.lbl_total = tk.Label(parent, text="Total")
        self.lbl_total.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.lbl_class_bonus = tk.Label(parent, text="Class Bonus")
        self.lbl_class_bonus.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.lbl_stat_bonus = tk.Label(parent, text="Stat Bonus")
        self.lbl_stat_bonus.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        self.lbl_armor_bonus = tk.Label(parent, text="Armor Bonus")
        self.lbl_armor_bonus.grid(row=0, column=4, padx=5, pady=5, sticky="w")

        self.lbl_misc_bonus = tk.Label(parent, text="Misc")
        self.lbl_misc_bonus.grid(row=0, column=5, padx=5, pady=5, sticky="w")

        self.lbl_fortitude = tk.Label(parent, text="Fortitude")
        self.lbl_fortitude.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.fortitude_1 = tk.Entry(parent, width=10)
        self.fortitude_1.grid(row=1, column=1, padx=5, pady=5)

        self.fortitude_2 = tk.Entry(parent, width=10)
        self.fortitude_2.grid(row=1, column=2, padx=5, pady=5)

        self.fortitude_3 = tk.Entry(parent, width=10)
        self.fortitude_3.grid(row=1, column=3, padx=5, pady=5)

        self.fortitude_4 = tk.Entry(parent, width=10)
        self.fortitude_4.grid(row=1, column=4, padx=5, pady=5)

        self.fortitude_5 = tk.Entry(parent, width=10)
        self.fortitude_5.grid(row=1, column=5, padx=5, pady=5)

        # Reflex
        self.lbl_reflex = tk.Label(parent, text="Reflex")
        self.lbl_reflex.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.reflex_1 = tk.Entry(parent, width=10)
        self.reflex_1.grid(row=2, column=1, padx=5, pady=5)

        self.reflex_2 = tk.Entry(parent, width=10)
        self.reflex_2.grid(row=2, column=2, padx=5, pady=5)

        self.reflex_3 = tk.Entry(parent, width=10)
        self.reflex_3.grid(row=2, column=3, padx=5, pady=5)

        self.reflex_4 = tk.Entry(parent, width=10)
        self.reflex_4.grid(row=2, column=4, padx=5, pady=5)

        self.reflex_5 = tk.Entry(parent, width=10)
        self.reflex_5.grid(row=2, column=5, padx=5, pady=5)

        # Will
        self.lbl_will = tk.Label(parent, text="Will")
        self.lbl_will.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.will_1 = tk.Entry(parent, width=10)
        self.will_1.grid(row=3, column=1, padx=5, pady=5)

        self.will_2 = tk.Entry(parent, width=10)
        self.will_2.grid(row=3, column=2, padx=5, pady=5)

        self.will_3 = tk.Entry(parent, width=10)
        self.will_3.grid(row=3, column=3, padx=5, pady=5)

        self.will_4 = tk.Entry(parent, width=10)
        self.will_4.grid(row=3, column=4, padx=5, pady=5)

        self.will_5 = tk.Entry(parent, width=10)
        self.will_5.grid(row=3, column=5, padx=5, pady=5)

        # Store the entries in a list if needed
        self.defense_entries = [
            self.fortitude_1,
            self.fortitude_2,
            self.fortitude_3,
            self.fortitude_4,
            self.fortitude_5,
            self.reflex_1,
            self.reflex_2,
            self.reflex_3,
            self.reflex_4,
            self.reflex_5,
            self.will_1,
            self.will_2,
            self.will_3,
            self.will_4,
            self.will_5,
        ]

    def create_damage_threshold_fields(self, parent):
        # Labels and Entries for Damage Threshold without loop

        # Fortitude
        self.lbl_fortitude = tk.Label(parent, text="Fortitude")
        self.lbl_fortitude.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.fortitude = tk.Entry(parent, width=5)
        self.fortitude.grid(row=0, column=1, padx=5, pady=5)

        # Labels
        self.lbl_total_def = tk.Label(parent, text="Total")
        self.lbl_total_def.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.lbl_misc_def = tk.Label(parent, text="Misc")
        self.lbl_misc_def.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        # Torso
        self.lbl_torso = tk.Label(parent, text="Torso")
        self.lbl_torso.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.torso = tk.Entry(parent, width=5)
        self.torso.grid(row=2, column=1, padx=5, pady=5)
        self.torso_misc = tk.Entry(parent, width=5)
        self.torso_misc.grid(row=2, column=2, padx=5, pady=5)

        # Head
        self.lbl_head = tk.Label(parent, text="Head")
        self.lbl_head.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.head = tk.Entry(parent, width=5)
        self.head.grid(row=3, column=1, padx=5, pady=5)
        self.head_misc = tk.Entry(parent, width=5)
        self.head_misc.grid(row=3, column=2, padx=5, pady=5)

        # Limbs
        self.lbl_limbs = tk.Label(parent, text="Limbs")
        self.lbl_limbs.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.limbs = tk.Entry(parent, width=5)
        self.limbs.grid(row=4, column=1, padx=5, pady=5)
        self.limbs_misc = tk.Entry(parent, width=5)
        self.limbs_misc.grid(row=4, column=2, padx=5, pady=5)

        # Store the entries in a list if needed
        self.damage_threshold_entries = [
            self.fortitude,
            self.torso,
            self.torso_misc,
            self.head,
            self.head_misc,
            self.limbs,
            self.limbs_misc,
        ]

    def create_armor_fields(self, parent):
        # Labels and Entries for Armor without loop
        # Armor
        self.lbl_armor = tk.Label(parent, text="Armor")
        self.lbl_armor.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.armor = tk.Entry(parent, width=50)
        self.armor.grid(row=0, column=1)

        # Fortitude Bonus
        self.lbl_fort_bonus = tk.Label(parent, text="Fortitude Bonus")
        self.lbl_fort_bonus.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.fort_bonus = tk.Entry(parent, width=3)
        self.fort_bonus.grid(row=1, column=1)

        # Reflex Bonus
        self.lbl_reflex_bonus = tk.Label(parent, text="Reflex Bonus")
        self.lbl_reflex_bonus.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.reflex_bonus = tk.Entry(parent, width=3)
        self.reflex_bonus.grid(row=2, column=1)

        # Max Dex Bonus
        self.lbl_max_dex_bonus = tk.Label(parent, text="Max Dex Bonus")
        self.lbl_max_dex_bonus.grid(
            row=3, column=0, padx=5, pady=5, sticky="w"
        )
        self.max_dex_bonus = tk.Entry(parent, width=3)
        self.max_dex_bonus.grid(row=3, column=1)

        # Additional Affects
        self.lbl_affects = tk.Label(parent, text="Additional Affects")
        self.lbl_affects.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.affects = tk.Entry(parent, width=50)
        self.affects.grid(row=4, column=1)

        # Store the entries in a list if needed
        self.armor_entries = [
            self.armor,
            self.fort_bonus,
            self.reflex_bonus,
            self.max_dex_bonus,
            self.affects,
        ]

    def create_weapon_fields(self, parent):
        # Labels and Entries for Weapons without loop
        # First weapon
        self.lbl_weapon_1 = tk.Label(parent, text="Weapon")
        self.lbl_weapon_1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.weapon_1 = tk.Entry(parent, width=25)
        self.weapon_1.grid(row=1, column=0, padx=5, pady=5)

        self.lbl_hit_mod_1 = tk.Label(parent, text="Hit Mod")
        self.lbl_hit_mod_1.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.hit_mod_1 = tk.Entry(parent, width=25)
        self.hit_mod_1.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_damage_1 = tk.Label(parent, text="Damage")
        self.lbl_damage_1.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.damage_1 = tk.Entry(parent, width=25)
        self.damage_1.grid(row=1, column=2, padx=5, pady=5)

        self.lbl_range_1 = tk.Label(parent, text="Range")
        self.lbl_range_1.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.range_1 = tk.Entry(parent, width=25)
        self.range_1.grid(row=1, column=3, padx=5, pady=5)

        self.lbl_crit_range_1 = tk.Label(parent, text="CritRange")
        self.lbl_crit_range_1.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.crit_range_1 = tk.Entry(parent, width=25)
        self.crit_range_1.grid(row=1, column=4, padx=5, pady=5)

        # Second weapon
        self.lbl_weapon_2 = tk.Label(parent, text="Weapon")
        self.lbl_weapon_2.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.weapon_2 = tk.Entry(parent, width=25)
        self.weapon_2.grid(row=3, column=0, padx=5, pady=5)

        self.lbl_hit_mod_2 = tk.Label(parent, text="Hit Mod")
        self.lbl_hit_mod_2.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.hit_mod_2 = tk.Entry(parent, width=25)
        self.hit_mod_2.grid(row=3, column=1, padx=5, pady=5)

        self.lbl_damage_2 = tk.Label(parent, text="Damage")
        self.lbl_damage_2.grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.damage_2 = tk.Entry(parent, width=25)
        self.damage_2.grid(row=3, column=2, padx=5, pady=5)

        self.lbl_range_2 = tk.Label(parent, text="Range")
        self.lbl_range_2.grid(row=2, column=3, padx=5, pady=5, sticky="w")
        self.range_2 = tk.Entry(parent, width=25)
        self.range_2.grid(row=3, column=3, padx=5, pady=5)

        self.lbl_crit_range_2 = tk.Label(parent, text="CritRange")
        self.lbl_crit_range_2.grid(row=2, column=4, padx=5, pady=5, sticky="w")
        self.crit_range_2 = tk.Entry(parent, width=25)
        self.crit_range_2.grid(row=3, column=4, padx=5, pady=5)

        # Third weapon
        self.lbl_weapon_3 = tk.Label(parent, text="Weapon")
        self.lbl_weapon_3.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.weapon_3 = tk.Entry(parent, width=25)
        self.weapon_3.grid(row=5, column=0, padx=5, pady=5)

        self.lbl_hit_mod_3 = tk.Label(parent, text="Hit Mod")
        self.lbl_hit_mod_3.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.hit_mod_3 = tk.Entry(parent, width=25)
        self.hit_mod_3.grid(row=5, column=1, padx=5, pady=5)

        self.lbl_damage_3 = tk.Label(parent, text="Damage")
        self.lbl_damage_3.grid(row=4, column=2, padx=5, pady=5, sticky="w")
        self.damage_3 = tk.Entry(parent, width=25)
        self.damage_3.grid(row=5, column=2, padx=5, pady=5)

        self.lbl_range_3 = tk.Label(parent, text="Range")
        self.lbl_range_3.grid(row=4, column=3, padx=5, pady=5, sticky="w")
        self.range_3 = tk.Entry(parent, width=25)
        self.range_3.grid(row=5, column=3, padx=5, pady=5)

        self.lbl_crit_range_3 = tk.Label(parent, text="CritRange")
        self.lbl_crit_range_3.grid(row=4, column=4, padx=5, pady=5, sticky="w")
        self.crit_range_3 = tk.Entry(parent, width=25)
        self.crit_range_3.grid(row=5, column=4, padx=5, pady=5)

        # Fourth weapon
        self.lbl_weapon_4 = tk.Label(parent, text="Weapon")
        self.lbl_weapon_4.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.weapon_4 = tk.Entry(parent, width=25)
        self.weapon_4.grid(row=7, column=0, padx=5, pady=5)

        self.lbl_hit_mod_4 = tk.Label(parent, text="Hit Mod")
        self.lbl_hit_mod_4.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        self.hit_mod_4 = tk.Entry(parent, width=25)
        self.hit_mod_4.grid(row=7, column=1, padx=5, pady=5)

        self.lbl_damage_4 = tk.Label(parent, text="Damage")
        self.lbl_damage_4.grid(row=6, column=2, padx=5, pady=5, sticky="w")
        self.damage_4 = tk.Entry(parent, width=25)
        self.damage_4.grid(row=7, column=2, padx=5, pady=5)

        self.lbl_range_4 = tk.Label(parent, text="Range")
        self.lbl_range_4.grid(row=6, column=3, padx=5, pady=5, sticky="w")
        self.range_4 = tk.Entry(parent, width=25)
        self.range_4.grid(row=7, column=3, padx=5, pady=5)

        self.lbl_crit_range_4 = tk.Label(parent, text="CritRange")
        self.lbl_crit_range_4.grid(row=6, column=4, padx=5, pady=5, sticky="w")
        self.crit_range_4 = tk.Entry(parent, width=25)
        self.crit_range_4.grid(row=7, column=4, padx=5, pady=5)

        # Fifth weapon
        self.lbl_weapon_5 = tk.Label(parent, text="Weapon")
        self.lbl_weapon_5.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.weapon_5 = tk.Entry(parent, width=25)
        self.weapon_5.grid(row=9, column=0, padx=5, pady=5)

        self.lbl_hit_mod_5 = tk.Label(parent, text="Hit Mod")
        self.lbl_hit_mod_5.grid(row=8, column=1, padx=5, pady=5, sticky="w")
        self.hit_mod_5 = tk.Entry(parent, width=25)
        self.hit_mod_5.grid(row=9, column=1, padx=5, pady=5)

        self.lbl_damage_5 = tk.Label(parent, text="Damage")
        self.lbl_damage_5.grid(row=8, column=2, padx=5, pady=5, sticky="w")
        self.damage_5 = tk.Entry(parent, width=25)
        self.damage_5.grid(row=9, column=2, padx=5, pady=5)

        self.lbl_range_5 = tk.Label(parent, text="Range")
        self.lbl_range_5.grid(row=8, column=3, padx=5, pady=5, sticky="w")
        self.range_5 = tk.Entry(parent, width=25)
        self.range_5.grid(row=9, column=3, padx=5, pady=5)

        self.lbl_crit_range_5 = tk.Label(parent, text="CritRange")
        self.lbl_crit_range_5.grid(row=8, column=4, padx=5, pady=5, sticky="w")
        self.crit_range_5 = tk.Entry(parent, width=25)
        self.crit_range_5.grid(row=9, column=4, padx=5, pady=5)

        # Store the entries in a list if needed
        self.weapon_entries = [
            self.weapon_1,
            self.hit_mod_1,
            self.damage_1,
            self.range_1,
            self.crit_range_1,
            self.weapon_2,
            self.hit_mod_2,
            self.damage_2,
            self.range_2,
            self.crit_range_2,
            self.weapon_3,
            self.hit_mod_3,
            self.damage_3,
            self.range_3,
            self.crit_range_3,
            self.weapon_4,
            self.hit_mod_4,
            self.damage_4,
            self.range_4,
            self.crit_range_4,
            self.weapon_5,
            self.hit_mod_5,
            self.damage_5,
            self.range_5,
            self.crit_range_5,
        ]

    def create_skill_fields(self, parent):

        self.lbl_skills_1 = tk.Label(parent, text="Skill")
        self.lbl_skills_1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.lbl_stat_1 = tk.Label(parent, text="Stat")
        self.lbl_stat_1.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.lbl_train_1 = tk.Label(parent, text="Training")
        self.lbl_train_1.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.lbl_focus_1 = tk.Label(parent, text="Focus")
        self.lbl_focus_1.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.lbl_misc_1 = tk.Label(parent, text="Misc")
        self.lbl_misc_1.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.lbl_modifier_1 = tk.Label(parent, text="Modifier")
        self.lbl_modifier_1.grid(row=0, column=5, padx=5, pady=5, sticky="w")

        self.lbl_acrobatics = tk.Label(parent, text="Acrobatics")
        self.lbl_acrobatics.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.lbl_dex = tk.Label(parent, text="Dex")
        self.lbl_dex.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.acro_train = tk.Entry(parent, width=1)
        self.acro_train.grid(row=1, column=2, padx=5, pady=5)
        self.acro_focus = tk.Entry(parent, width=1)
        self.acro_focus.grid(row=1, column=3, padx=5, pady=5)
        self.acro_misc = tk.Entry(parent, width=3)
        self.acro_misc.grid(row=1, column=4, padx=5, pady=5)
        self.acro_modifier = tk.Entry(parent, width=5)
        self.acro_modifier.grid(row=1, column=5, padx=5, pady=5)

        self.lbl_climb = tk.Label(parent, text="Climb")
        self.lbl_climb.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.lbl_str = tk.Label(parent, text="Str")
        self.lbl_str.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.climb_train = tk.Entry(parent, width=1)
        self.climb_train.grid(row=2, column=2, padx=5, pady=5)
        self.climb_focus = tk.Entry(parent, width=1)
        self.climb_focus.grid(row=2, column=3, padx=5, pady=5)
        self.climb_misc = tk.Entry(parent, width=3)
        self.climb_misc.grid(row=2, column=4, padx=5, pady=5)
        self.climb_modifier = tk.Entry(parent, width=5)
        self.climb_modifier.grid(row=2, column=5, padx=5, pady=5)

        self.lbl_deception = tk.Label(parent, text="Deception")
        self.lbl_deception.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.lbl_cha = tk.Label(parent, text="Cha")
        self.lbl_cha.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.deception_train = tk.Entry(parent, width=1)
        self.deception_train.grid(row=3, column=2, padx=5, pady=5)
        self.deception_focus = tk.Entry(parent, width=1)
        self.deception_focus.grid(row=3, column=3, padx=5, pady=5)
        self.deception_misc = tk.Entry(parent, width=3)
        self.deception_misc.grid(row=3, column=4, padx=5, pady=5)
        self.deception_modifier = tk.Entry(parent, width=5)
        self.deception_modifier.grid(row=3, column=5, padx=5, pady=5)

        self.lbl_endurance = tk.Label(parent, text="Endurance")
        self.lbl_endurance.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.lbl_con = tk.Label(parent, text="Con")
        self.lbl_con.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.endurance_train = tk.Entry(parent, width=1)
        self.endurance_train.grid(row=4, column=2, padx=5, pady=5)
        self.endurance_focus = tk.Entry(parent, width=1)
        self.endurance_focus.grid(row=4, column=3, padx=5, pady=5)
        self.endurance_misc = tk.Entry(parent, width=3)
        self.endurance_misc.grid(row=4, column=4, padx=5, pady=5)
        self.endurance_modifier = tk.Entry(parent, width=5)
        self.endurance_modifier.grid(row=4, column=5, padx=5, pady=5)

        self.lbl_get_info = tk.Label(parent, text="Gather Information")
        self.lbl_get_info.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.lbl_cha = tk.Label(parent, text="Cha")
        self.lbl_cha.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        self.get_info_train = tk.Entry(parent, width=1)
        self.get_info_train.grid(row=5, column=2, padx=5, pady=5)
        self.get_info_focus = tk.Entry(parent, width=1)
        self.get_info_focus.grid(row=5, column=3, padx=5, pady=5)
        self.get_info_misc = tk.Entry(parent, width=3)
        self.get_info_misc.grid(row=5, column=4, padx=5, pady=5)
        self.get_info_modifier = tk.Entry(parent, width=5)
        self.get_info_modifier.grid(row=5, column=5, padx=5, pady=5)

        self.lbl_initiative = tk.Label(parent, text="Initiative")
        self.lbl_initiative.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.lbl_dex = tk.Label(parent, text="Dex")
        self.lbl_dex.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        self.initiative_train = tk.Entry(parent, width=1)
        self.initiative_train.grid(row=6, column=2, padx=5, pady=5)
        self.initiative_focus = tk.Entry(parent, width=1)
        self.initiative_focus.grid(row=6, column=3, padx=5, pady=5)
        self.initiative_misc = tk.Entry(parent, width=3)
        self.initiative_misc.grid(row=6, column=4, padx=5, pady=5)
        self.initiative_modifier = tk.Entry(parent, width=5)
        self.initiative_modifier.grid(row=6, column=5, padx=5, pady=5)

        self.lbl_jump = tk.Label(parent, text="Jump")
        self.lbl_jump.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.lbl_str = tk.Label(parent, text="Str")
        self.lbl_str.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        self.jump_train = tk.Entry(parent, width=1)
        self.jump_train.grid(row=7, column=2, padx=5, pady=5)
        self.jump_focus = tk.Entry(parent, width=1)
        self.jump_focus.grid(row=7, column=3, padx=5, pady=5)
        self.jump_misc = tk.Entry(parent, width=3)
        self.jump_misc.grid(row=7, column=4, padx=5, pady=5)
        self.jump_modifier = tk.Entry(parent, width=5)
        self.jump_modifier.grid(row=7, column=5, padx=5, pady=5)

        self.lbl_know_bureau = tk.Label(
            parent, text="Knowledge (Bureaucracy)"
        )
        self.lbl_know_bureau.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=8, column=1, padx=5, pady=5, sticky="w")
        self.know_bureau_train = tk.Entry(parent, width=1)
        self.know_bureau_train.grid(row=8, column=2, padx=5, pady=5)
        self.know_bureau_focus = tk.Entry(parent, width=1)
        self.know_bureau_focus.grid(row=8, column=3, padx=5, pady=5)
        self.know_bureau_misc = tk.Entry(parent, width=3)
        self.know_bureau_misc.grid(row=8, column=4, padx=5, pady=5)
        self.know_bureau_modifier = tk.Entry(parent, width=5)
        self.know_bureau_modifier.grid(row=8, column=5, padx=5, pady=5)

        self.lbl_know_lore = tk.Label(
            parent, text="Knowledge (Galactic Lore)"
        )
        self.lbl_know_lore.grid(
            row=9, column=0, padx=5, pady=5, sticky="w"
        )
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=9, column=1, padx=5, pady=5, sticky="w")
        self.know_lore_train = tk.Entry(parent, width=1)
        self.know_lore_train.grid(
            row=9, column=2, padx=5, pady=5
        )
        self.know_lore_focus = tk.Entry(parent, width=1)
        self.know_lore_focus.grid(row=9, column=3, padx=5, pady=5)
        self.know_lore_misc = tk.Entry(parent, width=3)
        self.know_lore_misc.grid(row=9, column=4, padx=5, pady=5)
        self.know_lore_modifier = tk.Entry(parent, width=5)
        self.know_lore_modifier.grid(
            row=9, column=5, padx=5, pady=5
        )

        self.lbl_know_life = tk.Label(
            parent, text="Knowledge (Life Science)"
        )
        self.lbl_know_life.grid(
            row=10, column=0, padx=5, pady=5, sticky="w"
        )
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=10, column=1, padx=5, pady=5, sticky="w")
        self.know_life_train = tk.Entry(parent, width=1)
        self.know_life_train.grid(
            row=10, column=2, padx=5, pady=5
        )
        self.know_life_focus = tk.Entry(parent, width=1)
        self.know_life_focus.grid(row=10, column=3, padx=5, pady=5)
        self.know_life_misc = tk.Entry(parent, width=3)
        self.know_life_misc.grid(row=10, column=4, padx=5, pady=5)
        self.know_life_modifier = tk.Entry(parent, width=5)
        self.know_life_modifier.grid(
            row=10, column=5, padx=5, pady=5
        )

        self.lbl_know_phys = tk.Label(
            parent, text="Knowledge (Physical Science)"
        )
        self.lbl_know_phys.grid(
            row=11, column=0, padx=5, pady=5, sticky="w"
        )
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=11, column=1, padx=5, pady=5, sticky="w")
        self.know_phys_train = tk.Entry(parent, width=1)
        self.know_phys_train.grid(
            row=11, column=2, padx=5, pady=5
        )
        self.know_phys_focus = tk.Entry(parent, width=1)
        self.know_phys_focus.grid(
            row=11, column=3, padx=5, pady=5
        )
        self.know_phys_misc = tk.Entry(parent, width=3)
        self.know_phys_misc.grid(
            row=11, column=4, padx=5, pady=5
        )
        self.know_phys_modifier = tk.Entry(parent, width=5)
        self.know_phys_modifier.grid(
            row=11, column=5, padx=5, pady=5
        )

        self.lbl_know_soc = tk.Label(
            parent, text="Knowledge (Social Science)"
        )
        self.lbl_know_soc.grid(
            row=12, column=0, padx=5, pady=5, sticky="w"
        )
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=12, column=1, padx=5, pady=5, sticky="w")
        self.know_soc_train = tk.Entry(parent, width=1)
        self.know_soc_train.grid(
            row=12, column=2, padx=5, pady=5
        )
        self.know_soc_focus = tk.Entry(parent, width=1)
        self.know_soc_focus.grid(row=12, column=3, padx=5, pady=5)
        self.know_soc_misc = tk.Entry(parent, width=3)
        self.know_soc_misc.grid(row=12, column=4, padx=5, pady=5)
        self.know_soc_modifier = tk.Entry(parent, width=5)
        self.know_soc_modifier.grid(
            row=12, column=5, padx=5, pady=5
        )

        self.lbl_skills_2 = tk.Label(parent, text="Skill")
        self.lbl_skills_2.grid(row=0, column=6, padx=5, pady=5, sticky="w")
        self.lbl_stat_2 = tk.Label(parent, text="Stat")
        self.lbl_stat_2.grid(row=0, column=7, padx=5, pady=5, sticky="w")
        self.lbl_train_2 = tk.Label(parent, text="Training")
        self.lbl_train_2.grid(row=0, column=8, padx=5, pady=5, sticky="w")
        self.lbl_focus_2 = tk.Label(parent, text="Focus")
        self.lbl_focus_2.grid(row=0, column=9, padx=5, pady=5, sticky="w")
        self.lbl_misc_2 = tk.Label(parent, text="Misc")
        self.lbl_misc_2.grid(row=0, column=10, padx=5, pady=5, sticky="w")
        self.lbl_modifier_2 = tk.Label(parent, text="Modifier")
        self.lbl_modifier_2.grid(row=0, column=11, padx=5, pady=5, sticky="w")

        self.lbl_know_tac = tk.Label(parent, text="Knowledge (Tactics)")
        self.lbl_know_tac.grid(row=1, column=6, padx=5, pady=5, sticky="w")
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=1, column=7, padx=5, pady=5, sticky="w")
        self.know_tac_train = tk.Entry(parent, width=1)
        self.know_tac_train.grid(row=1, column=8, padx=5, pady=5)
        self.know_tac_focus = tk.Entry(parent, width=1)
        self.know_tac_focus.grid(row=1, column=9, padx=5, pady=5)
        self.know_tac_misc = tk.Entry(parent, width=3)
        self.know_tac_misc.grid(row=1, column=10, padx=5, pady=5)
        self.know_tac_modifier = tk.Entry(parent, width=5)
        self.know_tac_modifier.grid(row=1, column=11, padx=5, pady=5)

        self.lbl_know_tech = tk.Label(parent, text="Knowledge (Technology)")
        self.lbl_know_tech.grid(row=2, column=6, padx=5, pady=5, sticky="w")
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=2, column=7, padx=5, pady=5, sticky="w")
        self.know_tech_train = tk.Entry(parent, width=1)
        self.know_tech_train.grid(row=2, column=8, padx=5, pady=5)
        self.know_tech_focus = tk.Entry(parent, width=1)
        self.know_tech_focus.grid(row=2, column=9, padx=5, pady=5)
        self.know_tech_misc = tk.Entry(parent, width=3)
        self.know_tech_misc.grid(row=2, column=10, padx=5, pady=5)
        self.know_tech_modifier = tk.Entry(parent, width=5)
        self.know_tech_modifier.grid(row=2, column=11, padx=5, pady=5)

        self.lbl_mechanics = tk.Label(parent, text="Mechanics")
        self.lbl_mechanics.grid(row=3, column=6, padx=5, pady=5, sticky="w")
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=3, column=7, padx=5, pady=5, sticky="w")
        self.mechanics_train = tk.Entry(parent, width=1)
        self.mechanics_train.grid(row=3, column=8, padx=5, pady=5)
        self.mechanics_focus = tk.Entry(parent, width=1)
        self.mechanics_focus.grid(row=3, column=9, padx=5, pady=5)
        self.mechanics_misc = tk.Entry(parent, width=3)
        self.mechanics_misc.grid(row=3, column=10, padx=5, pady=5)
        self.mechanics_modifier = tk.Entry(parent, width=5)
        self.mechanics_modifier.grid(row=3, column=11, padx=5, pady=5)

        self.lbl_perception = tk.Label(parent, text="Perception")
        self.lbl_perception.grid(row=4, column=6, padx=5, pady=5, sticky="w")
        self.lbl_wis = tk.Label(parent, text="Wis")
        self.lbl_wis.grid(row=4, column=7, padx=5, pady=5, sticky="w")
        self.perception_train = tk.Entry(parent, width=1)
        self.perception_train.grid(row=4, column=8, padx=5, pady=5)
        self.perception_focus = tk.Entry(parent, width=1)
        self.perception_focus.grid(row=4, column=9, padx=5, pady=5)
        self.perception_misc = tk.Entry(parent, width=3)
        self.perception_misc.grid(row=4, column=10, padx=5, pady=5)
        self.perception_modifier = tk.Entry(parent, width=5)
        self.perception_modifier.grid(row=4, column=11, padx=5, pady=5)

        self.lbl_persuasion = tk.Label(parent, text="Persuasion")
        self.lbl_persuasion.grid(row=5, column=6, padx=5, pady=5, sticky="w")
        self.lbl_cha = tk.Label(parent, text="Cha")
        self.lbl_cha.grid(row=5, column=7, padx=5, pady=5, sticky="w")
        self.persuasion_train = tk.Entry(parent, width=1)
        self.persuasion_train.grid(row=5, column=8, padx=5, pady=5)
        self.persuasion_focus = tk.Entry(parent, width=1)
        self.persuasion_focus.grid(row=5, column=9, padx=5, pady=5)
        self.persuasion_misc = tk.Entry(parent, width=3)
        self.persuasion_misc.grid(row=5, column=10, padx=5, pady=5)
        self.persuasion_modifier = tk.Entry(parent, width=5)
        self.persuasion_modifier.grid(row=5, column=11, padx=5, pady=5)

        self.lbl_pilot = tk.Label(parent, text="Pilot")
        self.lbl_pilot.grid(row=6, column=6, padx=5, pady=5, sticky="w")
        self.lbl_dex = tk.Label(parent, text="Dex")
        self.lbl_dex.grid(row=6, column=7, padx=5, pady=5, sticky="w")
        self.pilot_train = tk.Entry(parent, width=1)
        self.pilot_train.grid(row=6, column=8, padx=5, pady=5)
        self.pilot_focus = tk.Entry(parent, width=1)
        self.pilot_focus.grid(row=6, column=9, padx=5, pady=5)
        self.pilot_misc = tk.Entry(parent, width=3)
        self.pilot_misc.grid(row=6, column=10, padx=5, pady=5)
        self.pilot_modifier = tk.Entry(parent, width=5)
        self.pilot_modifier.grid(row=6, column=11, padx=5, pady=5)

        self.lbl_ride = tk.Label(parent, text="Ride")
        self.lbl_ride.grid(row=7, column=6, padx=5, pady=5, sticky="w")
        self.lbl_dex = tk.Label(parent, text="Dex")
        self.lbl_dex.grid(row=7, column=7, padx=5, pady=5, sticky="w")
        self.ride_train = tk.Entry(parent, width=1)
        self.ride_train.grid(row=7, column=8, padx=5, pady=5)
        self.ride_focus = tk.Entry(parent, width=1)
        self.ride_focus.grid(row=7, column=9, padx=5, pady=5)
        self.ride_misc = tk.Entry(parent, width=3)
        self.ride_misc.grid(row=7, column=10, padx=5, pady=5)
        self.ride_modifier = tk.Entry(parent, width=5)
        self.ride_modifier.grid(row=7, column=11, padx=5, pady=5)

        self.lbl_stealth = tk.Label(parent, text="Stealth")
        self.lbl_stealth.grid(row=8, column=6, padx=5, pady=5, sticky="w")
        self.lbl_dex = tk.Label(parent, text="Dex")
        self.lbl_dex.grid(row=8, column=7, padx=5, pady=5, sticky="w")
        self.stealth_train = tk.Entry(parent, width=1)
        self.stealth_train.grid(row=8, column=8, padx=5, pady=5)
        self.stealth_focus = tk.Entry(parent, width=1)
        self.stealth_focus.grid(row=8, column=9, padx=5, pady=5)
        self.stealth_misc = tk.Entry(parent, width=3)
        self.stealth_misc.grid(row=8, column=10, padx=5, pady=5)
        self.stealth_modifier = tk.Entry(parent, width=5)
        self.stealth_modifier.grid(row=8, column=11, padx=5, pady=5)

        self.lbl_survival = tk.Label(parent, text="Survival")
        self.lbl_survival.grid(row=9, column=6, padx=5, pady=5, sticky="w")
        self.lbl_wis = tk.Label(parent, text="Wis")
        self.lbl_wis.grid(row=9, column=7, padx=5, pady=5, sticky="w")
        self.survival_train = tk.Entry(parent, width=1)
        self.survival_train.grid(row=9, column=8, padx=5, pady=5)
        self.survival_focus = tk.Entry(parent, width=1)
        self.survival_focus.grid(row=9, column=9, padx=5, pady=5)
        self.survival_misc = tk.Entry(parent, width=3)
        self.survival_misc.grid(row=9, column=10, padx=5, pady=5)
        self.survival_modifier = tk.Entry(parent, width=5)
        self.survival_modifier.grid(row=9, column=11, padx=5, pady=5)

        self.lbl_swim = tk.Label(parent, text="Swim")
        self.lbl_swim.grid(row=10, column=6, padx=5, pady=5, sticky="w")
        self.lbl_str = tk.Label(parent, text="Str")
        self.lbl_str.grid(row=10, column=7, padx=5, pady=5, sticky="w")
        self.swim_train = tk.Entry(parent, width=1)
        self.swim_train.grid(row=10, column=8, padx=5, pady=5)
        self.swim_focus = tk.Entry(parent, width=1)
        self.swim_focus.grid(row=10, column=9, padx=5, pady=5)
        self.swim_misc = tk.Entry(parent, width=3)
        self.swim_misc.grid(row=10, column=10, padx=5, pady=5)
        self.swim_modifier = tk.Entry(parent, width=5)
        self.swim_modifier.grid(row=10, column=11, padx=5, pady=5)

        self.lbl_injury = tk.Label(parent, text="Treat Injury")
        self.lbl_injury.grid(row=11, column=6, padx=5, pady=5, sticky="w")
        self.lbl_wis = tk.Label(parent, text="Wis")
        self.lbl_wis.grid(row=11, column=7, padx=5, pady=5, sticky="w")
        self.injury_train = tk.Entry(parent, width=1)
        self.injury_train.grid(row=11, column=8, padx=5, pady=5)
        self.injury_focus = tk.Entry(parent, width=1)
        self.injury_focus.grid(row=11, column=9, padx=5, pady=5)
        self.injury_misc = tk.Entry(parent, width=3)
        self.injury_misc.grid(row=11, column=10, padx=5, pady=5)
        self.injury_modifier = tk.Entry(parent, width=5)
        self.injury_modifier.grid(row=11, column=11, padx=5, pady=5)

        self.lbl_computer = tk.Label(parent, text="Use Computer")
        self.lbl_computer.grid(row=12, column=6, padx=5, pady=5, sticky="w")
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=12, column=7, padx=5, pady=5, sticky="w")
        self.computer_train = tk.Entry(parent, width=1)
        self.computer_train.grid(row=12, column=8, padx=5, pady=5)
        self.computer_focus = tk.Entry(parent, width=1)
        self.computer_focus.grid(row=12, column=9, padx=5, pady=5)
        self.computer_misc = tk.Entry(parent, width=3)
        self.computer_misc.grid(row=12, column=10, padx=5, pady=5)
        self.computer_modifier = tk.Entry(parent, width=5)
        self.computer_modifier.grid(row=12, column=11, padx=5, pady=5)

        self.lbl_use_force = tk.Label(parent, text="Use The Force")
        self.lbl_use_force.grid(row=13, column=6, padx=5, pady=5, sticky="w")
        self.lbl_wis = tk.Label(parent, text="Wis")
        self.lbl_wis.grid(row=13, column=7, padx=5, pady=5, sticky="w")
        self.use_force_train = tk.Entry(parent, width=1)
        self.use_force_train.grid(row=13, column=8, padx=5, pady=5)
        self.use_force_focus = tk.Entry(parent, width=1)
        self.use_force_focus.grid(row=13, column=9, padx=5, pady=5)
        self.use_force_misc = tk.Entry(parent, width=3)
        self.use_force_misc.grid(row=13, column=10, padx=5, pady=5)
        self.use_force_modifier = tk.Entry(parent, width=5)
        self.use_force_modifier.grid(row=13, column=11, padx=5, pady=5)

        skills_entries = [
            self.acro_train,
            self.acro_focus,
            self.acro_modifier,
            self.climb_train,
            self.climb_focus,
            self.climb_modifier,
            self.deception_train,
            self.deception_focus,
            self.deception_modifier,
            self.endurance_train,
            self.endurance_focus,
            self.endurance_modifier,
            self.get_info_train,
            self.get_info_focus,
            self.get_info_modifier,
            self.initiative_train,
            self.initiative_focus,
            self.initiative_modifier,
            self.jump_train,
            self.jump_focus,
            self.jump_modifier,
            self.know_bureau_train,
            self.know_bureau_focus,
            self.know_bureau_modifier,
            self.know_lore_train,
            self.know_lore_focus,
            self.know_lore_modifier,
            self.know_life_train,
            self.know_life_focus,
            self.know_life_modifier,
            self.know_phys_train,
            self.know_phys_focus,
            self.know_phys_modifier,
            self.know_soc_train,
            self.know_soc_focus,
            self.know_soc_modifier,
            self.know_tac_train,
            self.know_tac_focus,
            self.know_tac_modifier,
            self.know_tech_train,
            self.know_tech_focus,
            self.know_tech_modifier,
            self.mechanics_train,
            self.mechanics_focus,
            self.mechanics_modifier,
            self.perception_train,
            self.perception_focus,
            self.perception_modifier,
            self.persuasion_train,
            self.persuasion_focus,
            self.persuasion_modifier,
            self.pilot_train,
            self.pilot_focus,
            self.pilot_modifier,
            self.ride_train,
            self.ride_focus,
            self.ride_modifier,
            self.stealth_train,
            self.stealth_focus,
            self.stealth_modifier,
            self.survival_train,
            self.survival_focus,
            self.survival_modifier,
            self.injury_train,
            self.injury_focus,
            self.injury_modifier,
            self.computer_train,
            self.computer_focus,
            self.computer_modifier,
            self.use_force_train,
            self.use_force_focus,
            self.use_force_modifier,
        ]

    def create_force_school_fields(self, parent):
        # Meta labels
        self.lbl_schools = tk.Label(parent, text="Schools")
        self.lbl_schools.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.lbl_train = tk.Label(parent, text="Training")
        self.lbl_train.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.lbl_empty_1 = tk.Label(parent, text="")
        self.lbl_empty_1.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.lbl_empty_2 = tk.Label(parent, text="")
        self.lbl_empty_2.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        self.lbl_modifier = tk.Label(parent, text="Modifier")
        self.lbl_modifier.grid(row=0, column=4, padx=5, pady=5, sticky="w")

        # Labels and Entries for each school

        # Alchemy
        self.lbl_alchemy = tk.Label(parent, text="Alchemy")
        self.lbl_alchemy.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.alchemy_1 = tk.Entry(parent, width=1)
        self.alchemy_1.grid(row=1, column=1, padx=5, pady=5)
        self.alchemy_2 = tk.Entry(parent, width=1)
        self.alchemy_2.grid(row=1, column=2, padx=5, pady=5)
        self.alchemy_3 = tk.Entry(parent, width=1)
        self.alchemy_3.grid(row=1, column=3, padx=5, pady=5)
        self.alchemy_modifier = tk.Entry(parent, width=10)
        self.alchemy_modifier.grid(row=1, column=4, padx=5, pady=5)

        # Augmentation
        self.lbl_augmentation = tk.Label(parent, text="Augmentation")
        self.lbl_augmentation.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.augmentation_1 = tk.Entry(parent, width=1)
        self.augmentation_1.grid(row=2, column=1, padx=5, pady=5)
        self.augmentation_2 = tk.Entry(parent, width=1)
        self.augmentation_2.grid(row=2, column=2, padx=5, pady=5)
        self.augmentation_3 = tk.Entry(parent, width=1)
        self.augmentation_3.grid(row=2, column=3, padx=5, pady=5)
        self.augmentation_modifier = tk.Entry(parent, width=10)
        self.augmentation_modifier.grid(row=2, column=4, padx=5, pady=5)

        # Cognition
        self.lbl_cognition = tk.Label(parent, text="Cognition")
        self.lbl_cognition.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.cognition_1 = tk.Entry(parent, width=1)
        self.cognition_1.grid(row=3, column=1, padx=5, pady=5)
        self.cognition_2 = tk.Entry(parent, width=1)
        self.cognition_2.grid(row=3, column=2, padx=5, pady=5)
        self.cognition_3 = tk.Entry(parent, width=1)
        self.cognition_3.grid(row=3, column=3, padx=5, pady=5)
        self.cognition_modifier = tk.Entry(parent, width=10)
        self.cognition_modifier.grid(row=3, column=4, padx=5, pady=5)

        # Sorcery
        self.lbl_sorcery = tk.Label(parent, text="Sorcery")
        self.lbl_sorcery.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.sorcery_1 = tk.Entry(parent, width=1)
        self.sorcery_1.grid(row=4, column=1, padx=5, pady=5)
        self.sorcery_2 = tk.Entry(parent, width=1)
        self.sorcery_2.grid(row=4, column=2, padx=5, pady=5)
        self.sorcery_3 = tk.Entry(parent, width=1)
        self.sorcery_3.grid(row=4, column=3, padx=5, pady=5)
        self.sorcery_modifier = tk.Entry(parent, width=10)
        self.sorcery_modifier.grid(row=4, column=4, padx=5, pady=5)

        # Technokinesis
        self.lbl_techno = tk.Label(parent, text="Technokinesis")
        self.lbl_techno.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.techno_1 = tk.Entry(parent, width=1)
        self.techno_1.grid(row=5, column=1, padx=5, pady=5)
        self.techno_2 = tk.Entry(parent, width=1)
        self.techno_2.grid(row=5, column=2, padx=5, pady=5)
        self.techno_3 = tk.Entry(parent, width=1)
        self.techno_3.grid(row=5, column=3, padx=5, pady=5)
        self.techno_modifier = tk.Entry(parent, width=10)
        self.techno_modifier.grid(row=5, column=4, padx=5, pady=5)

        # Telekinesis
        self.lbl_tele = tk.Label(parent, text="Telekinesis")
        self.lbl_tele.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.tele_1 = tk.Entry(parent, width=1)
        self.tele_1.grid(row=6, column=1, padx=5, pady=5)
        self.tele_2 = tk.Entry(parent, width=1)
        self.tele_2.grid(row=6, column=2, padx=5, pady=5)
        self.tele_3 = tk.Entry(parent, width=1)
        self.tele_3.grid(row=6, column=3, padx=5, pady=5)
        self.tele_modifier = tk.Entry(parent, width=10)
        self.tele_modifier.grid(row=6, column=4, padx=5, pady=5)

        # Vitalism
        self.lbl_vitalism = tk.Label(parent, text="Vitalism")
        self.lbl_vitalism.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.vitalism_1 = tk.Entry(parent, width=1)
        self.vitalism_1.grid(row=7, column=1, padx=5, pady=5)
        self.vitalism_2 = tk.Entry(parent, width=1)
        self.vitalism_2.grid(row=7, column=2, padx=5, pady=5)
        self.vitalism_3 = tk.Entry(parent, width=1)
        self.vitalism_3.grid(row=7, column=3, padx=5, pady=5)
        self.vitalism_modifier = tk.Entry(parent, width=10)
        self.vitalism_modifier.grid(row=7, column=4, padx=5, pady=5)

        # Force Uses
        self.lbl_force_uses = tk.Label(parent, text="Force Uses")
        self.lbl_force_uses.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.force_uses = tk.Entry(parent, width=10)
        self.force_uses.grid(row=8, column=1, padx=5, pady=5)

        # Store the entries in a list
        self.force_school_entries = [
            self.alchemy_1,
            self.alchemy_2,
            self.alchemy_3,
            self.alchemy_modifier,
            self.augmentation_1,
            self.augmentation_2,
            self.augmentation_3,
            self.augmentation_modifier,
            self.cognition_1,
            self.cognition_2,
            self.cognition_3,
            self.cognition_modifier,
            self.sorcery_1,
            self.sorcery_2,
            self.sorcery_3,
            self.sorcery_modifier,
            self.techno_1,
            self.techno_2,
            self.techno_3,
            self.techno_modifier,
            self.tele_1,
            self.tele_2,
            self.tele_3,
            self.tele_modifier,
            self.vitalism_1,
            self.vitalism_2,
            self.vitalism_3,
            self.vitalism_modifier,
            self.force_uses,
        ]

    def create_force_tech_secret_fields(self, parent):
        # Labels for Force Techniques and Force Secrets
        self.lbl_force_techs = tk.Label(parent, text="Force Techniques")
        self.lbl_force_techs.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.lbl_force_sec = tk.Label(parent, text="Force Secrets")
        self.lbl_force_sec.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Entries for Force Techniques
        self.force_tech_1 = tk.Entry(parent, width=25)
        self.force_tech_1.grid(row=1, column=0, padx=5, pady=5)
        self.force_tech_2 = tk.Entry(parent, width=25)
        self.force_tech_2.grid(row=2, column=0, padx=5, pady=5)
        self.force_tech_3 = tk.Entry(parent, width=25)
        self.force_tech_3.grid(row=3, column=0, padx=5, pady=5)
        self.force_tech_4 = tk.Entry(parent, width=25)
        self.force_tech_4.grid(row=4, column=0, padx=5, pady=5)
        self.force_tech_5 = tk.Entry(parent, width=25)
        self.force_tech_5.grid(row=5, column=0, padx=5, pady=5)
        self.force_tech_6 = tk.Entry(parent, width=25)
        self.force_tech_6.grid(row=6, column=0, padx=5, pady=5)
        self.force_tech_7 = tk.Entry(parent, width=25)
        self.force_tech_7.grid(row=7, column=0, padx=5, pady=5)
        self.force_tech_8 = tk.Entry(parent, width=25)
        self.force_tech_8.grid(row=8, column=0, padx=5, pady=5)
        self.force_tech_9 = tk.Entry(parent, width=25)
        self.force_tech_9.grid(row=9, column=0, padx=5, pady=5)
        self.force_tech_10 = tk.Entry(parent, width=25)
        self.force_tech_10.grid(row=10, column=0, padx=5, pady=5)
        self.force_tech_11 = tk.Entry(parent, width=25)
        self.force_tech_11.grid(row=11, column=0, padx=5, pady=5)
        self.force_tech_12 = tk.Entry(parent, width=25)
        self.force_tech_12.grid(row=12, column=0, padx=5, pady=5)
        self.force_tech_13 = tk.Entry(parent, width=25)
        self.force_tech_13.grid(row=13, column=0, padx=5, pady=5)
        self.force_tech_14 = tk.Entry(parent, width=25)
        self.force_tech_14.grid(row=14, column=0, padx=5, pady=5)
        self.force_tech_15 = tk.Entry(parent, width=25)
        self.force_tech_15.grid(row=15, column=0, padx=5, pady=5)

        # Entries for Force Secrets
        self.force_secret_1 = tk.Entry(parent, width=25)
        self.force_secret_1.grid(row=1, column=1, padx=5, pady=5)
        self.force_secret_2 = tk.Entry(parent, width=25)
        self.force_secret_2.grid(row=2, column=1, padx=5, pady=5)
        self.force_secret_3 = tk.Entry(parent, width=25)
        self.force_secret_3.grid(row=3, column=1, padx=5, pady=5)
        self.force_secret_4 = tk.Entry(parent, width=25)
        self.force_secret_4.grid(row=4, column=1, padx=5, pady=5)
        self.force_secret_5 = tk.Entry(parent, width=25)
        self.force_secret_5.grid(row=5, column=1, padx=5, pady=5)
        self.force_secret_6 = tk.Entry(parent, width=25)
        self.force_secret_6.grid(row=6, column=1, padx=5, pady=5)
        self.force_secret_7 = tk.Entry(parent, width=25)
        self.force_secret_7.grid(row=7, column=1, padx=5, pady=5)
        self.force_secret_8 = tk.Entry(parent, width=25)
        self.force_secret_8.grid(row=8, column=1, padx=5, pady=5)
        self.force_secret_9 = tk.Entry(parent, width=25)
        self.force_secret_9.grid(row=9, column=1, padx=5, pady=5)
        self.force_secret_10 = tk.Entry(parent, width=25)
        self.force_secret_10.grid(row=10, column=1, padx=5, pady=5)
        self.force_secret_11 = tk.Entry(parent, width=25)
        self.force_secret_11.grid(row=11, column=1, padx=5, pady=5)
        self.force_secret_12 = tk.Entry(parent, width=25)
        self.force_secret_12.grid(row=12, column=1, padx=5, pady=5)
        self.force_secret_13 = tk.Entry(parent, width=25)
        self.force_secret_13.grid(row=13, column=1, padx=5, pady=5)
        self.force_secret_14 = tk.Entry(parent, width=25)
        self.force_secret_14.grid(row=14, column=1, padx=5, pady=5)
        self.force_secret_15 = tk.Entry(parent, width=25)
        self.force_secret_15.grid(row=15, column=1, padx=5, pady=5)

        # Store the entries in lists
        self.force_tech_entries = [
            self.force_tech_1,
            self.force_tech_2,
            self.force_tech_3,
            self.force_tech_4,
            self.force_tech_5,
            self.force_tech_6,
            self.force_tech_7,
            self.force_tech_8,
            self.force_tech_9,
            self.force_tech_10,
            self.force_tech_11,
            self.force_tech_12,
            self.force_tech_13,
            self.force_tech_14,
            self.force_tech_15,
        ]

        self.force_secret_entries = [
            self.force_secret_1,
            self.force_secret_2,
            self.force_secret_3,
            self.force_secret_4,
            self.force_secret_5,
            self.force_secret_6,
            self.force_secret_7,
            self.force_secret_8,
            self.force_secret_9,
            self.force_secret_10,
            self.force_secret_11,
            self.force_secret_12,
            self.force_secret_13,
            self.force_secret_14,
            self.force_secret_15,
        ]

    def create_feats_talents_fields(self, parent):
        # Labels for Feats and Talents
        self.lbl_feats = tk.Label(parent, text="Feats:")
        self.lbl_feats.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.lbl_talents = tk.Label(parent, text="Talents:")
        self.lbl_talents.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Entries for Feats
        self.feats_1 = tk.Entry(parent, width=25)
        self.feats_1.grid(row=1, column=0, padx=5, pady=5)
        self.feats_2 = tk.Entry(parent, width=25)
        self.feats_2.grid(row=2, column=0, padx=5, pady=5)
        self.feats_3 = tk.Entry(parent, width=25)
        self.feats_3.grid(row=3, column=0, padx=5, pady=5)
        self.feats_4 = tk.Entry(parent, width=25)
        self.feats_4.grid(row=4, column=0, padx=5, pady=5)
        self.feats_5 = tk.Entry(parent, width=25)
        self.feats_5.grid(row=5, column=0, padx=5, pady=5)
        self.feats_6 = tk.Entry(parent, width=25)
        self.feats_6.grid(row=6, column=0, padx=5, pady=5)
        self.feats_7 = tk.Entry(parent, width=25)
        self.feats_7.grid(row=7, column=0, padx=5, pady=5)
        self.feats_8 = tk.Entry(parent, width=25)
        self.feats_8.grid(row=8, column=0, padx=5, pady=5)
        self.feats_9 = tk.Entry(parent, width=25)
        self.feats_9.grid(row=9, column=0, padx=5, pady=5)
        self.feats_10 = tk.Entry(parent, width=25)
        self.feats_10.grid(row=10, column=0, padx=5, pady=5)
        self.feats_11 = tk.Entry(parent, width=25)
        self.feats_11.grid(row=11, column=0, padx=5, pady=5)
        self.feats_12 = tk.Entry(parent, width=25)
        self.feats_12.grid(row=12, column=0, padx=5, pady=5)
        self.feats_13 = tk.Entry(parent, width=25)
        self.feats_13.grid(row=13, column=0, padx=5, pady=5)
        self.feats_14 = tk.Entry(parent, width=25)
        self.feats_14.grid(row=14, column=0, padx=5, pady=5)
        self.feats_15 = tk.Entry(parent, width=25)
        self.feats_15.grid(row=15, column=0, padx=5, pady=5)

        # Entries for Talents
        self.talents_1 = tk.Entry(parent, width=25)
        self.talents_1.grid(row=1, column=1, padx=5, pady=5)
        self.talents_2 = tk.Entry(parent, width=25)
        self.talents_2.grid(row=2, column=1, padx=5, pady=5)
        self.talents_3 = tk.Entry(parent, width=25)
        self.talents_3.grid(row=3, column=1, padx=5, pady=5)
        self.talents_4 = tk.Entry(parent, width=25)
        self.talents_4.grid(row=4, column=1, padx=5, pady=5)
        self.talents_5 = tk.Entry(parent, width=25)
        self.talents_5.grid(row=5, column=1, padx=5, pady=5)
        self.talents_6 = tk.Entry(parent, width=25)
        self.talents_6.grid(row=6, column=1, padx=5, pady=5)
        self.talents_7 = tk.Entry(parent, width=25)
        self.talents_7.grid(row=7, column=1, padx=5, pady=5)
        self.talents_8 = tk.Entry(parent, width=25)
        self.talents_8.grid(row=8, column=1, padx=5, pady=5)
        self.talents_9 = tk.Entry(parent, width=25)
        self.talents_9.grid(row=9, column=1, padx=5, pady=5)
        self.talents_10 = tk.Entry(parent, width=25)
        self.talents_10.grid(row=10, column=1, padx=5, pady=5)
        self.talents_11 = tk.Entry(parent, width=25)
        self.talents_11.grid(row=11, column=1, padx=5, pady=5)
        self.talents_12 = tk.Entry(parent, width=25)
        self.talents_12.grid(row=12, column=1, padx=5, pady=5)
        self.talents_13 = tk.Entry(parent, width=25)
        self.talents_13.grid(row=13, column=1, padx=5, pady=5)
        self.talents_14 = tk.Entry(parent, width=25)
        self.talents_14.grid(row=14, column=1, padx=5, pady=5)
        self.talents_15 = tk.Entry(parent, width=25)
        self.talents_15.grid(row=15, column=1, padx=5, pady=5)

        # Store the entries in a list
        self.feats_talents_entries = [
            self.feats_1,
            self.feats_2,
            self.feats_3,
            self.feats_4,
            self.feats_5,
            self.feats_6,
            self.feats_7,
            self.feats_8,
            self.feats_9,
            self.feats_10,
            self.feats_11,
            self.feats_12,
            self.feats_13,
            self.feats_14,
            self.feats_15,
            self.talents_1,
            self.talents_2,
            self.talents_3,
            self.talents_4,
            self.talents_5,
            self.talents_6,
            self.talents_7,
            self.talents_8,
            self.talents_9,
            self.talents_10,
            self.talents_11,
            self.talents_12,
            self.talents_13,
            self.talents_14,
            self.talents_15,
        ]

    def create_equipment_fields(self, parent):
        # Label for Equipment
        self.lbl_equipment = tk.Label(parent, text="Equipment:")
        self.lbl_equipment.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Equipment Entries (8 rows, 4 columns)
        self.equipment_1 = tk.Entry(parent, width=25)
        self.equipment_1.grid(row=1, column=0, padx=5, pady=5)
        self.equipment_2 = tk.Entry(parent, width=25)
        self.equipment_2.grid(row=1, column=1, padx=5, pady=5)
        self.equipment_3 = tk.Entry(parent, width=25)
        self.equipment_3.grid(row=1, column=2, padx=5, pady=5)
        self.equipment_4 = tk.Entry(parent, width=25)
        self.equipment_4.grid(row=1, column=3, padx=5, pady=5)

        self.equipment_5 = tk.Entry(parent, width=25)
        self.equipment_5.grid(row=2, column=0, padx=5, pady=5)
        self.equipment_6 = tk.Entry(parent, width=25)
        self.equipment_6.grid(row=2, column=1, padx=5, pady=5)
        self.equipment_7 = tk.Entry(parent, width=25)
        self.equipment_7.grid(row=2, column=2, padx=5, pady=5)
        self.equipment_8 = tk.Entry(parent, width=25)
        self.equipment_8.grid(row=2, column=3, padx=5, pady=5)

        self.equipment_9 = tk.Entry(parent, width=25)
        self.equipment_9.grid(row=3, column=0, padx=5, pady=5)
        self.equipment_10 = tk.Entry(parent, width=25)
        self.equipment_10.grid(row=3, column=1, padx=5, pady=5)
        self.equipment_11 = tk.Entry(parent, width=25)
        self.equipment_11.grid(row=3, column=2, padx=5, pady=5)
        self.equipment_12 = tk.Entry(parent, width=25)
        self.equipment_12.grid(row=3, column=3, padx=5, pady=5)

        self.equipment_13 = tk.Entry(parent, width=25)
        self.equipment_13.grid(row=4, column=0, padx=5, pady=5)
        self.equipment_14 = tk.Entry(parent, width=25)
        self.equipment_14.grid(row=4, column=1, padx=5, pady=5)
        self.equipment_15 = tk.Entry(parent, width=25)
        self.equipment_15.grid(row=4, column=2, padx=5, pady=5)
        self.equipment_16 = tk.Entry(parent, width=25)
        self.equipment_16.grid(row=4, column=3, padx=5, pady=5)

        self.equipment_17 = tk.Entry(parent, width=25)
        self.equipment_17.grid(row=5, column=0, padx=5, pady=5)
        self.equipment_18 = tk.Entry(parent, width=25)
        self.equipment_18.grid(row=5, column=1, padx=5, pady=5)
        self.equipment_19 = tk.Entry(parent, width=25)
        self.equipment_19.grid(row=5, column=2, padx=5, pady=5)
        self.equipment_20 = tk.Entry(parent, width=25)
        self.equipment_20.grid(row=5, column=3, padx=5, pady=5)

        self.equipment_21 = tk.Entry(parent, width=25)
        self.equipment_21.grid(row=6, column=0, padx=5, pady=5)
        self.equipment_22 = tk.Entry(parent, width=25)
        self.equipment_22.grid(row=6, column=1, padx=5, pady=5)
        self.equipment_23 = tk.Entry(parent, width=25)
        self.equipment_23.grid(row=6, column=2, padx=5, pady=5)
        self.equipment_24 = tk.Entry(parent, width=25)
        self.equipment_24.grid(row=6, column=3, padx=5, pady=5)

        self.equipment_25 = tk.Entry(parent, width=25)
        self.equipment_25.grid(row=7, column=0, padx=5, pady=5)
        self.equipment_26 = tk.Entry(parent, width=25)
        self.equipment_26.grid(row=7, column=1, padx=5, pady=5)
        self.equipment_27 = tk.Entry(parent, width=25)
        self.equipment_27.grid(row=7, column=2, padx=5, pady=5)
        self.equipment_28 = tk.Entry(parent, width=25)
        self.equipment_28.grid(row=7, column=3, padx=5, pady=5)

        self.equipment_29 = tk.Entry(parent, width=25)
        self.equipment_29.grid(row=8, column=0, padx=5, pady=5)
        self.equipment_30 = tk.Entry(parent, width=25)
        self.equipment_30.grid(row=8, column=1, padx=5, pady=5)
        self.equipment_31 = tk.Entry(parent, width=25)
        self.equipment_31.grid(row=8, column=2, padx=5, pady=5)
        self.equipment_32 = tk.Entry(parent, width=25)
        self.equipment_32.grid(row=8, column=3, padx=5, pady=5)

        # Store the entries in a list
        self.equipment_entries = [
            self.equipment_1,
            self.equipment_2,
            self.equipment_3,
            self.equipment_4,
            self.equipment_5,
            self.equipment_6,
            self.equipment_7,
            self.equipment_8,
            self.equipment_9,
            self.equipment_10,
            self.equipment_11,
            self.equipment_12,
            self.equipment_13,
            self.equipment_14,
            self.equipment_15,
            self.equipment_16,
            self.equipment_17,
            self.equipment_18,
            self.equipment_19,
            self.equipment_20,
            self.equipment_21,
            self.equipment_22,
            self.equipment_23,
            self.equipment_24,
            self.equipment_25,
            self.equipment_26,
            self.equipment_27,
            self.equipment_28,
            self.equipment_29,
            self.equipment_30,
            self.equipment_31,
            self.equipment_32,
        ]

    def create_buttons(self):
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(
            fill="both",
            expand="yes",
            padx=10,
            pady=5
        )

        import_button = tk.Button(
            self.buttons_frame,
            text="Import from Json",
            command=self.import_from_json
        )
        import_button.pack(side="left", padx=5, pady=5)
        export_button = tk.Button(
            self.buttons_frame,
            text="Export to Json",
            command=self.export_to_json
        )
        export_button.pack(side="left", padx=5, pady=5)

    def export_to_json(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON files", "*.json")]
        )
        if file_path:
            data = {
                "Info": {
                    "Character Name": self.name.get(),
                    "Character Level": self.level.get(),
                    "Classes": self.classes.get(),
                    "Destiny": self.destiny.get(),
                    "Credits": self.credits.get(),
                    "Species": self.species.get(),
                    "Age": self.age.get(),
                    "Height": self.height.get(),
                    "Weight": self.weight.get(),
                    "Gender": self.gender.get(),
                    "Species Info": self.species_info.get(),
                    "Force Points": self.force_points.get(),
                    "Base Attack Bonus": self.base_attack.get(),
                    "Speed": self.speed.get(),
                    "Destiny Points": self.dest_point.get(),
                    "Damage Reduction": self.dam_red.get(),
                },
                "Languages": {
                    "Language 1": self.language_1.get(),
                    "Language 2": self.language_2.get(),
                    "Language 3": self.language_3.get(),
                    "Language 4": self.language_4.get(),
                    "Language 5": self.language_5.get(),
                    "Language 6": self.language_6.get(),
                    "Language 7": self.language_7.get(),
                    "Language 8": self.language_8.get(),
                    "Language 9": self.language_9.get(),
                    "Language 10": self.language_10.get(),
                },
                "Stats": {
                    "Strength": {
                        "Score": self.str_score.get(),
                        "Mod": str(
                            floor(
                                (
                                    int(
                                        self.str_score.get() if 
                                        self.str_score.get() else 0
                                    ) - 10
                                ) / 2
                            )
                        ),
                    },
                    "Dexterity": {
                        "Score": self.dex_score.get(),
                        "Mod": str(
                            floor(
                                (
                                    int(
                                        self.dex_score.get() if
                                        self.dex_score.get() else 0
                                    ) - 10
                                ) / 2
                            )
                        ),
                    },
                    "Constitution": {
                        "Score": self.con_score.get(),
                        "Mod": str(
                            floor(
                                (
                                    int(
                                        self.con_score.get() if
                                        self.con_score.get() else 0
                                    ) - 10
                                ) / 2
                            )
                        ),
                    },
                    "Intelligence": {
                        "Score": self.int_score.get(),
                        "Mod": str(
                            floor(
                                (
                                    int(
                                        self.int_score.get() if
                                        self.int_score.get() else 0
                                    ) - 10
                                ) / 2
                            )
                        ),
                    },
                    "Wisdom": {
                        "Score": self.wis_score.get(),
                        "Mod": str(
                            floor(
                                (
                                    int(
                                        self.wis_score.get() if
                                        self.wis_score.get() else 0
                                    ) - 10
                                ) / 2
                            )
                        ),
                    },
                    "Charisma": {
                        "Score": self.cha_score.get(),
                        "Mod": str(
                            floor(
                                (
                                    int(
                                        self.cha_score.get() if
                                        self.cha_score.get() else 0
                                    ) - 10
                                ) / 2
                            )
                        ),
                    },
                    "Willpower": {
                        "Score": self.will_score.get(),
                        "Mod": str(
                            floor(
                                (
                                    int(
                                        self.will_score.get() if
                                        self.will_score.get() else 0
                                    ) - 10
                                ) / 2
                            )
                        ),
                    },
                    "Dark Side": {
                        "Score": self.dark_score.get(),
                        "Mod": str(
                            floor(
                                (
                                    int(
                                        self.dark_score.get() if
                                        self.dark_score.get() else 0
                                    ) - 10
                                ) / 2
                            )
                        ),
                    },
                },
                "Defenses": {
                    "Fortitude": {
                        "Total": str(
                            int(
                                self.fortitude_2.get()
                                if self.fortitude_2.get()
                                else 0
                            )
                            + int(
                                self.fortitude_3.get()
                                if self.fortitude_3.get()
                                else 0
                            )
                            + int(
                                self.fortitude_4.get()
                                if self.fortitude_4.get()
                                else 0
                            )
                            + int(
                                self.fortitude_5.get()
                                if self.fortitude_5.get()
                                else 0
                            )
                        ),
                        "Class Bonus": self.fortitude_2.get(),
                        "Stat Bonus": self.fortitude_3.get(),
                        "Armor Bonus": self.fortitude_4.get(),
                        "Misc": self.fortitude_5.get(),
                    },
                    "Reflex": {
                        "Total": str(
                            int(
                                self.reflex_2.get()
                                if self.reflex_2.get()
                                else 0
                            )
                            + int(
                                self.reflex_3.get()
                                if self.reflex_3.get()
                                else 0
                            )
                            + int(
                                self.reflex_4.get()
                                if self.reflex_4.get()
                                else 0
                            )
                            + int(
                                self.reflex_5.get()
                                if self.reflex_5.get()
                                else 0
                            )
                        ),
                        "Class Bonus": self.reflex_2.get(),
                        "Stat Bonus": self.reflex_3.get(),
                        "Armor Bonus": self.reflex_4.get(),
                        "Misc": self.reflex_5.get(),
                    },
                    "Will": {
                        "Total": str(
                            int(
                                self.will_2.get()
                                if self.will_2.get()
                                else 0
                            )
                            + int(
                                self.will_3.get()
                                if self.will_3.get()
                                else 0
                            )
                            + int(
                                self.will_4.get()
                                if self.will_4.get()
                                else 0
                            )
                            + int(
                                self.will_5.get()
                                if self.will_5.get()
                                else 0
                            )
                        ),
                        "Class Bonus": self.will_2.get(),
                        "Stat Bonus": self.will_3.get(),
                        "Armor Bonus": self.will_4.get(),
                        "Misc": self.will_5.get(),
                    },
                },
                "Damage Thresholds": {
                    "Fortitude": str(
                        self.fortitude_1.get() if
                        self.fortitude_1.get() else 0
                    ),
                    "Torso": {
                        "Total": str(
                            int(
                                self.fortitude_1.get() if
                                self.fortitude_1.get() else 0
                            )
                            + int(
                                self.torso_misc.get()
                                if self.torso_misc.get()
                                else 0
                            )
                            + 10
                        ),
                        "Misc": self.torso_misc.get(),
                    },
                    "Head": {
                        "Total": str(
                            floor(
                                int(
                                    self.torso.get() if
                                    self.torso.get() else 0
                                ) / 2
                            )
                            + int(
                                self.head_misc.get()
                                if self.head_misc.get()
                                else 0
                            )
                        ),
                        "Misc": self.head_misc.get(),
                    },
                    "Limbs": {
                        "Total": str(
                            floor(
                                int(
                                    self.torso.get() if
                                    self.torso.get() else 0
                                ) / 2
                            )
                            + int(
                                self.limbs_misc.get()
                                if self.limbs_misc.get()
                                else 0
                            )
                        ),
                        "Misc": self.limbs_misc.get(),
                    },
                },
                "Armor": {
                    "Armor Name": self.armor.get(),
                    "Fortitude Bonus": self.fort_bonus.get(),
                    "Reflex Bonus": self.reflex_bonus.get(),
                    "Max Dex Bonus": self.max_dex_bonus.get(),
                    "Additional Affects": self.affects.get(),
                },
                "Weapons": {
                    "Weapon 1": {
                        "Weapon Name": self.weapon_1.get(),
                        "Hit Mod": self.hit_mod_1.get(),
                        "Damage": self.damage_1.get(),
                        "Range": self.range_1.get(),
                        "Crit Range": self.crit_range_1.get(),
                    },
                    "Weapon 2": {
                        "Weapon Name": self.weapon_2.get(),
                        "Hit Mod": self.hit_mod_2.get(),
                        "Damage": self.damage_2.get(),
                        "Range": self.range_2.get(),
                        "Crit Range": self.crit_range_2.get(),
                    },
                    "Weapon 3": {
                        "Weapon Name": self.weapon_3.get(),
                        "Hit Mod": self.hit_mod_3.get(),
                        "Damage": self.damage_3.get(),
                        "Range": self.range_3.get(),
                        "Crit Range": self.crit_range_3.get(),
                    },
                    "Weapon 4": {
                        "Weapon Name": self.weapon_4.get(),
                        "Hit Mod": self.hit_mod_4.get(),
                        "Damage": self.damage_4.get(),
                        "Range": self.range_4.get(),
                        "Crit Range": self.crit_range_4.get(),
                    },
                    "Weapon 5": {
                        "Weapon Name": self.weapon_5.get(),
                        "Hit Mod": self.hit_mod_5.get(),
                        "Damage": self.damage_5.get(),
                        "Range": self.range_5.get(),
                        "Crit Range": self.crit_range_5.get(),
                    },
                },
                "Skills": {
                    "Acrobatics": {
                        "Stat": "Dex",
                        "Total": str(
                            int(
                                self.dex_mod.get() if
                                self.dex_mod.get() else 0
                            )
                            + int(
                                self.acro_train.get() if
                                self.acro_train.get() else 0
                            )
                            + int(
                                self.acro_focus.get() if
                                self.acro_focus.get() else 0
                            )
                            + int(
                                self.acro_misc.get()
                                if self.acro_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.acro_train.get() == "1"
                            or self.acro_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.acro_focus.get() == "1"
                            or self.acro_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.acro_misc.get(),
                    },
                    "Climb": {
                        "Stat": "Str",
                        "Total": str(
                            int(
                                self.str_mod.get() if
                                self.str_mod.get() else 0
                            )
                            + int(
                                self.climb_train.get() if
                                self.climb_train.get() else 0
                            )
                            + int(
                                self.climb_focus.get() if
                                self.climb_focus.get() else 0
                            )
                            + int(
                                self.climb_misc.get()
                                if self.climb_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.climb_train.get() == "1"
                            or self.climb_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.climb_focus.get() == "1"
                            or self.climb_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.climb_misc.get(),
                    },
                    "Deception": {
                        "Stat": "Cha",
                        "Total": str(
                            int(
                                self.cha_mod.get() if
                                self.cha_mod.get() else 0
                            )
                            + int(
                                self.deception_train.get() if
                                self.deception_train.get() else 0
                            )
                            + int(
                                self.deception_focus.get() if
                                self.deception_focus.get() else 0
                            )
                            + int(
                                self.deception_misc.get()
                                if self.deception_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.deception_train.get() == "1"
                            or self.deception_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.deception_focus.get() == "1"
                            or self.deception_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.deception_misc.get(),
                    },
                    "Endurance": {
                        "Stat": "Con",
                        "Total": str(
                            int(
                                self.con_mod.get() if
                                self.con_mod.get() else 0
                            )
                            + int(
                                self.endurance_train.get() if
                                self.endurance_train.get() else 0
                            )
                            + int(
                                self.endurance_focus.get() if
                                self.endurance_focus.get() else 0
                            )
                            + int(
                                self.endurance_misc.get()
                                if self.endurance_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.endurance_train.get() == "1"
                            or self.endurance_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.endurance_focus.get() == "1"
                            or self.endurance_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.endurance_misc.get(),
                    },
                    "Gather Information": {
                        "Stat": "Cha",
                        "Total": str(
                            int(
                                self.cha_mod.get() if
                                self.cha_mod.get() else 0
                            )
                            + int(
                                self.get_info_train.get()
                                if self.get_info_train.get()
                                else 0
                            )
                            + int(
                                self.get_info_focus.get()
                                if self.get_info_focus.get()
                                else 0
                            )
                            + int(
                                self.get_info_misc.get()
                                if self.get_info_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.get_info_train.get() == "1"
                            or self.get_info_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.get_info_focus.get() == "1"
                            or self.get_info_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.get_info_misc.get(),
                    },
                    "Initiative": {
                        "Stat": "Dex",
                        "Total": str(
                            int(
                                self.dex_mod.get() if
                                self.dex_mod.get() else 0
                            )
                            + int(
                                self.initiative_train.get()
                                if self.initiative_train.get()
                                else 0
                            )
                            + int(
                                self.initiative_focus.get()
                                if self.initiative_focus.get()
                                else 0
                            )
                            + int(
                                self.initiative_misc.get()
                                if self.initiative_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.initiative_train.get() == "1"
                            or self.initiative_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.initiative_focus.get() == "1"
                            or self.initiative_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.initiative_misc.get(),
                    },
                    "Jump": {
                        "Stat": "Str",
                        "Total": str(
                            int(
                                self.str_mod.get() if
                                self.str_mod.get() else 0
                            )
                            + int(
                                self.jump_train.get() if
                                self.jump_train.get() else 0
                            )
                            + int(
                                self.jump_focus.get() if
                                self.jump_focus.get() else 0
                            )
                            + int(
                                self.jump_misc.get()
                                if self.jump_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.jump_train.get() == "1"
                            or self.jump_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.jump_focus.get() == "1"
                            or self.jump_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.jump_misc.get(),
                    },
                    "Knowledge": {
                        "Stat": "Int",
                        "Type": {
                            "Bureaucracy": {
                                "Total": str(
                                    int(
                                        self.int_mod.get()
                                        if self.int_mod.get()
                                        else 0
                                    )
                                    + int(
                                        self.know_bureau_train.get()
                                        if self.know_bureau_train.get()
                                        else 0
                                    )
                                    + int(
                                        self.know_bureau_focus.get()
                                        if self.know_bureau_focus.get()
                                        else 0
                                        )
                                    + int(
                                        self.know_bureau_misc.get()
                                        if self.know_bureau_misc.get()
                                        else 0
                                    )
                                ),
                                "Training": (
                                    5
                                    if self.know_bureau_train.get()
                                    == "1"
                                    or self.know_bureau_train.get()
                                    == "5"
                                    else 0
                                ),
                                "Focus": (
                                    5
                                    if self.know_bureau_focus.get()
                                    == "1"
                                    or self.know_bureau_focus.get()
                                    == "5"
                                    else 0
                                ),
                                "Misc": self.know_bureau_misc.get(),
                            },
                            "Galactic Lore": {
                                "Total": str(
                                    int(
                                        self.int_mod.get() if
                                        self.int_mod.get() else 0
                                    )
                                    + int(
                                        self.know_lore_train.get() if
                                        self.know_lore_train.get() 
                                        else 0
                                    )
                                    + int(
                                        self.know_lore_focus.get() if
                                        self.know_lore_focus.get() 
                                        else 0
                                    )
                                    + int(
                                        self.know_lore_misc.get()
                                        if self.know_lore_misc.get()
                                        else 0
                                    )
                                ),
                                "Training": (
                                    5
                                    if self.know_lore_train.get()
                                    == "1"
                                    or self.know_lore_train.get()
                                    == "5"
                                    else 0
                                ),
                                "Focus": (
                                    5
                                    if self.know_lore_focus.get()
                                    == "1"
                                    or self.know_lore_focus.get()
                                    == "5"
                                    else 0
                                ),
                                "Misc": self.know_lore_misc.get(),
                            },
                            "Life Science": {
                                "Total": str(
                                    int(
                                        self.int_mod.get() if
                                        self.int_mod.get() else 0
                                    )
                                    + int(
                                        self.know_life_train.get() if
                                        self.know_life_train.get()
                                        else 0
                                    )
                                    + int(
                                        self.know_life_focus.get() if
                                        self.know_life_focus.get()
                                        else 0
                                    )
                                    + int(
                                        self.know_life_misc.get()
                                        if self.know_life_misc.get()
                                        else 0
                                    )
                                ),
                                "Training": (
                                    5
                                    if self.know_life_train.get()
                                    == "1"
                                    or self.know_life_train.get()
                                    == "5"
                                    else 0
                                ),
                                "Focus": (
                                    5
                                    if self.know_life_focus.get()
                                    == "1"
                                    or self.know_life_focus.get()
                                    == "5"
                                    else 0
                                ),
                                "Misc": self.know_life_misc.get(),
                            },
                            "Physical Science": {
                                "Total": str(
                                    int(
                                        self.int_mod.get() if
                                        self.int_mod.get() else 0
                                    )
                                    + int(
                                        self.know_phys_train.get() if
                                        self.know_phys_train.get()
                                        else 0
                                    )
                                    + int(
                                        self.know_phys_focus.get() if
                                        self.know_phys_focus.get() else 0
                                    )
                                    + int(
                                        self.know_phys_misc.get()
                                        if self.know_phys_misc.get()
                                        else 0
                                    )
                                ),
                                "Training": (
                                    5
                                    if self.know_phys_train.get()
                                    == "1"
                                    or self.know_phys_train.get()
                                    == "5"
                                    else 0
                                ),
                                "Focus": (
                                    5
                                    if self.know_phys_focus.get()
                                    == "1"
                                    or self.know_phys_focus.get()
                                    == "5"
                                    else 0
                                ),
                                "Misc": self.know_phys_misc.get(),
                            },
                            "Social Science": {
                                "Total": str(
                                    int(
                                        self.int_mod.get() if
                                        self.int_mod.get() else 0
                                    )
                                    + int(
                                        self.know_soc_train.get() if
                                        self.know_soc_train.get()
                                        else 0
                                    )
                                    + int(
                                        self.know_soc_focus.get() if
                                        self.know_soc_focus.get()
                                        else 0
                                    )
                                    + int(
                                        self.know_soc_misc.get()
                                        if self.know_soc_misc.get()
                                        else 0
                                    )
                                ),
                                "Training": (
                                    5
                                    if self.know_soc_train.get()
                                    == "1"
                                    or self.know_soc_train.get()
                                    == "5"
                                    else 0
                                ),
                                "Focus": (
                                    5
                                    if self.know_soc_focus.get()
                                    == "1"
                                    or self.know_soc_focus.get()
                                    == "5"
                                    else 0
                                ),
                                "Misc": self.know_soc_misc.get(),
                            },
                            "Tactics": {
                                "Total": str(
                                    int(
                                        self.int_mod.get() if
                                        self.int_mod.get() else 0
                                    )
                                    + int(
                                        self.know_tac_train.get() if
                                        self.know_tac_train.get()
                                        else 0
                                    )
                                    + int(
                                        self.know_tac_focus.get() if
                                        self.know_tac_focus.get()
                                        else 0
                                    )
                                    + int(
                                        self.know_tac_misc.get()
                                        if self.know_tac_misc.get()
                                        else 0
                                    )
                                ),
                                "Training": (
                                    5
                                    if self.know_tac_train.get()
                                    == "1"
                                    or self.know_tac_train.get()
                                    == "5"
                                    else 0
                                ),
                                "Focus": (
                                    5
                                    if self.know_tac_focus.get() == "1"
                                    or self.know_tac_focus.get() == "5"
                                    else 0
                                ),
                                "Misc": self.know_tac_misc.get(),
                            },
                            "Technology": {
                                "Total": str(
                                    int(
                                        self.int_mod.get() if
                                        self.int_mod.get() else 0
                                    )
                                    + int(
                                        self.know_tech_train.get() if
                                        self.know_tech_train.get()
                                        else 0
                                    )
                                    + int(
                                        self.know_tech_focus.get() if
                                        self.know_tech_focus.get()
                                        else 0
                                    )
                                    + int(
                                        self.know_tech_misc.get()
                                        if self.know_tech_misc.get()
                                        else 0
                                    )
                                ),
                                "Training": (
                                    5
                                    if self.know_tech_train.get()
                                    == "1"
                                    or self.know_tech_train.get()
                                    == "5"
                                    else 0
                                ),
                                "Focus": (
                                    5
                                    if self.know_tech_focus.get()
                                    == "1"
                                    or self.know_tech_focus.get()
                                    == "5"
                                    else 0
                                ),
                                "Misc": self.know_tech_misc.get(),
                            },
                        },
                    },
                    "Mechanics": {
                        "Stat": "Int",
                        "Total": str(
                            int(
                                self.int_mod.get() if
                                self.int_mod.get() else 0
                            )
                            + int(
                                self.mechanics_train.get() if
                                self.mechanics_train.get() else 0
                            )
                            + int(
                                self.mechanics_focus.get() if
                                self.mechanics_focus.get() else 0
                            )
                            + int(
                                self.mechanics_misc.get()
                                if self.mechanics_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.mechanics_train.get() == "1"
                            or self.mechanics_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.mechanics_focus.get() == "1"
                            or self.mechanics_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.mechanics_misc.get(),
                    },
                    "Perception": {
                        "Stat": "Wis",
                        "Total": str(
                            int(
                                self.wis_mod.get() if
                                self.wis_mod.get() else 0
                            )
                            + int(
                                self.perception_train.get() if
                                self.perception_train.get() else 0
                            )
                            + int(
                                self.perception_focus.get() if
                                self.perception_focus.get() else 0
                            )
                            + int(
                                self.perception_misc.get()
                                if self.perception_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.perception_train.get() == "1"
                            or self.perception_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.perception_focus.get() == "1"
                            or self.perception_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.perception_misc.get(),
                    },
                    "Persuasion": {
                        "Stat": "Cha",
                        "Total": str(
                            int(
                                self.cha_mod.get() if
                                self.cha_mod.get() else 0
                            )
                            + int(
                                self.persuasion_train.get() if
                                self.persuasion_train.get() else 0
                            )
                            + int(
                                self.persuasion_focus.get() if
                                self.persuasion_focus.get() else 0
                            )
                            + int(
                                self.persuasion_misc.get()
                                if self.persuasion_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.persuasion_train.get() == "1"
                            or self.persuasion_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.persuasion_focus.get() == "1"
                            or self.persuasion_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.persuasion_misc.get(),
                    },
                    "Pilot": {
                        "Stat": "Dex",
                        "Total": str(
                            int(
                                self.dex_mod.get() if
                                self.dex_mod.get() else 0
                            )
                            + int(
                                self.pilot_train.get() if
                                self.pilot_train.get() else 0
                            )
                            + int(
                                self.pilot_focus.get() if
                                self.pilot_focus.get() else 0
                            )
                            + int(
                                self.pilot_misc.get()
                                if self.pilot_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.pilot_train.get() == "1"
                            or self.pilot_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.pilot_focus.get() == "1"
                            or self.pilot_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.pilot_misc.get(),
                    },
                    "Ride": {
                        "Stat": "Dex",
                        "Total": str(
                            int(
                                self.dex_mod.get() if
                                self.dex_mod.get() else 0
                            )
                            + int(
                                self.ride_train.get() if
                                self.ride_train.get() else 0
                            )
                            + int(
                                self.ride_focus.get() if
                                self.ride_focus.get() else 0
                            )
                            + int(
                                self.ride_misc.get()
                                if self.ride_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.ride_train.get() == "1"
                            or self.ride_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.ride_focus.get() == "1"
                            or self.ride_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.ride_misc.get(),
                    },
                    "Stealth": {
                        "Stat": "Dex",
                        "Total": str(
                            int(
                                self.dex_mod.get() if
                                self.dex_mod.get() else 0
                            )
                            + int(
                                self.stealth_train.get() if
                                self.stealth_train.get() else 0
                            )
                            + int(
                                self.stealth_focus.get() if
                                self.stealth_focus.get() else 0
                            )
                            + int(
                                self.stealth_misc.get()
                                if self.stealth_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.stealth_train.get() == "1"
                            or self.stealth_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.stealth_focus.get() == "1"
                            or self.stealth_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.stealth_misc.get(),
                    },
                    "Survival": {
                        "Stat": "Wis",
                        "Total": str(
                            int(
                                self.wis_mod.get() if
                                self.wis_mod.get() else 0
                            )
                            + int(
                                self.survival_train.get() if
                                self.survival_train.get() else 0
                            )
                            + int(
                                self.survival_focus.get() if
                                self.survival_focus.get() else 0
                            )
                            + int(
                                self.survival_misc.get()
                                if self.survival_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.survival_train.get() == "1"
                            or self.survival_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.survival_focus.get() == "1"
                            or self.survival_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.survival_misc.get(),
                    },
                    "Swim": {
                        "Stat": "Str",
                        "Total": str(
                            int(
                                self.str_mod.get() if
                                self.str_mod.get() else 0
                            )
                            + int(
                                self.swim_train.get() if
                                self.swim_train.get() else 0
                            )
                            + int(
                                self.swim_focus.get() if
                                self.swim_focus.get() else 0
                            )
                            + int(
                                self.swim_misc.get()
                                if self.swim_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.swim_train.get() == "1"
                            or self.swim_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.swim_focus.get() == "1"
                            or self.swim_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.swim_misc.get(),
                    },
                    "Treat Injury": {
                        "Stat": "Int",
                        "Total": str(
                            int(
                                self.int_mod.get() if
                                self.int_mod.get() else 0
                            )
                            + int(
                                self.injury_train.get()
                                if self.injury_train.get()
                                else 0
                            )
                            + int(
                                self.injury_focus.get()
                                if self.injury_focus.get()
                                else 0
                            )
                            + int(
                                self.injury_misc.get()
                                if self.injury_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.injury_train.get() == "1"
                            or self.injury_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.injury_focus.get() == "1"
                            or self.injury_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.injury_misc.get(),
                    },
                    "Use Computer": {
                        "Stat": "Int",
                        "Total": str(
                            int(
                                self.int_mod.get() if
                                self.int_mod.get() else 0
                            )
                            + int(
                                self.computer_train.get()
                                if self.computer_train.get()
                                else 0
                            )
                            + int(
                                self.computer_focus.get() if
                                self.computer_focus.get() else 0
                            )
                            + int(
                                self.computer_misc.get()
                                if self.computer_misc.get()
                                else 0
                            )
                        ),
                        "Training": (
                            5
                            if self.computer_train.get() == "1"
                            or self.computer_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.computer_focus.get() == "1"
                            or self.computer_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.computer_misc.get(),
                    },
                    "Use the Force": {
                        "Stat": "Cha/Will",
                        "Total": (
                            str(
                                int(
                                    self.use_force_train.get() if
                                    self.use_force_train.get() else 0
                                )
                                + int(
                                    self.use_force_focus.get() if
                                    self.use_force_focus.get() else 0
                                )
                                + int(
                                    self.use_force_misc.get()
                                    if self.use_force_misc.get()
                                    else 0
                                )
                                + int(
                                    int(
                                        self.cha_mod.get() if
                                        self.cha_mod.get() else 0
                                    )
                                    if int(
                                        self.cha_mod.get() if
                                        self.cha_mod.get() else 0
                                    )
                                    > int(
                                        self.will_mod.get() if
                                        self.will_mod.get() else 0
                                    )
                                    else int(
                                        self.will_mod.get() if
                                        self.will_mod.get() else 0
                                    )
                                )
                            )
                        ),
                        "Training": (
                            5
                            if self.use_force_train.get() == "1"
                            or self.use_force_train.get() == "5"
                            else 0
                        ),
                        "Focus": (
                            5
                            if self.use_force_focus.get() == "1"
                            or self.use_force_focus.get() == "5"
                            else 0
                        ),
                        "Misc": self.use_force_misc.get(),
                    },
                },
                "Force Schools": {
                    "Force School": {
                        "Alchemy": {
                            "Total": self.alchemy_modifier.get(),
                            "Training 1": self.alchemy_1.get(),
                            "Training 2": self.alchemy_2.get(),
                            "Training 3": self.alchemy_3.get(),
                        },
                        "Augmentation": {
                            "Total": self.augmentation_modifier.get(),
                            "Training 1": self.augmentation_1.get(),
                            "Training 2": self.augmentation_2.get(),
                            "Training 3": self.augmentation_3.get(),
                        },
                        "Cognition": {
                            "Total": self.cognition_modifier.get(),
                            "Training 1": self.cognition_1.get(),
                            "Training 2": self.cognition_2.get(),
                            "Training 3": self.cognition_3.get(),
                        },
                        "Sorcery": {
                            "Total": self.sorcery_modifier.get(),
                            "Training 1": self.sorcery_1.get(),
                            "Training 2": self.sorcery_2.get(),
                            "Training 3": self.sorcery_3.get(),
                        },
                        "Technokinesis": {
                            "Total": self.techno_modifier.get(),
                            "Training 1": self.techno_1.get(),
                            "Training 2": self.techno_2.get(),
                            "Training 3": self.techno_3.get(),
                        },
                        "Telekinesis": {
                            "Total": self.tele_modifier.get(),
                            "Training 1": self.tele_1.get(),
                            "Training 2": self.tele_2.get(),
                            "Training 3": self.tele_3.get(),
                        },
                        "Vitalism": {
                            "Total": self.vitalism_modifier.get(),
                            "Training 1": self.vitalism_1.get(),
                            "Training 2": self.vitalism_2.get(),
                            "Training 3": self.vitalism_3.get(),
                        },
                    },
                    "Force Uses": self.force_uses.get(),
                },
                "Force Techniques": {
                    "Force Technique 1": self.force_tech_1.get(),
                    "Force Technique 2": self.force_tech_2.get(),
                    "Force Technique 3": self.force_tech_3.get(),
                    "Force Technique 4": self.force_tech_4.get(),
                    "Force Technique 5": self.force_tech_5.get(),
                    "Force Technique 6": self.force_tech_6.get(),
                    "Force Technique 7": self.force_tech_7.get(),
                    "Force Technique 8": self.force_tech_8.get(),
                    "Force Technique 9": self.force_tech_9.get(),
                    "Force Technique 10": self.force_tech_10.get(),
                    "Force Technique 11": self.force_tech_11.get(),
                    "Force Technique 12": self.force_tech_12.get(),
                    "Force Technique 13": self.force_tech_13.get(),
                    "Force Technique 14": self.force_tech_14.get(),
                    "Force Technique 15": self.force_tech_15.get(),
                },
                "Force Secrets": {
                    "Force Secret 1": self.force_secret_1.get(),
                    "Force Secret 2": self.force_secret_2.get(),
                    "Force Secret 3": self.force_secret_3.get(),
                    "Force Secret 4": self.force_secret_4.get(),
                    "Force Secret 5": self.force_secret_5.get(),
                    "Force Secret 6": self.force_secret_6.get(),
                    "Force Secret 7": self.force_secret_7.get(),
                    "Force Secret 8": self.force_secret_8.get(),
                    "Force Secret 9": self.force_secret_9.get(),
                    "Force Secret 10": self.force_secret_10.get(),
                    "Force Secret 11": self.force_secret_11.get(),
                    "Force Secret 12": self.force_secret_12.get(),
                    "Force Secret 13": self.force_secret_13.get(),
                    "Force Secret 14": self.force_secret_14.get(),
                    "Force Secret 15": self.force_secret_15.get(),
                },
                "Feats": {
                    "Feat 1": self.feats_1.get(),
                    "Feat 2": self.feats_2.get(),
                    "Feat 3": self.feats_3.get(),
                    "Feat 4": self.feats_4.get(),
                    "Feat 5": self.feats_5.get(),
                    "Feat 6": self.feats_6.get(),
                    "Feat 7": self.feats_7.get(),
                    "Feat 8": self.feats_8.get(),
                    "Feat 9": self.feats_9.get(),
                    "Feat 10": self.feats_10.get(),
                    "Feat 11": self.feats_11.get(),
                    "Feat 12": self.feats_12.get(),
                    "Feat 13": self.feats_13.get(),
                    "Feat 14": self.feats_14.get(),
                    "Feat 15": self.feats_15.get(),
                },
                "Talents": {
                    "Talent 1": self.talents_1.get(),
                    "Talent 2": self.talents_2.get(),
                    "Talent 3": self.talents_3.get(),
                    "Talent 4": self.talents_4.get(),
                    "Talent 5": self.talents_5.get(),
                    "Talent 6": self.talents_6.get(),
                    "Talent 7": self.talents_7.get(),
                    "Talent 8": self.talents_8.get(),
                    "Talent 9": self.talents_9.get(),
                    "Talent 10": self.talents_10.get(),
                    "Talent 11": self.talents_11.get(),
                    "Talent 12": self.talents_12.get(),
                    "Talent 13": self.talents_13.get(),
                    "Talent 14": self.talents_14.get(),
                    "Talent 15": self.talents_15.get(),
                },
                "Equipment": {
                    "Equipment 1": self.equipment_1.get(),
                    "Equipment 2": self.equipment_2.get(),
                    "Equipment 3": self.equipment_3.get(),
                    "Equipment 4": self.equipment_4.get(),
                    "Equipment 5": self.equipment_5.get(),
                    "Equipment 6": self.equipment_6.get(),
                    "Equipment 7": self.equipment_7.get(),
                    "Equipment 8": self.equipment_8.get(),
                    "Equipment 9": self.equipment_9.get(),
                    "Equipment 10": self.equipment_10.get(),
                    "Equipment 11": self.equipment_11.get(),
                    "Equipment 12": self.equipment_12.get(),
                    "Equipment 13": self.equipment_13.get(),
                    "Equipment 14": self.equipment_14.get(),
                    "Equipment 15": self.equipment_15.get(),
                    "Equipment 16": self.equipment_16.get(),
                    "Equipment 17": self.equipment_17.get(),
                    "Equipment 18": self.equipment_18.get(),
                    "Equipment 19": self.equipment_19.get(),
                    "Equipment 20": self.equipment_20.get(),
                    "Equipment 21": self.equipment_21.get(),
                    "Equipment 22": self.equipment_22.get(),
                    "Equipment 23": self.equipment_23.get(),
                    "Equipment 24": self.equipment_24.get(),
                    "Equipment 25": self.equipment_25.get(),
                    "Equipment 26": self.equipment_26.get(),
                    "Equipment 27": self.equipment_27.get(),
                    "Equipment 28": self.equipment_28.get(),
                    "Equipment 29": self.equipment_29.get(),
                    "Equipment 30": self.equipment_30.get(),
                    "Equipment 31": self.equipment_31.get(),
                    "Equipment 32": self.equipment_32.get(),
                },
            }

            # Write the data to a JSON file
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
            messagebox.showinfo("Export Successful", f"Data exported to {file_path}")

    def import_from_json(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "r") as file:
                data = json.load(file)

            # Populate the fields in the Tkinter interface
            self.name.delete(0, tk.END)
            self.name.insert(0, data["Info"]["Character Name"])

            self.level.delete(0, tk.END)
            self.level.insert(0, data["Info"]["Character Level"])

            self.classes.delete(0, tk.END)
            self.classes.insert(0, data["Info"]["Classes"])

            self.destiny.delete(0, tk.END)
            self.destiny.insert(0, data["Info"]["Destiny"])

            self.credits.delete(0, tk.END)
            self.credits.insert(0, data["Info"]["Credits"])

            self.species.delete(0, tk.END)
            self.species.insert(0, data["Info"]["Species"])

            self.age.delete(0, tk.END)
            self.age.insert(0, data["Info"]["Age"])

            self.height.delete(0, tk.END)
            self.height.insert(0, data["Info"]["Height"])

            self.weight.delete(0, tk.END)
            self.weight.insert(0, data["Info"]["Weight"])

            self.gender.delete(0, tk.END)
            self.gender.insert(0, data["Info"]["Gender"])

            self.species_info.delete(0, tk.END)
            self.species_info.insert(0, data["Info"]["Species Info"])

            self.force_points.delete(0, tk.END)
            self.force_points.insert(0, data["Info"]["Force Points"])

            self.base_attack.delete(0, tk.END)
            self.base_attack.insert(0, data["Info"]["Base Attack Bonus"])

            self.speed.delete(0, tk.END)
            self.speed.insert(0, data["Info"]["Speed"])

            self.dest_point.delete(0, tk.END)
            self.dest_point.insert(0, data["Info"]["Destiny Points"])

            self.dam_red.delete(0, tk.END)
            self.dam_red.insert(0, data["Info"]["Damage Reduction"])

            # Languages
            for i in range(10):
                language_key = f"Language {i+1}"
                entry = getattr(self, f"language_{i+1}")
                entry.delete(0, tk.END)
                entry.insert(0, data["Languages"][language_key])

            # Stats
            self.str_score.delete(0, tk.END)
            self.str_score.insert(0, data["Stats"]["Strength"]["Score"])

            self.str_mod.delete(0, tk.END)
            self.str_mod.insert(0, data["Stats"]["Strength"]["Mod"])

            self.dex_score.delete(0, tk.END)
            self.dex_score.insert(0, data["Stats"]["Dexterity"]["Score"])

            self.dex_mod.delete(0, tk.END)
            self.dex_mod.insert(0, data["Stats"]["Dexterity"]["Mod"])

            self.con_score.delete(0, tk.END)
            self.con_score.insert(
                0, data["Stats"]["Constitution"]["Score"]
            )

            self.con_mod.delete(0, tk.END)
            self.con_mod.insert(0, data["Stats"]["Constitution"]["Mod"])

            self.int_score.delete(0, tk.END)
            self.int_score.insert(
                0, data["Stats"]["Intelligence"]["Score"]
            )

            self.int_mod.delete(0, tk.END)
            self.int_mod.insert(0, data["Stats"]["Intelligence"]["Mod"])

            self.wis_score.delete(0, tk.END)
            self.wis_score.insert(0, data["Stats"]["Wisdom"]["Score"])

            self.wis_mod.delete(0, tk.END)
            self.wis_mod.insert(0, data["Stats"]["Wisdom"]["Mod"])

            self.cha_score.delete(0, tk.END)
            self.cha_score.insert(0, data["Stats"]["Charisma"]["Score"])

            self.cha_mod.delete(0, tk.END)
            self.cha_mod.insert(0, data["Stats"]["Charisma"]["Mod"])

            self.will_score.delete(0, tk.END)
            self.will_score.insert(0, data["Stats"]["Willpower"]["Score"])

            self.will_mod.delete(0, tk.END)
            self.will_mod.insert(0, data["Stats"]["Willpower"]["Mod"])

            if "Dark Side" in data["Stats"].keys():
                self.dark_score.delete(0, tk.END)
                self.dark_score.insert(0, data["Stats"]["Dark Side"]["Score"])

                self.dark_mod.delete(0, tk.END)
                self.dark_mod.insert(0, data["Stats"]["Dark Side"]["Mod"])

            # Defenses
            self.fortitude_1.delete(0, tk.END)
            self.fortitude_1.insert(0, data["Defenses"]["Fortitude"]["Total"])

            self.fortitude_2.delete(0, tk.END)
            self.fortitude_2.insert(
                0, data["Defenses"]["Fortitude"]["Class Bonus"]
            )

            self.fortitude_3.delete(0, tk.END)
            self.fortitude_3.insert(
                0, data["Defenses"]["Fortitude"]["Stat Bonus"]
            )

            self.fortitude_4.delete(0, tk.END)
            self.fortitude_4.insert(
                0, data["Defenses"]["Fortitude"]["Armor Bonus"]
            )

            self.fortitude_5.delete(0, tk.END)
            self.fortitude_5.insert(0, data["Defenses"]["Fortitude"]["Misc"])

            self.reflex_1.delete(0, tk.END)
            self.reflex_1.insert(0, data["Defenses"]["Reflex"]["Total"])

            self.reflex_2.delete(0, tk.END)
            self.reflex_2.insert(0, data["Defenses"]["Reflex"]["Class Bonus"])

            self.reflex_3.delete(0, tk.END)
            self.reflex_3.insert(0, data["Defenses"]["Reflex"]["Stat Bonus"])

            self.reflex_4.delete(0, tk.END)
            self.reflex_4.insert(0, data["Defenses"]["Reflex"]["Armor Bonus"])

            self.reflex_5.delete(0, tk.END)
            self.reflex_5.insert(0, data["Defenses"]["Reflex"]["Misc"])

            self.will_1.delete(0, tk.END)
            self.will_1.insert(0, data["Defenses"]["Will"]["Total"])

            self.will_2.delete(0, tk.END)
            self.will_2.insert(0, data["Defenses"]["Will"]["Class Bonus"])

            self.will_3.delete(0, tk.END)
            self.will_3.insert(0, data["Defenses"]["Will"]["Stat Bonus"])

            self.will_4.delete(0, tk.END)
            self.will_4.insert(0, data["Defenses"]["Will"]["Armor Bonus"])

            self.will_5.delete(0, tk.END)
            self.will_5.insert(0, data["Defenses"]["Will"]["Misc"])

            # Damage Thresholds
            if "Fortitude" in data["Damage Thresholds"].keys():
                self.fortitude.delete(0, tk.END)
                self.fortitude.insert(0, data["Damage Thresholds"]["Fortitude"])

            if "Total" in data["Damage Thresholds"]["Torso"].keys():
                self.torso.delete(0, tk.END)
                self.torso.insert(0, data["Damage Thresholds"]["Torso"]["Total"])

            if "Misc" in data["Damage Thresholds"]["Torso"].keys():
                self.torso_misc.delete(0, tk.END)
                self.torso_misc.insert(
                    0, data["Damage Thresholds"]["Torso"]["Misc"]
                )

            if "Total" in data["Damage Thresholds"]["Head"].keys():
                self.head.delete(0, tk.END)
                self.head.insert(0, data["Damage Thresholds"]["Head"]["Total"])

            if "Misc" in data["Damage Thresholds"]["Head"].keys():
                self.head_misc.delete(0, tk.END)
                self.head_misc.insert(
                    0, data["Damage Thresholds"]["Head"]["Misc"]
                )

            if "Total" in data["Damage Thresholds"]["Limbs"].keys():
                self.limbs.delete(0, tk.END)
                self.limbs.insert(0, data["Damage Thresholds"]["Limbs"]["Total"])

            if "Misc" in data["Damage Thresholds"]["Limbs"].keys():
                self.limbs_misc.delete(0, tk.END)
                self.limbs_misc.insert(
                    0, data["Damage Thresholds"]["Limbs"]["Misc"]
                )

            # Armor
            self.armor.delete(0, tk.END)
            self.armor.insert(0, data["Armor"]["Armor Name"])

            self.fort_bonus.delete(0, tk.END)
            self.fort_bonus.insert(0, data["Armor"]["Fortitude Bonus"])

            self.reflex_bonus.delete(0, tk.END)
            self.reflex_bonus.insert(0, data["Armor"]["Reflex Bonus"])

            self.max_dex_bonus.delete(0, tk.END)
            self.max_dex_bonus.insert(0, data["Armor"]["Max Dex Bonus"])

            self.affects.delete(0, tk.END)
            self.affects.insert(0, data["Armor"]["Additional Affects"])

            # Weapons
            self.weapon_1.delete(0, tk.END)
            self.weapon_1.insert(0, data["Weapons"]["Weapon 1"]["Weapon Name"])

            self.hit_mod_1.delete(0, tk.END)
            self.hit_mod_1.insert(0, data["Weapons"]["Weapon 1"]["Hit Mod"])

            self.damage_1.delete(0, tk.END)
            self.damage_1.insert(0, data["Weapons"]["Weapon 1"]["Damage"])

            self.range_1.delete(0, tk.END)
            self.range_1.insert(0, data["Weapons"]["Weapon 1"]["Range"])

            self.crit_range_1.delete(0, tk.END)
            self.crit_range_1.insert(0, data["Weapons"]["Weapon 1"]["Crit Range"])

            self.weapon_2.delete(0, tk.END)
            self.weapon_2.insert(0, data["Weapons"]["Weapon 2"]["Weapon Name"])

            self.hit_mod_2.delete(0, tk.END)
            self.hit_mod_2.insert(0, data["Weapons"]["Weapon 2"]["Hit Mod"])

            self.damage_2.delete(0, tk.END)
            self.damage_2.insert(0, data["Weapons"]["Weapon 2"]["Damage"])

            self.range_2.delete(0, tk.END)
            self.range_2.insert(0, data["Weapons"]["Weapon 2"]["Range"])

            self.crit_range_2.delete(0, tk.END)
            self.crit_range_2.insert(0, data["Weapons"]["Weapon 2"]["Crit Range"])

            self.weapon_3.delete(0, tk.END)
            self.weapon_3.insert(0, data["Weapons"]["Weapon 3"]["Weapon Name"])

            self.hit_mod_3.delete(0, tk.END)
            self.hit_mod_3.insert(0, data["Weapons"]["Weapon 3"]["Hit Mod"])

            self.damage_3.delete(0, tk.END)
            self.damage_3.insert(0, data["Weapons"]["Weapon 3"]["Damage"])

            self.range_3.delete(0, tk.END)
            self.range_3.insert(0, data["Weapons"]["Weapon 3"]["Range"])

            self.crit_range_3.delete(0, tk.END)
            self.crit_range_3.insert(0, data["Weapons"]["Weapon 3"]["Crit Range"])

            self.weapon_4.delete(0, tk.END)
            self.weapon_4.insert(0, data["Weapons"]["Weapon 4"]["Weapon Name"])

            self.hit_mod_4.delete(0, tk.END)
            self.hit_mod_4.insert(0, data["Weapons"]["Weapon 4"]["Hit Mod"])

            self.damage_4.delete(0, tk.END)
            self.damage_4.insert(0, data["Weapons"]["Weapon 4"]["Damage"])

            self.range_4.delete(0, tk.END)
            self.range_4.insert(0, data["Weapons"]["Weapon 4"]["Range"])

            self.crit_range_4.delete(0, tk.END)
            self.crit_range_4.insert(0, data["Weapons"]["Weapon 4"]["Crit Range"])

            self.weapon_5.delete(0, tk.END)
            self.weapon_5.insert(0, data["Weapons"]["Weapon 5"]["Weapon Name"])

            self.hit_mod_5.delete(0, tk.END)
            self.hit_mod_5.insert(0, data["Weapons"]["Weapon 5"]["Hit Mod"])

            self.damage_5.delete(0, tk.END)
            self.damage_5.insert(0, data["Weapons"]["Weapon 5"]["Damage"])

            self.range_5.delete(0, tk.END)
            self.range_5.insert(0, data["Weapons"]["Weapon 5"]["Range"])

            self.crit_range_5.delete(0, tk.END)
            self.crit_range_5.insert(0, data["Weapons"]["Weapon 5"]["Crit Range"])

            # Skills
            self.acro_train.delete(0, tk.END)
            self.acro_train.insert(0, data["Skills"]["Acrobatics"]["Training"])

            self.acro_focus.delete(0, tk.END)
            self.acro_focus.insert(0, data["Skills"]["Acrobatics"]["Focus"])

            if "Misc" in data["Skills"]["Acrobatics"].keys():
                self.acro_misc.delete(0, tk.END)
                self.acro_misc.insert(0, data["Skills"]["Acrobatics"]["Misc"])

            self.acro_modifier.delete(0, tk.END)
            self.acro_modifier.insert(0, data["Skills"]["Acrobatics"]["Total"])

            self.climb_train.delete(0, tk.END)
            self.climb_train.insert(0, data["Skills"]["Climb"]["Training"])

            self.climb_focus.delete(0, tk.END)
            self.climb_focus.insert(0, data["Skills"]["Climb"]["Focus"])

            if "Misc" in data["Skills"]["Climb"].keys():
                self.climb_misc.delete(0, tk.END)
                self.climb_misc.insert(0, data["Skills"]["Climb"]["Misc"])

            self.climb_modifier.delete(0, tk.END)
            self.climb_modifier.insert(0, data["Skills"]["Climb"]["Total"])

            self.deception_train.delete(0, tk.END)
            self.deception_train.insert(
                0, data["Skills"]["Deception"]["Training"]
            )

            self.deception_focus.delete(0, tk.END)
            self.deception_focus.insert(0, data["Skills"]["Deception"]["Focus"])

            if "Misc" in data["Skills"]["Deception"].keys():
                self.deception_misc.delete(0, tk.END)
                self.deception_misc.insert(0, data["Skills"]["Deception"]["Misc"])

            self.deception_modifier.delete(0, tk.END)
            self.deception_modifier.insert(
                0, data["Skills"]["Deception"]["Total"]
            )

            self.endurance_train.delete(0, tk.END)
            self.endurance_train.insert(
                0, data["Skills"]["Endurance"]["Training"]
            )

            self.endurance_focus.delete(0, tk.END)
            self.endurance_focus.insert(0, data["Skills"]["Endurance"]["Focus"])

            if "Misc" in data["Skills"]["Endurance"].keys():
                self.endurance_misc.delete(0, tk.END)
                self.endurance_misc.insert(0, data["Skills"]["Endurance"]["Misc"])

            self.endurance_modifier.delete(0, tk.END)
            self.endurance_modifier.insert(
                0, data["Skills"]["Endurance"]["Total"]
            )

            self.get_info_train.delete(0, tk.END)
            self.get_info_train.insert(
                0, data["Skills"]["Gather Information"]["Training"]
            )

            self.get_info_focus.delete(0, tk.END)
            self.get_info_focus.insert(
                0, data["Skills"]["Gather Information"]["Focus"]
            )

            if "Misc" in data["Skills"]["Gather Information"].keys():
                self.get_info_misc.delete(0, tk.END)
                self.get_info_misc.insert(
                    0, data["Skills"]["Gather Information"]["Misc"]
                )

            self.get_info_modifier.delete(0, tk.END)
            self.get_info_modifier.insert(
                0, data["Skills"]["Gather Information"]["Total"]
            )

            self.initiative_train.delete(0, tk.END)
            self.initiative_train.insert(
                0, data["Skills"]["Initiative"]["Training"]
            )

            self.initiative_focus.delete(0, tk.END)
            self.initiative_focus.insert(0, data["Skills"]["Initiative"]["Focus"])

            if "Misc" in data["Skills"]["Initiative"].keys():
                self.initiative_misc.delete(0, tk.END)
                self.initiative_misc.insert(
                    0, data["Skills"]["Initiative"]["Misc"]
                )

            self.initiative_modifier.delete(0, tk.END)
            self.initiative_modifier.insert(
                0, data["Skills"]["Initiative"]["Total"]
            )

            self.jump_train.delete(0, tk.END)
            self.jump_train.insert(0, data["Skills"]["Jump"]["Training"])

            self.jump_focus.delete(0, tk.END)
            self.jump_focus.insert(0, data["Skills"]["Jump"]["Focus"])

            if "Misc" in data["Skills"]["Jump"].keys():
                self.jump_misc.delete(0, tk.END)
                self.jump_misc.insert(0, data["Skills"]["Jump"]["Misc"])

            self.jump_modifier.delete(0, tk.END)
            self.jump_modifier.insert(0, data["Skills"]["Jump"]["Total"])

            self.know_bureau_train.delete(0, tk.END)
            self.know_bureau_train.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Bureaucracy"]["Training"]
            )

            self.know_bureau_focus.delete(0, tk.END)
            self.know_bureau_focus.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Bureaucracy"]["Focus"]
            )

            if "Misc" in data["Skills"]["Knowledge"]["Type"]["Bureaucracy"].keys():
                self.know_bureau_misc.delete(0, tk.END)
                self.know_bureau_misc.insert(
                    0, data["Skills"]["Knowledge"]["Type"]["Bureaucracy"]["Misc"]
                )

            self.know_bureau_modifier.delete(0, tk.END)
            self.know_bureau_modifier.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Bureaucracy"]["Total"]
            )

            self.know_lore_train.delete(0, tk.END)
            self.know_lore_train.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Galactic Lore"]["Training"]
            )

            self.know_lore_focus.delete(0, tk.END)
            self.know_lore_focus.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Galactic Lore"]["Focus"]
            )

            if "Misc" in data["Skills"]["Knowledge"]["Type"]["Galactic Lore"].keys():
                self.know_lore_misc.delete(0, tk.END)
                self.know_lore_misc.insert(
                    0, data["Skills"]["Knowledge"]["Type"]["Galactic Lore"]["Misc"]
                )

            self.know_lore_modifier.delete(0, tk.END)
            self.know_lore_modifier.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Galactic Lore"]["Total"]
            )

            self.know_life_train.delete(0, tk.END)
            self.know_life_train.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Life Science"]["Training"]
            )

            self.know_life_focus.delete(0, tk.END)
            self.know_life_focus.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Life Science"]["Focus"]
            )

            if "Misc" in data["Skills"]["Knowledge"]["Type"]["Life Science"].keys():
                self.know_life_misc.delete(0, tk.END)
                self.know_life_misc.insert(
                    0, data["Skills"]["Knowledge"]["Type"]["Life Science"]["Misc"]
                )

            self.know_life_modifier.delete(0, tk.END)
            self.know_life_modifier.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Life Science"]["Total"]
            )

            self.know_phys_train.delete(0, tk.END)
            self.know_phys_train.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Physical Science"]["Training"]
            )

            self.know_phys_focus.delete(0, tk.END)
            self.know_phys_focus.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Physical Science"]["Focus"]
            )

            if "Misc" in data["Skills"]["Knowledge"]["Type"]["Physical Science"].keys():
                self.know_phys_misc.delete(0, tk.END)
                self.know_phys_misc.insert(
                    0, data["Skills"]["Knowledge"]["Type"]["Physical Science"]["Misc"]
                )

            self.know_phys_modifier.delete(0, tk.END)
            self.know_phys_modifier.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Physical Science"]["Total"]
            )

            self.know_soc_train.delete(0, tk.END)
            self.know_soc_train.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Social Science"]["Training"]
            )

            self.know_soc_focus.delete(0, tk.END)
            self.know_soc_focus.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Social Science"]["Focus"]
            )

            if "Misc" in data["Skills"]["Knowledge"]["Type"]["Social Science"].keys():
                self.know_soc_misc.delete(0, tk.END)
                self.know_soc_misc.insert(
                    0, data["Skills"]["Knowledge"]["Type"]["Social Science"]["Misc"]
                )

            self.know_soc_modifier.delete(0, tk.END)
            self.know_soc_modifier.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Social Science"]["Total"]
            )

            self.know_tac_train.delete(0, tk.END)
            self.know_tac_train.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Tactics"]["Training"]
            )

            self.know_tac_focus.delete(0, tk.END)
            self.know_tac_focus.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Tactics"]["Focus"]
            )

            if "Misc" in data["Skills"]["Knowledge"]["Type"]["Tactics"].keys():
                self.know_tac_misc.delete(0, tk.END)
                self.know_tac_misc.insert(
                    0, data["Skills"]["Knowledge"]["Type"]["Tactics"]["Misc"]
                )

            self.know_tac_modifier.delete(0, tk.END)
            self.know_tac_modifier.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Tactics"]["Total"]
            )

            self.know_tech_train.delete(0, tk.END)
            self.know_tech_train.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Technology"]["Training"]
            )

            self.know_tech_focus.delete(0, tk.END)
            self.know_tech_focus.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Technology"]["Focus"]
            )

            if "Misc" in data["Skills"]["Knowledge"]["Type"]["Technology"].keys():
                self.know_tech_misc.delete(0, tk.END)
                self.know_tech_misc.insert(
                    0, data["Skills"]["Knowledge"]["Type"]["Technology"]["Misc"]
                )

            self.know_tech_modifier.delete(0, tk.END)
            self.know_tech_modifier.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Technology"]["Total"]
            )

            self.mechanics_train.delete(0, tk.END)
            self.mechanics_train.insert(
                0, data["Skills"]["Mechanics"]["Training"]
            )

            self.mechanics_focus.delete(0, tk.END)
            self.mechanics_focus.insert(0, data["Skills"]["Mechanics"]["Focus"])

            if "Misc" in data["Skills"]["Mechanics"].keys():
                self.mechanics_misc.delete(0, tk.END)
                self.mechanics_misc.insert(0, data["Skills"]["Mechanics"]["Misc"])

            self.mechanics_modifier.delete(0, tk.END)
            self.mechanics_modifier.insert(
                0, data["Skills"]["Mechanics"]["Total"]
            )

            self.perception_train.delete(0, tk.END)
            self.perception_train.insert(
                0, data["Skills"]["Perception"]["Training"]
            )

            self.perception_focus.delete(0, tk.END)
            self.perception_focus.insert(0, data["Skills"]["Perception"]["Focus"])

            if "Misc" in data["Skills"]["Perception"].keys():
                self.perception_misc.delete(0, tk.END)
                self.perception_misc.insert(
                    0, data["Skills"]["Perception"]["Misc"]
                )

            self.perception_modifier.delete(0, tk.END)
            self.perception_modifier.insert(
                0, data["Skills"]["Perception"]["Total"]
            )

            self.persuasion_train.delete(0, tk.END)
            self.persuasion_train.insert(
                0, data["Skills"]["Persuasion"]["Training"]
            )

            self.persuasion_focus.delete(0, tk.END)
            self.persuasion_focus.insert(0, data["Skills"]["Persuasion"]["Focus"])

            if "Misc" in data["Skills"]["Persuasion"].keys():
                self.persuasion_misc.delete(0, tk.END)
                self.persuasion_misc.insert(
                    0, data["Skills"]["Persuasion"]["Misc"]
                )

            self.persuasion_modifier.delete(0, tk.END)
            self.persuasion_modifier.insert(
                0, data["Skills"]["Persuasion"]["Total"]
            )

            self.pilot_train.delete(0, tk.END)
            self.pilot_train.insert(0, data["Skills"]["Pilot"]["Training"])

            self.pilot_focus.delete(0, tk.END)
            self.pilot_focus.insert(0, data["Skills"]["Pilot"]["Focus"])

            if "Misc" in data["Skills"]["Pilot"].keys():
                self.pilot_misc.delete(0, tk.END)
                self.pilot_misc.insert(0, data["Skills"]["Pilot"]["Misc"])

            self.pilot_modifier.delete(0, tk.END)
            self.pilot_modifier.insert(0, data["Skills"]["Pilot"]["Total"])

            self.ride_train.delete(0, tk.END)
            self.ride_train.insert(0, data["Skills"]["Ride"]["Training"])

            self.ride_focus.delete(0, tk.END)
            self.ride_focus.insert(0, data["Skills"]["Ride"]["Focus"])

            if "Misc" in data["Skills"]["Ride"].keys():
                self.ride_misc.delete(0, tk.END)
                self.ride_misc.insert(0, data["Skills"]["Ride"]["Misc"])

            self.ride_modifier.delete(0, tk.END)
            self.ride_modifier.insert(0, data["Skills"]["Ride"]["Total"])

            self.stealth_train.delete(0, tk.END)
            self.stealth_train.insert(0, data["Skills"]["Stealth"]["Training"])

            self.stealth_focus.delete(0, tk.END)
            self.stealth_focus.insert(0, data["Skills"]["Stealth"]["Focus"])

            if "Misc" in data["Skills"]["Stealth"].keys():
                self.stealth_misc.delete(0, tk.END)
                self.stealth_misc.insert(0, data["Skills"]["Stealth"]["Misc"])

            self.stealth_modifier.delete(0, tk.END)
            self.stealth_modifier.insert(0, data["Skills"]["Stealth"]["Total"])

            self.survival_train.delete(0, tk.END)
            self.survival_train.insert(
                0, data["Skills"]["Survival"]["Training"]
            )

            self.survival_focus.delete(0, tk.END)
            self.survival_focus.insert(0, data["Skills"]["Survival"]["Focus"])

            if "Misc" in data["Skills"]["Survival"].keys():
                self.survival_misc.delete(0, tk.END)
                self.survival_misc.insert(0, data["Skills"]["Survival"]["Misc"])

            self.survival_modifier.delete(0, tk.END)
            self.survival_modifier.insert(0, data["Skills"]["Survival"]["Total"])

            self.swim_train.delete(0, tk.END)
            self.swim_train.insert(0, data["Skills"]["Swim"]["Training"])

            self.swim_focus.delete(0, tk.END)
            self.swim_focus.insert(0, data["Skills"]["Swim"]["Focus"])

            if "Misc" in data["Skills"]["Swim"].keys():
                self.swim_misc.delete(0, tk.END)
                self.swim_misc.insert(0, data["Skills"]["Swim"]["Misc"])

            self.swim_modifier.delete(0, tk.END)
            self.swim_modifier.insert(0, data["Skills"]["Swim"]["Total"])

            self.injury_train.delete(0, tk.END)
            self.injury_train.insert(
                0, data["Skills"]["Treat Injury"]["Training"]
            )

            self.injury_focus.delete(0, tk.END)
            self.injury_focus.insert(
                0, data["Skills"]["Treat Injury"]["Focus"]
            )

            if "Misc" in data["Skills"]["Treat Injury"].keys():
                self.injury_misc.delete(0, tk.END)
                self.injury_misc.insert(
                    0, data["Skills"]["Treat Injury"]["Misc"]
                )

            self.injury_modifier.delete(0, tk.END)
            self.injury_modifier.insert(
                0, data["Skills"]["Treat Injury"]["Total"]
            )

            self.computer_train.delete(0, tk.END)
            self.computer_train.insert(
                0, data["Skills"]["Use Computer"]["Training"]
            )

            self.computer_focus.delete(0, tk.END)
            self.computer_focus.insert(
                0, data["Skills"]["Use Computer"]["Focus"]
            )

            if "Misc" in data["Skills"]["Use Computer"].keys():
                self.computer_misc.delete(0, tk.END)
                self.computer_misc.insert(
                    0, data["Skills"]["Use Computer"]["Misc"]
                )

            self.computer_modifier.delete(0, tk.END)
            self.computer_modifier.insert(
                0, data["Skills"]["Use Computer"]["Total"]
            )

            self.use_force_train.delete(0, tk.END)
            self.use_force_train.insert(
                0, data["Skills"]["Use the Force"]["Training"]
            )

            self.use_force_focus.delete(0, tk.END)
            self.use_force_focus.insert(
                0, data["Skills"]["Use the Force"]["Focus"]
            )

            if "Misc" in data["Skills"]["Use the Force"].keys():
                self.use_force_misc.delete(0, tk.END)
                self.use_force_misc.insert(
                    0, data["Skills"]["Use the Force"]["Misc"]
                )

            self.use_force_modifier.delete(0, tk.END)
            self.use_force_modifier.insert(
                0, data["Skills"]["Use the Force"]["Total"]
            )

            # Force Schools
            self.alchemy_1.delete(0, tk.END)
            self.alchemy_1.insert(
                0, data["Force Schools"]["Force School"]["Alchemy"]["Training 1"]
            )

            self.alchemy_2.delete(0, tk.END)
            self.alchemy_2.insert(
                0, data["Force Schools"]["Force School"]["Alchemy"]["Training 2"]
            )

            self.alchemy_3.delete(0, tk.END)
            self.alchemy_3.insert(
                0, data["Force Schools"]["Force School"]["Alchemy"]["Training 3"]
            )

            self.alchemy_modifier.delete(0, tk.END)
            self.alchemy_modifier.insert(
                0, data["Force Schools"]["Force School"]["Alchemy"]["Total"]
            )

            self.augmentation_1.delete(0, tk.END)
            self.augmentation_1.insert(
                0, data["Force Schools"]["Force School"]["Augmentation"]["Training 1"]
            )

            self.augmentation_2.delete(0, tk.END)
            self.augmentation_2.insert(
                0, data["Force Schools"]["Force School"]["Augmentation"]["Training 2"]
            )

            self.augmentation_3.delete(0, tk.END)
            self.augmentation_3.insert(
                0, data["Force Schools"]["Force School"]["Augmentation"]["Training 3"]
            )

            self.augmentation_modifier.delete(0, tk.END)
            self.augmentation_modifier.insert(
                0, data["Force Schools"]["Force School"]["Augmentation"]["Total"]
            )

            self.cognition_1.delete(0, tk.END)
            self.cognition_1.insert(
                0, data["Force Schools"]["Force School"]["Cognition"]["Training 1"]
            )

            self.cognition_2.delete(0, tk.END)
            self.cognition_2.insert(
                0, data["Force Schools"]["Force School"]["Cognition"]["Training 2"]
            )

            self.cognition_3.delete(0, tk.END)
            self.cognition_3.insert(
                0, data["Force Schools"]["Force School"]["Cognition"]["Training 3"]
            )

            self.cognition_modifier.delete(0, tk.END)
            self.cognition_modifier.insert(
                0, data["Force Schools"]["Force School"]["Cognition"]["Total"]
            )

            self.sorcery_1.delete(0, tk.END)
            self.sorcery_1.insert(
                0, data["Force Schools"]["Force School"]["Sorcery"]["Training 1"]
            )

            self.sorcery_2.delete(0, tk.END)
            self.sorcery_2.insert(
                0, data["Force Schools"]["Force School"]["Sorcery"]["Training 2"]
            )

            self.sorcery_3.delete(0, tk.END)
            self.sorcery_3.insert(
                0, data["Force Schools"]["Force School"]["Sorcery"]["Training 3"]
            )

            self.sorcery_modifier.delete(0, tk.END)
            self.sorcery_modifier.insert(
                0, data["Force Schools"]["Force School"]["Sorcery"]["Total"]
            )

            self.techno_1.delete(0, tk.END)
            self.techno_1.insert(
                0, data["Force Schools"]["Force School"]["Technokinesis"]["Training 1"]
            )

            self.techno_2.delete(0, tk.END)
            self.techno_2.insert(
                0, data["Force Schools"]["Force School"]["Technokinesis"]["Training 2"]
            )

            self.techno_3.delete(0, tk.END)
            self.techno_3.insert(
                0, data["Force Schools"]["Force School"]["Technokinesis"]["Training 3"]
            )

            self.techno_modifier.delete(0, tk.END)
            self.techno_modifier.insert(
                0, data["Force Schools"]["Force School"]["Technokinesis"]["Total"]
            )

            self.tele_1.delete(0, tk.END)
            self.tele_1.insert(
                0, data["Force Schools"]["Force School"]["Telekinesis"]["Training 1"]
            )

            self.tele_2.delete(0, tk.END)
            self.tele_2.insert(
                0, data["Force Schools"]["Force School"]["Telekinesis"]["Training 2"]
            )

            self.tele_3.delete(0, tk.END)
            self.tele_3.insert(
                0, data["Force Schools"]["Force School"]["Telekinesis"]["Training 3"]
            )

            self.tele_modifier.delete(0, tk.END)
            self.tele_modifier.insert(
                0, data["Force Schools"]["Force School"]["Telekinesis"]["Total"]
            )

            self.vitalism_1.delete(0, tk.END)
            self.vitalism_1.insert(
                0, data["Force Schools"]["Force School"]["Vitalism"]["Training 1"]
            )

            self.vitalism_2.delete(0, tk.END)
            self.vitalism_2.insert(
                0, data["Force Schools"]["Force School"]["Vitalism"]["Training 2"]
            )

            self.vitalism_3.delete(0, tk.END)
            self.vitalism_3.insert(
                0, data["Force Schools"]["Force School"]["Vitalism"]["Training 3"]
            )

            self.vitalism_modifier.delete(0, tk.END)
            self.vitalism_modifier.insert(
                0, data["Force Schools"]["Force School"]["Vitalism"]["Total"]
            )

            self.force_uses.delete(0, tk.END)
            self.force_uses.insert(0, data["Force Schools"]["Force Uses"])

            # Force Techs
            self.force_tech_1.delete(0, tk.END)
            self.force_tech_1.insert(
                0, data["Force Techniques"]["Force Technique 1"]
            )

            self.force_tech_2.delete(0, tk.END)
            self.force_tech_2.insert(
                0, data["Force Techniques"]["Force Technique 2"]
            )

            self.force_tech_3.delete(0, tk.END)
            self.force_tech_3.insert(
                0, data["Force Techniques"]["Force Technique 3"]
            )

            self.force_tech_4.delete(0, tk.END)
            self.force_tech_4.insert(
                0, data["Force Techniques"]["Force Technique 4"]
            )

            self.force_tech_5.delete(0, tk.END)
            self.force_tech_5.insert(
                0, data["Force Techniques"]["Force Technique 5"]
            )

            self.force_tech_6.delete(0, tk.END)
            self.force_tech_6.insert(
                0, data["Force Techniques"]["Force Technique 6"]
            )

            self.force_tech_7.delete(0, tk.END)
            self.force_tech_7.insert(
                0, data["Force Techniques"]["Force Technique 7"]
            )

            self.force_tech_8.delete(0, tk.END)
            self.force_tech_8.insert(
                0, data["Force Techniques"]["Force Technique 8"]
            )

            self.force_tech_9.delete(0, tk.END)
            self.force_tech_9.insert(
                0, data["Force Techniques"]["Force Technique 9"]
            )

            self.force_tech_10.delete(0, tk.END)
            self.force_tech_10.insert(
                0, data["Force Techniques"]["Force Technique 10"]
            )

            self.force_tech_11.delete(0, tk.END)
            self.force_tech_11.insert(
                0, data["Force Techniques"]["Force Technique 11"]
            )

            self.force_tech_12.delete(0, tk.END)
            self.force_tech_12.insert(
                0, data["Force Techniques"]["Force Technique 12"]
            )

            self.force_tech_13.delete(0, tk.END)
            self.force_tech_13.insert(
                0, data["Force Techniques"]["Force Technique 13"]
            )

            self.force_tech_14.delete(0, tk.END)
            self.force_tech_14.insert(
                0, data["Force Techniques"]["Force Technique 14"]
            )

            self.force_tech_15.delete(0, tk.END)
            self.force_tech_15.insert(
                0, data["Force Techniques"]["Force Technique 15"]
            )

            # Force Secrets
            self.force_secret_1.delete(0, tk.END)
            self.force_secret_1.insert(0, data["Force Secrets"]["Force Secret 1"])

            self.force_secret_2.delete(0, tk.END)
            self.force_secret_2.insert(0, data["Force Secrets"]["Force Secret 2"])

            self.force_secret_3.delete(0, tk.END)
            self.force_secret_3.insert(0, data["Force Secrets"]["Force Secret 3"])

            self.force_secret_4.delete(0, tk.END)
            self.force_secret_4.insert(0, data["Force Secrets"]["Force Secret 4"])

            self.force_secret_5.delete(0, tk.END)
            self.force_secret_5.insert(0, data["Force Secrets"]["Force Secret 5"])

            self.force_secret_6.delete(0, tk.END)
            self.force_secret_6.insert(0, data["Force Secrets"]["Force Secret 6"])

            self.force_secret_7.delete(0, tk.END)
            self.force_secret_7.insert(0, data["Force Secrets"]["Force Secret 7"])

            self.force_secret_8.delete(0, tk.END)
            self.force_secret_8.insert(0, data["Force Secrets"]["Force Secret 8"])

            self.force_secret_9.delete(0, tk.END)
            self.force_secret_9.insert(0, data["Force Secrets"]["Force Secret 9"])

            self.force_secret_10.delete(0, tk.END)
            self.force_secret_10.insert(
                0, data["Force Secrets"]["Force Secret 10"]
            )

            self.force_secret_11.delete(0, tk.END)
            self.force_secret_11.insert(
                0, data["Force Secrets"]["Force Secret 11"]
            )

            self.force_secret_12.delete(0, tk.END)
            self.force_secret_12.insert(
                0, data["Force Secrets"]["Force Secret 12"]
            )

            self.force_secret_13.delete(0, tk.END)
            self.force_secret_13.insert(
                0, data["Force Secrets"]["Force Secret 13"]
            )

            self.force_secret_14.delete(0, tk.END)
            self.force_secret_14.insert(
                0, data["Force Secrets"]["Force Secret 14"]
            )

            self.force_secret_15.delete(0, tk.END)
            self.force_secret_15.insert(
                0, data["Force Secrets"]["Force Secret 15"]
            )

            # Feats
            self.feats_1.delete(0, tk.END)
            self.feats_1.insert(0, data["Feats"]["Feat 1"])

            self.feats_2.delete(0, tk.END)
            self.feats_2.insert(0, data["Feats"]["Feat 2"])

            self.feats_3.delete(0, tk.END)
            self.feats_3.insert(0, data["Feats"]["Feat 3"])

            self.feats_4.delete(0, tk.END)
            self.feats_4.insert(0, data["Feats"]["Feat 4"])

            self.feats_5.delete(0, tk.END)
            self.feats_5.insert(0, data["Feats"]["Feat 5"])

            self.feats_6.delete(0, tk.END)
            self.feats_6.insert(0, data["Feats"]["Feat 6"])

            self.feats_7.delete(0, tk.END)
            self.feats_7.insert(0, data["Feats"]["Feat 7"])

            self.feats_8.delete(0, tk.END)
            self.feats_8.insert(0, data["Feats"]["Feat 8"])

            self.feats_9.delete(0, tk.END)
            self.feats_9.insert(0, data["Feats"]["Feat 9"])

            self.feats_10.delete(0, tk.END)
            self.feats_10.insert(0, data["Feats"]["Feat 10"])

            self.feats_11.delete(0, tk.END)
            self.feats_11.insert(0, data["Feats"]["Feat 11"])

            self.feats_12.delete(0, tk.END)
            self.feats_12.insert(0, data["Feats"]["Feat 12"])

            self.feats_13.delete(0, tk.END)
            self.feats_13.insert(0, data["Feats"]["Feat 13"])

            self.feats_14.delete(0, tk.END)
            self.feats_14.insert(0, data["Feats"]["Feat 14"])

            self.feats_15.delete(0, tk.END)
            self.feats_15.insert(0, data["Feats"]["Feat 15"])

            # Talents
            self.talents_1.delete(0, tk.END)
            self.talents_1.insert(0, data["Talents"]["Talent 1"])

            self.talents_2.delete(0, tk.END)
            self.talents_2.insert(0, data["Talents"]["Talent 2"])

            self.talents_3.delete(0, tk.END)
            self.talents_3.insert(0, data["Talents"]["Talent 3"])

            self.talents_4.delete(0, tk.END)
            self.talents_4.insert(0, data["Talents"]["Talent 4"])

            self.talents_5.delete(0, tk.END)
            self.talents_5.insert(0, data["Talents"]["Talent 5"])

            self.talents_6.delete(0, tk.END)
            self.talents_6.insert(0, data["Talents"]["Talent 6"])

            self.talents_7.delete(0, tk.END)
            self.talents_7.insert(0, data["Talents"]["Talent 7"])

            self.talents_8.delete(0, tk.END)
            self.talents_8.insert(0, data["Talents"]["Talent 8"])

            self.talents_9.delete(0, tk.END)
            self.talents_9.insert(0, data["Talents"]["Talent 9"])

            self.talents_10.delete(0, tk.END)
            self.talents_10.insert(0, data["Talents"]["Talent 10"])

            self.talents_11.delete(0, tk.END)
            self.talents_11.insert(0, data["Talents"]["Talent 11"])

            self.talents_12.delete(0, tk.END)
            self.talents_12.insert(0, data["Talents"]["Talent 12"])

            self.talents_13.delete(0, tk.END)
            self.talents_13.insert(0, data["Talents"]["Talent 13"])

            self.talents_14.delete(0, tk.END)
            self.talents_14.insert(0, data["Talents"]["Talent 14"])

            self.talents_15.delete(0, tk.END)
            self.talents_15.insert(0, data["Talents"]["Talent 15"])

            # Equipment
            self.equipment_1.delete(0, tk.END)
            self.equipment_1.insert(0, data["Equipment"]["Equipment 1"])

            self.equipment_2.delete(0, tk.END)
            self.equipment_2.insert(0, data["Equipment"]["Equipment 2"])

            self.equipment_3.delete(0, tk.END)
            self.equipment_3.insert(0, data["Equipment"]["Equipment 3"])

            self.equipment_4.delete(0, tk.END)
            self.equipment_4.insert(0, data["Equipment"]["Equipment 4"])

            self.equipment_5.delete(0, tk.END)
            self.equipment_5.insert(0, data["Equipment"]["Equipment 5"])

            self.equipment_6.delete(0, tk.END)
            self.equipment_6.insert(0, data["Equipment"]["Equipment 6"])

            self.equipment_7.delete(0, tk.END)
            self.equipment_7.insert(0, data["Equipment"]["Equipment 7"])

            self.equipment_8.delete(0, tk.END)
            self.equipment_8.insert(0, data["Equipment"]["Equipment 8"])

            self.equipment_9.delete(0, tk.END)
            self.equipment_9.insert(0, data["Equipment"]["Equipment 9"])

            self.equipment_10.delete(0, tk.END)
            self.equipment_10.insert(0, data["Equipment"]["Equipment 10"])

            self.equipment_11.delete(0, tk.END)
            self.equipment_11.insert(0, data["Equipment"]["Equipment 11"])

            self.equipment_12.delete(0, tk.END)
            self.equipment_12.insert(0, data["Equipment"]["Equipment 12"])

            self.equipment_13.delete(0, tk.END)
            self.equipment_13.insert(0, data["Equipment"]["Equipment 13"])

            self.equipment_14.delete(0, tk.END)
            self.equipment_14.insert(0, data["Equipment"]["Equipment 14"])

            self.equipment_15.delete(0, tk.END)
            self.equipment_15.insert(0, data["Equipment"]["Equipment 15"])

            self.equipment_16.delete(0, tk.END)
            self.equipment_16.insert(0, data["Equipment"]["Equipment 16"])

            self.equipment_17.delete(0, tk.END)
            self.equipment_17.insert(0, data["Equipment"]["Equipment 17"])

            self.equipment_18.delete(0, tk.END)
            self.equipment_18.insert(0, data["Equipment"]["Equipment 18"])

            self.equipment_19.delete(0, tk.END)
            self.equipment_19.insert(0, data["Equipment"]["Equipment 19"])

            self.equipment_20.delete(0, tk.END)
            self.equipment_20.insert(0, data["Equipment"]["Equipment 20"])

            self.equipment_21.delete(0, tk.END)
            self.equipment_21.insert(0, data["Equipment"]["Equipment 21"])

            self.equipment_22.delete(0, tk.END)
            self.equipment_22.insert(0, data["Equipment"]["Equipment 22"])

            self.equipment_23.delete(0, tk.END)
            self.equipment_23.insert(0, data["Equipment"]["Equipment 23"])

            self.equipment_24.delete(0, tk.END)
            self.equipment_24.insert(0, data["Equipment"]["Equipment 24"])

            self.equipment_25.delete(0, tk.END)
            self.equipment_25.insert(0, data["Equipment"]["Equipment 25"])

            self.equipment_26.delete(0, tk.END)
            self.equipment_26.insert(0, data["Equipment"]["Equipment 26"])

            self.equipment_27.delete(0, tk.END)
            self.equipment_27.insert(0, data["Equipment"]["Equipment 27"])

            self.equipment_28.delete(0, tk.END)
            self.equipment_28.insert(0, data["Equipment"]["Equipment 28"])

            self.equipment_29.delete(0, tk.END)
            self.equipment_29.insert(0, data["Equipment"]["Equipment 29"])

            self.equipment_30.delete(0, tk.END)
            self.equipment_30.insert(0, data["Equipment"]["Equipment 30"])

            self.equipment_31.delete(0, tk.END)
            self.equipment_31.insert(0, data["Equipment"]["Equipment 31"])

            self.equipment_32.delete(0, tk.END)
            self.equipment_32.insert(0, data["Equipment"]["Equipment 32"])


if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterSheetApp(root)
    root.mainloop()
