import json
import os

class JSONVacancy():
    """Абстрактный метод для создания и удаления JSON-файлов"""

    def safe_vacancy(self):
        """Метод для сохранения данных о вакансиях в файл"""
        pass

    def delete_vacancy(self):
        """Метод для удаления не нужного файла"""
        pass


class HHVacancy(JSONVacancy):
    """Класс для создания и удаления файлов с данными по вакансиям из сайта HH.ru"""

    def __init__(self, my_list):
        """Инициализатор класса"""
        self.my_list: list

    def safe_vacancy(self):
        """Метод для сохранения данных о вакансиях в файл"""
        with open('../data/suitable_vacancies.json', 'w', encoding="utf-8") as file:
            json.dump(self.my_list, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self):
        """Метод для удаления не нужного файла"""
        os.remove("../data/data_vacancy.json")
