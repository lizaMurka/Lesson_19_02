try:
    string = input("Enter a line: ")
    char = input("Enter the character to search: ")

    count = 0
    for i in range(len(string)):
        if string[i] == char:
            count += 1

    print(f"Symbol '{char}' meets {count} once.")

except Exception as error:
    print(f"Error: {error}")
