"""
1) Program should read data.txt
2) Count the numbers of words and lines.
3) Find "key" word.
"""

with open("data.txt") as file:
    data = file.read() # 1st part
    num_of_words = len(data.replace("\n", " ").strip().split(" "))
    num_of_lines = len(data.split("\n"))
    # user_input = input("Type key word, You are looking for: ")
    index = data.index("key") # pass user_input if you want program to be more interactive and uncomment recent line.
    print(("Number of words: {}.\n" +
           "Number of lines: {}.\n" +
           "Index of searched word: {}.").format(num_of_words, num_of_lines, index))