# Файл data.py необходим для хранения данных

# Заголовок
headers = {
    "Content-Type": "application/json"
}

# Заголовок набора
kit_headers = {
    "Content-Type": "application/json",
    "Authorization": ""
}

# Тело запроса на создание нового пользователя
user_body = {
    "firstName": "Оля",
    "phone": "+79956255526",
    "address": "г. Санкт-Петербург, пр-кт Просвещения, д. 69"
}

# Тело запроса на создание нового набора данного пользователя
kit_body = {
    "name": "Набор"
}