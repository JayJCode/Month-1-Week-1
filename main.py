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
import os
from datetime import datetime
import argparse

# 4th part.
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="The name of the file we filter through")
parser.add_argument("-k", "--key", help="The key name or symbol to be filtered in file")
args = parser.parse_args()

# 5th part. Using sys to get file_name, and os to get some information about this file.
# Lastly using datetime for changing format to a readable for human being

# file_name = sys.argv[1] // no longer in use, since we use argparse
if not os.path.exists(args.file):
    print("There is not a such file")
    exit(1)
file_size = os.stat(args.file).st_size
file_mod_time = datetime.fromtimestamp(os.stat(args.file).st_mtime)
print(("ABOUT CHOSEN FILE:\n" +
       "File name: {}\n" +
       "File size: {}\n" +
       "Last modified: {}\n").format(args.file, file_size, file_mod_time))

with open(args.file) as file:
    data = file.read() # 1st part.
    num_of_words = len(data.replace("\n", " ").strip().split(" ")) # 2nd part.
    num_of_lines = len(data.split("\n"))
    index = data.index(args.key) # 3rd part. // use of args added
    print(("ABOUT ITS CONTENT:\n" +
           "Number of words: {}\n" +
           "Number of lines: {}\n" +
           "Index of searched word: {}").format(num_of_words, num_of_lines, index))