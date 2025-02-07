import os
from datetime import datetime


class FileManager:
    def __init__(self, file_path):
        self.__content__ = None
        self.__file_path__ = file_path

    def get_content(self):
        return self.__content__

    def get_path(self):
        return self.__file_path__

    def save(self, content):
        with open(self.__file_path__, "w", encoding="utf-8") as file:
            file.write(content)

    def read(self):
        with open(self.__file_path__, "r", encoding="utf-8") as file:
            self.__content__ = file.read()

    def get_file_info(self):
        # Gives info about: name, size, date of last modification
        file_size = os.stat(self.__file_path__).st_size
        file_mod_time = datetime.fromtimestamp(os.stat(self.__file_path__).st_mtime)
        message = ("ABOUT CHOSEN FILE:\n" +
               "File name: {}\n" +
               "File size: {}\n" +
               "Last modified: {}\n").format(self.__file_path__, file_size, file_mod_time)
        return message

    def investigate_file(self, key):
        # Checking number of words, lines in text and showing index of searched word.
        num_of_words = len(self.__content__.replace("\n", " ").strip().split(" "))
        num_of_lines = len(self.__content__.split("\n"))
        index = self.__content__.index(key)
        message = ("ABOUT ITS CONTENT:\n" +
               "Number of words: {}\n" +
               "Number of lines: {}\n" +
               "Index of \"{}\": {}").format(num_of_words, num_of_lines, key, index)
        return message