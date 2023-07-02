# Файл create_kit_name_kit_test.py необходим для хранения всех чек-листов

# Импорт необходимых пакетов
import sender_stand_request
import data

# Коды для решения задачи
#1. Код для создания нового пользователя
def create_new_user():

   # Копируется словарь с телом запроса из файла "data.py"
   user_body = data.user_body.copy()

   # В переменную "user_response" сохраняется результат запроса на создание пользователя
   user_response = sender_stand_request.post_new_user(user_body)

   # Проверка, что код ответа равен 201
   assert user_response.status_code == 201

   # Проверка, что в ответе есть не пустое поле authToken не пустое
   assert user_response.json()["authToken"] != ""

   # Возврат значений
   return user_response.json()["authToken"]


#2. Код для получения заголовка для нового набора
def get_header_kit(auth_token):
    current_header = data.kit_headers.copy()
    current_header["Authorization"] = "Bearer " + auth_token

    # Возврат значений
    return current_header

#3. Код для получения тела запроса
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name

    # Возврат значений
    return current_body

#4. Код для создания нового набора для пользователя
def create_new_kit(auth_token,kit_body):
    kit_headers = get_header_kit(auth_token)

    # Возврат значений
    return sender_stand_request.post_new_user_kit(kit_headers, kit_body)


# Позитивные / негативные проверки
# Позитивные проверки
def positive_assert(name):
    auth_token = create_new_user()
    kit_body = get_kit_body(name)
    response = create_new_kit(auth_token, kit_body)

    # Проверка, что код ответа равен 201
    assert response.status_code == 201
    assert response.json()["name"] == name

# Негативные проверки
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    auth_token = create_new_user()
    response = create_new_kit(auth_token, kit_body)

    # Проверка, что код ответа равен 400
    assert response.status_code == 400
    assert response.json()["name"] == name

    # Проверяется текст в теле ответа в атрибуте "message"
    assert response.json()["message"] == "Не все необходимые параметры были переданы"

# Тестирование по чек-листу
# Тест №1. Допустимое количество символов (1)
def test_valid_symbol_1_in_name_get_positive_response():
    positive_assert("a")

# Тест №2. Допустимое количество символов (511)
def test_valid_symbol_511_in_name_get_positive_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест №3. Недопустимое количество символов (0)
def test_invalid_symbol_0_in_name_get_negative_response():
    negative_assert_code_400("")

# Тест №4. Недопустимое количество символов (512)
def test_invalid_symbol_512_in_name_get_negative_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест №5. Допустимые латинские буквы (QWErty)
def test_valid_latin_alphabet_in_name_get_positive_response():
    positive_assert("QWErty")

# Тест №6. Допустимые буквы кириллицы (Мария)
def test_valid_cyrillic_alphabet_in_name_get_positive_response():
    positive_assert("Мария")

# Тест №7. Допустимые спецсимволы ("№%@",)
def test_valid_special_symbol_in_name_get_positive_response():
    positive_assert("№%@",)

# Тест №8. Допустимые пробелы ("Человек и КО")
def test_valid_whitespace_in_name_get_positive_response():
    positive_assert("Человек и КО")

# Тест №9. Допустимые цифры (123)
def test_valid_numbers_in_name_get_positive_response():
    positive_assert("123")

# Тест №10. Параметр не передан в запросе
def negative_assert_no_kit_name(name):
    kit_body = get_kit_body(name)
    auth_token = create_new_user()
    response = create_new_kit(auth_token, kit_body)

    # Проверка, что код ответа равен 400
    assert response.status_code == 400

    # Проверка, что в теле ответа атрибут "code" равен 400
    assert response.json()["code"] == 400

    # Проверяется текст в теле ответа в атрибуте "message"
    assert response.json()["message"] == "Не все необходимые параметры были переданы"

def test_invalid_create_user_no_kit_name_get_negative_response():
    # Копируется словарь с телом запроса из файла "data.py" в переменную "kit_body"
    kit_body = data.kit_body.copy()

    # Удаление параметра "name" из запроса
    kit_body.pop("name")

    # Проверка полученного ответа
    negative_assert_no_kit_name(kit_body)

# Тест 11. Недопустимый тип параметра name: число
def test_invalid_create_user_number_kit_name_get_negative_response():

    # В переменную "kit_body" сохраняется обновлённое тело запроса
    kit_body = get_kit_body(123)
    auth_token = create_new_user()
    response = create_new_kit(auth_token, kit_body)

    # Проверка, что код ответа равен 400
    assert response.status_code == 400

    # Проверяется текст в теле ответа в атрибуте "message"
    assert response.json()["message"] == "Не все необходимые параметры были переданы"

    # Проверка, что код ответа равен 400
    assert response.status_code == 400

