#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

# Default python packages
import os
from datetime import datetime
import argparse

# pip installed python packages
import requests

# 4th part.
"""
Example use: py main.py -f data.txt -k name -c africa
"""
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="The name of the file we filter through")
parser.add_argument("-k", "--key", help="The key name or symbol to be filtered in file")
parser.add_argument("-c", "--country", help="The country name of which data will be download to data.txt")
args = parser.parse_args()

# 6th part. Using REST countries, to get some information into data.txt
base_url = "https://restcountries.com/v3.1/"
r = requests.get(base_url + "name/{}".format(args.country))

with open(args.file, "w", encoding="utf-8") as file:
    file.write(r.text)

# 5th part. Using os to get some information about this file and datetime for changing format to a readable for human being
if not os.path.exists(args.file):
    print("There is not a such file")
    exit(1)
file_size = os.stat(args.file).st_size
file_mod_time = datetime.fromtimestamp(os.stat(args.file).st_mtime)
print(("ABOUT CHOSEN FILE:\n" +
       "File name: {}\n" +
       "File size: {}\n" +
       "Last modified: {}\n").format(args.file, file_size, file_mod_time))

with open(args.file, "r", encoding="utf-8") as file:
    data = file.read() # 1st part.
    num_of_words = len(data.replace("\n", " ").strip().split(" ")) # 2nd part.
    num_of_lines = len(data.split("\n"))
    index = data.index(args.key) # 3rd part. // use of args added
    print(("ABOUT ITS CONTENT:\n" +
           "Number of words: {}\n" +
           "Number of lines: {}\n" +
           "Index of searched word: {}").format(num_of_words, num_of_lines, index))