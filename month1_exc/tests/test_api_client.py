"""
Testing functionality of APIClient class
"""
import pytest

from month1_exc.src.api_client import APIClient

class TestAPIClient:

    @pytest.fixture
    def api_client(self):
        """
        Creates an instance. Working on 'https://restcountries.com/v3.1/'
        :return: APIClient class
        """
        return APIClient()

    def test_init(self, api_client):
        assert api_client.get_base_url() == "https://restcountries.com/v3.1/"

    def test_get_data(self, api_client):
        text = api_client.get_data("capital", "warsaw")
        assert text == ('[{"name":{"common":"Poland","official":"Republic of Poland",'
                        '"nativeName":{"pol":{"official":"Rzeczpospolita Polska","common":"Polska"}}},'
                        '"tld":[".pl"],"cca2":"PL","ccn3":"616","cca3":"POL","cioc":"POL","independent":true,'
                        '"status":"officially-assigned","unMember":true,'
                        '"currencies":{"PLN":{"name":"Polish złoty","symbol":"zł"}},'
                        '"idd":{"root":"+4","suffixes":["8"]},"capital":["Warsaw"],'
                        '"altSpellings":["PL","Republic of Poland","Rzeczpospolita Polska"],'
                        '"region":"Europe","subregion":"Central Europe","languages":{"pol":"Polish"},'
                        '"translations":{"ara":{"official":"الجمهورية البولندية","common":"بولندا"},'
                        '"bre":{"official":"Republik Polonia","common":"Polonia"},'
                        '"ces":{"official":"Polská republika","common":"Polsko"},'
                        '"cym":{"official":"Republic of Poland","common":"Poland"},'
                        '"deu":{"official":"Republik Polen","common":"Polen"},'
                        '"est":{"official":"Poola Vabariik","common":"Poola"},'
                        '"fin":{"official":"Puolan tasavalta","common":"Puola"},'
                        '"fra":{"official":"République de Pologne","common":"Pologne"},'
                        '"hrv":{"official":"Republika Poljska","common":"Poljska"},'
                        '"hun":{"official":"Lengyel Köztársaság","common":"Lengyelország"},'
                        '"ita":{"official":"Repubblica di Polonia","common":"Polonia"},'
                        '"jpn":{"official":"ポーランド共和国","common":"ポーランド"},'
                        '"kor":{"official":"폴란드 공화국","common":"폴란드"},'
                        '"nld":{"official":"Republiek Polen","common":"Polen"},'
                        '"per":{"official":"جمهوری لهستان","common":"لهستان"},'
                        '"pol":{"official":"Rzeczpospolita Polska","common":"Polska"},'
                        '"por":{"official":"República da Polónia","common":"Polónia"},'
                        '"rus":{"official":"Республика Польша","common":"Польша"},'
                        '"slk":{"official":"Poľská republika","common":"Poľsko"},'
                        '"spa":{"official":"República de Polonia","common":"Polonia"},'
                        '"srp":{"official":"Република Пољска","common":"Пољска"},'
                        '"swe":{"official":"Republiken Polen","common":"Polen"},'
                        '"tur":{"official":"Polonya Cumhuriyeti","common":"Polonya"},'
                        '"urd":{"official":"جمہوریہ پولینڈ","common":"پولینڈ"},'
                        '"zho":{"official":"波兰共和国","common":"波兰"}},"latlng":[52.0,20.0],'
                        '"landlocked":false,"borders":["BLR","CZE","DEU","LTU","RUS","SVK","UKR"],'
                        '"area":312679.0,"demonyms":{"eng":{"f":"Polish","m":"Polish"},'
                        '"fra":{"f":"Polonaise","m":"Polonais"}},"flag":"\\uD83C\\uDDF5\\uD83C\\uDDF1",'
                        '"maps":{"googleMaps":"https://goo.gl/maps/gY9Xw4Sf4415P4949",'
                        '"openStreetMaps":"https://www.openstreetmap.org/relation/49715"},'
                        '"population":37950802,"gini":{"2018":30.2},"fifa":"POL",'
                        '"car":{"signs":["PL"],"side":"right"},"timezones":["UTC+01:00"],'
                        '"continents":["Europe"],"flags":{"png":"https://flagcdn.com/w320/pl.png",'
                        '"svg":"https://flagcdn.com/pl.svg",'
                        '"alt":"The flag of Poland is composed of two equal horizontal bands of white and red."},'
                        '"coatOfArms":{"png":"https://mainfacts.com/media/images/coats_of_arms/pl.png",'
                        '"svg":"https://mainfacts.com/media/images/coats_of_arms/pl.svg"},"startOfWeek":"monday",'
                        '"capitalInfo":{"latlng":[52.25,21.0]},"postalCode":{"format":"##-###","regex":"^(\\\\d{5})$"}}]')