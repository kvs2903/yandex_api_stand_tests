import data
import sender_stand_request
import pytest

# проверка успешного создания набора для конкретного пользователя
def test_success_kit_user():
    response = sender_stand_request.post_new_client_kit(data.new_kit)
    assert response.status_code == 201

# параметризация для ключа "name" в названии набора: ПОЗИТИВНЫЕ проверки
@pytest.mark.parametrize("name",[
    pytest.param("A", id="kit_user_1_simvol"),
    pytest.param("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabC",
                 id="kit_user_511_simvol"),
    pytest.param("QWErty", id="kit_user_Qwerty"),
    pytest.param("Мария", id="kit_user_russian_name"),
    pytest.param("\'№%@\',", id="kit_user_spec"),
    pytest.param("Человек и КО ", id="kit_user_probel"),
    pytest.param("123", id="kit_user_cifri")
        ])

# функция для ПОЗИТИВНОЙ проверки значений ключа "name"
def test_positive_assert (name):
    body_modify_positive = data.modify_name_kit_body(name)
    response = sender_stand_request.post_new_client_kit(body_modify_positive)
    # проверка, что возвращается 201
    assert response.status_code == 201
    # проверка, что имя в запросе совпадает с именем ответа
    assert response.json()["name"] == name

# параметризация для ключа "name" в названии набора: НЕГАТИВНЫЕ проверки
@pytest.mark.parametrize("name",[
    pytest.param("", id="kit_user_0_simvol"),
    pytest.param("Abcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD",
                 id="kit_user_512_simvol"),
    pytest.param(123, id="kit_user_chislo")
        ])

# функция НЕГАТИВНОЙ проверки значений ключа "name"
def test_negative_assert (name):
    body_modify_error = data.modify_name_kit_body(name)
    response = sender_stand_request.post_new_client_kit(body_modify_error)
    assert response.status_code == 400

# функция НЕГАТИВНОЙ проверки НЕПЕРЕДАННОГО значения ключа "name"
def test_negative_kit_user_ne_peredan ():
    body_modify_ne_peredan = data.new_kit.copy()
    body_modify_ne_peredan.pop("name")
    response = sender_stand_request.post_new_client_kit(body_modify_ne_peredan)
    assert response.status_code == 400
