import requests
import json


class Parser:
    """Родительский класс get-запросов"""

    def add_vacancy(self):
        """Метод создания JSON-файла и сохранения в него данных по запросу"""
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        """Магический метод инициализаций объектов для отправки get-запроса"""
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        """Метод отправки get-запроса на сайт Head Hunter"""
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    def add_vacancy(self):
        """Метод создания JSON-файла и сохранения в него данных по запросу"""
        if self.vacancies is not None:
            with open('../data/data_vacancy.json', 'w', encoding="utf-8") as file:
                json.dump(self.vacancies, file, indent=4, ensure_ascii=False)


h_1 = HH()
h = h_1.load_vacancies("develop")
print(h_1.add_vacancy())