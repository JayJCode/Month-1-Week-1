import requests


class APIClient:
    def __init__(self):
        self.__base_url = "https://restcountries.com/v3.1/"

    def get_base_url(self):
        return self.__base_url

    def get_data(self, category, value):
        return requests.get(self.__base_url + "{}/{}".format(category, value)).text