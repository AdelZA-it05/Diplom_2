import allure
import pytest
from faker import Faker
fake = Faker()

import data
from methods.user_methods import UserMethods

from conftest import user


class TestLoginUser():

    @allure.title('Логин пользователя')
    @allure.description('Проверка корректной авторизации под существующим пользователем и неверным логином и паролем')

    @allure.testcase('Тест-кейс: логин под существующим пользователем')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_login_exist_user(self, user):
        testloginuser = UserMethods()
        responce = testloginuser.login_user(user[2][0], user[2][1])
        p_refreshtoken = responce[1]["refreshToken"]
        testloginuser.logout_user(p_refreshtoken)
        assert responce[0] == data.CODE_EXIST_USER_LOGIN and responce[1]["success"] == data.MSG_EXIST_USER_LOGIN

    @allure.testcase('Тест-кейс: логин с неверным логином и паролем')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_login_fake_user(self):
        testloginuser = UserMethods()
        responce = testloginuser.login_user(fake.email(),  fake.password())
        assert responce[0] == data.CODE_FAKE_USER_LOGIN and responce[1]["message"] == data.MSG_FAKE_USER_LOGIN
