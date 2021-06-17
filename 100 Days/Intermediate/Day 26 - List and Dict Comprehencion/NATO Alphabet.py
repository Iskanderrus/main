import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
word = input("Enter the word:\n").upper()
output_dict = {row.letter: row.code for (index, row) in df.iterrows()}
list_of_codes = [output_dict[letter] for letter in word]
print(list_of_codes)
