import configuration
import requests
import data

# создание нового пользователя
def post_new_user (body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user (data.user_body)
print(response.status_code)
# сохраняем токен запроса в переменную
user_token = response.json()


# сохраняем в измененный заголовок данные авторизации
data.headers_user ["Authorization"] = "Bearer " + str(response.json()['authToken'])



# создание нового набора для конкретного пользователя
def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         headers=data.headers_user,
                         json=body
                         )
response = post_new_client_kit(data.new_kit)

