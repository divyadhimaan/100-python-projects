import os

day_number = 31

path = "/Users/divyadhiman/Documents/Projects/100-python-projects/100-python-projects/"
folder_name = ""
try:
    while day_number != 36:
        folder_name = path + "Day-" + str(day_number)
        os.mkdir(folder_name)
        day_number = day_number + 1
        print(f"Folder 'Day-{day_number}' created.")
except FileExistsError:
    print(f"Folder 'Day-{day_number}' already exists.")