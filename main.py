# Task 1
# You have two text files. Find out if their lines match. If
# they don’t, print the mismatched line from each file.

def task1(file1, file2):
    with open(file1, "r") as file_handler:
        text1 = file_handler.readlines()

    with open(file2, "r") as file_handler:
        text2 = file_handler.readlines()

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

task1("Task1_1.txt", "Task1_2.txt")


# Task 2
# You have a text file. Create a new file and write the following statistics based on the source file to it:
# ■ Number of characters;
# ■ Number of lines;
# ■ Number of vowels;
# ■ Number of consonants;
# ■ Number of digits.

def task2(file):
    with open(file, "r") as file_handler:
        text = file_handler.readlines()

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

task2("Task2.txt")

"""Task3
Task 3
You have a text file. Delete the last line from it. Write
the result to another file. """

def task3(file):
    with open(file, "r") as file_handler:
        text = file_handler.readlines()

    file_handler = open("Task3_output.txt", "w")
    for i in range(len(text)-1):
        file_handler.writelines(text[i])
    file_handler.close()

task3("Task3-6.txt")


"""Task 4
You have a text file. Find the length of the longest line."""

def task4(file):
    with open(file, "r") as file_handler:
        text = file_handler.readlines()

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

print(f"The longest line is {task4("Task3-6.txt")} characters long.")

""" Task 5
You have a text file. Count how many times the word
specified by the user occurs in it."""

user_input = input("Input the searched word: ")

def task5(file, word):
    with open(file, "r") as file_handler:
        text = file_handler.read()

    wordlist = text.rsplit()
    for i in range(len(wordlist)):
        wordlist[i] = wordlist[i].rstrip('.,"')
    for i in range(len(wordlist)):
        wordlist[i] = wordlist[i].lower()
    word = word.lower()

    counter = 0
    for i in wordlist:
        if i == word:
            counter += 1

    return f"The word '{word}' has been found {counter} times."

print(task5("Task3-6.txt", user_input))

"""Task 6
You have a text file. Find and replace the specified word.
The user determines what to search for and to what it should
be replaced with."""

input_old_word = input("Input a word which you want to replace: ")
input_new_word = input("Input a word which you want to insert: ")


def task6(file, old_word=input_old_word, new_word=input_new_word):
    with open(file, "r") as file_handler:
        text = file_handler.read()

    wordlist = text.rsplit()

    upper_new_word = new_word.capitalize()
    lower_new_word = new_word.lower()

    for i in range(len(wordlist)):
        if old_word.lower() in wordlist[i].lower():
            if wordlist[i].islower():
                if not wordlist[i][-1].isalpha():
                    wordlist[i] = lower_new_word + wordlist[i][-1]
                else:
                    wordlist[i] = lower_new_word

            if wordlist[i][0].isupper():
                if not wordlist[i][-1].isalpha():
                    wordlist[i] = upper_new_word + wordlist[i][-1]
                else:
                    wordlist[i] = upper_new_word

    with open("Task6_output.txt", "w") as file_handler:
        for i in wordlist:
            file_handler.write(f"{i} ")

task6("Task3-6.txt")