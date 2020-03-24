import json
import os
import glob


relics = {
    'achievement.botania:thorRing': 0,
    'achievement.botania:lokiRing': 0,
    'achievement.botania:odinRing': 0,
    'achievement.botania:kingKey': 0,
    'achievement.botania:flugelEye': 0,
    'achievement.botania:infiniteFruit': 0
}

confirm = input('Before we proceed, make sure you have a backup of the JSON files you are removing the achievements from just in case.'
                '\nAll achievement files must be placed in a folder called "achievements". Did you do what I said? (y or n): ')
if not os.path.isdir(os.getcwd() + '/achievements'):
    print('You think you can pull one over on me? :P \nPlease create the "achievements" directory, place your achievements file in it and re-run the script before proceeding.')
    exit(0)
else:
    if confirm.lower() == 'y':
        print('Okay. Now please type the numbers for following items sperated by commas to select which relics you want to remove. Type "all" to remove all '
            '\n\t[1] Thor Ring\n\t[2] Loki ring\n\t[3] Odin Ring\n\t[4] Key of Kings Law\n\t[5] Eye of the Flugel\n\t[6] Fruit of Grisaia')
        user_relic_input = input('Enter your numbers (Example: "1,2,4,6"): ').split(',')
    else:
        print('Please create the "achievements" folder, make a backup of your achievements file and then run the script again.')
        exit(0)


relics_to_remove = []
if len(user_relic_input) == 1 and user_relic_input[0] == "all":
    relics['achievement.botania:thorRing'] = 1
    relics_to_remove.append('\t[1] Thor Ring')

    relics['achievement.botania:lokiRing'] = 1
    relics_to_remove.append('\t[2] Loki Ring')

    relics['achievement.botania:odinRing'] = 1
    relics_to_remove.append('\t[3] Odin Ring')

    relics['achievement.botania:kingKey'] = 1
    relics_to_remove.append('\t[4] Key of Kings Law')

    relics['achievement.botania:flugelEye'] = 1
    relics_to_remove.append('\t[5] Eye of the Flugel')

    relics['achievement.botania:infiniteFruit'] = 1
    relics_to_remove.append('\t[6] Fruit of Grisaia')
elif len(user_relic_input) >= 1:
    for num in user_relic_input:
        if num == '1':
            relics['achievement.botania:thorRing'] = 1
            relics_to_remove.append('\t[1] Thor Ring')
        elif num == '2':
            relics['achievement.botania:lokiRing'] = 1
            relics_to_remove.append('\t[2] Loki Ring')
        elif num == '3':
            relics['achievement.botania:odinRing'] = 1
            relics_to_remove.append('\t[3] Odin Ring')
        elif num == '4':
            relics['achievement.botania:kingKey'] = 1
            relics_to_remove.append('\t[4] Key of Kings Law')
        elif num == '5':
            relics['achievement.botania:flugelEye'] = 1
            relics_to_remove.append('\t[5] Eye of the Flugel')
        elif num == '6':
            relics['achievement.botania:infiniteFruit'] = 1
            relics_to_remove.append('\t[6] Fruit of Grisaia')
else:
    print('Please input at least one relic to remove.')
    exit(0)

relics_to_remove = "\n".join(relics_to_remove)
confirm2 = input(f"You have chosen the following relics to remove: \n{relics_to_remove}\nIs this correct? (y or n): ")
if confirm2.lower() == 'n':
    print('Okay, Please run the script again and make sure to be careful which relics you select.')
    quit(0)
if confirm2.lower() == 'y':
    print('Great. Now I will remove the achievements from the files.')
    for fpath in glob.glob('achievements/*.json'):
        fname = os.path.basename(fpath)
        print(f"Opening file: {fpath}")
        with open(fpath, 'r') as f:
            jfile = json.load(f)
            removed_relics = []
            for relic in relics:
                status = relics.get(relic)
                print(status)
                if status == None:
                    print('An unexpected error occured. Please try again and if it continues, report it to Column01')
                    quit(0)
                if status == 1 or status == "1":
                    if jfile.get(relic) is not None:
                        jfile.pop(relic)
                        removed_relics.append(relic)
            if len(removed_relics) == 0:
                print('\tNo selected relics were found in the file. Please verify that they are already not in the file or that you selected the correct ones.')
                exit(0)
            else:
                removed_relics = ", ".join(removed_relics)
                outfile = open(fname, 'w+')
                json.dump(jfile, outfile, separators=(",", ":"))
                print(f"\tFile has been output to: {fname} in the main script folder. \nPlease verify it's contents before uploading it to the server.")
                print(f"\tRelics that were removed:\n\t{removed_relics}")
