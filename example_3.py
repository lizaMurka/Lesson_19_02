try:
    string = input("Enter a line: ")
    word_to_find = input("Enter a word to search: ")
    word_to_replace = input("Enter a word to change: ")

    new_string = string.replace(word_to_find, word_to_replace)

    print(f"Received line: {new_string}")

except Exception as error:
    print(f"Error: {error}")
