import pandas as pd

PATH_TO_FILE = "100-python-projects/Day-26/NatoAlphabet/nato_phonetic_alphabet.csv"



#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
file_content = pd.read_csv(PATH_TO_FILE)
phonetic_dict = {row.letter: row.code for (index,row) in file_content.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter any word: ").upper()
result = [phonetic_dict[letter] for letter in user_input]
print(result)