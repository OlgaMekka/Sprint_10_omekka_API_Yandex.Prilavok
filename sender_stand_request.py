# Файл sender_stand_request.py необходим для хранения всех запросов

# Импорт необходимых пакетов
import configuration
import requests
import data

# 1. GET-запрос на получение страницы с документацией API Яндекс.Прилавка
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
    response = get_docs()
    print(response.status_code)
    print(response.text)


# 2. GET-запрос на получение страницы с логами основного сервера Яндекс.Прилавка
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)
    response = get_logs()
    print(response.status_code)
    print(response.headers)
    print(response.text)


# 3. GET-запрос на получение таблицы с текущими зарегистрированными пользователями Яндекс.Прилавка
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
    response = get_users_table()
    print(response.status_code)
    print(response.headers)
    print(response.text)

# 4. POST-запрос на создание нового пользователя Яндекс.Прилавка
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)
     # response = post_new_user(data.user_body)
     # print(response.status_code)

# 5. POST-запрос на создание нового набора для данного пользователя Яндекс.Прилавка
def post_new_user_kit(kit_headers,kit_body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_KIT,
                        json=kit_body,
                        headers=kit_headers)
     # response = post_new_user_kit(data.kit_headers, data.kit_body)
     # print(response.status_code)