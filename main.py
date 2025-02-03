"""
Week 1
1) Program should read data.txt
2) Count the numbers of words and lines.
3) Find "key" word.

Week 2
4) Extend your previous script to use Python’s argparse.
5) Integrate at least one standard library (os/sys/datetime) in a meaningful way.
6) Populate data in the text file you are working with by fetching it from an external API using requests.
"""
import sys
import argparse

file_name = sys.argv[1] # 5th part. Using sys to get file_name, which we are going to open

with open(file_name) as file:
    data = file.read() # 1st part.
    num_of_words = len(data.replace("\n", " ").strip().split(" ")) # 2nd part.
    num_of_lines = len(data.split("\n"))
    index = data.index("key") # 3rd part.
    print(("Number of words: {}.\n" +
           "Number of lines: {}.\n" +
           "Index of searched word: {}.").format(num_of_words, num_of_lines, index))