student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    print(index)
    print(row)
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pd.read_csv('nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_data_frame = {row.letter:row.code for (index, row) in df.iterrows()}
print(nato_data_frame)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter a word: ')
final_list = [nato_data_frame[letters.upper()] for letters in word]
print(final_list)