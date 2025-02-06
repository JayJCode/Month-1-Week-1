"""
Week 1
1) Program should read data.txt
2) Count the numbers of words and lines.
3) Find "key" word.

Week 2
1) Extend your previous script to use Python’s argparse.
2) Integrate at least one standard library (os/sys/datetime) in a meaningful way.
3) Populate data in the text file you are working with by fetching it from an external API using requests.

Week 3
1) Reorganize program (use functions, main etc.).
2) Use classes (APIClient, FileManager).
3) Create tests using pytest in separate folder.
"""

import os
from datetime import datetime
import argparse

from api_client import APIClient
from file_manager import FileManager

"""
Example use: py main.py -f data.txt -k name -c africa
"""
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="The name of the file we filter through")
parser.add_argument("-k", "--key", help="The key name or symbol to be filtered in file")
parser.add_argument("-c", "--country", help="The country name of which data will be download to data.txt")
args = parser.parse_args()

def check_parameters():
    return os.path.exists(args.file)

def get_file_info(file):
    # Gives info about: name, size, date of last modification
    file_size = os.stat(args.file).st_size
    file_mod_time = datetime.fromtimestamp(os.stat(args.file).st_mtime)
    print(("ABOUT CHOSEN FILE:\n" +
           "File name: {}\n" +
           "File size: {}\n" +
           "Last modified: {}\n").format(args.file, file_size, file_mod_time))

def investigate_text(text, key):
    # Checking number of words, lines in text and showing index of searched word.
    num_of_words = len(text.replace("\n", " ").strip().split(" "))
    num_of_lines = len(text.split("\n"))
    index = text.index(key)
    print(("ABOUT ITS CONTENT:\n" +
           "Number of words: {}\n" +
           "Number of lines: {}\n" +
           "Index of {}: {}").format(num_of_words, num_of_lines, key, index))

def main():
    api_client = APIClient()
    file_manager = FileManager(args.file)

    data = api_client.get_data("name", args.country)
    file_manager.save(data)
    get_file_info(args.file)
    text = file_manager.read()
    investigate_text(text, args.key)

if __name__=="__main__":
    main()