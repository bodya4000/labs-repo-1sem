def find_missing_letter(list_of_letters):
    for i in range(len(list_of_letters)):
        ascii_code_of_current_letter = ord(list_of_letters[i])
        ascii_code_of_next_letter = ord(list_of_letters[i + 1])
        if ascii_code_of_current_letter + 1 != ascii_code_of_next_letter:
            ascii_code_of_missing_letter = ascii_code_of_current_letter + 1
            return chr(ascii_code_of_missing_letter)


print(find_missing_letter(['a', 'b', 'd', 'e']))
print(find_missing_letter(['A', 'B', 'D', 'E']))

