import os
import glob


confirm = input('Make sure you put the island files into a folder named "islands". Did you do that? (y or n): ')
if not os.path.isdir(os.getcwd() + '/islands'):
    print('You think you can pull one over on me? :P \nPlease create the "islands" directory, place your islands files in it and re-run the script before proceeding.')
    exit(0)
else:
    if confirm == 'y':
        search_string = input("Enter name of person you'd like to search for (CaSe SeNsItIvE): ")
        occurrences = 0
        # For all files in the script's directory (place it with the island files)
        for fpath in glob.glob('islands/*.yml'):
            fname = os.path.basename(fpath)
            # Open it
            fo = open(fpath)
            line_no = 1
            for line in fo:
                # Search for the string on that line and if it finds it, print the file name and line number so you can go look for it.
                index = line.find(search_string)
                if index != -1:
                    print(f"Found search string on line {line_no} in file: {fname}")
                    occurrences += 1
                line_no += 1
            fo.close()
        print(f"Finished searching files in directory for string. Number of occurrences: {occurrences}")
    else:
        print('Please create the "islands" folder, make a backup of your islands files and then run the script again.')
        exit(0)