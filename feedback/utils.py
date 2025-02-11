
menu = [
    {'title': 'Запросить', 'url': 'test_constructor'},
    {'title': 'Исходящие запросы', 'url': 'my_tests'},
    {'title': 'Личная страница', 'url': 'user_dashboard'},
    {'title': 'Входящие запросы', 'url': 'available_tests'},
    {'title': 'Пользователи', 'url': 'users'},
]


def get_data(title):
    data = {
        'title': title,
        'menu': menu,
    }
    return data
