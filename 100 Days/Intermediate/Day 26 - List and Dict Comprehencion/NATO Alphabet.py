import pandas as pd

# df = pd.read_csv("nato_phonetic_alphabet.csv")
#
# done = False
# while not done:
#     word = input("Enter the word:\n").upper()
#     output_dict = {row.letter: row.code for (index, row) in df.iterrows()}
#     try:
#         list_of_codes = [output_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in Latin alphabet, please.")
#     else:
#         done = True
#         print(list_of_codes)

df = pd.read_csv("nato_phonetic_alphabet.csv")


def phonetic_spell():
    word = input("Enter the word:\n").upper()
    output_dict = {row.letter: row.code for (index, row) in df.iterrows()}
    try:
        list_of_codes = [output_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in Latin alphabet, please.")
        phonetic_spell()
    else:
        print(list_of_codes)


phonetic_spell()
