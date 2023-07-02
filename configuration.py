# Файл configuration.py необходим для хранения URL и путей запроса

# 1. URL Яндекс.Прилавка
URL_SERVICE = "https://482bf720-ab32-4d5f-8cff-5b269335e9d3.serverhub.praktikum-services.ru"

# 2. Путь до документации Яндекс.Прилавка
DOC_PATH = "/docs/"

# 3. Путь до логов основного сервера Яндекс.Прилавка
LOG_MAIN_PATH = "/api/logs/main/"

# 4. Путь до таблицы с текущими зарегистрированными пользователями Яндекс.Прилавка
USERS_TABLE_PATH = "/api/db/resources/user_model.csv"

# 5. Путь до запроса для создания нового пользователя Яндекс.Прилавка
CREATE_USER_PATH = "/api/v1/users/"

# 6. Путь до запроса для создания нового набора для данного пользователя Яндекс.Прилавка
CREATE_NEW_KIT = "/api/v1/kits"