headers = {
    "Content-Type": "application/json"
}

headers_user = {
    "Content-Type": "application/json",
    "Authorization": "Bearer"
}

new_kit = {
    "name": "my_kit"
}

user_body = {
    "firstName": "Анатолий",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}


def modify_kit_body(key,value):
    new_body=new_kit.copy()
    new_body[key]=value
    return new_body


def modify_name_kit_body(value):
    return modify_kit_body("name", value)

