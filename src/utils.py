from src.vacancy_api import HH


def user_interaction():
    """"""
    search_query = input("Введите поисковый запрос: ")
    hh = HH()
    hh.load_vacancies(search_query)
    hh.add_vacancy()
    city_search = input("Введите")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите желаемую зарплату: ")
