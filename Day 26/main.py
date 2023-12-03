import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}
print(phonetic)
input_value = input("Enter a name: ").upper()

output = [phonetic[letter] for letter in input_value]
print(output)