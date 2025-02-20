"""
Testing functionality of FileManager class
"""

import os.path
from datetime import datetime
import pytest

from month1_exc.src.file_manager import FileManager

class TestFileManager:

    @pytest.fixture
    def file_manager(self):
        """
        Creates an instance. Working on 'test.txt'
        :return: FileManager class
        """
        return FileManager("test.txt")

    def test_init(self, file_manager):
        assert file_manager.get_path() == "test.txt"


    def test_save(self, file_manager):
        file_manager.save("Test file content")
        assert os.stat("test.txt").st_size

    def test_read(self, file_manager):
        file_manager.save("Test file content")
        file_manager.read()
        assert file_manager.get_content() == "Test file content"

    def test_file_info(self, file_manager):
        file_manager.save("Test file content")
        message = file_manager.get_file_info()
        assert message == ("ABOUT CHOSEN FILE:\n" +
                            "File name: test.txt\n" +
                            "File size: 17\n" +
                            "Last modified: {}\n".format(datetime.fromtimestamp(os.stat(file_manager.get_path()).st_mtime)))

    def test_investigate_file(self, file_manager):
        file_manager.save("Test file content")
        file_manager.read()
        message = file_manager.investigate_file("file")
        assert message == ("ABOUT ITS CONTENT:\n" +
                           "Number of words: 3\n" +
                           "Number of lines: 1\n" +
                           "Index of \"file\": 5")