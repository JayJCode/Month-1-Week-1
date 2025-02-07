import os.path
from datetime import datetime
from src.file_manager import FileManager

def test_init():
    file_manager = FileManager("test.txt")
    assert file_manager.get_path() == "test.txt"

def test_save():
    file_manager = FileManager("test.txt")
    file_manager.save("Test file content")
    assert os.stat("test.txt").st_size

def test_read():
    file_manager = FileManager("test.txt")
    file_manager.save("Test file content")
    file_manager.read()
    assert file_manager.__content__ == "Test file content"

def test_file_info():
    file_manager = FileManager("test.txt")
    file_manager.save("Test file content")
    message = file_manager.get_file_info()
    assert message == ("ABOUT CHOSEN FILE:\n" +
                        "File name: test.txt\n" +
                        "File size: 17\n" +
                        "Last modified: {}\n".format(datetime.fromtimestamp(os.stat(file_manager.__file_path__).st_mtime)))

def test_investigate_file():
    file_manager = FileManager("test.txt")
    file_manager.save("Test file content")
    file_manager.read()
    message = file_manager.investigate_file("file")
    assert message == ("ABOUT ITS CONTENT:\n" +
                       "Number of words: 3\n" +
                       "Number of lines: 1\n" +
                       "Index of \"file\": 5")