#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
PATH_TO_INPUT_FILE = "100-python-projects/Day-24/mailMerge/Input/Letters/starting_letter.txt"
PATH_TO_INPUT_NAMES = "100-python-projects/Day-24/mailMerge/Input/Names/invited_names.txt"

PATH_TO_OUTPUT = "100-python-projects/Day-24/mailMerge/Output/ReadyToSend"

PLACEHOLDER = "[name]"

with open(PATH_TO_INPUT_NAMES) as name_file:
    names = name_file.readlines()
    all_names = [name.strip() for name in names]


with open(PATH_TO_INPUT_FILE) as file:
    letter_content = file.read()
    for name in all_names:
        new_letter_content = letter_content.replace(PLACEHOLDER, name)
        with open(f"{PATH_TO_OUTPUT}/letter_for_{name}.txt", mode="w") as letter_file:
            letter_file.write(new_letter_content)
