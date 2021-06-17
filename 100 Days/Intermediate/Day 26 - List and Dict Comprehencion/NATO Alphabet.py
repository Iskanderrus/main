import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
word = input("Enter the word:\n")
output_dict = {row.letter.upper(): row.code for (index, row) in df.iterrows()}
list_of_codes = [code for (letter, code) in output_dict.items() if letter in word.upper()]
print(list_of_codes)
