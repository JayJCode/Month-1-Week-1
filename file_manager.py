class FileManager:
    def __init__(self, file_path):
        self.__file_path__ = file_path

    def save(self, content):
        with open(self.__file_path__, "w", encoding="utf-8") as file:
            file.write(content)

    def read(self):
        with open(self.__file_path__, "r", encoding="utf-8") as file:
            content = file.read()
        return content