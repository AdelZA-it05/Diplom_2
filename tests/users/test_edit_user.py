import allure
import pytest
from faker import Faker
fake = Faker()

import data
from methods.user_methods import UserMethods


class TestEditUser():


    @allure.title('Изменение данных пользователя')
    @allure.description('Проверка корректного изменения данных пользователя с авторизацией и без авторизации')
    @allure.testcase('Тест-кейс: изменение данных с авторизацией')
    @pytest.mark.parametrize('is_param',
                             ['{"email": new_email, "password": new_password, "name": new_name}',
                              '{"email": new_email, "password": password, "name": name}',
                              '{"email": email, "password": new_password, "name": name}',
                              '{"email": email, "password": password, "name": new_name}'])
    def test_edit_autorized_user(self, is_param):
        testedituser = UserMethods()
        responce = testedituser.create_user()

        email, password, name = responce[2][0], responce[2][1], responce[2][2]
        responce = testedituser.login_user(email, password)
        p_accesstoken = responce[1]["accessToken"]

        new_email, new_password, new_name = fake.email(), fake.password(), fake.user_name()

        data_param = is_param
        responce = testedituser.edit_autorized_user_data(data_param, p_accesstoken)

        assert responce[0] == data.CODE_AUTORIZED_USER_EDIT and responce[1]["success"] == data.MSG_AUTORIZED_USER_EDIT

    @allure.testcase('Тест-кейс: изменение данных без авторизациии')
    @pytest.mark.parametrize('is_param',
                             ['{"email": new_email, "password": new_password, "name": new_name}',
                              '{"email": new_email, "password": password, "name": name}',
                              '{"email": email, "password": new_password, "name": name}',
                              '{"email": email, "password": password, "name": new_name}'])
    def test_edit_unautorized_user(self, is_param):
        testedituser = UserMethods()
        responce = testedituser.create_user()

        email, password, name = responce[2][0], responce[2][1], responce[2][2]
        p_accesstoken = None

        new_email, new_password, new_name = fake.email(), fake.password(), fake.user_name()

        data_param = is_param

        responce = testedituser.edit_autorized_user_data(data_param, p_accesstoken)

        assert responce[0] == data.CODE_UNAUTORIZED_USER_EDIT and responce[1][
            "success"] == data.MSG_UNAUTORIZED_USER_EDIT


        data_param = {"email": new_email, "password": new_password, "name": new_name}
        responce = testedituser.edit_autorized_user_data(data_param, p_accesstoken)

        assert responce[0] == data.CODE_AUTORIZED_USER_EDIT and responce[1]["success"] == data.MSG_AUTORIZED_USER_EDIT

    @allure.testcase('Тест-кейс: изменение данных без авторизациии')
    @allure.issue('Ссылка на баг', 'BUG-007')
    @pytest.mark.parametrize('is_param',
                             [0, 1, 2, 3])
    def test_edit_unautorized_user(self, is_param):
        testedituser = UserMethods()
        responce = testedituser.create_user()

        email, password, name = responce[2][0], responce[2][1], responce[2][2]
        p_accesstoken = None

        new_email = new_password = new_name = None
        if is_param == 0: new_email, new_password, new_name = fake.email(), fake.password(), fake.user_name()
        if is_param == 1: new_email, new_password, new_name = fake.email(), password, name
        if is_param == 2: new_email, new_password, new_name = email, fake.password(), name
        if is_param == 3: new_email, new_password, new_name = email, password, fake.user_name()

        data_param = {"email": new_email, "password": new_password, "name": new_name}
        responce = testedituser.edit_autorized_user_data(data_param, p_accesstoken)

        assert responce[0] == data.CODE_UNAUTORIZED_USER_EDIT and responce[1]["success"] == data.MSG_UNAUTORIZED_USER_EDIT
