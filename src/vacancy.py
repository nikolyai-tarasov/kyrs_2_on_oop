import json


class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = ('name', 'city', 'url', 'salary', 'result')

    def __init__(self, name, city, salary):
        """Инициализатор для класса"""
        self.name: str
        self.city: str
        self.url: str
        self.salary: float
        self.result = []

    def __reform_file(self):
        """Метод для обработки JSON-ответа от сайта HH.ru"""
        with open("../data/data_vacancy.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        for i in data:
            self.result.append({
                "name": i["name"],
                "city": i["area"]["name"],
                "salary": {"from": i["salary"]["from"],
                           "to": i["salary"]["to"]},
                "url": i["alternate_url"],
                "description": i["snippet"]["requirement"]
            })

    def filter_city(self):
        """Метод фильтрации списка вакансий по нужному городу"""
        for i in self.result:
            if i["city"] != self.city:
                self.result.remove(i)

    def __lt__(self, other):
        """ Магический метод фильтрации списка вакансий по заработной плате"""
        for i in self.result:
            if other < self.salary:
                self.result.remove(i)
