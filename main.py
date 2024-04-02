# Task 1
# You have two text files. Find out if their lines match. If
# they don’t, print the mismatched line from each file.

def task1(file1, file2):

    file_handler = open(file1, "r")
    text1 = file_handler.readlines()
    file_handler.close()

    file_handler = open(file2, "r")
    text2 = file_handler.readlines()
    file_handler.close()

    for i in range(len(text1)-1):
        text1[i] = text1[i].rstrip("\n")
    for i in range(len(text2)-1):
        text2[i] = text2[i].rstrip("\n")

    error_counter = 0
    for i in range(len(text1)-1):
        if text1[i] != text2[i]:
            error_counter += 1
            if error_counter == 1:
                print("The following lines don't match:")
            print(f"line {i}   file 1:{text1[i]}    file 2:{text2[i]}")
    if error_counter == 0:
        print("No difference has been found.")

# task1("Task1_1.txt", "Task1_2.txt")


# Task 2
# You have a text file. Create a new file and write the following statistics based on the source file to it:
# ■ Number of characters;
# ■ Number of lines;
# ■ Number of vowels;
# ■ Number of consonants;
# ■ Number of digits.

def task2(file):
    file_handler = open(file, "r")
    text = file_handler.readlines()
    file_handler.close()

    for i in range(len(text) - 1):
        text[i] = text[i].rstrip("\n")

    characters = 0
    lines = 0
    vowels = 0
    consonants = 0
    digits = 0

    vowel = "aeiouyAEIOUY"
    consonant = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"


    for i in range(len(text)):
        lines += 1

        for j in range(len(text[i])):
            characters += 1

            if text[i][j].isdigit() == True:
                digits += 1
            if text[i][j] in vowel:
                vowels += 1
            if text[i][j] in consonant:
                consonants += 1

    file_handler = open("Task2_output.txt", "w")
    file_handler.write(f"characters: {characters}\n")
    file_handler.write(f"lines: {lines}\n")
    file_handler.write(f"vowels: {vowels}\n")
    file_handler.write(f"consonants: {consonants}\n")
    file_handler.write(f"digits: {digits}")
    file_handler.close()

#task2("Task2.txt")

"""Task3
Task 3
You have a text file. Delete the last line from it. Write
the result to another file. """

def task3(file):
    file_handler = open(file, "r")
    text = file_handler.readlines()
    file_handler.close()

    file_handler = open("Task3_output.txt", "w")
    for i in range(len(text)-1):
        file_handler.writelines(text[i])
    file_handler.close()

#task3("Task3-6.txt")

"""Task 4
You have a text file. Find the length of the longest line."""

def task4(file):
    file_handler = open(file, "r")
    text = file_handler.readlines()
    file_handler.close()

    counter = 0
    max_count = 0
    for i in range(len(text)):
        if counter > max_count:
            max_count = counter
        counter = 0
        for j in range(len(text[i])):
            counter += 1

        if counter > max_count:
            max_count = counter

    return(max_count)

# print(f"The longest line is {task4("Task3-6.txt")} characters long.")

