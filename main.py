try:
    count_letters = 0
    count_digits = 0

    string = input("Enter a line: ")

    if not string:
        print("Enter a line that is not  empty.")
        exit()

    for index in range(len(string)):
        char = string[index]
        if char.isalpha():
            count_letters += 1
        elif char.isdigit():
            count_digits += 1

    print(f"Number of lettes: {count_letters}")
    print(f"Number of digits: {count_digits}")

except Exception as error:
    print(f"Error: {error}")
