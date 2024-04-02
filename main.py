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

