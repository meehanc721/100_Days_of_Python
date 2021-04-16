import pandas


#TODO 1. Create a dictionary in this format:
data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user = input("Enter a word: ").upper()
    try:
        nato_list = [nato_dict[letter] for letter in user]
    except KeyError:
        print("Letters Only")
        generate_phonetic()
    else:
        print(nato_list)

generate_phonetic()

