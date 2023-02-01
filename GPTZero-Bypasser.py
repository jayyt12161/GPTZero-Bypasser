import random

def replace_letters(file_buffer):
    # Changes all AEOaeo letters with the cyrillic varients.
    file_buffer = file_buffer.replace('a', 'а')
    file_buffer = file_buffer.replace('e', 'е')
    file_buffer = file_buffer.replace('o', 'о')
    file_buffer = file_buffer.replace('A', 'А')
    file_buffer = file_buffer.replace('E', 'Е')
    file_buffer = file_buffer.replace('O', 'О')
    return file_buffer

def insert_zwj(input_string):
    output_string = ""
    zwj = "\u200D" # Zero Width Joiner unicode character
    for char in input_string:
        output_string += char
        # Randomly insert zero width joiner
        if random.random() < 0.2: # Lower number = Less ZWJ
            output_string += zwj
    return output_string


print(insert_zwj(replace_letters(input())))

input()
