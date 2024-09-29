from abc import ABC, abstractmethod
import json
import os


class JSONVacancy(ABC):
    """Абстрактный метод для создания и удаления JSON-файлов"""

    @abstractmethod
    def safe_vacancy(self):
        """Метод для сохранения данных о вакансиях в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self):
        """Метод для удаления не нужного файла"""
        pass


class HHVacancy(JSONVacancy):
    """Класс для создания и удаления файлов с данными по вакансиям из сайта HH.ru"""

    def __init__(self, stock_list):
        """Инициализатор класса"""
        self.stock_list: list
        self._file_name_del = "../data/data_vacancy.json"
        self._file_name_save = '../data/suitable_vacancies.json'
        self.final_list = []

    def safe_vacancy(self):
        """Метод для сохранения данных о вакансиях в файл"""
        with open(self._file_name_save, 'r', encoding="utf-8") as file:
            data = json.load(file)
            for i in data:
                if i in self.stock_list:
                    continue
                else:
                    self.final_list.append(i)

        if os.path.exists(self._file_name_save):
            with open(self._file_name_save, 'a', encoding="utf-8") as file:
                json.dump(self.final_list, file, indent=4, ensure_ascii=False)
        else:
            with open(self._file_name_save, 'w', encoding="utf-8") as file:
                json.dump(self.stock_list, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self):
        """Метод для удаления не нужного файла"""
        os.remove(self._file_name_del)
