from unittest.mock import Mock, patch
from src.vacancy_api import HH

data_json_vac = {
    "id": "109792373",
    "premium": 'false',
    "name": "React Front-End Developer (Frontend разработчик)",
    "department": 'null',
    "has_test": 'false',
    "response_letter_required": 'false',
    "area": {
        "id": "2759",
        "name": "Ташкент",
        "url": "https://api.hh.ru/areas/2759"
    },
    "salary": 'null',
    "type": {
        "id": "open",
        "name": "Открытая"
    },
    "address": 'null',
    "response_url": 'null',
    "sort_point_distance": 'null',
    "published_at": "2024-10-31T19:51:37+0300",
    "created_at": "2024-10-31T19:51:37+0300",
    "archived": 'false',
    "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109792373",
    "show_logo_in_search": 'null',
    "insider_interview": 'null',
    "url": "https://api.hh.ru/vacancies/109792373?host=hh.ru",
    "alternate_url": "https://hh.ru/vacancy/109792373",
    "relations": [],
    "employer": {
        "id": "11566922",
        "name": "VISSEN CA",
        "url": "https://api.hh.ru/employers/11566922",
        "alternate_url": "https://hh.ru/employer/11566922",
        "logo_urls": {
            "240": "https://img.hhcdn.ru/employer-logo/7025775.png",
            "90": "https://img.hhcdn.ru/employer-logo/7025774.png",
            "original": "https://img.hhcdn.ru/employer-logo-original/1351461.png"
        },
        "vacancies_url": "https://api.hh.ru/vacancies?employer_id=11566922",
        "accredited_it_employer": 'false',
        "trusted": 'true'
    },
    "snippet": {
        "requirement": "Базовые знания HTML / CSS / JavaScript. React / React Native. English (на уровне понимания технических текстов). Русский язык (для общения). ",
        "responsibility": "Основы Front-End разработки."
    },
    "contacts": 'null',
    "schedule": {
        "id": "flexible",
        "name": "Гибкий график"
    },
    "working_days": [],
    "working_time_intervals": [],
    "working_time_modes": [],
    "accept_temporary": 'false',
    "professional_roles": [
        {
            "id": "96",
            "name": "Программист, разработчик"
        }
    ],
    "accept_incomplete_resumes": 'false',
    "experience": {
        "id": "between1And3",
        "name": "От 1 года до 3 лет"
    },
    "employment": {
        "id": "full",
        "name": "Полная занятость"
    },
    "adv_response_url": 'null',
    "is_adv_vacancy": 'false',
    "adv_context": 'null'
}


@patch("requests.get")
def test_hh(mock_get):
    """"""
    mock_get.return_value.json.return_value = {"items": [data_json_vac]}

    value = ''
    hh_1 = HH()
    hh_1.load_vacancies(value)
    result = hh_1.vacancies

    assert result == data_json_vac
