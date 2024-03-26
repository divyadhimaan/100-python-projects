import os

day_number = 31

path = "/Users/divyadhiman/Documents/Projects/100-python-projects/100-python-projects/"
folder_name = ""
try:
    while day_number != 50:
        folder_name = path + "Day-" + str(day_number)
        os.rmdir(folder_name)
        day_number = day_number + 1
        print(f"Folder 'Day-{day_number}' removed.")
except FileNotFoundError:
    print(f"Folder 'Day-{day_number}' doesnot exists.")