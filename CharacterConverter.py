import json
from sys import argv


def convert_txt_to_json(txt_file, json_output_file):
    # Define the structure of the JSON output
    character_data = {
        "Info": {},
        "Languages": {},
        "Stats": {},
        "Defenses": {},
        "Damage Thresholds": {},
        "Armor": {},
        "Weapons": {},
        "Skills": {},
        "Force Schools": {"Force School": {}},
        "Force Techniques": {},
        "Force Secrets": {},
        "Feats": {},
        "Talents": {},
        "Equipment": {},
    }

    # Helper function to split and clean lines
    def clean_line(line):
        return line.strip().replace('"', "")

    # Reading the txt file
    with open(txt_file, "r") as f:
        lines = f.readlines()

    # Parsing the txt file to populate the character_data structure
    i = 0
    while i < len(lines):
        line = clean_line(lines[i])

        # Info Section
        if i == 0:
            character_data["Info"]["Character Name"] = line
        elif i == 1:
            character_data["Info"]["Character Level"] = line
        elif i == 2:
            character_data["Info"]["Classes"] = line
        elif i == 3:
            character_data["Info"]["Destiny"] = line
        elif i == 4:
            character_data["Info"]["Credits"] = line
        elif i == 5:
            character_data["Info"]["Species"] = line
        elif i == 6:
            character_data["Info"]["Age"] = line
        elif i == 7:
            character_data["Info"]["Height"] = line
        elif i == 8:
            character_data["Info"]["Weight"] = line
        elif i == 9:
            character_data["Info"]["Gender"] = line
        elif i == 10:
            character_data["Info"]["Species Info"] = line
        elif i == 11:
            character_data["Info"]["Force Points"] = line
        elif i == 12:
            character_data["Info"]["Base Attack Bonus"] = line
        elif i == 13:
            character_data["Info"]["Speed"] = line
        elif i == 14:
            character_data["Info"]["Destiny Points"] = line
        elif i == 15:
            character_data["Info"]["Damage Reduction"] = line

        # Languages Section
        elif 16 <= i <= 25:
            character_data["Languages"][f"Language {i-15}"] = line

        # Stats Section
        elif i == 26:
            character_data["Stats"]["Strength"] = {
                "Score": line,
                "Mod": lines[i + 1].strip(),
            }
        elif i == 28:
            character_data["Stats"]["Dexterity"] = {
                "Score": line,
                "Mod": lines[i + 1].strip(),
            }
        elif i == 30:
            character_data["Stats"]["Constitution"] = {
                "Score": line,
                "Mod": lines[i + 1].strip(),
            }
        elif i == 32:
            character_data["Stats"]["Intelligence"] = {
                "Score": line,
                "Mod": lines[i + 1].strip(),
            }
        elif i == 34:
            character_data["Stats"]["Wisdom"] = {
                "Score": line,
                "Mod": lines[i + 1].strip(),
            }
        elif i == 36:
            character_data["Stats"]["Charisma"] = {
                "Score": line,
                "Mod": lines[i + 1].strip(),
            }
        elif i == 38:
            character_data["Stats"]["Willpower"] = {
                "Score": line,
                "Mod": lines[i + 1].strip(),
            }

        # Defenses Section
        elif i == 40:
            character_data["Defenses"]["Fortitude"] = {
                "Total": line,
                "Class Bonus": lines[i + 1].strip(),
                "Stat Bonus": lines[i + 2].strip(),
                "Armor Bonus": lines[i + 3].strip(),
                "Misc": lines[i + 4].strip(),
            }
        elif i == 45:
            character_data["Defenses"]["Reflex"] = {
                "Total": line,
                "Class Bonus": lines[i + 1].strip(),
                "Stat Bonus": lines[i + 2].strip(),
                "Armor Bonus": lines[i + 3].strip(),
                "Misc": lines[i + 4].strip(),
            }
        elif i == 50:
            character_data["Defenses"]["Will"] = {
                "Total": line,
                "Class Bonus": lines[i + 1].strip(),
                "Stat Bonus": lines[i + 2].strip(),
                "Armor Bonus": lines[i + 3].strip(),
                "Misc": lines[i + 4].strip(),
            }

        # Damage Thresholds Section
        elif i == 55:
            character_data["Damage Thresholds"]["Torso"] = {
                "Total": line,
                "Fortitude Bonus": lines[i + 1].strip(),
                "Misc": lines[i + 2].strip(),
            }
        elif i == 58:
            character_data["Damage Thresholds"]["Head"] = {
                "Total": line,
                "Torso Bonus": lines[i + 1].strip(),
            }
        elif i == 60:
            character_data["Damage Thresholds"]["Limbs"] = {
                "Total": line,
                "Torso Bonus": lines[i + 1].strip(),
            }

        # Armor Section
        elif i == 62:
            character_data["Armor"] = {
                "Armor Name": line,
                "Fortitude Bonus": lines[i + 1].strip(),
                "Reflex Bonus": lines[i + 2].strip(),
                "Max Dex Bonus": lines[i + 3].strip(),
                "Additional Affects": lines[i + 4].strip(),
            }

        # Weapons Section
        elif i == 67:
            character_data["Weapons"]["Weapon 1"] = {
                "Weapon Name": line,
                "Hit Mod": lines[i + 1].strip(),
                "Damage": lines[i + 2].strip(),
                "Range": lines[i + 3].strip(),
                "Crit Range": lines[i + 4].strip(),
            }
        elif i == 72:
            character_data["Weapons"]["Weapon 2"] = {
                "Weapon Name": line,
                "Hit Mod": lines[i + 1].strip(),
                "Damage": lines[i + 2].strip(),
                "Range": lines[i + 3].strip(),
                "Crit Range": lines[i + 4].strip(),
            }
        elif i == 77:
            character_data["Weapons"]["Weapon 3"] = {
                "Weapon Name": line,
                "Hit Mod": lines[i + 1].strip(),
                "Damage": lines[i + 2].strip(),
                "Range": lines[i + 3].strip(),
                "Crit Range": lines[i + 4].strip(),
            }
        elif i == 82:
            character_data["Weapons"]["Weapon 4"] = {
                "Weapon Name": line,
                "Hit Mod": lines[i + 1].strip(),
                "Damage": lines[i + 2].strip(),
                "Range": lines[i + 3].strip(),
                "Crit Range": lines[i + 4].strip(),
            }
        elif i == 87:
            character_data["Weapons"]["Weapon 5"] = {
                "Weapon Name": line,
                "Hit Mod": lines[i + 1].strip(),
                "Damage": lines[i + 2].strip(),
                "Range": lines[i + 3].strip(),
                "Crit Range": lines[i + 4].strip(),
            }

        # Skills Section
        elif i == 92:  # Acrobatics
            character_data["Skills"]["Acrobatics"] = {
                "Stat": "Dex",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 97:  # Climb
            character_data["Skills"]["Climb"] = {
                "Stat": "Str",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 102:  # Deception
            character_data["Skills"]["Deception"] = {
                "Stat": "Cha",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 107:  # Endurance
            character_data["Skills"]["Endurance"] = {
                "Stat": "Con",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 112:  # Gather Information
            character_data["Skills"]["Gather Information"] = {
                "Stat": "Cha",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 117:  # Initiative
            character_data["Skills"]["Initiative"] = {
                "Stat": "Dex",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 122:  # Jump
            character_data["Skills"]["Jump"] = {
                "Stat": "Str",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 127:  # Knowledge (Bureaucracy)
            character_data["Skills"]["Knowledge"] = {}
            character_data["Skills"]["Knowledge"]["Type"] = {}
            character_data["Skills"]["Knowledge"]["Type"]["Bureaucracy"] = {
                "Stat": "Int",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 132:  # Knowledge (Galactic Lore)
            character_data["Skills"]["Knowledge"]["Type"]["Galactic Lore"] = {
                "Stat": "Int",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 137:  # Knowledge (Life Science)
            character_data["Skills"]["Knowledge"]["Type"]["Life Science"] = {
                "Stat": "Int",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 142:  # Knowledge (Physical Science)
            character_data["Skills"]["Knowledge"]["Type"]["Physical Science"] = {
                "Stat": "Int",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 147:  # Knowledge (Social Science)
            character_data["Skills"]["Knowledge"]["Type"]["Social Science"] = {
                "Stat": "Int",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 152:  # Knowledge (Tactics)
            character_data["Skills"]["Knowledge"]["Type"]["Tactics"] = {
                "Stat": "Int",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 157:  # Knowledge (Technology)
            character_data["Skills"]["Knowledge"]["Type"]["Technology"] = {
                "Stat": "Int",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 162:  # Mechanics
            character_data["Skills"]["Mechanics"] = {
                "Stat": "Int",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 167:  # Perception
            character_data["Skills"]["Perception"] = {
                "Stat": "Wis",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 172:  # Persuasion
            character_data["Skills"]["Persuasion"] = {
                "Stat": "Cha",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 177:  # Pilot
            character_data["Skills"]["Pilot"] = {
                "Stat": "Dex",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 182:  # Ride
            character_data["Skills"]["Ride"] = {
                "Stat": "Dex",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 187:  # Stealth
            character_data["Skills"]["Stealth"] = {
                "Stat": "Dex",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 192:  # Survival
            character_data["Skills"]["Survival"] = {
                "Stat": "Wis",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 197:  # Swim
            character_data["Skills"]["Swim"] = {
                "Stat": "Str",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 202:  # Treat Injury
            character_data["Skills"]["Treat Injury"] = {
                "Stat": "Int",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 207:  # Use Computer
            character_data["Skills"]["Use Computer"] = {
                "Stat": "Int",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }
        elif i == 212:  # Use the Force
            character_data["Skills"]["Use the Force"] = {
                "Stat": "Cha/Will",
                "Training": lines[i + 2],
                "Focus": lines[i + 3].strip(),
                "Total": lines[i + 4].strip(),
            }

        # Force Schools Section
        elif i == 217:  # Alchemy
            character_data["Force Schools"]["Force School"]["Alchemy"] = {
                "Total": line,
                "Training 1": lines[i + 1].strip(),
                "Training 2": lines[i + 2].strip(),
                "Training 3": lines[i + 3].strip(),
            }
        elif i == 221:  # Augmentation
            character_data["Force Schools"]["Force School"]["Augmentation"] = {
                "Total": line,
                "Training 1": lines[i + 1].strip(),
                "Training 2": lines[i + 2].strip(),
                "Training 3": lines[i + 3].strip(),
            }
        elif i == 225:  # Cognition
            character_data["Force Schools"]["Force School"]["Cognition"] = {
                "Total": line,
                "Training 1": lines[i + 1].strip(),
                "Training 2": lines[i + 2].strip(),
                "Training 3": lines[i + 3].strip(),
            }
        elif i == 229:  # Sorcery
            character_data["Force Schools"]["Force School"]["Sorcery"] = {
                "Total": line,
                "Training 1": lines[i + 1].strip(),
                "Training 2": lines[i + 2].strip(),
                "Training 3": lines[i + 3].strip(),
            }
        elif i == 233:  # Technokinesis
            character_data["Force Schools"]["Force School"]["Technokinesis"] = {
                "Total": line,
                "Training 1": lines[i + 1].strip(),
                "Training 2": lines[i + 2].strip(),
                "Training 3": lines[i + 3].strip(),
            }
        elif i == 237:  # Telekinesis
            character_data["Force Schools"]["Force School"]["Telekinesis"] = {
                "Total": line,
                "Training 1": lines[i + 1].strip(),
                "Training 2": lines[i + 2].strip(),
                "Training 3": lines[i + 3].strip(),
            }
        elif i == 241:  # Vitalism
            character_data["Force Schools"]["Force School"]["Vitalism"] = {
                "Total": line,
                "Training 1": lines[i + 1].strip(),
                "Training 2": lines[i + 2].strip(),
                "Training 3": lines[i + 3].strip(),
            }

        # Force Uses
        elif i == 245:  # Force Uses
            character_data["Force Schools"]["Force Uses"] = line

            # Force Techniques Section
        elif i == 246:  # Force Technique 1
            character_data["Force Techniques"]["Force Technique 1"] = line
        elif i == 247:  # Force Technique 2
            character_data["Force Techniques"]["Force Technique 2"] = line
        elif i == 248:  # Force Technique 3
            character_data["Force Techniques"]["Force Technique 3"] = line
        elif i == 249:  # Force Technique 4
            character_data["Force Techniques"]["Force Technique 4"] = line
        elif i == 250:  # Force Technique 5
            character_data["Force Techniques"]["Force Technique 5"] = line
        elif i == 251:  # Force Technique 6
            character_data["Force Techniques"]["Force Technique 6"] = line
        elif i == 252:  # Force Technique 7
            character_data["Force Techniques"]["Force Technique 7"] = line
        elif i == 253:  # Force Technique 8
            character_data["Force Techniques"]["Force Technique 8"] = line
        elif i == 254:  # Force Technique 9
            character_data["Force Techniques"]["Force Technique 9"] = line
        elif i == 255:  # Force Technique 10
            character_data["Force Techniques"]["Force Technique 10"] = line
        elif i == 256:  # Force Technique 11
            character_data["Force Techniques"]["Force Technique 11"] = line
        elif i == 257:  # Force Technique 12
            character_data["Force Techniques"]["Force Technique 12"] = line
        elif i == 258:  # Force Technique 13
            character_data["Force Techniques"]["Force Technique 13"] = line
        elif i == 259:  # Force Technique 14
            character_data["Force Techniques"]["Force Technique 14"] = line
        elif i == 260:  # Force Technique 15
            character_data["Force Techniques"]["Force Technique 15"] = line

        # Force Secrets Section
        elif i == 261:  # Force Secret 1
            character_data["Force Secrets"]["Force Secret 1"] = line
        elif i == 262:  # Force Secret 2
            character_data["Force Secrets"]["Force Secret 2"] = line
        elif i == 263:  # Force Secret 3
            character_data["Force Secrets"]["Force Secret 3"] = line
        elif i == 264:  # Force Secret 4
            character_data["Force Secrets"]["Force Secret 4"] = line
        elif i == 265:  # Force Secret 5
            character_data["Force Secrets"]["Force Secret 5"] = line
        elif i == 266:  # Force Secret 6
            character_data["Force Secrets"]["Force Secret 6"] = line
        elif i == 267:  # Force Secret 7
            character_data["Force Secrets"]["Force Secret 7"] = line
        elif i == 268:  # Force Secret 8
            character_data["Force Secrets"]["Force Secret 8"] = line
        elif i == 269:  # Force Secret 9
            character_data["Force Secrets"]["Force Secret 9"] = line
        elif i == 270:  # Force Secret 10
            character_data["Force Secrets"]["Force Secret 10"] = line
        elif i == 271:  # Force Secret 11
            character_data["Force Secrets"]["Force Secret 11"] = line
        elif i == 272:  # Force Secret 12
            character_data["Force Secrets"]["Force Secret 12"] = line
        elif i == 273:  # Force Secret 13
            character_data["Force Secrets"]["Force Secret 13"] = line
        elif i == 274:  # Force Secret 14
            character_data["Force Secrets"]["Force Secret 14"] = line
        elif i == 275:  # Force Secret 15
            character_data["Force Secrets"]["Force Secret 15"] = line

        # Feats Section
        elif i == 276:  # Feat 1
            character_data["Feats"]["Feat 1"] = line
        elif i == 277:  # Feat 2
            character_data["Talents"]["Talent 1"] = line
        elif i == 278:  # Feat 3
            character_data["Feats"]["Feat 2"] = line
        elif i == 279:  # Feat 4
            character_data["Talents"]["Talent 2"] = line
        elif i == 280:  # Feat 5
            character_data["Feats"]["Feat 3"] = line
        elif i == 281:  # Feat 6
            character_data["Talents"]["Talent 3"] = line
        elif i == 282:  # Feat 7
            character_data["Feats"]["Feat 4"] = line
        elif i == 283:  # Feat 8
            character_data["Talents"]["Talent 4"] = line
        elif i == 284:  # Feat 9
            character_data["Feats"]["Feat 5"] = line
        elif i == 285:  # Feat 10
            character_data["Talents"]["Talent 5"] = line
        elif i == 286:  # Feat 11
            character_data["Feats"]["Feat 6"] = line
        elif i == 287:  # Feat 12
            character_data["Talents"]["Talent 6"] = line
        elif i == 288:  # Feat 13
            character_data["Feats"]["Feat 7"] = line
        elif i == 289:  # Feat 14
            character_data["Talents"]["Talent 7"] = line
        elif i == 290:  # Feat 15
            character_data["Feats"]["Feat 8"] = line
        elif i == 291:  # Feat 16
            character_data["Talents"]["Talent 8"] = line
        elif i == 292:  # Feat 17
            character_data["Feats"]["Feat 9"] = line
        elif i == 293:  # Feat 18
            character_data["Talents"]["Talent 9"] = line
        elif i == 294:  # Feat 19
            character_data["Feats"]["Feat 10"] = line
        elif i == 295:  # Feat 20
            character_data["Talents"]["Talent 10"] = line
        elif i == 296:  # Feat 21
            character_data["Feats"]["Feat 11"] = line
        elif i == 297:  # Feat 22
            character_data["Talents"]["Talent 11"] = line
        elif i == 298:  # Feat 23
            character_data["Feats"]["Feat 12"] = line
        elif i == 299:  # Feat 24
            character_data["Talents"]["Talent 12"] = line
        elif i == 300:  # Feat 25
            character_data["Feats"]["Feat 13"] = line
        elif i == 301:  # Feat 26
            character_data["Talents"]["Talent 13"] = line
        elif i == 302:  # Feat 27
            character_data["Feats"]["Feat 14"] = line
        elif i == 303:  # Feat 28
            character_data["Talents"]["Talent 14"] = line
        elif i == 304:  # Feat 29
            character_data["Feats"]["Feat 15"] = line
        elif i == 305:  # Feat 30
            character_data["Talents"]["Talent 15"] = line

        # Equipment Section
        elif i == 306:
            character_data["Equipment"]["Equipment 1"] = line
        elif i == 307:
            character_data["Equipment"]["Equipment 2"] = line
        elif i == 308:
            character_data["Equipment"]["Equipment 3"] = line
        elif i == 309:
            character_data["Equipment"]["Equipment 4"] = line
        elif i == 310:
            character_data["Equipment"]["Equipment 5"] = line
        elif i == 311:
            character_data["Equipment"]["Equipment 6"] = line
        elif i == 312:
            character_data["Equipment"]["Equipment 7"] = line
        elif i == 313:
            character_data["Equipment"]["Equipment 8"] = line
        elif i == 314:
            character_data["Equipment"]["Equipment 9"] = line
        elif i == 315:
            character_data["Equipment"]["Equipment 10"] = line
        elif i == 316:
            character_data["Equipment"]["Equipment 11"] = line
        elif i == 317:
            character_data["Equipment"]["Equipment 12"] = line
        elif i == 318:
            character_data["Equipment"]["Equipment 13"] = line
        elif i == 319:
            character_data["Equipment"]["Equipment 14"] = line
        elif i == 320:
            character_data["Equipment"]["Equipment 15"] = line
        elif i == 321:
            character_data["Equipment"]["Equipment 16"] = line
        elif i == 322:
            character_data["Equipment"]["Equipment 17"] = line
        elif i == 323:
            character_data["Equipment"]["Equipment 18"] = line
        elif i == 324:
            character_data["Equipment"]["Equipment 19"] = line
        elif i == 325:
            character_data["Equipment"]["Equipment 20"] = line
        elif i == 326:
            character_data["Equipment"]["Equipment 21"] = line
        elif i == 327:
            character_data["Equipment"]["Equipment 22"] = line
        elif i == 328:
            character_data["Equipment"]["Equipment 23"] = line
        elif i == 329:
            character_data["Equipment"]["Equipment 24"] = line
        elif i == 330:
            character_data["Equipment"]["Equipment 25"] = line
        elif i == 331:
            character_data["Equipment"]["Equipment 26"] = line
        elif i == 332:
            character_data["Equipment"]["Equipment 27"] = line
        elif i == 333:
            character_data["Equipment"]["Equipment 28"] = line
        elif i == 334:
            character_data["Equipment"]["Equipment 29"] = line
        elif i == 335:
            character_data["Equipment"]["Equipment 30"] = line
        elif i == 336:
            character_data["Equipment"]["Equipment 31"] = line

        # Continue parsing other fields in similar manner
        # for the other parts of the character sheet...

        i += 1

    # Write the parsed data to JSON
    with open(json_output_file, "w") as json_file:
        json.dump(character_data, json_file, indent=4)


# Example usage
txt_file = f"{argv[1]}.txt"
json_output_file = f"{argv[1]}.json"
convert_txt_to_json(txt_file, json_output_file)
