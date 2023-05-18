from yaml import safe_load
import json

class Container:
    def __init__(self):
        self.__data = safe_load(open('F:/PythonProject/studentsService/config.yml', 'r'))
        self.__db = self.__data["db"]
        self.__sheet = self.__data["sheet"]

    def get_sheet(self):
        return self.__sheet

    def get_db(self):
        return self.__db

    db = property(get_db)
    sheet = property(get_sheet)
    print()


