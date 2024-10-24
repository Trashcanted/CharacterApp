import json
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
        # Labels and Entries without loop
        # Row 0
        self.lbl_name = tk.Label(parent, text="Character Name")
        self.lbl_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_name = tk.Entry(parent, width=25)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_level = tk.Label(parent, text="Character Level")
        self.lbl_level.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_level = tk.Entry(parent, width=25)
        self.entry_level.grid(row=0, column=3, padx=5, pady=5)

        # Row 1
        self.lbl_classes = tk.Label(parent, text="Classes")
        self.lbl_classes.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_classes = tk.Entry(parent, width=25)
        self.entry_classes.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_destiny = tk.Label(parent, text="Destiny")
        self.lbl_destiny.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.entry_destiny = tk.Entry(parent, width=25)
        self.entry_destiny.grid(row=1, column=3, padx=5, pady=5)

        # Row 2
        self.lbl_credits = tk.Label(parent, text="Credits")
        self.lbl_credits.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_credits = tk.Entry(parent, width=25)
        self.entry_credits.grid(row=2, column=1, padx=5, pady=5)

        self.lbl_species = tk.Label(parent, text="Species")
        self.lbl_species.grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.entry_species = tk.Entry(parent, width=25)
        self.entry_species.grid(row=2, column=3, padx=5, pady=5)

        # Row 3
        self.lbl_age = tk.Label(parent, text="Age")
        self.lbl_age.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_age = tk.Entry(parent, width=25)
        self.entry_age.grid(row=3, column=1, padx=5, pady=5)

        self.lbl_height = tk.Label(parent, text="Height")
        self.lbl_height.grid(row=3, column=2, padx=5, pady=5, sticky="w")
        self.entry_height = tk.Entry(parent, width=25)
        self.entry_height.grid(row=3, column=3, padx=5, pady=5)

        # Row 4
        self.lbl_weight = tk.Label(parent, text="Weight")
        self.lbl_weight.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_weight = tk.Entry(parent, width=25)
        self.entry_weight.grid(row=4, column=1, padx=5, pady=5)

        self.lbl_gender = tk.Label(parent, text="Gender")
        self.lbl_gender.grid(row=4, column=2, padx=5, pady=5, sticky="w")
        self.entry_gender = tk.Entry(parent, width=25)
        self.entry_gender.grid(row=4, column=3, padx=5, pady=5)

        # Row 5
        self.lbl_species_info = tk.Label(parent, text="Species Info")
        self.lbl_species_info.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.entry_species_info = tk.Entry(parent, width=25)
        self.entry_species_info.grid(row=5, column=1, padx=5, pady=5)

        self.lbl_force_points = tk.Label(parent, text="Force Points")
        self.lbl_force_points.grid(row=5, column=2, padx=5, pady=5, sticky="w")
        self.entry_force_points = tk.Entry(parent, width=25)
        self.entry_force_points.grid(row=5, column=3, padx=5, pady=5)

        # Row 6
        self.lbl_base_attack_bonus = tk.Label(parent, text="Base Attack Bonus")
        self.lbl_base_attack_bonus.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.entry_base_attack_bonus = tk.Entry(parent, width=25)
        self.entry_base_attack_bonus.grid(row=6, column=1, padx=5, pady=5)

        self.lbl_speed = tk.Label(parent, text="Speed")
        self.lbl_speed.grid(row=6, column=2, padx=5, pady=5, sticky="w")
        self.entry_speed = tk.Entry(parent, width=25)
        self.entry_speed.grid(row=6, column=3, padx=5, pady=5)

        # Row 7
        self.lbl_destiny_points = tk.Label(parent, text="Destiny Points")
        self.lbl_destiny_points.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.entry_destiny_points = tk.Entry(parent, width=25)
        self.entry_destiny_points.grid(row=7, column=1, padx=5, pady=5)

        self.lbl_damage_reduction = tk.Label(parent, text="Damage Reduction")
        self.lbl_damage_reduction.grid(row=7, column=2, padx=5, pady=5, sticky="w")
        self.entry_damage_reduction = tk.Entry(parent, width=25)
        self.entry_damage_reduction.grid(row=7, column=3, padx=5, pady=5)

        # Store the entries in a list if needed
        self.info_entries = [
            self.entry_name,
            self.entry_level,
            self.entry_classes,
            self.entry_destiny,
            self.entry_credits,
            self.entry_species,
            self.entry_age,
            self.entry_height,
            self.entry_weight,
            self.entry_gender,
            self.entry_species_info,
            self.entry_force_points,
            self.entry_base_attack_bonus,
            self.entry_speed,
            self.entry_destiny_points,
            self.entry_damage_reduction,
        ]

    def create_language_fields(self, parent):
        # Label for "Languages"
        self.lbl_languages = tk.Label(parent, text="Languages:")
        self.lbl_languages.grid(row=8, column=0, padx=5, pady=5, sticky="w")

        # Manually adding 10 language Entry fields
        self.entry_language_1 = tk.Entry(parent, width=25)
        self.entry_language_1.grid(row=8, column=1, padx=5, pady=5)

        self.entry_language_2 = tk.Entry(parent, width=25)
        self.entry_language_2.grid(row=9, column=1, padx=5, pady=5)

        self.entry_language_3 = tk.Entry(parent, width=25)
        self.entry_language_3.grid(row=10, column=1, padx=5, pady=5)

        self.entry_language_4 = tk.Entry(parent, width=25)
        self.entry_language_4.grid(row=11, column=1, padx=5, pady=5)

        self.entry_language_5 = tk.Entry(parent, width=25)
        self.entry_language_5.grid(row=12, column=1, padx=5, pady=5)

        self.entry_language_6 = tk.Entry(parent, width=25)
        self.entry_language_6.grid(row=8, column=2, padx=5, pady=5)

        self.entry_language_7 = tk.Entry(parent, width=25)
        self.entry_language_7.grid(row=9, column=2, padx=5, pady=5)

        self.entry_language_8 = tk.Entry(parent, width=25)
        self.entry_language_8.grid(row=10, column=2, padx=5, pady=5)

        self.entry_language_9 = tk.Entry(parent, width=25)
        self.entry_language_9.grid(row=11, column=2, padx=5, pady=5)

        self.entry_language_10 = tk.Entry(parent, width=25)
        self.entry_language_10.grid(row=12, column=2, padx=5, pady=5)

        # Store the entries in a list if needed
        self.language_entries = [
            self.entry_language_1,
            self.entry_language_2,
            self.entry_language_3,
            self.entry_language_4,
            self.entry_language_5,
            self.entry_language_6,
            self.entry_language_7,
            self.entry_language_8,
            self.entry_language_9,
            self.entry_language_10,
        ]

    def create_stat_fields(self, parent):
        # Labels and Entries for stats without loop
        # Strength
        self.lbl_strength = tk.Label(parent, text="Strength")
        self.lbl_strength.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_strength_score = tk.Entry(parent, width=10)
        self.entry_strength_score.grid(row=0, column=1, padx=5, pady=5)
        self.entry_strength_mod = tk.Entry(parent, width=10)
        self.entry_strength_mod.grid(row=0, column=2, padx=5, pady=5)

        # Dexterity
        self.lbl_dexterity = tk.Label(parent, text="Dexterity")
        self.lbl_dexterity.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_dexterity_score = tk.Entry(parent, width=10)
        self.entry_dexterity_score.grid(row=1, column=1, padx=5, pady=5)
        self.entry_dexterity_mod = tk.Entry(parent, width=10)
        self.entry_dexterity_mod.grid(row=1, column=2, padx=5, pady=5)

        # Constitution
        self.lbl_constitution = tk.Label(parent, text="Constitution")
        self.lbl_constitution.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_constitution_score = tk.Entry(parent, width=10)
        self.entry_constitution_score.grid(row=2, column=1, padx=5, pady=5)
        self.entry_constitution_mod = tk.Entry(parent, width=10)
        self.entry_constitution_mod.grid(row=2, column=2, padx=5, pady=5)

        # Intelligence
        self.lbl_intelligence = tk.Label(parent, text="Intelligence")
        self.lbl_intelligence.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_intelligence_score = tk.Entry(parent, width=10)
        self.entry_intelligence_score.grid(row=3, column=1, padx=5, pady=5)
        self.entry_intelligence_mod = tk.Entry(parent, width=10)
        self.entry_intelligence_mod.grid(row=3, column=2, padx=5, pady=5)

        # Wisdom
        self.lbl_wisdom = tk.Label(parent, text="Wisdom")
        self.lbl_wisdom.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_wisdom_score = tk.Entry(parent, width=10)
        self.entry_wisdom_score.grid(row=4, column=1, padx=5, pady=5)
        self.entry_wisdom_mod = tk.Entry(parent, width=10)
        self.entry_wisdom_mod.grid(row=4, column=2, padx=5, pady=5)

        # Charisma
        self.lbl_charisma = tk.Label(parent, text="Charisma")
        self.lbl_charisma.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.entry_charisma_score = tk.Entry(parent, width=10)
        self.entry_charisma_score.grid(row=5, column=1, padx=5, pady=5)
        self.entry_charisma_mod = tk.Entry(parent, width=10)
        self.entry_charisma_mod.grid(row=5, column=2, padx=5, pady=5)

        # Willpower
        self.lbl_willpower = tk.Label(parent, text="Willpower")
        self.lbl_willpower.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.entry_willpower_score = tk.Entry(parent, width=10)
        self.entry_willpower_score.grid(row=6, column=1, padx=5, pady=5)
        self.entry_willpower_mod = tk.Entry(parent, width=10)
        self.entry_willpower_mod.grid(row=6, column=2, padx=5, pady=5)

        # Store the entries in a list if needed
        self.stat_entries = [
            self.entry_strength_score,
            self.entry_strength_mod,
            self.entry_dexterity_score,
            self.entry_dexterity_mod,
            self.entry_constitution_score,
            self.entry_constitution_mod,
            self.entry_intelligence_score,
            self.entry_intelligence_mod,
            self.entry_wisdom_score,
            self.entry_wisdom_mod,
            self.entry_charisma_score,
            self.entry_charisma_mod,
            self.entry_willpower_score,
            self.entry_willpower_mod,
        ]

    def create_defense_fields(self, parent):
        # Labels and Entries for defenses without loop
        # Fortitude
        self.lbl_fortitude = tk.Label(parent, text="Fortitude")
        self.lbl_fortitude.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.entry_fortitude_1 = tk.Entry(parent, width=10)
        self.entry_fortitude_1.grid(row=0, column=1, padx=5, pady=5)

        self.entry_fortitude_2 = tk.Entry(parent, width=10)
        self.entry_fortitude_2.grid(row=0, column=2, padx=5, pady=5)

        self.entry_fortitude_3 = tk.Entry(parent, width=10)
        self.entry_fortitude_3.grid(row=0, column=3, padx=5, pady=5)

        self.entry_fortitude_4 = tk.Entry(parent, width=10)
        self.entry_fortitude_4.grid(row=0, column=4, padx=5, pady=5)

        self.entry_fortitude_5 = tk.Entry(parent, width=10)
        self.entry_fortitude_5.grid(row=0, column=5, padx=5, pady=5)

        # Reflex
        self.lbl_reflex = tk.Label(parent, text="Reflex")
        self.lbl_reflex.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.entry_reflex_1 = tk.Entry(parent, width=10)
        self.entry_reflex_1.grid(row=1, column=1, padx=5, pady=5)

        self.entry_reflex_2 = tk.Entry(parent, width=10)
        self.entry_reflex_2.grid(row=1, column=2, padx=5, pady=5)

        self.entry_reflex_3 = tk.Entry(parent, width=10)
        self.entry_reflex_3.grid(row=1, column=3, padx=5, pady=5)

        self.entry_reflex_4 = tk.Entry(parent, width=10)
        self.entry_reflex_4.grid(row=1, column=4, padx=5, pady=5)

        self.entry_reflex_5 = tk.Entry(parent, width=10)
        self.entry_reflex_5.grid(row=1, column=5, padx=5, pady=5)

        # Will
        self.lbl_will = tk.Label(parent, text="Will")
        self.lbl_will.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.entry_will_1 = tk.Entry(parent, width=10)
        self.entry_will_1.grid(row=2, column=1, padx=5, pady=5)

        self.entry_will_2 = tk.Entry(parent, width=10)
        self.entry_will_2.grid(row=2, column=2, padx=5, pady=5)

        self.entry_will_3 = tk.Entry(parent, width=10)
        self.entry_will_3.grid(row=2, column=3, padx=5, pady=5)

        self.entry_will_4 = tk.Entry(parent, width=10)
        self.entry_will_4.grid(row=2, column=4, padx=5, pady=5)

        self.entry_will_5 = tk.Entry(parent, width=10)
        self.entry_will_5.grid(row=2, column=5, padx=5, pady=5)

        # Store the entries in a list if needed
        self.defense_entries = [
            self.entry_fortitude_1,
            self.entry_fortitude_2,
            self.entry_fortitude_3,
            self.entry_fortitude_4,
            self.entry_fortitude_5,
            self.entry_reflex_1,
            self.entry_reflex_2,
            self.entry_reflex_3,
            self.entry_reflex_4,
            self.entry_reflex_5,
            self.entry_will_1,
            self.entry_will_2,
            self.entry_will_3,
            self.entry_will_4,
            self.entry_will_5,
        ]

    def create_damage_threshold_fields(self, parent):
        # Labels and Entries for Damage Threshold without loop
        # Torso
        self.lbl_torso = tk.Label(parent, text="Torso")
        self.lbl_torso.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_torso = tk.Entry(parent, width=10)
        self.entry_torso.grid(row=1, column=0, padx=5, pady=5)

        # Fortitude
        self.lbl_fortitude = tk.Label(parent, text="Fortitude")
        self.lbl_fortitude.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.entry_fortitude = tk.Entry(parent, width=10)
        self.entry_fortitude.grid(row=1, column=1, padx=5, pady=5)

        # Misc
        self.lbl_misc = tk.Label(parent, text="Misc")
        self.lbl_misc.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_misc = tk.Entry(parent, width=10)
        self.entry_misc.grid(row=1, column=2, padx=5, pady=5)

        # Head
        self.lbl_head = tk.Label(parent, text="Head")
        self.lbl_head.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.entry_head = tk.Entry(parent, width=10)
        self.entry_head.grid(row=1, column=3, padx=5, pady=5)

        # Head Bonus
        self.lbl_head_bonus = tk.Label(parent, text="Head Bonus")
        self.lbl_head_bonus.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.entry_head_bonus = tk.Entry(parent, width=10)
        self.entry_head_bonus.grid(row=1, column=4, padx=5, pady=5)

        # Limbs
        self.lbl_limbs = tk.Label(parent, text="Limbs")
        self.lbl_limbs.grid(row=0, column=5, padx=5, pady=5, sticky="w")
        self.entry_limbs = tk.Entry(parent, width=10)
        self.entry_limbs.grid(row=1, column=5, padx=5, pady=5)

        # Limb Bonus
        self.lbl_limb_bonus = tk.Label(parent, text="Limb Bonus")
        self.lbl_limb_bonus.grid(row=0, column=6, padx=5, pady=5, sticky="w")
        self.entry_limb_bonus = tk.Entry(parent, width=10)
        self.entry_limb_bonus.grid(row=1, column=6, padx=5, pady=5)

        # Store the entries in a list if needed
        self.damage_threshold_entries = [
            self.entry_torso,
            self.entry_fortitude,
            self.entry_misc,
            self.entry_head,
            self.entry_head_bonus,
            self.entry_limbs,
            self.entry_limb_bonus,
        ]

    def create_armor_fields(self, parent):
        # Labels and Entries for Armor without loop
        # Armor
        self.lbl_armor = tk.Label(parent, text="Armor")
        self.lbl_armor.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_armor = tk.Entry(parent, width=50)
        self.entry_armor.grid(row=0, column=1)

        # Fortitude Bonus
        self.lbl_fortitude_bonus = tk.Label(parent, text="Fortitude Bonus")
        self.lbl_fortitude_bonus.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_fortitude_bonus = tk.Entry(parent, width=3)
        self.entry_fortitude_bonus.grid(row=1, column=1)

        # Reflex Bonus
        self.lbl_reflex_bonus = tk.Label(parent, text="Reflex Bonus")
        self.lbl_reflex_bonus.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_reflex_bonus = tk.Entry(parent, width=3)
        self.entry_reflex_bonus.grid(row=2, column=1)

        # Max Dex Bonus
        self.lbl_max_dex_bonus = tk.Label(parent, text="Max Dex Bonus")
        self.lbl_max_dex_bonus.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_max_dex_bonus = tk.Entry(parent, width=3)
        self.entry_max_dex_bonus.grid(row=3, column=1)

        # Additional Affects
        self.lbl_additional_affects = tk.Label(parent, text="Additional Affects")
        self.lbl_additional_affects.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_additional_affects = tk.Entry(parent, width=50)
        self.entry_additional_affects.grid(row=4, column=1)

        # Store the entries in a list if needed
        self.armor_entries = [
            self.entry_armor,
            self.entry_fortitude_bonus,
            self.entry_reflex_bonus,
            self.entry_max_dex_bonus,
            self.entry_additional_affects,
        ]

    def create_weapon_fields(self, parent):
        # Labels and Entries for Weapons without loop
        # First weapon
        self.lbl_weapon_1 = tk.Label(parent, text="Weapon")
        self.lbl_weapon_1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_weapon_1 = tk.Entry(parent, width=25)
        self.entry_weapon_1.grid(row=1, column=0, padx=5, pady=5)

        self.lbl_hit_mod_1 = tk.Label(parent, text="Hit Mod")
        self.lbl_hit_mod_1.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.entry_hit_mod_1 = tk.Entry(parent, width=25)
        self.entry_hit_mod_1.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_damage_1 = tk.Label(parent, text="Damage")
        self.lbl_damage_1.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_damage_1 = tk.Entry(parent, width=25)
        self.entry_damage_1.grid(row=1, column=2, padx=5, pady=5)

        self.lbl_range_1 = tk.Label(parent, text="Range")
        self.lbl_range_1.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.entry_range_1 = tk.Entry(parent, width=25)
        self.entry_range_1.grid(row=1, column=3, padx=5, pady=5)

        self.lbl_crit_range_1 = tk.Label(parent, text="CritRange")
        self.lbl_crit_range_1.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.entry_crit_range_1 = tk.Entry(parent, width=25)
        self.entry_crit_range_1.grid(row=1, column=4, padx=5, pady=5)

        # Second weapon
        self.lbl_weapon_2 = tk.Label(parent, text="Weapon")
        self.lbl_weapon_2.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_weapon_2 = tk.Entry(parent, width=25)
        self.entry_weapon_2.grid(row=3, column=0, padx=5, pady=5)

        self.lbl_hit_mod_2 = tk.Label(parent, text="Hit Mod")
        self.lbl_hit_mod_2.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.entry_hit_mod_2 = tk.Entry(parent, width=25)
        self.entry_hit_mod_2.grid(row=3, column=1, padx=5, pady=5)

        self.lbl_damage_2 = tk.Label(parent, text="Damage")
        self.lbl_damage_2.grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.entry_damage_2 = tk.Entry(parent, width=25)
        self.entry_damage_2.grid(row=3, column=2, padx=5, pady=5)

        self.lbl_range_2 = tk.Label(parent, text="Range")
        self.lbl_range_2.grid(row=2, column=3, padx=5, pady=5, sticky="w")
        self.entry_range_2 = tk.Entry(parent, width=25)
        self.entry_range_2.grid(row=3, column=3, padx=5, pady=5)

        self.lbl_crit_range_2 = tk.Label(parent, text="CritRange")
        self.lbl_crit_range_2.grid(row=2, column=4, padx=5, pady=5, sticky="w")
        self.entry_crit_range_2 = tk.Entry(parent, width=25)
        self.entry_crit_range_2.grid(row=3, column=4, padx=5, pady=5)

        # Third weapon
        self.lbl_weapon_3 = tk.Label(parent, text="Weapon")
        self.lbl_weapon_3.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_weapon_3 = tk.Entry(parent, width=25)
        self.entry_weapon_3.grid(row=5, column=0, padx=5, pady=5)

        self.lbl_hit_mod_3 = tk.Label(parent, text="Hit Mod")
        self.lbl_hit_mod_3.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.entry_hit_mod_3 = tk.Entry(parent, width=25)
        self.entry_hit_mod_3.grid(row=5, column=1, padx=5, pady=5)

        self.lbl_damage_3 = tk.Label(parent, text="Damage")
        self.lbl_damage_3.grid(row=4, column=2, padx=5, pady=5, sticky="w")
        self.entry_damage_3 = tk.Entry(parent, width=25)
        self.entry_damage_3.grid(row=5, column=2, padx=5, pady=5)

        self.lbl_range_3 = tk.Label(parent, text="Range")
        self.lbl_range_3.grid(row=4, column=3, padx=5, pady=5, sticky="w")
        self.entry_range_3 = tk.Entry(parent, width=25)
        self.entry_range_3.grid(row=5, column=3, padx=5, pady=5)

        self.lbl_crit_range_3 = tk.Label(parent, text="CritRange")
        self.lbl_crit_range_3.grid(row=4, column=4, padx=5, pady=5, sticky="w")
        self.entry_crit_range_3 = tk.Entry(parent, width=25)
        self.entry_crit_range_3.grid(row=5, column=4, padx=5, pady=5)

        # Fourth weapon
        self.lbl_weapon_4 = tk.Label(parent, text="Weapon")
        self.lbl_weapon_4.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.entry_weapon_4 = tk.Entry(parent, width=25)
        self.entry_weapon_4.grid(row=7, column=0, padx=5, pady=5)

        self.lbl_hit_mod_4 = tk.Label(parent, text="Hit Mod")
        self.lbl_hit_mod_4.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        self.entry_hit_mod_4 = tk.Entry(parent, width=25)
        self.entry_hit_mod_4.grid(row=7, column=1, padx=5, pady=5)

        self.lbl_damage_4 = tk.Label(parent, text="Damage")
        self.lbl_damage_4.grid(row=6, column=2, padx=5, pady=5, sticky="w")
        self.entry_damage_4 = tk.Entry(parent, width=25)
        self.entry_damage_4.grid(row=7, column=2, padx=5, pady=5)

        self.lbl_range_4 = tk.Label(parent, text="Range")
        self.lbl_range_4.grid(row=6, column=3, padx=5, pady=5, sticky="w")
        self.entry_range_4 = tk.Entry(parent, width=25)
        self.entry_range_4.grid(row=7, column=3, padx=5, pady=5)

        self.lbl_crit_range_4 = tk.Label(parent, text="CritRange")
        self.lbl_crit_range_4.grid(row=6, column=4, padx=5, pady=5, sticky="w")
        self.entry_crit_range_4 = tk.Entry(parent, width=25)
        self.entry_crit_range_4.grid(row=7, column=4, padx=5, pady=5)

        # Fifth weapon
        self.lbl_weapon_5 = tk.Label(parent, text="Weapon")
        self.lbl_weapon_5.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.entry_weapon_5 = tk.Entry(parent, width=25)
        self.entry_weapon_5.grid(row=9, column=0, padx=5, pady=5)

        self.lbl_hit_mod_5 = tk.Label(parent, text="Hit Mod")
        self.lbl_hit_mod_5.grid(row=8, column=1, padx=5, pady=5, sticky="w")
        self.entry_hit_mod_5 = tk.Entry(parent, width=25)
        self.entry_hit_mod_5.grid(row=9, column=1, padx=5, pady=5)

        self.lbl_damage_5 = tk.Label(parent, text="Damage")
        self.lbl_damage_5.grid(row=8, column=2, padx=5, pady=5, sticky="w")
        self.entry_damage_5 = tk.Entry(parent, width=25)
        self.entry_damage_5.grid(row=9, column=2, padx=5, pady=5)

        self.lbl_range_5 = tk.Label(parent, text="Range")
        self.lbl_range_5.grid(row=8, column=3, padx=5, pady=5, sticky="w")
        self.entry_range_5 = tk.Entry(parent, width=25)
        self.entry_range_5.grid(row=9, column=3, padx=5, pady=5)

        self.lbl_crit_range_5 = tk.Label(parent, text="CritRange")
        self.lbl_crit_range_5.grid(row=8, column=4, padx=5, pady=5, sticky="w")
        self.entry_crit_range_5 = tk.Entry(parent, width=25)
        self.entry_crit_range_5.grid(row=9, column=4, padx=5, pady=5)

        # Store the entries in a list if needed
        self.weapon_entries = [
            self.entry_weapon_1,
            self.entry_hit_mod_1,
            self.entry_damage_1,
            self.entry_range_1,
            self.entry_crit_range_1,
            self.entry_weapon_2,
            self.entry_hit_mod_2,
            self.entry_damage_2,
            self.entry_range_2,
            self.entry_crit_range_2,
            self.entry_weapon_3,
            self.entry_hit_mod_3,
            self.entry_damage_3,
            self.entry_range_3,
            self.entry_crit_range_3,
            self.entry_weapon_4,
            self.entry_hit_mod_4,
            self.entry_damage_4,
            self.entry_range_4,
            self.entry_crit_range_4,
            self.entry_weapon_5,
            self.entry_hit_mod_5,
            self.entry_damage_5,
            self.entry_range_5,
            self.entry_crit_range_5,
        ]

    def create_skill_fields(self, parent):

        self.lbl_skills_1 = tk.Label(parent, text="Skill")
        self.lbl_skills_1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.lbl_stat_1 = tk.Label(parent, text="Stat")
        self.lbl_stat_1.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.lbl_training_1 = tk.Label(parent, text="Training")
        self.lbl_training_1.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.lbl_focus_1 = tk.Label(parent, text="Focus")
        self.lbl_focus_1.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.lbl_modifier_1 = tk.Label(parent, text="Modifier")
        self.lbl_modifier_1.grid(row=0, column=4, padx=5, pady=5, sticky="w")

        self.lbl_acrobatics = tk.Label(parent, text="Acrobatics")
        self.lbl_acrobatics.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.lbl_dex = tk.Label(parent, text="Dex")
        self.lbl_dex.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.entry_acro_training = tk.Entry(parent, width=1)
        self.entry_acro_training.grid(row=1, column=2, padx=5, pady=5)
        self.entry_acro_focus = tk.Entry(parent, width=1)
        self.entry_acro_focus.grid(row=1, column=3, padx=5, pady=5)
        self.entry_acro_modifier = tk.Entry(parent, width=5)
        self.entry_acro_modifier.grid(row=1, column=4, padx=5, pady=5)

        self.lbl_climb = tk.Label(parent, text="Climb")
        self.lbl_climb.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.lbl_str = tk.Label(parent, text="Str")
        self.lbl_str.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.entry_climb_training = tk.Entry(parent, width=1)
        self.entry_climb_training.grid(row=2, column=2, padx=5, pady=5)
        self.entry_climb_focus = tk.Entry(parent, width=1)
        self.entry_climb_focus.grid(row=2, column=3, padx=5, pady=5)
        self.entry_climb_modifier = tk.Entry(parent, width=5)
        self.entry_climb_modifier.grid(row=2, column=4, padx=5, pady=5)

        self.lbl_deception = tk.Label(parent, text="Deception")
        self.lbl_deception.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.lbl_cha = tk.Label(parent, text="Cha")
        self.lbl_cha.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.entry_deception_training = tk.Entry(parent, width=1)
        self.entry_deception_training.grid(row=3, column=2, padx=5, pady=5)
        self.entry_deception_focus = tk.Entry(parent, width=1)
        self.entry_deception_focus.grid(row=3, column=3, padx=5, pady=5)
        self.entry_deception_modifier = tk.Entry(parent, width=5)
        self.entry_deception_modifier.grid(row=3, column=4, padx=5, pady=5)

        self.lbl_endurance = tk.Label(parent, text="Endurance")
        self.lbl_endurance.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.lbl_con = tk.Label(parent, text="Con")
        self.lbl_con.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.entry_endurance_training = tk.Entry(parent, width=1)
        self.entry_endurance_training.grid(row=4, column=2, padx=5, pady=5)
        self.entry_endurance_focus = tk.Entry(parent, width=1)
        self.entry_endurance_focus.grid(row=4, column=3, padx=5, pady=5)
        self.entry_endurance_modifier = tk.Entry(parent, width=5)
        self.entry_endurance_modifier.grid(row=4, column=4, padx=5, pady=5)

        self.lbl_gather_information = tk.Label(parent, text="Gather Information")
        self.lbl_gather_information.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.lbl_cha = tk.Label(parent, text="Cha")
        self.lbl_cha.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        self.entry_gather_information_training = tk.Entry(parent, width=1)
        self.entry_gather_information_training.grid(row=5, column=2, padx=5, pady=5)
        self.entry_gather_information_focus = tk.Entry(parent, width=1)
        self.entry_gather_information_focus.grid(row=5, column=3, padx=5, pady=5)
        self.entry_gather_information_modifier = tk.Entry(parent, width=5)
        self.entry_gather_information_modifier.grid(row=5, column=4, padx=5, pady=5)

        self.lbl_initiative = tk.Label(parent, text="Initiative")
        self.lbl_initiative.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.lbl_dex = tk.Label(parent, text="Dex")
        self.lbl_dex.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        self.entry_initiative_training = tk.Entry(parent, width=1)
        self.entry_initiative_training.grid(row=6, column=2, padx=5, pady=5)
        self.entry_initiative_focus = tk.Entry(parent, width=1)
        self.entry_initiative_focus.grid(row=6, column=3, padx=5, pady=5)
        self.entry_initiative_modifier = tk.Entry(parent, width=5)
        self.entry_initiative_modifier.grid(row=6, column=4, padx=5, pady=5)

        self.lbl_jump = tk.Label(parent, text="Jump")
        self.lbl_jump.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.lbl_str = tk.Label(parent, text="Str")
        self.lbl_str.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        self.entry_jump_training = tk.Entry(parent, width=1)
        self.entry_jump_training.grid(row=7, column=2, padx=5, pady=5)
        self.entry_jump_focus = tk.Entry(parent, width=1)
        self.entry_jump_focus.grid(row=7, column=3, padx=5, pady=5)
        self.entry_jump_modifier = tk.Entry(parent, width=5)
        self.entry_jump_modifier.grid(row=7, column=4, padx=5, pady=5)

        self.lbl_knowledge_bureaucracy = tk.Label(
            parent, text="Knowledge (Bureaucracy)"
        )
        self.lbl_knowledge_bureaucracy.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=8, column=1, padx=5, pady=5, sticky="w")
        self.entry_knowledge_bureaucracy_training = tk.Entry(parent, width=1)
        self.entry_knowledge_bureaucracy_training.grid(row=8, column=2, padx=5, pady=5)
        self.entry_knowledge_bureaucracy_focus = tk.Entry(parent, width=1)
        self.entry_knowledge_bureaucracy_focus.grid(row=8, column=3, padx=5, pady=5)
        self.entry_knowledge_bureaucracy_modifier = tk.Entry(parent, width=5)
        self.entry_knowledge_bureaucracy_modifier.grid(row=8, column=4, padx=5, pady=5)

        self.lbl_knowledge_galactic_lore = tk.Label(
            parent, text="Knowledge (Galactic Lore)"
        )
        self.lbl_knowledge_galactic_lore.grid(
            row=9, column=0, padx=5, pady=5, sticky="w"
        )
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=9, column=1, padx=5, pady=5, sticky="w")
        self.entry_knowledge_galactic_lore_training = tk.Entry(parent, width=1)
        self.entry_knowledge_galactic_lore_training.grid(
            row=9, column=2, padx=5, pady=5
        )
        self.entry_knowledge_galactic_lore_focus = tk.Entry(parent, width=1)
        self.entry_knowledge_galactic_lore_focus.grid(row=9, column=3, padx=5, pady=5)
        self.entry_knowledge_galactic_lore_modifier = tk.Entry(parent, width=5)
        self.entry_knowledge_galactic_lore_modifier.grid(
            row=9, column=4, padx=5, pady=5
        )

        self.lbl_knowledge_life_science = tk.Label(
            parent, text="Knowledge (Life Science)"
        )
        self.lbl_knowledge_life_science.grid(
            row=10, column=0, padx=5, pady=5, sticky="w"
        )
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=10, column=1, padx=5, pady=5, sticky="w")
        self.entry_knowledge_life_science_training = tk.Entry(parent, width=1)
        self.entry_knowledge_life_science_training.grid(
            row=10, column=2, padx=5, pady=5
        )
        self.entry_knowledge_life_science_focus = tk.Entry(parent, width=1)
        self.entry_knowledge_life_science_focus.grid(row=10, column=3, padx=5, pady=5)
        self.entry_knowledge_life_science_modifier = tk.Entry(parent, width=5)
        self.entry_knowledge_life_science_modifier.grid(
            row=10, column=4, padx=5, pady=5
        )

        self.lbl_knowledge_physical_science = tk.Label(
            parent, text="Knowledge (Physical Science)"
        )
        self.lbl_knowledge_physical_science.grid(
            row=11, column=0, padx=5, pady=5, sticky="w"
        )
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=11, column=1, padx=5, pady=5, sticky="w")
        self.entry_knowledge_physical_science_training = tk.Entry(parent, width=1)
        self.entry_knowledge_physical_science_training.grid(
            row=11, column=2, padx=5, pady=5
        )
        self.entry_knowledge_physical_science_focus = tk.Entry(parent, width=1)
        self.entry_knowledge_physical_science_focus.grid(
            row=11, column=3, padx=5, pady=5
        )
        self.entry_knowledge_physical_science_modifier = tk.Entry(parent, width=5)
        self.entry_knowledge_physical_science_modifier.grid(
            row=11, column=4, padx=5, pady=5
        )

        self.lbl_knowledge_social_science = tk.Label(
            parent, text="Knowledge (Social Science)"
        )
        self.lbl_knowledge_social_science.grid(
            row=12, column=0, padx=5, pady=5, sticky="w"
        )
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=12, column=1, padx=5, pady=5, sticky="w")
        self.entry_knowledge_social_science_training = tk.Entry(parent, width=1)
        self.entry_knowledge_social_science_training.grid(
            row=12, column=2, padx=5, pady=5
        )
        self.entry_knowledge_social_science_focus = tk.Entry(parent, width=1)
        self.entry_knowledge_social_science_focus.grid(row=12, column=3, padx=5, pady=5)
        self.entry_knowledge_social_science_modifier = tk.Entry(parent, width=5)
        self.entry_knowledge_social_science_modifier.grid(
            row=12, column=4, padx=5, pady=5
        )

        self.lbl_skills_2 = tk.Label(parent, text="Skill")
        self.lbl_skills_2.grid(row=0, column=5, padx=5, pady=5, sticky="w")
        self.lbl_stat_2 = tk.Label(parent, text="Stat")
        self.lbl_stat_2.grid(row=0, column=6, padx=5, pady=5, sticky="w")
        self.lbl_training_2 = tk.Label(parent, text="Training")
        self.lbl_training_2.grid(row=0, column=7, padx=5, pady=5, sticky="w")
        self.lbl_focus_2 = tk.Label(parent, text="Focus")
        self.lbl_focus_2.grid(row=0, column=8, padx=5, pady=5, sticky="w")
        self.lbl_modifier_2 = tk.Label(parent, text="Modifier")
        self.lbl_modifier_2.grid(row=0, column=9, padx=5, pady=5, sticky="w")

        self.lbl_knowledge_tactics = tk.Label(parent, text="Knowledge (Tactics)")
        self.lbl_knowledge_tactics.grid(row=1, column=5, padx=5, pady=5, sticky="w")
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=1, column=6, padx=5, pady=5, sticky="w")
        self.entry_knowledge_tactics_training = tk.Entry(parent, width=1)
        self.entry_knowledge_tactics_training.grid(row=1, column=7, padx=5, pady=5)
        self.entry_knowledge_tactics_focus = tk.Entry(parent, width=1)
        self.entry_knowledge_tactics_focus.grid(row=1, column=8, padx=5, pady=5)
        self.entry_knowledge_tactics_modifier = tk.Entry(parent, width=5)
        self.entry_knowledge_tactics_modifier.grid(row=1, column=9, padx=5, pady=5)

        self.lbl_knowledge_technology = tk.Label(parent, text="Knowledge (Technology)")
        self.lbl_knowledge_technology.grid(row=2, column=5, padx=5, pady=5, sticky="w")
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=2, column=6, padx=5, pady=5, sticky="w")
        self.entry_knowledge_technology_training = tk.Entry(parent, width=1)
        self.entry_knowledge_technology_training.grid(row=2, column=7, padx=5, pady=5)
        self.entry_knowledge_technology_focus = tk.Entry(parent, width=1)
        self.entry_knowledge_technology_focus.grid(row=2, column=8, padx=5, pady=5)
        self.entry_knowledge_technology_modifier = tk.Entry(parent, width=5)
        self.entry_knowledge_technology_modifier.grid(row=2, column=9, padx=5, pady=5)

        self.lbl_mechanics = tk.Label(parent, text="Mechanics")
        self.lbl_mechanics.grid(row=3, column=5, padx=5, pady=5, sticky="w")
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=3, column=6, padx=5, pady=5, sticky="w")
        self.entry_mechanics_training = tk.Entry(parent, width=1)
        self.entry_mechanics_training.grid(row=3, column=7, padx=5, pady=5)
        self.entry_mechanics_focus = tk.Entry(parent, width=1)
        self.entry_mechanics_focus.grid(row=3, column=8, padx=5, pady=5)
        self.entry_mechanics_modifier = tk.Entry(parent, width=5)
        self.entry_mechanics_modifier.grid(row=3, column=9, padx=5, pady=5)

        self.lbl_perception = tk.Label(parent, text="Perception")
        self.lbl_perception.grid(row=4, column=5, padx=5, pady=5, sticky="w")
        self.lbl_wis = tk.Label(parent, text="Wis")
        self.lbl_wis.grid(row=4, column=6, padx=5, pady=5, sticky="w")
        self.entry_perception_training = tk.Entry(parent, width=1)
        self.entry_perception_training.grid(row=4, column=7, padx=5, pady=5)
        self.entry_perception_focus = tk.Entry(parent, width=1)
        self.entry_perception_focus.grid(row=4, column=8, padx=5, pady=5)
        self.entry_perception_modifier = tk.Entry(parent, width=5)
        self.entry_perception_modifier.grid(row=4, column=9, padx=5, pady=5)

        self.lbl_persuasion = tk.Label(parent, text="Persuasion")
        self.lbl_persuasion.grid(row=5, column=5, padx=5, pady=5, sticky="w")
        self.lbl_cha = tk.Label(parent, text="Cha")
        self.lbl_cha.grid(row=5, column=6, padx=5, pady=5, sticky="w")
        self.entry_persuasion_training = tk.Entry(parent, width=1)
        self.entry_persuasion_training.grid(row=5, column=7, padx=5, pady=5)
        self.entry_persuasion_focus = tk.Entry(parent, width=1)
        self.entry_persuasion_focus.grid(row=5, column=8, padx=5, pady=5)
        self.entry_persuasion_modifier = tk.Entry(parent, width=5)
        self.entry_persuasion_modifier.grid(row=5, column=9, padx=5, pady=5)

        self.lbl_pilot = tk.Label(parent, text="Pilot")
        self.lbl_pilot.grid(row=6, column=5, padx=5, pady=5, sticky="w")
        self.lbl_dex = tk.Label(parent, text="Dex")
        self.lbl_dex.grid(row=6, column=6, padx=5, pady=5, sticky="w")
        self.entry_pilot_training = tk.Entry(parent, width=1)
        self.entry_pilot_training.grid(row=6, column=7, padx=5, pady=5)
        self.entry_pilot_focus = tk.Entry(parent, width=1)
        self.entry_pilot_focus.grid(row=6, column=8, padx=5, pady=5)
        self.entry_pilot_modifier = tk.Entry(parent, width=5)
        self.entry_pilot_modifier.grid(row=6, column=9, padx=5, pady=5)

        self.lbl_ride = tk.Label(parent, text="Ride")
        self.lbl_ride.grid(row=7, column=5, padx=5, pady=5, sticky="w")
        self.lbl_dex = tk.Label(parent, text="Dex")
        self.lbl_dex.grid(row=7, column=6, padx=5, pady=5, sticky="w")
        self.entry_ride_training = tk.Entry(parent, width=1)
        self.entry_ride_training.grid(row=7, column=7, padx=5, pady=5)
        self.entry_ride_focus = tk.Entry(parent, width=1)
        self.entry_ride_focus.grid(row=7, column=8, padx=5, pady=5)
        self.entry_ride_modifier = tk.Entry(parent, width=5)
        self.entry_ride_modifier.grid(row=7, column=9, padx=5, pady=5)

        self.lbl_stealth = tk.Label(parent, text="Stealth")
        self.lbl_stealth.grid(row=8, column=5, padx=5, pady=5, sticky="w")
        self.lbl_dex = tk.Label(parent, text="Dex")
        self.lbl_dex.grid(row=8, column=6, padx=5, pady=5, sticky="w")
        self.entry_stealth_training = tk.Entry(parent, width=1)
        self.entry_stealth_training.grid(row=8, column=7, padx=5, pady=5)
        self.entry_stealth_focus = tk.Entry(parent, width=1)
        self.entry_stealth_focus.grid(row=8, column=8, padx=5, pady=5)
        self.entry_stealth_modifier = tk.Entry(parent, width=5)
        self.entry_stealth_modifier.grid(row=8, column=9, padx=5, pady=5)

        self.lbl_survival = tk.Label(parent, text="Survival")
        self.lbl_survival.grid(row=9, column=5, padx=5, pady=5, sticky="w")
        self.lbl_wis = tk.Label(parent, text="Wis")
        self.lbl_wis.grid(row=9, column=6, padx=5, pady=5, sticky="w")
        self.entry_survival_training = tk.Entry(parent, width=1)
        self.entry_survival_training.grid(row=9, column=7, padx=5, pady=5)
        self.entry_survival_focus = tk.Entry(parent, width=1)
        self.entry_survival_focus.grid(row=9, column=8, padx=5, pady=5)
        self.entry_survival_modifier = tk.Entry(parent, width=5)
        self.entry_survival_modifier.grid(row=9, column=9, padx=5, pady=5)

        self.lbl_swim = tk.Label(parent, text="Swim")
        self.lbl_swim.grid(row=10, column=5, padx=5, pady=5, sticky="w")
        self.lbl_str = tk.Label(parent, text="Str")
        self.lbl_str.grid(row=10, column=6, padx=5, pady=5, sticky="w")
        self.entry_swim_training = tk.Entry(parent, width=1)
        self.entry_swim_training.grid(row=10, column=7, padx=5, pady=5)
        self.entry_swim_focus = tk.Entry(parent, width=1)
        self.entry_swim_focus.grid(row=10, column=8, padx=5, pady=5)
        self.entry_swim_modifier = tk.Entry(parent, width=5)
        self.entry_swim_modifier.grid(row=10, column=9, padx=5, pady=5)

        self.lbl_treat_injury = tk.Label(parent, text="Treat Injury")
        self.lbl_treat_injury.grid(row=11, column=5, padx=5, pady=5, sticky="w")
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=11, column=6, padx=5, pady=5, sticky="w")
        self.entry_treat_injury_training = tk.Entry(parent, width=1)
        self.entry_treat_injury_training.grid(row=11, column=7, padx=5, pady=5)
        self.entry_treat_injury_focus = tk.Entry(parent, width=1)
        self.entry_treat_injury_focus.grid(row=11, column=8, padx=5, pady=5)
        self.entry_treat_injury_modifier = tk.Entry(parent, width=5)
        self.entry_treat_injury_modifier.grid(row=11, column=9, padx=5, pady=5)

        self.lbl_use_computer = tk.Label(parent, text="Use Computer")
        self.lbl_use_computer.grid(row=12, column=5, padx=5, pady=5, sticky="w")
        self.lbl_int = tk.Label(parent, text="Int")
        self.lbl_int.grid(row=12, column=6, padx=5, pady=5, sticky="w")
        self.entry_use_computer_training = tk.Entry(parent, width=1)
        self.entry_use_computer_training.grid(row=12, column=7, padx=5, pady=5)
        self.entry_use_computer_focus = tk.Entry(parent, width=1)
        self.entry_use_computer_focus.grid(row=12, column=8, padx=5, pady=5)
        self.entry_use_computer_modifier = tk.Entry(parent, width=5)
        self.entry_use_computer_modifier.grid(row=12, column=9, padx=5, pady=5)

        self.lbl_use_the_force = tk.Label(parent, text="Use The Force")
        self.lbl_use_the_force.grid(row=13, column=5, padx=5, pady=5, sticky="w")
        self.lbl_cha_will = tk.Label(parent, text="Cha/Will")
        self.lbl_cha_will.grid(row=13, column=6, padx=5, pady=5, sticky="w")
        self.entry_use_the_force_training = tk.Entry(parent, width=1)
        self.entry_use_the_force_training.grid(row=13, column=7, padx=5, pady=5)
        self.entry_use_the_force_focus = tk.Entry(parent, width=1)
        self.entry_use_the_force_focus.grid(row=13, column=8, padx=5, pady=5)
        self.entry_use_the_force_modifier = tk.Entry(parent, width=5)
        self.entry_use_the_force_modifier.grid(row=13, column=9, padx=5, pady=5)

        skills_entries = [
            self.entry_acro_training,
            self.entry_acro_focus,
            self.entry_acro_modifier,
            self.entry_climb_training,
            self.entry_climb_focus,
            self.entry_climb_modifier,
            self.entry_deception_training,
            self.entry_deception_focus,
            self.entry_deception_modifier,
            self.entry_endurance_training,
            self.entry_endurance_focus,
            self.entry_endurance_modifier,
            self.entry_gather_information_training,
            self.entry_gather_information_focus,
            self.entry_gather_information_modifier,
            self.entry_initiative_training,
            self.entry_initiative_focus,
            self.entry_initiative_modifier,
            self.entry_jump_training,
            self.entry_jump_focus,
            self.entry_jump_modifier,
            self.entry_knowledge_bureaucracy_training,
            self.entry_knowledge_bureaucracy_focus,
            self.entry_knowledge_bureaucracy_modifier,
            self.entry_knowledge_galactic_lore_training,
            self.entry_knowledge_galactic_lore_focus,
            self.entry_knowledge_galactic_lore_modifier,
            self.entry_knowledge_life_science_training,
            self.entry_knowledge_life_science_focus,
            self.entry_knowledge_life_science_modifier,
            self.entry_knowledge_physical_science_training,
            self.entry_knowledge_physical_science_focus,
            self.entry_knowledge_physical_science_modifier,
            self.entry_knowledge_social_science_training,
            self.entry_knowledge_social_science_focus,
            self.entry_knowledge_social_science_modifier,
            self.entry_knowledge_tactics_training,
            self.entry_knowledge_tactics_focus,
            self.entry_knowledge_tactics_modifier,
            self.entry_knowledge_technology_training,
            self.entry_knowledge_technology_focus,
            self.entry_knowledge_technology_modifier,
            self.entry_mechanics_training,
            self.entry_mechanics_focus,
            self.entry_mechanics_modifier,
            self.entry_perception_training,
            self.entry_perception_focus,
            self.entry_perception_modifier,
            self.entry_persuasion_training,
            self.entry_persuasion_focus,
            self.entry_persuasion_modifier,
            self.entry_pilot_training,
            self.entry_pilot_focus,
            self.entry_pilot_modifier,
            self.entry_ride_training,
            self.entry_ride_focus,
            self.entry_ride_modifier,
            self.entry_stealth_training,
            self.entry_stealth_focus,
            self.entry_stealth_modifier,
            self.entry_survival_training,
            self.entry_survival_focus,
            self.entry_survival_modifier,
            self.entry_treat_injury_training,
            self.entry_treat_injury_focus,
            self.entry_treat_injury_modifier,
            self.entry_use_computer_training,
            self.entry_use_computer_focus,
            self.entry_use_computer_modifier,
            self.entry_use_the_force_training,
            self.entry_use_the_force_focus,
            self.entry_use_the_force_modifier,
        ]

    def create_force_school_fields(self, parent):
        # Meta labels
        self.lbl_schools = tk.Label(parent, text="Schools")
        self.lbl_schools.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.lbl_training = tk.Label(parent, text="Training")
        self.lbl_training.grid(row=0, column=1, padx=5, pady=5, sticky="w")

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
        self.entry_alchemy_1 = tk.Entry(parent, width=1)
        self.entry_alchemy_1.grid(row=1, column=1, padx=5, pady=5)
        self.entry_alchemy_2 = tk.Entry(parent, width=1)
        self.entry_alchemy_2.grid(row=1, column=2, padx=5, pady=5)
        self.entry_alchemy_3 = tk.Entry(parent, width=1)
        self.entry_alchemy_3.grid(row=1, column=3, padx=5, pady=5)
        self.entry_alchemy_modifier = tk.Entry(parent, width=10)
        self.entry_alchemy_modifier.grid(row=1, column=4, padx=5, pady=5)

        # Augmentation
        self.lbl_augmentation = tk.Label(parent, text="Augmentation")
        self.lbl_augmentation.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_augmentation_1 = tk.Entry(parent, width=1)
        self.entry_augmentation_1.grid(row=2, column=1, padx=5, pady=5)
        self.entry_augmentation_2 = tk.Entry(parent, width=1)
        self.entry_augmentation_2.grid(row=2, column=2, padx=5, pady=5)
        self.entry_augmentation_3 = tk.Entry(parent, width=1)
        self.entry_augmentation_3.grid(row=2, column=3, padx=5, pady=5)
        self.entry_augmentation_modifier = tk.Entry(parent, width=10)
        self.entry_augmentation_modifier.grid(row=2, column=4, padx=5, pady=5)

        # Cognition
        self.lbl_cognition = tk.Label(parent, text="Cognition")
        self.lbl_cognition.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_cognition_1 = tk.Entry(parent, width=1)
        self.entry_cognition_1.grid(row=3, column=1, padx=5, pady=5)
        self.entry_cognition_2 = tk.Entry(parent, width=1)
        self.entry_cognition_2.grid(row=3, column=2, padx=5, pady=5)
        self.entry_cognition_3 = tk.Entry(parent, width=1)
        self.entry_cognition_3.grid(row=3, column=3, padx=5, pady=5)
        self.entry_cognition_modifier = tk.Entry(parent, width=10)
        self.entry_cognition_modifier.grid(row=3, column=4, padx=5, pady=5)

        # Sorcery
        self.lbl_sorcery = tk.Label(parent, text="Sorcery")
        self.lbl_sorcery.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_sorcery_1 = tk.Entry(parent, width=1)
        self.entry_sorcery_1.grid(row=4, column=1, padx=5, pady=5)
        self.entry_sorcery_2 = tk.Entry(parent, width=1)
        self.entry_sorcery_2.grid(row=4, column=2, padx=5, pady=5)
        self.entry_sorcery_3 = tk.Entry(parent, width=1)
        self.entry_sorcery_3.grid(row=4, column=3, padx=5, pady=5)
        self.entry_sorcery_modifier = tk.Entry(parent, width=10)
        self.entry_sorcery_modifier.grid(row=4, column=4, padx=5, pady=5)

        # Technokinesis
        self.lbl_technokinesis = tk.Label(parent, text="Technokinesis")
        self.lbl_technokinesis.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.entry_technokinesis_1 = tk.Entry(parent, width=1)
        self.entry_technokinesis_1.grid(row=5, column=1, padx=5, pady=5)
        self.entry_technokinesis_2 = tk.Entry(parent, width=1)
        self.entry_technokinesis_2.grid(row=5, column=2, padx=5, pady=5)
        self.entry_technokinesis_3 = tk.Entry(parent, width=1)
        self.entry_technokinesis_3.grid(row=5, column=3, padx=5, pady=5)
        self.entry_technokinesis_modifier = tk.Entry(parent, width=10)
        self.entry_technokinesis_modifier.grid(row=5, column=4, padx=5, pady=5)

        # Telekinesis
        self.lbl_telekinesis = tk.Label(parent, text="Telekinesis")
        self.lbl_telekinesis.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.entry_telekinesis_1 = tk.Entry(parent, width=1)
        self.entry_telekinesis_1.grid(row=6, column=1, padx=5, pady=5)
        self.entry_telekinesis_2 = tk.Entry(parent, width=1)
        self.entry_telekinesis_2.grid(row=6, column=2, padx=5, pady=5)
        self.entry_telekinesis_3 = tk.Entry(parent, width=1)
        self.entry_telekinesis_3.grid(row=6, column=3, padx=5, pady=5)
        self.entry_telekinesis_modifier = tk.Entry(parent, width=10)
        self.entry_telekinesis_modifier.grid(row=6, column=4, padx=5, pady=5)

        # Vitalism
        self.lbl_vitalism = tk.Label(parent, text="Vitalism")
        self.lbl_vitalism.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.entry_vitalism_1 = tk.Entry(parent, width=1)
        self.entry_vitalism_1.grid(row=7, column=1, padx=5, pady=5)
        self.entry_vitalism_2 = tk.Entry(parent, width=1)
        self.entry_vitalism_2.grid(row=7, column=2, padx=5, pady=5)
        self.entry_vitalism_3 = tk.Entry(parent, width=1)
        self.entry_vitalism_3.grid(row=7, column=3, padx=5, pady=5)
        self.entry_vitalism_modifier = tk.Entry(parent, width=10)
        self.entry_vitalism_modifier.grid(row=7, column=4, padx=5, pady=5)

        # Force Uses
        self.lbl_force_uses = tk.Label(parent, text="Force Uses")
        self.lbl_force_uses.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.entry_force_uses = tk.Entry(parent, width=10)
        self.entry_force_uses.grid(row=8, column=1, padx=5, pady=5)

        # Store the entries in a list
        self.force_school_entries = [
            self.entry_alchemy_1,
            self.entry_alchemy_2,
            self.entry_alchemy_3,
            self.entry_alchemy_modifier,
            self.entry_augmentation_1,
            self.entry_augmentation_2,
            self.entry_augmentation_3,
            self.entry_augmentation_modifier,
            self.entry_cognition_1,
            self.entry_cognition_2,
            self.entry_cognition_3,
            self.entry_cognition_modifier,
            self.entry_sorcery_1,
            self.entry_sorcery_2,
            self.entry_sorcery_3,
            self.entry_sorcery_modifier,
            self.entry_technokinesis_1,
            self.entry_technokinesis_2,
            self.entry_technokinesis_3,
            self.entry_technokinesis_modifier,
            self.entry_telekinesis_1,
            self.entry_telekinesis_2,
            self.entry_telekinesis_3,
            self.entry_telekinesis_modifier,
            self.entry_vitalism_1,
            self.entry_vitalism_2,
            self.entry_vitalism_3,
            self.entry_vitalism_modifier,
            self.entry_force_uses,
        ]

    def create_force_tech_secret_fields(self, parent):
        # Labels for Force Techniques and Force Secrets
        self.lbl_force_techniques = tk.Label(parent, text="Force Techniques")
        self.lbl_force_techniques.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.lbl_force_secrets = tk.Label(parent, text="Force Secrets")
        self.lbl_force_secrets.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Entries for Force Techniques
        self.entry_force_tech_1 = tk.Entry(parent, width=25)
        self.entry_force_tech_1.grid(row=1, column=0, padx=5, pady=5)
        self.entry_force_tech_2 = tk.Entry(parent, width=25)
        self.entry_force_tech_2.grid(row=2, column=0, padx=5, pady=5)
        self.entry_force_tech_3 = tk.Entry(parent, width=25)
        self.entry_force_tech_3.grid(row=3, column=0, padx=5, pady=5)
        self.entry_force_tech_4 = tk.Entry(parent, width=25)
        self.entry_force_tech_4.grid(row=4, column=0, padx=5, pady=5)
        self.entry_force_tech_5 = tk.Entry(parent, width=25)
        self.entry_force_tech_5.grid(row=5, column=0, padx=5, pady=5)
        self.entry_force_tech_6 = tk.Entry(parent, width=25)
        self.entry_force_tech_6.grid(row=6, column=0, padx=5, pady=5)
        self.entry_force_tech_7 = tk.Entry(parent, width=25)
        self.entry_force_tech_7.grid(row=7, column=0, padx=5, pady=5)
        self.entry_force_tech_8 = tk.Entry(parent, width=25)
        self.entry_force_tech_8.grid(row=8, column=0, padx=5, pady=5)
        self.entry_force_tech_9 = tk.Entry(parent, width=25)
        self.entry_force_tech_9.grid(row=9, column=0, padx=5, pady=5)
        self.entry_force_tech_10 = tk.Entry(parent, width=25)
        self.entry_force_tech_10.grid(row=10, column=0, padx=5, pady=5)
        self.entry_force_tech_11 = tk.Entry(parent, width=25)
        self.entry_force_tech_11.grid(row=11, column=0, padx=5, pady=5)
        self.entry_force_tech_12 = tk.Entry(parent, width=25)
        self.entry_force_tech_12.grid(row=12, column=0, padx=5, pady=5)
        self.entry_force_tech_13 = tk.Entry(parent, width=25)
        self.entry_force_tech_13.grid(row=13, column=0, padx=5, pady=5)
        self.entry_force_tech_14 = tk.Entry(parent, width=25)
        self.entry_force_tech_14.grid(row=14, column=0, padx=5, pady=5)
        self.entry_force_tech_15 = tk.Entry(parent, width=25)
        self.entry_force_tech_15.grid(row=15, column=0, padx=5, pady=5)

        # Entries for Force Secrets
        self.entry_force_secret_1 = tk.Entry(parent, width=25)
        self.entry_force_secret_1.grid(row=1, column=1, padx=5, pady=5)
        self.entry_force_secret_2 = tk.Entry(parent, width=25)
        self.entry_force_secret_2.grid(row=2, column=1, padx=5, pady=5)
        self.entry_force_secret_3 = tk.Entry(parent, width=25)
        self.entry_force_secret_3.grid(row=3, column=1, padx=5, pady=5)
        self.entry_force_secret_4 = tk.Entry(parent, width=25)
        self.entry_force_secret_4.grid(row=4, column=1, padx=5, pady=5)
        self.entry_force_secret_5 = tk.Entry(parent, width=25)
        self.entry_force_secret_5.grid(row=5, column=1, padx=5, pady=5)
        self.entry_force_secret_6 = tk.Entry(parent, width=25)
        self.entry_force_secret_6.grid(row=6, column=1, padx=5, pady=5)
        self.entry_force_secret_7 = tk.Entry(parent, width=25)
        self.entry_force_secret_7.grid(row=7, column=1, padx=5, pady=5)
        self.entry_force_secret_8 = tk.Entry(parent, width=25)
        self.entry_force_secret_8.grid(row=8, column=1, padx=5, pady=5)
        self.entry_force_secret_9 = tk.Entry(parent, width=25)
        self.entry_force_secret_9.grid(row=9, column=1, padx=5, pady=5)
        self.entry_force_secret_10 = tk.Entry(parent, width=25)
        self.entry_force_secret_10.grid(row=10, column=1, padx=5, pady=5)
        self.entry_force_secret_11 = tk.Entry(parent, width=25)
        self.entry_force_secret_11.grid(row=11, column=1, padx=5, pady=5)
        self.entry_force_secret_12 = tk.Entry(parent, width=25)
        self.entry_force_secret_12.grid(row=12, column=1, padx=5, pady=5)
        self.entry_force_secret_13 = tk.Entry(parent, width=25)
        self.entry_force_secret_13.grid(row=13, column=1, padx=5, pady=5)
        self.entry_force_secret_14 = tk.Entry(parent, width=25)
        self.entry_force_secret_14.grid(row=14, column=1, padx=5, pady=5)
        self.entry_force_secret_15 = tk.Entry(parent, width=25)
        self.entry_force_secret_15.grid(row=15, column=1, padx=5, pady=5)

        # Store the entries in lists
        self.force_tech_entries = [
            self.entry_force_tech_1,
            self.entry_force_tech_2,
            self.entry_force_tech_3,
            self.entry_force_tech_4,
            self.entry_force_tech_5,
            self.entry_force_tech_6,
            self.entry_force_tech_7,
            self.entry_force_tech_8,
            self.entry_force_tech_9,
            self.entry_force_tech_10,
            self.entry_force_tech_11,
            self.entry_force_tech_12,
            self.entry_force_tech_13,
            self.entry_force_tech_14,
            self.entry_force_tech_15,
        ]

        self.force_secret_entries = [
            self.entry_force_secret_1,
            self.entry_force_secret_2,
            self.entry_force_secret_3,
            self.entry_force_secret_4,
            self.entry_force_secret_5,
            self.entry_force_secret_6,
            self.entry_force_secret_7,
            self.entry_force_secret_8,
            self.entry_force_secret_9,
            self.entry_force_secret_10,
            self.entry_force_secret_11,
            self.entry_force_secret_12,
            self.entry_force_secret_13,
            self.entry_force_secret_14,
            self.entry_force_secret_15,
        ]

    def create_feats_talents_fields(self, parent):
        # Labels for Feats and Talents
        self.lbl_feats = tk.Label(parent, text="Feats:")
        self.lbl_feats.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.lbl_talents = tk.Label(parent, text="Talents:")
        self.lbl_talents.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Entries for Feats
        self.entry_feats_1 = tk.Entry(parent, width=25)
        self.entry_feats_1.grid(row=1, column=0, padx=5, pady=5)
        self.entry_feats_2 = tk.Entry(parent, width=25)
        self.entry_feats_2.grid(row=2, column=0, padx=5, pady=5)
        self.entry_feats_3 = tk.Entry(parent, width=25)
        self.entry_feats_3.grid(row=3, column=0, padx=5, pady=5)
        self.entry_feats_4 = tk.Entry(parent, width=25)
        self.entry_feats_4.grid(row=4, column=0, padx=5, pady=5)
        self.entry_feats_5 = tk.Entry(parent, width=25)
        self.entry_feats_5.grid(row=5, column=0, padx=5, pady=5)
        self.entry_feats_6 = tk.Entry(parent, width=25)
        self.entry_feats_6.grid(row=6, column=0, padx=5, pady=5)
        self.entry_feats_7 = tk.Entry(parent, width=25)
        self.entry_feats_7.grid(row=7, column=0, padx=5, pady=5)
        self.entry_feats_8 = tk.Entry(parent, width=25)
        self.entry_feats_8.grid(row=8, column=0, padx=5, pady=5)
        self.entry_feats_9 = tk.Entry(parent, width=25)
        self.entry_feats_9.grid(row=9, column=0, padx=5, pady=5)
        self.entry_feats_10 = tk.Entry(parent, width=25)
        self.entry_feats_10.grid(row=10, column=0, padx=5, pady=5)
        self.entry_feats_11 = tk.Entry(parent, width=25)
        self.entry_feats_11.grid(row=11, column=0, padx=5, pady=5)
        self.entry_feats_12 = tk.Entry(parent, width=25)
        self.entry_feats_12.grid(row=12, column=0, padx=5, pady=5)
        self.entry_feats_13 = tk.Entry(parent, width=25)
        self.entry_feats_13.grid(row=13, column=0, padx=5, pady=5)
        self.entry_feats_14 = tk.Entry(parent, width=25)
        self.entry_feats_14.grid(row=14, column=0, padx=5, pady=5)
        self.entry_feats_15 = tk.Entry(parent, width=25)
        self.entry_feats_15.grid(row=15, column=0, padx=5, pady=5)

        # Entries for Talents
        self.entry_talents_1 = tk.Entry(parent, width=25)
        self.entry_talents_1.grid(row=1, column=1, padx=5, pady=5)
        self.entry_talents_2 = tk.Entry(parent, width=25)
        self.entry_talents_2.grid(row=2, column=1, padx=5, pady=5)
        self.entry_talents_3 = tk.Entry(parent, width=25)
        self.entry_talents_3.grid(row=3, column=1, padx=5, pady=5)
        self.entry_talents_4 = tk.Entry(parent, width=25)
        self.entry_talents_4.grid(row=4, column=1, padx=5, pady=5)
        self.entry_talents_5 = tk.Entry(parent, width=25)
        self.entry_talents_5.grid(row=5, column=1, padx=5, pady=5)
        self.entry_talents_6 = tk.Entry(parent, width=25)
        self.entry_talents_6.grid(row=6, column=1, padx=5, pady=5)
        self.entry_talents_7 = tk.Entry(parent, width=25)
        self.entry_talents_7.grid(row=7, column=1, padx=5, pady=5)
        self.entry_talents_8 = tk.Entry(parent, width=25)
        self.entry_talents_8.grid(row=8, column=1, padx=5, pady=5)
        self.entry_talents_9 = tk.Entry(parent, width=25)
        self.entry_talents_9.grid(row=9, column=1, padx=5, pady=5)
        self.entry_talents_10 = tk.Entry(parent, width=25)
        self.entry_talents_10.grid(row=10, column=1, padx=5, pady=5)
        self.entry_talents_11 = tk.Entry(parent, width=25)
        self.entry_talents_11.grid(row=11, column=1, padx=5, pady=5)
        self.entry_talents_12 = tk.Entry(parent, width=25)
        self.entry_talents_12.grid(row=12, column=1, padx=5, pady=5)
        self.entry_talents_13 = tk.Entry(parent, width=25)
        self.entry_talents_13.grid(row=13, column=1, padx=5, pady=5)
        self.entry_talents_14 = tk.Entry(parent, width=25)
        self.entry_talents_14.grid(row=14, column=1, padx=5, pady=5)
        self.entry_talents_15 = tk.Entry(parent, width=25)
        self.entry_talents_15.grid(row=15, column=1, padx=5, pady=5)

        # Store the entries in a list
        self.feats_talents_entries = [
            self.entry_feats_1,
            self.entry_feats_2,
            self.entry_feats_3,
            self.entry_feats_4,
            self.entry_feats_5,
            self.entry_feats_6,
            self.entry_feats_7,
            self.entry_feats_8,
            self.entry_feats_9,
            self.entry_feats_10,
            self.entry_feats_11,
            self.entry_feats_12,
            self.entry_feats_13,
            self.entry_feats_14,
            self.entry_feats_15,
            self.entry_talents_1,
            self.entry_talents_2,
            self.entry_talents_3,
            self.entry_talents_4,
            self.entry_talents_5,
            self.entry_talents_6,
            self.entry_talents_7,
            self.entry_talents_8,
            self.entry_talents_9,
            self.entry_talents_10,
            self.entry_talents_11,
            self.entry_talents_12,
            self.entry_talents_13,
            self.entry_talents_14,
            self.entry_talents_15,
        ]

    def create_equipment_fields(self, parent):
        # Label for Equipment
        self.lbl_equipment = tk.Label(parent, text="Equipment:")
        self.lbl_equipment.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Equipment Entries (8 rows, 4 columns)
        self.entry_equipment_1 = tk.Entry(parent, width=25)
        self.entry_equipment_1.grid(row=1, column=0, padx=5, pady=5)
        self.entry_equipment_2 = tk.Entry(parent, width=25)
        self.entry_equipment_2.grid(row=1, column=1, padx=5, pady=5)
        self.entry_equipment_3 = tk.Entry(parent, width=25)
        self.entry_equipment_3.grid(row=1, column=2, padx=5, pady=5)
        self.entry_equipment_4 = tk.Entry(parent, width=25)
        self.entry_equipment_4.grid(row=1, column=3, padx=5, pady=5)

        self.entry_equipment_5 = tk.Entry(parent, width=25)
        self.entry_equipment_5.grid(row=2, column=0, padx=5, pady=5)
        self.entry_equipment_6 = tk.Entry(parent, width=25)
        self.entry_equipment_6.grid(row=2, column=1, padx=5, pady=5)
        self.entry_equipment_7 = tk.Entry(parent, width=25)
        self.entry_equipment_7.grid(row=2, column=2, padx=5, pady=5)
        self.entry_equipment_8 = tk.Entry(parent, width=25)
        self.entry_equipment_8.grid(row=2, column=3, padx=5, pady=5)

        self.entry_equipment_9 = tk.Entry(parent, width=25)
        self.entry_equipment_9.grid(row=3, column=0, padx=5, pady=5)
        self.entry_equipment_10 = tk.Entry(parent, width=25)
        self.entry_equipment_10.grid(row=3, column=1, padx=5, pady=5)
        self.entry_equipment_11 = tk.Entry(parent, width=25)
        self.entry_equipment_11.grid(row=3, column=2, padx=5, pady=5)
        self.entry_equipment_12 = tk.Entry(parent, width=25)
        self.entry_equipment_12.grid(row=3, column=3, padx=5, pady=5)

        self.entry_equipment_13 = tk.Entry(parent, width=25)
        self.entry_equipment_13.grid(row=4, column=0, padx=5, pady=5)
        self.entry_equipment_14 = tk.Entry(parent, width=25)
        self.entry_equipment_14.grid(row=4, column=1, padx=5, pady=5)
        self.entry_equipment_15 = tk.Entry(parent, width=25)
        self.entry_equipment_15.grid(row=4, column=2, padx=5, pady=5)
        self.entry_equipment_16 = tk.Entry(parent, width=25)
        self.entry_equipment_16.grid(row=4, column=3, padx=5, pady=5)

        self.entry_equipment_17 = tk.Entry(parent, width=25)
        self.entry_equipment_17.grid(row=5, column=0, padx=5, pady=5)
        self.entry_equipment_18 = tk.Entry(parent, width=25)
        self.entry_equipment_18.grid(row=5, column=1, padx=5, pady=5)
        self.entry_equipment_19 = tk.Entry(parent, width=25)
        self.entry_equipment_19.grid(row=5, column=2, padx=5, pady=5)
        self.entry_equipment_20 = tk.Entry(parent, width=25)
        self.entry_equipment_20.grid(row=5, column=3, padx=5, pady=5)

        self.entry_equipment_21 = tk.Entry(parent, width=25)
        self.entry_equipment_21.grid(row=6, column=0, padx=5, pady=5)
        self.entry_equipment_22 = tk.Entry(parent, width=25)
        self.entry_equipment_22.grid(row=6, column=1, padx=5, pady=5)
        self.entry_equipment_23 = tk.Entry(parent, width=25)
        self.entry_equipment_23.grid(row=6, column=2, padx=5, pady=5)
        self.entry_equipment_24 = tk.Entry(parent, width=25)
        self.entry_equipment_24.grid(row=6, column=3, padx=5, pady=5)

        self.entry_equipment_25 = tk.Entry(parent, width=25)
        self.entry_equipment_25.grid(row=7, column=0, padx=5, pady=5)
        self.entry_equipment_26 = tk.Entry(parent, width=25)
        self.entry_equipment_26.grid(row=7, column=1, padx=5, pady=5)
        self.entry_equipment_27 = tk.Entry(parent, width=25)
        self.entry_equipment_27.grid(row=7, column=2, padx=5, pady=5)
        self.entry_equipment_28 = tk.Entry(parent, width=25)
        self.entry_equipment_28.grid(row=7, column=3, padx=5, pady=5)

        self.entry_equipment_29 = tk.Entry(parent, width=25)
        self.entry_equipment_29.grid(row=8, column=0, padx=5, pady=5)
        self.entry_equipment_30 = tk.Entry(parent, width=25)
        self.entry_equipment_30.grid(row=8, column=1, padx=5, pady=5)
        self.entry_equipment_31 = tk.Entry(parent, width=25)
        self.entry_equipment_31.grid(row=8, column=2, padx=5, pady=5)
        self.entry_equipment_32 = tk.Entry(parent, width=25)
        self.entry_equipment_32.grid(row=8, column=3, padx=5, pady=5)

        # Store the entries in a list
        self.equipment_entries = [
            self.entry_equipment_1,
            self.entry_equipment_2,
            self.entry_equipment_3,
            self.entry_equipment_4,
            self.entry_equipment_5,
            self.entry_equipment_6,
            self.entry_equipment_7,
            self.entry_equipment_8,
            self.entry_equipment_9,
            self.entry_equipment_10,
            self.entry_equipment_11,
            self.entry_equipment_12,
            self.entry_equipment_13,
            self.entry_equipment_14,
            self.entry_equipment_15,
            self.entry_equipment_16,
            self.entry_equipment_17,
            self.entry_equipment_18,
            self.entry_equipment_19,
            self.entry_equipment_20,
            self.entry_equipment_21,
            self.entry_equipment_22,
            self.entry_equipment_23,
            self.entry_equipment_24,
            self.entry_equipment_25,
            self.entry_equipment_26,
            self.entry_equipment_27,
            self.entry_equipment_28,
            self.entry_equipment_29,
            self.entry_equipment_30,
            self.entry_equipment_31,
            self.entry_equipment_32,
        ]

    def create_buttons(self):
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(fill="both", expand="yes", padx=10, pady=5)

        import_button = tk.Button(
            self.buttons_frame, text="Import from Json", command=self.import_from_json
        )
        import_button.pack(side="left", padx=5, pady=5)
        export_button = tk.Button(
            self.buttons_frame, text="Export to Json", command=self.export_to_json
        )
        export_button.pack(side="left", padx=5, pady=5)

    def export_to_json(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON files", "*.json")]
        )
        if file_path:
            data = {
                "Info": {
                    "Character Name": self.entry_name.get(),
                    "Character Level": self.entry_level.get(),
                    "Classes": self.entry_classes.get(),
                    "Destiny": self.entry_destiny.get(),
                    "Credits": self.entry_credits.get(),
                    "Species": self.entry_species.get(),
                    "Age": self.entry_age.get(),
                    "Height": self.entry_height.get(),
                    "Weight": self.entry_weight.get(),
                    "Gender": self.entry_gender.get(),
                    "Species Info": self.entry_species_info.get(),
                    "Force Points": self.entry_force_points.get(),
                    "Base Attack Bonus": self.entry_base_attack_bonus.get(),
                    "Speed": self.entry_speed.get(),
                    "Destiny Points": self.entry_destiny_points.get(),
                    "Damage Reduction": self.entry_damage_reduction.get(),
                },
                "Languages": {
                    "Language 1": self.entry_language_1.get(),
                    "Language 2": self.entry_language_2.get(),
                    "Language 3": self.entry_language_3.get(),
                    "Language 4": self.entry_language_4.get(),
                    "Language 5": self.entry_language_5.get(),
                    "Language 6": self.entry_language_6.get(),
                    "Language 7": self.entry_language_7.get(),
                    "Language 8": self.entry_language_8.get(),
                    "Language 9": self.entry_language_9.get(),
                    "Language 10": self.entry_language_10.get(),
                },
                "Stats": {
                    "Strength": {
                        "Score": self.entry_strength_score.get(),
                        "Mod": self.entry_strength_mod.get(),
                    },
                    "Dexterity": {
                        "Score": self.entry_dexterity_score.get(),
                        "Mod": self.entry_dexterity_mod.get(),
                    },
                    "Constitution": {
                        "Score": self.entry_constitution_score.get(),
                        "Mod": self.entry_constitution_mod.get(),
                    },
                    "Intelligence": {
                        "Score": self.entry_intelligence_score.get(),
                        "Mod": self.entry_intelligence_mod.get(),
                    },
                    "Wisdom": {
                        "Score": self.entry_wisdom_score.get(),
                        "Mod": self.entry_wisdom_mod.get(),
                    },
                    "Charisma": {
                        "Score": self.entry_charisma_score.get(),
                        "Mod": self.entry_charisma_mod.get(),
                    },
                    "Willpower": {
                        "Score": self.entry_willpower_score.get(),
                        "Mod": self.entry_willpower_mod.get(),
                    },
                },
                "Defenses": {
                    "Fortitude": {
                        "Total": self.entry_fortitude_1.get(),
                        "Class Bonus": self.entry_fortitude_2.get(),
                        "Stat Bonus": self.entry_fortitude_3.get(),
                        "Armor Bonus": self.entry_fortitude_4.get(),
                        "Misc": self.entry_fortitude_5.get(),
                    },
                    "Reflex": {
                        "Total": self.entry_reflex_1.get(),
                        "Class Bonus": self.entry_reflex_2.get(),
                        "Stat Bonus": self.entry_reflex_3.get(),
                        "Armor Bonus": self.entry_reflex_4.get(),
                        "Misc": self.entry_reflex_5.get(),
                    },
                    "Will": {
                        "Total": self.entry_will_1.get(),
                        "Class Bonus": self.entry_will_2.get(),
                        "Stat Bonus": self.entry_will_3.get(),
                        "Armor Bonus": self.entry_will_4.get(),
                        "Misc": self.entry_will_5.get(),
                    },
                },
                "Damage Thresholds": {
                    "Torso": {
                        "Total": self.entry_torso.get(),
                        "Fortitude Bonus": self.entry_fortitude_bonus.get(),
                        "Misc": self.entry_misc.get(),
                    },
                    "Head": {
                        "Total": self.entry_head.get(),
                        "Torso Bonus": self.entry_head_bonus.get(),
                    },
                    "Limbs": {
                        "Total": self.entry_limbs.get(),
                        "Torso Bonus": self.entry_limb_bonus.get(),
                    },
                },
                "Armor": {
                    "Armor Name": self.entry_armor.get(),
                    "Fortitude Bonus": self.entry_fortitude_bonus.get(),
                    "Reflex Bonus": self.entry_reflex_bonus.get(),
                    "Max Dex Bonus": self.entry_max_dex_bonus.get(),
                    "Additional Affects": self.entry_additional_affects.get(),
                },
                "Weapons": {
                    "Weapon 1": {
                        "Weapon Name": self.entry_weapon_1.get(),
                        "Hit Mod": self.entry_hit_mod_1.get(),
                        "Damage": self.entry_damage_1.get(),
                        "Range": self.entry_range_1.get(),
                        "Crit Range": self.entry_crit_range_1.get(),
                    },
                    "Weapon 2": {
                        "Weapon Name": self.entry_weapon_2.get(),
                        "Hit Mod": self.entry_hit_mod_2.get(),
                        "Damage": self.entry_damage_2.get(),
                        "Range": self.entry_range_2.get(),
                        "Crit Range": self.entry_crit_range_2.get(),
                    },
                    "Weapon 3": {
                        "Weapon Name": self.entry_weapon_3.get(),
                        "Hit Mod": self.entry_hit_mod_3.get(),
                        "Damage": self.entry_damage_3.get(),
                        "Range": self.entry_range_3.get(),
                        "Crit Range": self.entry_crit_range_3.get(),
                    },
                    "Weapon 4": {
                        "Weapon Name": self.entry_weapon_4.get(),
                        "Hit Mod": self.entry_hit_mod_4.get(),
                        "Damage": self.entry_damage_4.get(),
                        "Range": self.entry_range_4.get(),
                        "Crit Range": self.entry_crit_range_4.get(),
                    },
                    "Weapon 5": {
                        "Weapon Name": self.entry_weapon_5.get(),
                        "Hit Mod": self.entry_hit_mod_5.get(),
                        "Damage": self.entry_damage_5.get(),
                        "Range": self.entry_range_5.get(),
                        "Crit Range": self.entry_crit_range_5.get(),
                    },
                },
                "Skills": {
                    "Acrobatics": {
                        "Stat": "Dex",
                        "Total": self.entry_acro_modifier.get(),
                        "Training": self.entry_acro_training.get(),
                        "Focus": self.entry_acro_focus.get(),
                    },
                    "Climb": {
                        "Stat": "Str",
                        "Total": self.entry_climb_modifier.get(),
                        "Training": self.entry_climb_training.get(),
                        "Focus": self.entry_climb_focus.get(),
                    },
                    "Deception": {
                        "Stat": "Cha",
                        "Total": self.entry_deception_modifier.get(),
                        "Training": self.entry_deception_training.get(),
                        "Focus": self.entry_deception_focus.get(),
                    },
                    "Endurance": {
                        "Stat": "Con",
                        "Total": self.entry_endurance_modifier.get(),
                        "Training": self.entry_endurance_training.get(),
                        "Focus": self.entry_endurance_focus.get(),
                    },
                    "Gather Information": {
                        "Stat": "Cha",
                        "Total": self.entry_gather_information_modifier.get(),
                        "Training": self.entry_gather_information_training.get(),
                        "Focus": self.entry_gather_information_focus.get(),
                    },
                    "Initiative": {
                        "Stat": "Dex",
                        "Total": self.entry_initiative_modifier.get(),
                        "Training": self.entry_initiative_training.get(),
                        "Focus": self.entry_initiative_focus.get(),
                    },
                    "Jump": {
                        "Stat": "Str",
                        "Total": self.entry_jump_modifier.get(),
                        "Training": self.entry_jump_training.get(),
                        "Focus": self.entry_jump_focus.get(),
                    },
                    "Knowledge": {
                        "Stat": "Int",
                        "Type": {
                            "Bureaucracy": {
                                "Total": self.entry_knowledge_bureaucracy_modifier.get(),
                                "Training": self.entry_knowledge_bureaucracy_training.get(),
                                "Focus": self.entry_knowledge_bureaucracy_focus.get(),
                            },
                            "Galactic Lore": {
                                "Total": self.entry_knowledge_galactic_lore_modifier.get(),
                                "Training": self.entry_knowledge_galactic_lore_training.get(),
                                "Focus": self.entry_knowledge_galactic_lore_focus.get(),
                            },
                            "Life Science": {
                                "Total": self.entry_knowledge_life_science_modifier.get(),
                                "Training": self.entry_knowledge_life_science_training.get(),
                                "Focus": self.entry_knowledge_life_science_focus.get(),
                            },
                            "Physical Science": {
                                "Total": self.entry_knowledge_physical_science_modifier.get(),
                                "Training": self.entry_knowledge_physical_science_training.get(),
                                "Focus": self.entry_knowledge_physical_science_focus.get(),
                            },
                            "Social Science": {
                                "Total": self.entry_knowledge_social_science_modifier.get(),
                                "Training": self.entry_knowledge_social_science_training.get(),
                                "Focus": self.entry_knowledge_social_science_focus.get(),
                            },
                            "Tactics": {
                                "Total": self.entry_knowledge_tactics_modifier.get(),
                                "Training": self.entry_knowledge_tactics_training.get(),
                                "Focus": self.entry_knowledge_tactics_focus.get(),
                            },
                            "Technology": {
                                "Total": self.entry_knowledge_technology_modifier.get(),
                                "Training": self.entry_knowledge_technology_training.get(),
                                "Focus": self.entry_knowledge_technology_focus.get(),
                            },
                        },
                    },
                    "Mechanics": {
                        "Stat": "Int",
                        "Total": self.entry_mechanics_modifier.get(),
                        "Training": self.entry_mechanics_training.get(),
                        "Focus": self.entry_mechanics_focus.get(),
                    },
                    "Perception": {
                        "Stat": "Wis",
                        "Total": self.entry_perception_modifier.get(),
                        "Training": self.entry_perception_training.get(),
                        "Focus": self.entry_perception_focus.get(),
                    },
                    "Persuasion": {
                        "Stat": "Cha",
                        "Total": self.entry_persuasion_modifier.get(),
                        "Training": self.entry_persuasion_training.get(),
                        "Focus": self.entry_persuasion_focus.get(),
                    },
                    "Pilot": {
                        "Stat": "Dex",
                        "Total": self.entry_pilot_modifier.get(),
                        "Training": self.entry_pilot_training.get(),
                        "Focus": self.entry_pilot_focus.get(),
                    },
                    "Ride": {
                        "Stat": "Dex",
                        "Total": self.entry_ride_modifier.get(),
                        "Training": self.entry_ride_training.get(),
                        "Focus": self.entry_ride_focus.get(),
                    },
                    "Stealth": {
                        "Stat": "Dex",
                        "Total": self.entry_stealth_modifier.get(),
                        "Training": self.entry_stealth_training.get(),
                        "Focus": self.entry_stealth_focus.get(),
                    },
                    "Survival": {
                        "Stat": "Wis",
                        "Total": self.entry_survival_modifier.get(),
                        "Training": self.entry_survival_training.get(),
                        "Focus": self.entry_survival_focus.get(),
                    },
                    "Swim": {
                        "Stat": "Str",
                        "Total": self.entry_swim_modifier.get(),
                        "Training": self.entry_swim_training.get(),
                        "Focus": self.entry_swim_focus.get(),
                    },
                    "Treat Injury": {
                        "Stat": "Int",
                        "Total": self.entry_treat_injury_modifier.get(),
                        "Training": self.entry_treat_injury_training.get(),
                        "Focus": self.entry_treat_injury_focus.get(),
                    },
                    "Use Computer": {
                        "Stat": "Int",
                        "Total": self.entry_use_computer_modifier.get(),
                        "Training": self.entry_use_computer_training.get(),
                        "Focus": self.entry_use_computer_focus.get(),
                    },
                    "Use the Force": {
                        "Stat": "Cha/Will",
                        "Total": self.entry_use_the_force_modifier.get(),
                        "Training": self.entry_use_the_force_training.get(),
                        "Focus": self.entry_use_the_force_focus.get(),
                    },
                },
                "Force Schools": {
                    "Force School": {
                        "Alchemy": {
                            "Total": self.entry_alchemy_modifier.get(),
                            "Training 1": self.entry_alchemy_1.get(),
                            "Training 2": self.entry_alchemy_2.get(),
                            "Training 3": self.entry_alchemy_3.get(),
                        },
                        "Augmentation": {
                            "Total": self.entry_augmentation_modifier.get(),
                            "Training 1": self.entry_augmentation_1.get(),
                            "Training 2": self.entry_augmentation_2.get(),
                            "Training 3": self.entry_augmentation_3.get(),
                        },
                        "Cognition": {
                            "Total": self.entry_cognition_modifier.get(),
                            "Training 1": self.entry_cognition_1.get(),
                            "Training 2": self.entry_cognition_2.get(),
                            "Training 3": self.entry_cognition_3.get(),
                        },
                        "Sorcery": {
                            "Total": self.entry_sorcery_modifier.get(),
                            "Training 1": self.entry_sorcery_1.get(),
                            "Training 2": self.entry_sorcery_2.get(),
                            "Training 3": self.entry_sorcery_3.get(),
                        },
                        "Technokinesis": {
                            "Total": self.entry_technokinesis_modifier.get(),
                            "Training 1": self.entry_technokinesis_1.get(),
                            "Training 2": self.entry_technokinesis_2.get(),
                            "Training 3": self.entry_technokinesis_3.get(),
                        },
                        "Telekinesis": {
                            "Total": self.entry_telekinesis_modifier.get(),
                            "Training 1": self.entry_telekinesis_1.get(),
                            "Training 2": self.entry_telekinesis_2.get(),
                            "Training 3": self.entry_telekinesis_3.get(),
                        },
                        "Vitalism": {
                            "Total": self.entry_vitalism_modifier.get(),
                            "Training 1": self.entry_vitalism_1.get(),
                            "Training 2": self.entry_vitalism_2.get(),
                            "Training 3": self.entry_vitalism_3.get(),
                        },
                    },
                    "Force Uses": self.entry_force_uses.get(),
                },
                "Force Techniques": {
                    "Force Technique 1": self.entry_force_tech_1.get(),
                    "Force Technique 2": self.entry_force_tech_2.get(),
                    "Force Technique 3": self.entry_force_tech_3.get(),
                    "Force Technique 4": self.entry_force_tech_4.get(),
                    "Force Technique 5": self.entry_force_tech_5.get(),
                    "Force Technique 6": self.entry_force_tech_6.get(),
                    "Force Technique 7": self.entry_force_tech_7.get(),
                    "Force Technique 8": self.entry_force_tech_8.get(),
                    "Force Technique 9": self.entry_force_tech_9.get(),
                    "Force Technique 10": self.entry_force_tech_10.get(),
                    "Force Technique 11": self.entry_force_tech_11.get(),
                    "Force Technique 12": self.entry_force_tech_12.get(),
                    "Force Technique 13": self.entry_force_tech_13.get(),
                    "Force Technique 14": self.entry_force_tech_14.get(),
                    "Force Technique 15": self.entry_force_tech_15.get(),
                },
                "Force Secrets": {
                    "Force Secret 1": self.entry_force_secret_1.get(),
                    "Force Secret 2": self.entry_force_secret_2.get(),
                    "Force Secret 3": self.entry_force_secret_3.get(),
                    "Force Secret 4": self.entry_force_secret_4.get(),
                    "Force Secret 5": self.entry_force_secret_5.get(),
                    "Force Secret 6": self.entry_force_secret_6.get(),
                    "Force Secret 7": self.entry_force_secret_7.get(),
                    "Force Secret 8": self.entry_force_secret_8.get(),
                    "Force Secret 9": self.entry_force_secret_9.get(),
                    "Force Secret 10": self.entry_force_secret_10.get(),
                    "Force Secret 11": self.entry_force_secret_11.get(),
                    "Force Secret 12": self.entry_force_secret_12.get(),
                    "Force Secret 13": self.entry_force_secret_13.get(),
                    "Force Secret 14": self.entry_force_secret_14.get(),
                    "Force Secret 15": self.entry_force_secret_15.get(),
                },
                "Feats": {
                    "Feat 1": self.entry_feats_1.get(),
                    "Feat 2": self.entry_feats_2.get(),
                    "Feat 3": self.entry_feats_3.get(),
                    "Feat 4": self.entry_feats_4.get(),
                    "Feat 5": self.entry_feats_5.get(),
                    "Feat 6": self.entry_feats_6.get(),
                    "Feat 7": self.entry_feats_7.get(),
                    "Feat 8": self.entry_feats_8.get(),
                    "Feat 9": self.entry_feats_9.get(),
                    "Feat 10": self.entry_feats_10.get(),
                    "Feat 11": self.entry_feats_11.get(),
                    "Feat 12": self.entry_feats_12.get(),
                    "Feat 13": self.entry_feats_13.get(),
                    "Feat 14": self.entry_feats_14.get(),
                    "Feat 15": self.entry_feats_15.get(),
                },
                "Talents": {
                    "Talent 1": self.entry_talents_1.get(),
                    "Talent 2": self.entry_talents_2.get(),
                    "Talent 3": self.entry_talents_3.get(),
                    "Talent 4": self.entry_talents_4.get(),
                    "Talent 5": self.entry_talents_5.get(),
                    "Talent 6": self.entry_talents_6.get(),
                    "Talent 7": self.entry_talents_7.get(),
                    "Talent 8": self.entry_talents_8.get(),
                    "Talent 9": self.entry_talents_9.get(),
                    "Talent 10": self.entry_talents_10.get(),
                    "Talent 11": self.entry_talents_11.get(),
                    "Talent 12": self.entry_talents_12.get(),
                    "Talent 13": self.entry_talents_13.get(),
                    "Talent 14": self.entry_talents_14.get(),
                    "Talent 15": self.entry_talents_15.get(),
                },
                "Equipment": {
                    "Equipment 1": self.entry_equipment_1.get(),
                    "Equipment 2": self.entry_equipment_2.get(),
                    "Equipment 3": self.entry_equipment_3.get(),
                    "Equipment 4": self.entry_equipment_4.get(),
                    "Equipment 5": self.entry_equipment_5.get(),
                    "Equipment 6": self.entry_equipment_6.get(),
                    "Equipment 7": self.entry_equipment_7.get(),
                    "Equipment 8": self.entry_equipment_8.get(),
                    "Equipment 9": self.entry_equipment_9.get(),
                    "Equipment 10": self.entry_equipment_10.get(),
                    "Equipment 11": self.entry_equipment_11.get(),
                    "Equipment 12": self.entry_equipment_12.get(),
                    "Equipment 13": self.entry_equipment_13.get(),
                    "Equipment 14": self.entry_equipment_14.get(),
                    "Equipment 15": self.entry_equipment_15.get(),
                    "Equipment 16": self.entry_equipment_16.get(),
                    "Equipment 17": self.entry_equipment_17.get(),
                    "Equipment 18": self.entry_equipment_18.get(),
                    "Equipment 19": self.entry_equipment_19.get(),
                    "Equipment 20": self.entry_equipment_20.get(),
                    "Equipment 21": self.entry_equipment_21.get(),
                    "Equipment 22": self.entry_equipment_22.get(),
                    "Equipment 23": self.entry_equipment_23.get(),
                    "Equipment 24": self.entry_equipment_24.get(),
                    "Equipment 25": self.entry_equipment_25.get(),
                    "Equipment 26": self.entry_equipment_26.get(),
                    "Equipment 27": self.entry_equipment_27.get(),
                    "Equipment 28": self.entry_equipment_28.get(),
                    "Equipment 29": self.entry_equipment_29.get(),
                    "Equipment 30": self.entry_equipment_30.get(),
                    "Equipment 31": self.entry_equipment_31.get(),
                    "Equipment 32": self.entry_equipment_32.get(),
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
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, data["Info"]["Character Name"])

            self.entry_level.delete(0, tk.END)
            self.entry_level.insert(0, data["Info"]["Character Level"])

            self.entry_classes.delete(0, tk.END)
            self.entry_classes.insert(0, data["Info"]["Classes"])

            self.entry_destiny.delete(0, tk.END)
            self.entry_destiny.insert(0, data["Info"]["Destiny"])

            self.entry_credits.delete(0, tk.END)
            self.entry_credits.insert(0, data["Info"]["Credits"])

            self.entry_species.delete(0, tk.END)
            self.entry_species.insert(0, data["Info"]["Species"])

            self.entry_age.delete(0, tk.END)
            self.entry_age.insert(0, data["Info"]["Age"])

            self.entry_height.delete(0, tk.END)
            self.entry_height.insert(0, data["Info"]["Height"])

            self.entry_weight.delete(0, tk.END)
            self.entry_weight.insert(0, data["Info"]["Weight"])

            self.entry_gender.delete(0, tk.END)
            self.entry_gender.insert(0, data["Info"]["Gender"])

            self.entry_species_info.delete(0, tk.END)
            self.entry_species_info.insert(0, data["Info"]["Species Info"])

            self.entry_force_points.delete(0, tk.END)
            self.entry_force_points.insert(0, data["Info"]["Force Points"])

            self.entry_base_attack_bonus.delete(0, tk.END)
            self.entry_base_attack_bonus.insert(0, data["Info"]["Base Attack Bonus"])

            self.entry_speed.delete(0, tk.END)
            self.entry_speed.insert(0, data["Info"]["Speed"])

            self.entry_destiny_points.delete(0, tk.END)
            self.entry_destiny_points.insert(0, data["Info"]["Destiny Points"])

            self.entry_damage_reduction.delete(0, tk.END)
            self.entry_damage_reduction.insert(0, data["Info"]["Damage Reduction"])

            # Languages
            for i in range(10):
                language_key = f"Language {i+1}"
                entry = getattr(self, f"entry_language_{i+1}")
                entry.delete(0, tk.END)
                entry.insert(0, data["Languages"][language_key])

            # Stats
            self.entry_strength_score.delete(0, tk.END)
            self.entry_strength_score.insert(0, data["Stats"]["Strength"]["Score"])

            self.entry_strength_mod.delete(0, tk.END)
            self.entry_strength_mod.insert(0, data["Stats"]["Strength"]["Mod"])

            self.entry_dexterity_score.delete(0, tk.END)
            self.entry_dexterity_score.insert(0, data["Stats"]["Dexterity"]["Score"])

            self.entry_dexterity_mod.delete(0, tk.END)
            self.entry_dexterity_mod.insert(0, data["Stats"]["Dexterity"]["Mod"])

            self.entry_constitution_score.delete(0, tk.END)
            self.entry_constitution_score.insert(
                0, data["Stats"]["Constitution"]["Score"]
            )

            self.entry_constitution_mod.delete(0, tk.END)
            self.entry_constitution_mod.insert(0, data["Stats"]["Constitution"]["Mod"])

            self.entry_intelligence_score.delete(0, tk.END)
            self.entry_intelligence_score.insert(
                0, data["Stats"]["Intelligence"]["Score"]
            )

            self.entry_intelligence_mod.delete(0, tk.END)
            self.entry_intelligence_mod.insert(0, data["Stats"]["Intelligence"]["Mod"])

            self.entry_wisdom_score.delete(0, tk.END)
            self.entry_wisdom_score.insert(0, data["Stats"]["Wisdom"]["Score"])

            self.entry_wisdom_mod.delete(0, tk.END)
            self.entry_wisdom_mod.insert(0, data["Stats"]["Wisdom"]["Mod"])

            self.entry_charisma_score.delete(0, tk.END)
            self.entry_charisma_score.insert(0, data["Stats"]["Charisma"]["Score"])

            self.entry_charisma_mod.delete(0, tk.END)
            self.entry_charisma_mod.insert(0, data["Stats"]["Charisma"]["Mod"])

            self.entry_willpower_score.delete(0, tk.END)
            self.entry_willpower_score.insert(0, data["Stats"]["Willpower"]["Score"])

            self.entry_willpower_mod.delete(0, tk.END)
            self.entry_willpower_mod.insert(0, data["Stats"]["Willpower"]["Mod"])

            # Defenses
            self.entry_fortitude_1.delete(0, tk.END)
            self.entry_fortitude_1.insert(0, data["Defenses"]["Fortitude"]["Total"])

            self.entry_fortitude_2.delete(0, tk.END)
            self.entry_fortitude_2.insert(
                0, data["Defenses"]["Fortitude"]["Class Bonus"]
            )

            self.entry_fortitude_3.delete(0, tk.END)
            self.entry_fortitude_3.insert(
                0, data["Defenses"]["Fortitude"]["Stat Bonus"]
            )

            self.entry_fortitude_4.delete(0, tk.END)
            self.entry_fortitude_4.insert(
                0, data["Defenses"]["Fortitude"]["Armor Bonus"]
            )

            self.entry_fortitude_5.delete(0, tk.END)
            self.entry_fortitude_5.insert(0, data["Defenses"]["Fortitude"]["Misc"])

            self.entry_reflex_1.delete(0, tk.END)
            self.entry_reflex_1.insert(0, data["Defenses"]["Reflex"]["Total"])

            self.entry_reflex_2.delete(0, tk.END)
            self.entry_reflex_2.insert(0, data["Defenses"]["Reflex"]["Class Bonus"])

            self.entry_reflex_3.delete(0, tk.END)
            self.entry_reflex_3.insert(0, data["Defenses"]["Reflex"]["Stat Bonus"])

            self.entry_reflex_4.delete(0, tk.END)
            self.entry_reflex_4.insert(0, data["Defenses"]["Reflex"]["Armor Bonus"])

            self.entry_reflex_5.delete(0, tk.END)
            self.entry_reflex_5.insert(0, data["Defenses"]["Reflex"]["Misc"])

            self.entry_will_1.delete(0, tk.END)
            self.entry_will_1.insert(0, data["Defenses"]["Will"]["Total"])

            self.entry_will_2.delete(0, tk.END)
            self.entry_will_2.insert(0, data["Defenses"]["Will"]["Class Bonus"])

            self.entry_will_3.delete(0, tk.END)
            self.entry_will_3.insert(0, data["Defenses"]["Will"]["Stat Bonus"])

            self.entry_will_4.delete(0, tk.END)
            self.entry_will_4.insert(0, data["Defenses"]["Will"]["Armor Bonus"])

            self.entry_will_5.delete(0, tk.END)
            self.entry_will_5.insert(0, data["Defenses"]["Will"]["Misc"])

            # Damage Thresholds
            self.entry_torso.delete(0, tk.END)
            self.entry_torso.insert(0, data["Damage Thresholds"]["Torso"]["Total"])

            self.entry_fortitude.delete(0, tk.END)
            self.entry_fortitude.insert(
                0, data["Damage Thresholds"]["Torso"]["Fortitude Bonus"]
            )

            self.entry_misc.delete(0, tk.END)
            self.entry_misc.insert(0, data["Damage Thresholds"]["Torso"]["Misc"])

            self.entry_head.delete(0, tk.END)
            self.entry_head.insert(0, data["Damage Thresholds"]["Head"]["Total"])

            self.entry_head_bonus.delete(0, tk.END)
            self.entry_head_bonus.insert(
                0, data["Damage Thresholds"]["Head"]["Torso Bonus"]
            )

            self.entry_limbs.delete(0, tk.END)
            self.entry_limbs.insert(0, data["Damage Thresholds"]["Limbs"]["Total"])

            self.entry_limb_bonus.delete(0, tk.END)
            self.entry_limb_bonus.insert(
                0, data["Damage Thresholds"]["Limbs"]["Torso Bonus"]
            )

            # Armor
            self.entry_armor.delete(0, tk.END)
            self.entry_armor.insert(0, data["Armor"]["Armor Name"])

            self.entry_fortitude_bonus.delete(0, tk.END)
            self.entry_fortitude_bonus.insert(0, data["Armor"]["Fortitude Bonus"])

            self.entry_reflex_bonus.delete(0, tk.END)
            self.entry_reflex_bonus.insert(0, data["Armor"]["Reflex Bonus"])

            self.entry_max_dex_bonus.delete(0, tk.END)
            self.entry_max_dex_bonus.insert(0, data["Armor"]["Max Dex Bonus"])

            self.entry_additional_affects.delete(0, tk.END)
            self.entry_additional_affects.insert(0, data["Armor"]["Additional Affects"])

            # Weapons
            self.entry_weapon_1.delete(0, tk.END)
            self.entry_weapon_1.insert(0, data["Weapons"]["Weapon 1"]["Weapon Name"])

            self.entry_hit_mod_1.delete(0, tk.END)
            self.entry_hit_mod_1.insert(0, data["Weapons"]["Weapon 1"]["Hit Mod"])

            self.entry_damage_1.delete(0, tk.END)
            self.entry_damage_1.insert(0, data["Weapons"]["Weapon 1"]["Damage"])

            self.entry_range_1.delete(0, tk.END)
            self.entry_range_1.insert(0, data["Weapons"]["Weapon 1"]["Range"])

            self.entry_crit_range_1.delete(0, tk.END)
            self.entry_crit_range_1.insert(0, data["Weapons"]["Weapon 1"]["Crit Range"])

            self.entry_weapon_2.delete(0, tk.END)
            self.entry_weapon_2.insert(0, data["Weapons"]["Weapon 2"]["Weapon Name"])

            self.entry_hit_mod_2.delete(0, tk.END)
            self.entry_hit_mod_2.insert(0, data["Weapons"]["Weapon 2"]["Hit Mod"])

            self.entry_damage_2.delete(0, tk.END)
            self.entry_damage_2.insert(0, data["Weapons"]["Weapon 2"]["Damage"])

            self.entry_range_2.delete(0, tk.END)
            self.entry_range_2.insert(0, data["Weapons"]["Weapon 2"]["Range"])

            self.entry_crit_range_2.delete(0, tk.END)
            self.entry_crit_range_2.insert(0, data["Weapons"]["Weapon 2"]["Crit Range"])

            self.entry_weapon_3.delete(0, tk.END)
            self.entry_weapon_3.insert(0, data["Weapons"]["Weapon 3"]["Weapon Name"])

            self.entry_hit_mod_3.delete(0, tk.END)
            self.entry_hit_mod_3.insert(0, data["Weapons"]["Weapon 3"]["Hit Mod"])

            self.entry_damage_3.delete(0, tk.END)
            self.entry_damage_3.insert(0, data["Weapons"]["Weapon 3"]["Damage"])

            self.entry_range_3.delete(0, tk.END)
            self.entry_range_3.insert(0, data["Weapons"]["Weapon 3"]["Range"])

            self.entry_crit_range_3.delete(0, tk.END)
            self.entry_crit_range_3.insert(0, data["Weapons"]["Weapon 3"]["Crit Range"])

            self.entry_weapon_4.delete(0, tk.END)
            self.entry_weapon_4.insert(0, data["Weapons"]["Weapon 4"]["Weapon Name"])

            self.entry_hit_mod_4.delete(0, tk.END)
            self.entry_hit_mod_4.insert(0, data["Weapons"]["Weapon 4"]["Hit Mod"])

            self.entry_damage_4.delete(0, tk.END)
            self.entry_damage_4.insert(0, data["Weapons"]["Weapon 4"]["Damage"])

            self.entry_range_4.delete(0, tk.END)
            self.entry_range_4.insert(0, data["Weapons"]["Weapon 4"]["Range"])

            self.entry_crit_range_4.delete(0, tk.END)
            self.entry_crit_range_4.insert(0, data["Weapons"]["Weapon 4"]["Crit Range"])

            self.entry_weapon_5.delete(0, tk.END)
            self.entry_weapon_5.insert(0, data["Weapons"]["Weapon 5"]["Weapon Name"])

            self.entry_hit_mod_5.delete(0, tk.END)
            self.entry_hit_mod_5.insert(0, data["Weapons"]["Weapon 5"]["Hit Mod"])

            self.entry_damage_5.delete(0, tk.END)
            self.entry_damage_5.insert(0, data["Weapons"]["Weapon 5"]["Damage"])

            self.entry_range_5.delete(0, tk.END)
            self.entry_range_5.insert(0, data["Weapons"]["Weapon 5"]["Range"])

            self.entry_crit_range_5.delete(0, tk.END)
            self.entry_crit_range_5.insert(0, data["Weapons"]["Weapon 5"]["Crit Range"])

            # Skills
            self.entry_acro_training.delete(0, tk.END)
            self.entry_acro_training.insert(0, data["Skills"]["Acrobatics"]["Training"])

            self.entry_acro_focus.delete(0, tk.END)
            self.entry_acro_focus.insert(0, data["Skills"]["Acrobatics"]["Focus"])

            self.entry_acro_modifier.delete(0, tk.END)
            self.entry_acro_modifier.insert(0, data["Skills"]["Acrobatics"]["Total"])

            self.entry_climb_training.delete(0, tk.END)
            self.entry_climb_training.insert(0, data["Skills"]["Climb"]["Training"])

            self.entry_climb_focus.delete(0, tk.END)
            self.entry_climb_focus.insert(0, data["Skills"]["Climb"]["Focus"])

            self.entry_climb_modifier.delete(0, tk.END)
            self.entry_climb_modifier.insert(0, data["Skills"]["Climb"]["Total"])

            self.entry_deception_training.delete(0, tk.END)
            self.entry_deception_training.insert(
                0, data["Skills"]["Deception"]["Training"]
            )

            self.entry_deception_focus.delete(0, tk.END)
            self.entry_deception_focus.insert(0, data["Skills"]["Deception"]["Focus"])

            self.entry_deception_modifier.delete(0, tk.END)
            self.entry_deception_modifier.insert(
                0, data["Skills"]["Deception"]["Total"]
            )

            self.entry_endurance_training.delete(0, tk.END)
            self.entry_endurance_training.insert(
                0, data["Skills"]["Endurance"]["Training"]
            )

            self.entry_endurance_focus.delete(0, tk.END)
            self.entry_endurance_focus.insert(0, data["Skills"]["Endurance"]["Focus"])

            self.entry_endurance_modifier.delete(0, tk.END)
            self.entry_endurance_modifier.insert(
                0, data["Skills"]["Endurance"]["Total"]
            )

            self.entry_gather_information_training.delete(0, tk.END)
            self.entry_gather_information_training.insert(
                0, data["Skills"]["Gather Information"]["Training"]
            )

            self.entry_gather_information_focus.delete(0, tk.END)
            self.entry_gather_information_focus.insert(
                0, data["Skills"]["Gather Information"]["Focus"]
            )

            self.entry_gather_information_modifier.delete(0, tk.END)
            self.entry_gather_information_modifier.insert(
                0, data["Skills"]["Gather Information"]["Total"]
            )

            self.entry_initiative_training.delete(0, tk.END)
            self.entry_initiative_training.insert(
                0, data["Skills"]["Initiative"]["Training"]
            )

            self.entry_initiative_focus.delete(0, tk.END)
            self.entry_initiative_focus.insert(0, data["Skills"]["Initiative"]["Focus"])

            self.entry_initiative_modifier.delete(0, tk.END)
            self.entry_initiative_modifier.insert(
                0, data["Skills"]["Initiative"]["Total"]
            )

            self.entry_jump_training.delete(0, tk.END)
            self.entry_jump_training.insert(0, data["Skills"]["Jump"]["Training"])

            self.entry_jump_focus.delete(0, tk.END)
            self.entry_jump_focus.insert(0, data["Skills"]["Jump"]["Focus"])

            self.entry_jump_modifier.delete(0, tk.END)
            self.entry_jump_modifier.insert(0, data["Skills"]["Jump"]["Total"])

            self.entry_knowledge_bureaucracy_training.delete(0, tk.END)
            self.entry_knowledge_bureaucracy_training.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Bureaucracy"]["Training"]
            )

            self.entry_knowledge_bureaucracy_focus.delete(0, tk.END)
            self.entry_knowledge_bureaucracy_focus.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Bureaucracy"]["Focus"]
            )

            self.entry_knowledge_bureaucracy_modifier.delete(0, tk.END)
            self.entry_knowledge_bureaucracy_modifier.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Bureaucracy"]["Total"]
            )

            self.entry_knowledge_galactic_lore_training.delete(0, tk.END)
            self.entry_knowledge_galactic_lore_training.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Galactic Lore"]["Training"]
            )

            self.entry_knowledge_galactic_lore_focus.delete(0, tk.END)
            self.entry_knowledge_galactic_lore_focus.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Galactic Lore"]["Focus"]
            )

            self.entry_knowledge_galactic_lore_modifier.delete(0, tk.END)
            self.entry_knowledge_galactic_lore_modifier.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Galactic Lore"]["Total"]
            )

            self.entry_knowledge_life_science_training.delete(0, tk.END)
            self.entry_knowledge_life_science_training.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Life Science"]["Training"]
            )

            self.entry_knowledge_life_science_focus.delete(0, tk.END)
            self.entry_knowledge_life_science_focus.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Life Science"]["Focus"]
            )

            self.entry_knowledge_life_science_modifier.delete(0, tk.END)
            self.entry_knowledge_life_science_modifier.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Life Science"]["Total"]
            )

            self.entry_knowledge_physical_science_training.delete(0, tk.END)
            self.entry_knowledge_physical_science_training.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Physical Science"]["Training"]
            )

            self.entry_knowledge_physical_science_focus.delete(0, tk.END)
            self.entry_knowledge_physical_science_focus.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Physical Science"]["Focus"]
            )

            self.entry_knowledge_physical_science_modifier.delete(0, tk.END)
            self.entry_knowledge_physical_science_modifier.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Physical Science"]["Total"]
            )

            self.entry_knowledge_social_science_training.delete(0, tk.END)
            self.entry_knowledge_social_science_training.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Social Science"]["Training"]
            )

            self.entry_knowledge_social_science_focus.delete(0, tk.END)
            self.entry_knowledge_social_science_focus.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Social Science"]["Focus"]
            )

            self.entry_knowledge_social_science_modifier.delete(0, tk.END)
            self.entry_knowledge_social_science_modifier.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Social Science"]["Total"]
            )

            self.entry_knowledge_tactics_training.delete(0, tk.END)
            self.entry_knowledge_tactics_training.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Tactics"]["Training"]
            )

            self.entry_knowledge_tactics_focus.delete(0, tk.END)
            self.entry_knowledge_tactics_focus.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Tactics"]["Focus"]
            )

            self.entry_knowledge_tactics_modifier.delete(0, tk.END)
            self.entry_knowledge_tactics_modifier.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Tactics"]["Total"]
            )

            self.entry_knowledge_technology_training.delete(0, tk.END)
            self.entry_knowledge_technology_training.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Technology"]["Training"]
            )

            self.entry_knowledge_technology_focus.delete(0, tk.END)
            self.entry_knowledge_technology_focus.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Technology"]["Focus"]
            )

            self.entry_knowledge_technology_modifier.delete(0, tk.END)
            self.entry_knowledge_technology_modifier.insert(
                0, data["Skills"]["Knowledge"]["Type"]["Technology"]["Total"]
            )

            self.entry_mechanics_training.delete(0, tk.END)
            self.entry_mechanics_training.insert(
                0, data["Skills"]["Mechanics"]["Training"]
            )

            self.entry_mechanics_focus.delete(0, tk.END)
            self.entry_mechanics_focus.insert(0, data["Skills"]["Mechanics"]["Focus"])

            self.entry_mechanics_modifier.delete(0, tk.END)
            self.entry_mechanics_modifier.insert(
                0, data["Skills"]["Mechanics"]["Total"]
            )

            self.entry_perception_training.delete(0, tk.END)
            self.entry_perception_training.insert(
                0, data["Skills"]["Perception"]["Training"]
            )

            self.entry_perception_focus.delete(0, tk.END)
            self.entry_perception_focus.insert(0, data["Skills"]["Perception"]["Focus"])

            self.entry_perception_modifier.delete(0, tk.END)
            self.entry_perception_modifier.insert(
                0, data["Skills"]["Perception"]["Total"]
            )

            self.entry_persuasion_training.delete(0, tk.END)
            self.entry_persuasion_training.insert(
                0, data["Skills"]["Persuasion"]["Training"]
            )

            self.entry_persuasion_focus.delete(0, tk.END)
            self.entry_persuasion_focus.insert(0, data["Skills"]["Persuasion"]["Focus"])

            self.entry_persuasion_modifier.delete(0, tk.END)
            self.entry_persuasion_modifier.insert(
                0, data["Skills"]["Persuasion"]["Total"]
            )

            self.entry_pilot_training.delete(0, tk.END)
            self.entry_pilot_training.insert(0, data["Skills"]["Pilot"]["Training"])

            self.entry_pilot_focus.delete(0, tk.END)
            self.entry_pilot_focus.insert(0, data["Skills"]["Pilot"]["Focus"])

            self.entry_pilot_modifier.delete(0, tk.END)
            self.entry_pilot_modifier.insert(0, data["Skills"]["Pilot"]["Total"])

            self.entry_ride_training.delete(0, tk.END)
            self.entry_ride_training.insert(0, data["Skills"]["Ride"]["Training"])

            self.entry_ride_focus.delete(0, tk.END)
            self.entry_ride_focus.insert(0, data["Skills"]["Ride"]["Focus"])

            self.entry_ride_modifier.delete(0, tk.END)
            self.entry_ride_modifier.insert(0, data["Skills"]["Ride"]["Total"])

            self.entry_stealth_training.delete(0, tk.END)
            self.entry_stealth_training.insert(0, data["Skills"]["Stealth"]["Training"])

            self.entry_stealth_focus.delete(0, tk.END)
            self.entry_stealth_focus.insert(0, data["Skills"]["Stealth"]["Focus"])

            self.entry_stealth_modifier.delete(0, tk.END)
            self.entry_stealth_modifier.insert(0, data["Skills"]["Stealth"]["Total"])

            self.entry_survival_training.delete(0, tk.END)
            self.entry_survival_training.insert(
                0, data["Skills"]["Survival"]["Training"]
            )

            self.entry_survival_focus.delete(0, tk.END)
            self.entry_survival_focus.insert(0, data["Skills"]["Survival"]["Focus"])

            self.entry_survival_modifier.delete(0, tk.END)
            self.entry_survival_modifier.insert(0, data["Skills"]["Survival"]["Total"])

            self.entry_swim_training.delete(0, tk.END)
            self.entry_swim_training.insert(0, data["Skills"]["Swim"]["Training"])

            self.entry_swim_focus.delete(0, tk.END)
            self.entry_swim_focus.insert(0, data["Skills"]["Swim"]["Focus"])

            self.entry_swim_modifier.delete(0, tk.END)
            self.entry_swim_modifier.insert(0, data["Skills"]["Swim"]["Total"])

            self.entry_treat_injury_training.delete(0, tk.END)
            self.entry_treat_injury_training.insert(
                0, data["Skills"]["Treat Injury"]["Training"]
            )

            self.entry_treat_injury_focus.delete(0, tk.END)
            self.entry_treat_injury_focus.insert(
                0, data["Skills"]["Treat Injury"]["Focus"]
            )

            self.entry_treat_injury_modifier.delete(0, tk.END)
            self.entry_treat_injury_modifier.insert(
                0, data["Skills"]["Treat Injury"]["Total"]
            )

            self.entry_use_computer_training.delete(0, tk.END)
            self.entry_use_computer_training.insert(
                0, data["Skills"]["Use Computer"]["Training"]
            )

            self.entry_use_computer_focus.delete(0, tk.END)
            self.entry_use_computer_focus.insert(
                0, data["Skills"]["Use Computer"]["Focus"]
            )

            self.entry_use_computer_modifier.delete(0, tk.END)
            self.entry_use_computer_modifier.insert(
                0, data["Skills"]["Use Computer"]["Total"]
            )

            self.entry_use_the_force_training.delete(0, tk.END)
            self.entry_use_the_force_training.insert(
                0, data["Skills"]["Use the Force"]["Training"]
            )

            self.entry_use_the_force_focus.delete(0, tk.END)
            self.entry_use_the_force_focus.insert(
                0, data["Skills"]["Use the Force"]["Focus"]
            )

            self.entry_use_the_force_modifier.delete(0, tk.END)
            self.entry_use_the_force_modifier.insert(
                0, data["Skills"]["Use the Force"]["Total"]
            )

            # Force Schools
            self.entry_alchemy_1.delete(0, tk.END)
            self.entry_alchemy_1.insert(
                0, data["Force Schools"]["Force School"]["Alchemy"]["Training 1"]
            )

            self.entry_alchemy_2.delete(0, tk.END)
            self.entry_alchemy_2.insert(
                0, data["Force Schools"]["Force School"]["Alchemy"]["Training 2"]
            )

            self.entry_alchemy_3.delete(0, tk.END)
            self.entry_alchemy_3.insert(
                0, data["Force Schools"]["Force School"]["Alchemy"]["Training 3"]
            )

            self.entry_alchemy_modifier.delete(0, tk.END)
            self.entry_alchemy_modifier.insert(
                0, data["Force Schools"]["Force School"]["Alchemy"]["Total"]
            )

            self.entry_augmentation_1.delete(0, tk.END)
            self.entry_augmentation_1.insert(
                0, data["Force Schools"]["Force School"]["Augmentation"]["Training 1"]
            )

            self.entry_augmentation_2.delete(0, tk.END)
            self.entry_augmentation_2.insert(
                0, data["Force Schools"]["Force School"]["Augmentation"]["Training 2"]
            )

            self.entry_augmentation_3.delete(0, tk.END)
            self.entry_augmentation_3.insert(
                0, data["Force Schools"]["Force School"]["Augmentation"]["Training 3"]
            )

            self.entry_augmentation_modifier.delete(0, tk.END)
            self.entry_augmentation_modifier.insert(
                0, data["Force Schools"]["Force School"]["Augmentation"]["Total"]
            )

            self.entry_cognition_1.delete(0, tk.END)
            self.entry_cognition_1.insert(
                0, data["Force Schools"]["Force School"]["Cognition"]["Training 1"]
            )

            self.entry_cognition_2.delete(0, tk.END)
            self.entry_cognition_2.insert(
                0, data["Force Schools"]["Force School"]["Cognition"]["Training 2"]
            )

            self.entry_cognition_3.delete(0, tk.END)
            self.entry_cognition_3.insert(
                0, data["Force Schools"]["Force School"]["Cognition"]["Training 3"]
            )

            self.entry_cognition_modifier.delete(0, tk.END)
            self.entry_cognition_modifier.insert(
                0, data["Force Schools"]["Force School"]["Cognition"]["Total"]
            )

            self.entry_sorcery_1.delete(0, tk.END)
            self.entry_sorcery_1.insert(
                0, data["Force Schools"]["Force School"]["Sorcery"]["Training 1"]
            )

            self.entry_sorcery_2.delete(0, tk.END)
            self.entry_sorcery_2.insert(
                0, data["Force Schools"]["Force School"]["Sorcery"]["Training 2"]
            )

            self.entry_sorcery_3.delete(0, tk.END)
            self.entry_sorcery_3.insert(
                0, data["Force Schools"]["Force School"]["Sorcery"]["Training 3"]
            )

            self.entry_sorcery_modifier.delete(0, tk.END)
            self.entry_sorcery_modifier.insert(
                0, data["Force Schools"]["Force School"]["Sorcery"]["Total"]
            )

            self.entry_technokinesis_1.delete(0, tk.END)
            self.entry_technokinesis_1.insert(
                0, data["Force Schools"]["Force School"]["Technokinesis"]["Training 1"]
            )

            self.entry_technokinesis_2.delete(0, tk.END)
            self.entry_technokinesis_2.insert(
                0, data["Force Schools"]["Force School"]["Technokinesis"]["Training 2"]
            )

            self.entry_technokinesis_3.delete(0, tk.END)
            self.entry_technokinesis_3.insert(
                0, data["Force Schools"]["Force School"]["Technokinesis"]["Training 3"]
            )

            self.entry_technokinesis_modifier.delete(0, tk.END)
            self.entry_technokinesis_modifier.insert(
                0, data["Force Schools"]["Force School"]["Technokinesis"]["Total"]
            )

            self.entry_telekinesis_1.delete(0, tk.END)
            self.entry_telekinesis_1.insert(
                0, data["Force Schools"]["Force School"]["Telekinesis"]["Training 1"]
            )

            self.entry_telekinesis_2.delete(0, tk.END)
            self.entry_telekinesis_2.insert(
                0, data["Force Schools"]["Force School"]["Telekinesis"]["Training 2"]
            )

            self.entry_telekinesis_3.delete(0, tk.END)
            self.entry_telekinesis_3.insert(
                0, data["Force Schools"]["Force School"]["Telekinesis"]["Training 3"]
            )

            self.entry_telekinesis_modifier.delete(0, tk.END)
            self.entry_telekinesis_modifier.insert(
                0, data["Force Schools"]["Force School"]["Telekinesis"]["Total"]
            )

            self.entry_vitalism_1.delete(0, tk.END)
            self.entry_vitalism_1.insert(
                0, data["Force Schools"]["Force School"]["Vitalism"]["Training 1"]
            )

            self.entry_vitalism_2.delete(0, tk.END)
            self.entry_vitalism_2.insert(
                0, data["Force Schools"]["Force School"]["Vitalism"]["Training 2"]
            )

            self.entry_vitalism_3.delete(0, tk.END)
            self.entry_vitalism_3.insert(
                0, data["Force Schools"]["Force School"]["Vitalism"]["Training 3"]
            )

            self.entry_vitalism_modifier.delete(0, tk.END)
            self.entry_vitalism_modifier.insert(
                0, data["Force Schools"]["Force School"]["Vitalism"]["Total"]
            )

            self.entry_force_uses.delete(0, tk.END)
            self.entry_force_uses.insert(0, data["Force Schools"]["Force Uses"])

            # Force Techs
            self.entry_force_tech_1.delete(0, tk.END)
            self.entry_force_tech_1.insert(
                0, data["Force Techniques"]["Force Technique 1"]
            )

            self.entry_force_tech_2.delete(0, tk.END)
            self.entry_force_tech_2.insert(
                0, data["Force Techniques"]["Force Technique 2"]
            )

            self.entry_force_tech_3.delete(0, tk.END)
            self.entry_force_tech_3.insert(
                0, data["Force Techniques"]["Force Technique 3"]
            )

            self.entry_force_tech_4.delete(0, tk.END)
            self.entry_force_tech_4.insert(
                0, data["Force Techniques"]["Force Technique 4"]
            )

            self.entry_force_tech_5.delete(0, tk.END)
            self.entry_force_tech_5.insert(
                0, data["Force Techniques"]["Force Technique 5"]
            )

            self.entry_force_tech_6.delete(0, tk.END)
            self.entry_force_tech_6.insert(
                0, data["Force Techniques"]["Force Technique 6"]
            )

            self.entry_force_tech_7.delete(0, tk.END)
            self.entry_force_tech_7.insert(
                0, data["Force Techniques"]["Force Technique 7"]
            )

            self.entry_force_tech_8.delete(0, tk.END)
            self.entry_force_tech_8.insert(
                0, data["Force Techniques"]["Force Technique 8"]
            )

            self.entry_force_tech_9.delete(0, tk.END)
            self.entry_force_tech_9.insert(
                0, data["Force Techniques"]["Force Technique 9"]
            )

            self.entry_force_tech_10.delete(0, tk.END)
            self.entry_force_tech_10.insert(
                0, data["Force Techniques"]["Force Technique 10"]
            )

            self.entry_force_tech_11.delete(0, tk.END)
            self.entry_force_tech_11.insert(
                0, data["Force Techniques"]["Force Technique 11"]
            )

            self.entry_force_tech_12.delete(0, tk.END)
            self.entry_force_tech_12.insert(
                0, data["Force Techniques"]["Force Technique 12"]
            )

            self.entry_force_tech_13.delete(0, tk.END)
            self.entry_force_tech_13.insert(
                0, data["Force Techniques"]["Force Technique 13"]
            )

            self.entry_force_tech_14.delete(0, tk.END)
            self.entry_force_tech_14.insert(
                0, data["Force Techniques"]["Force Technique 14"]
            )

            self.entry_force_tech_15.delete(0, tk.END)
            self.entry_force_tech_15.insert(
                0, data["Force Techniques"]["Force Technique 15"]
            )

            # Force Secrets
            self.entry_force_secret_1.delete(0, tk.END)
            self.entry_force_secret_1.insert(0, data["Force Secrets"]["Force Secret 1"])

            self.entry_force_secret_2.delete(0, tk.END)
            self.entry_force_secret_2.insert(0, data["Force Secrets"]["Force Secret 2"])

            self.entry_force_secret_3.delete(0, tk.END)
            self.entry_force_secret_3.insert(0, data["Force Secrets"]["Force Secret 3"])

            self.entry_force_secret_4.delete(0, tk.END)
            self.entry_force_secret_4.insert(0, data["Force Secrets"]["Force Secret 4"])

            self.entry_force_secret_5.delete(0, tk.END)
            self.entry_force_secret_5.insert(0, data["Force Secrets"]["Force Secret 5"])

            self.entry_force_secret_6.delete(0, tk.END)
            self.entry_force_secret_6.insert(0, data["Force Secrets"]["Force Secret 6"])

            self.entry_force_secret_7.delete(0, tk.END)
            self.entry_force_secret_7.insert(0, data["Force Secrets"]["Force Secret 7"])

            self.entry_force_secret_8.delete(0, tk.END)
            self.entry_force_secret_8.insert(0, data["Force Secrets"]["Force Secret 8"])

            self.entry_force_secret_9.delete(0, tk.END)
            self.entry_force_secret_9.insert(0, data["Force Secrets"]["Force Secret 9"])

            self.entry_force_secret_10.delete(0, tk.END)
            self.entry_force_secret_10.insert(
                0, data["Force Secrets"]["Force Secret 10"]
            )

            self.entry_force_secret_11.delete(0, tk.END)
            self.entry_force_secret_11.insert(
                0, data["Force Secrets"]["Force Secret 11"]
            )

            self.entry_force_secret_12.delete(0, tk.END)
            self.entry_force_secret_12.insert(
                0, data["Force Secrets"]["Force Secret 12"]
            )

            self.entry_force_secret_13.delete(0, tk.END)
            self.entry_force_secret_13.insert(
                0, data["Force Secrets"]["Force Secret 13"]
            )

            self.entry_force_secret_14.delete(0, tk.END)
            self.entry_force_secret_14.insert(
                0, data["Force Secrets"]["Force Secret 14"]
            )

            self.entry_force_secret_15.delete(0, tk.END)
            self.entry_force_secret_15.insert(
                0, data["Force Secrets"]["Force Secret 15"]
            )

            # Feats
            self.entry_feats_1.delete(0, tk.END)
            self.entry_feats_1.insert(0, data["Feats"]["Feat 1"])

            self.entry_feats_2.delete(0, tk.END)
            self.entry_feats_2.insert(0, data["Feats"]["Feat 2"])

            self.entry_feats_3.delete(0, tk.END)
            self.entry_feats_3.insert(0, data["Feats"]["Feat 3"])

            self.entry_feats_4.delete(0, tk.END)
            self.entry_feats_4.insert(0, data["Feats"]["Feat 4"])

            self.entry_feats_5.delete(0, tk.END)
            self.entry_feats_5.insert(0, data["Feats"]["Feat 5"])

            self.entry_feats_6.delete(0, tk.END)
            self.entry_feats_6.insert(0, data["Feats"]["Feat 6"])

            self.entry_feats_7.delete(0, tk.END)
            self.entry_feats_7.insert(0, data["Feats"]["Feat 7"])

            self.entry_feats_8.delete(0, tk.END)
            self.entry_feats_8.insert(0, data["Feats"]["Feat 8"])

            self.entry_feats_9.delete(0, tk.END)
            self.entry_feats_9.insert(0, data["Feats"]["Feat 9"])

            self.entry_feats_10.delete(0, tk.END)
            self.entry_feats_10.insert(0, data["Feats"]["Feat 10"])

            self.entry_feats_11.delete(0, tk.END)
            self.entry_feats_11.insert(0, data["Feats"]["Feat 11"])

            self.entry_feats_12.delete(0, tk.END)
            self.entry_feats_12.insert(0, data["Feats"]["Feat 12"])

            self.entry_feats_13.delete(0, tk.END)
            self.entry_feats_13.insert(0, data["Feats"]["Feat 13"])

            self.entry_feats_14.delete(0, tk.END)
            self.entry_feats_14.insert(0, data["Feats"]["Feat 14"])

            self.entry_feats_15.delete(0, tk.END)
            self.entry_feats_15.insert(0, data["Feats"]["Feat 15"])

            # Talents
            self.entry_talents_1.delete(0, tk.END)
            self.entry_talents_1.insert(0, data["Talents"]["Talent 1"])

            self.entry_talents_2.delete(0, tk.END)
            self.entry_talents_2.insert(0, data["Talents"]["Talent 2"])

            self.entry_talents_3.delete(0, tk.END)
            self.entry_talents_3.insert(0, data["Talents"]["Talent 3"])

            self.entry_talents_4.delete(0, tk.END)
            self.entry_talents_4.insert(0, data["Talents"]["Talent 4"])

            self.entry_talents_5.delete(0, tk.END)
            self.entry_talents_5.insert(0, data["Talents"]["Talent 5"])

            self.entry_talents_6.delete(0, tk.END)
            self.entry_talents_6.insert(0, data["Talents"]["Talent 6"])

            self.entry_talents_7.delete(0, tk.END)
            self.entry_talents_7.insert(0, data["Talents"]["Talent 7"])

            self.entry_talents_8.delete(0, tk.END)
            self.entry_talents_8.insert(0, data["Talents"]["Talent 8"])

            self.entry_talents_9.delete(0, tk.END)
            self.entry_talents_9.insert(0, data["Talents"]["Talent 9"])

            self.entry_talents_10.delete(0, tk.END)
            self.entry_talents_10.insert(0, data["Talents"]["Talent 10"])

            self.entry_talents_11.delete(0, tk.END)
            self.entry_talents_11.insert(0, data["Talents"]["Talent 11"])

            self.entry_talents_12.delete(0, tk.END)
            self.entry_talents_12.insert(0, data["Talents"]["Talent 12"])

            self.entry_talents_13.delete(0, tk.END)
            self.entry_talents_13.insert(0, data["Talents"]["Talent 13"])

            self.entry_talents_14.delete(0, tk.END)
            self.entry_talents_14.insert(0, data["Talents"]["Talent 14"])

            self.entry_talents_15.delete(0, tk.END)
            self.entry_talents_15.insert(0, data["Talents"]["Talent 15"])

            # Equipment
            self.entry_equipment_1.delete(0, tk.END)
            self.entry_equipment_1.insert(0, data["Equipment"]["Equipment 1"])

            self.entry_equipment_2.delete(0, tk.END)
            self.entry_equipment_2.insert(0, data["Equipment"]["Equipment 2"])

            self.entry_equipment_3.delete(0, tk.END)
            self.entry_equipment_3.insert(0, data["Equipment"]["Equipment 3"])

            self.entry_equipment_4.delete(0, tk.END)
            self.entry_equipment_4.insert(0, data["Equipment"]["Equipment 4"])

            self.entry_equipment_5.delete(0, tk.END)
            self.entry_equipment_5.insert(0, data["Equipment"]["Equipment 5"])

            self.entry_equipment_6.delete(0, tk.END)
            self.entry_equipment_6.insert(0, data["Equipment"]["Equipment 6"])

            self.entry_equipment_7.delete(0, tk.END)
            self.entry_equipment_7.insert(0, data["Equipment"]["Equipment 7"])

            self.entry_equipment_8.delete(0, tk.END)
            self.entry_equipment_8.insert(0, data["Equipment"]["Equipment 8"])

            self.entry_equipment_9.delete(0, tk.END)
            self.entry_equipment_9.insert(0, data["Equipment"]["Equipment 9"])

            self.entry_equipment_10.delete(0, tk.END)
            self.entry_equipment_10.insert(0, data["Equipment"]["Equipment 10"])

            self.entry_equipment_11.delete(0, tk.END)
            self.entry_equipment_11.insert(0, data["Equipment"]["Equipment 11"])

            self.entry_equipment_12.delete(0, tk.END)
            self.entry_equipment_12.insert(0, data["Equipment"]["Equipment 12"])

            self.entry_equipment_13.delete(0, tk.END)
            self.entry_equipment_13.insert(0, data["Equipment"]["Equipment 13"])

            self.entry_equipment_14.delete(0, tk.END)
            self.entry_equipment_14.insert(0, data["Equipment"]["Equipment 14"])

            self.entry_equipment_15.delete(0, tk.END)
            self.entry_equipment_15.insert(0, data["Equipment"]["Equipment 15"])

            self.entry_equipment_16.delete(0, tk.END)
            self.entry_equipment_16.insert(0, data["Equipment"]["Equipment 16"])

            self.entry_equipment_17.delete(0, tk.END)
            self.entry_equipment_17.insert(0, data["Equipment"]["Equipment 17"])

            self.entry_equipment_18.delete(0, tk.END)
            self.entry_equipment_18.insert(0, data["Equipment"]["Equipment 18"])

            self.entry_equipment_19.delete(0, tk.END)
            self.entry_equipment_19.insert(0, data["Equipment"]["Equipment 19"])

            self.entry_equipment_20.delete(0, tk.END)
            self.entry_equipment_20.insert(0, data["Equipment"]["Equipment 20"])

            self.entry_equipment_21.delete(0, tk.END)
            self.entry_equipment_21.insert(0, data["Equipment"]["Equipment 21"])

            self.entry_equipment_22.delete(0, tk.END)
            self.entry_equipment_22.insert(0, data["Equipment"]["Equipment 22"])

            self.entry_equipment_23.delete(0, tk.END)
            self.entry_equipment_23.insert(0, data["Equipment"]["Equipment 23"])

            self.entry_equipment_24.delete(0, tk.END)
            self.entry_equipment_24.insert(0, data["Equipment"]["Equipment 24"])

            self.entry_equipment_25.delete(0, tk.END)
            self.entry_equipment_25.insert(0, data["Equipment"]["Equipment 25"])

            self.entry_equipment_26.delete(0, tk.END)
            self.entry_equipment_26.insert(0, data["Equipment"]["Equipment 26"])

            self.entry_equipment_27.delete(0, tk.END)
            self.entry_equipment_27.insert(0, data["Equipment"]["Equipment 27"])

            self.entry_equipment_28.delete(0, tk.END)
            self.entry_equipment_28.insert(0, data["Equipment"]["Equipment 28"])

            self.entry_equipment_29.delete(0, tk.END)
            self.entry_equipment_29.insert(0, data["Equipment"]["Equipment 29"])

            self.entry_equipment_30.delete(0, tk.END)
            self.entry_equipment_30.insert(0, data["Equipment"]["Equipment 30"])

            self.entry_equipment_31.delete(0, tk.END)
            self.entry_equipment_31.insert(0, data["Equipment"]["Equipment 31"])

            self.entry_equipment_32.delete(0, tk.END)
            self.entry_equipment_32.insert(0, data["Equipment"]["Equipment 32"])


if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterSheetApp(root)
    root.mainloop()
