import pandas as pd

PATH_TO_FILE = "100-python-projects/Day-26/NatoAlphabet/nato_phonetic_alphabet.csv"

file_content = pd.read_csv(PATH_TO_FILE)
phonetic_dict = {row.letter: row.code for (index,row) in file_content.iterrows()}


# Handling keyerror if digits entered
def generate_phonetic():
    user_input = input("Enter any word: ").upper()
    try:
        result = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phonetic()
    else:
        print(result)
        
generate_phonetic()