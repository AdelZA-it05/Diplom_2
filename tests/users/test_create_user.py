import allure
import pytest
from faker import Faker
fake = Faker()


import data
from methods.user_methods import UserMethods

class TestCreateUser():

    @allure.title('Создание пользователя')
    @allure.description('Проверка корректного создания пользователя')

    @allure.testcase('создание уникального пользователя')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_create_uniq_user(self):
        testcreateuser = UserMethods()
        responce = testcreateuser.create_user()
        assert responce[0] ==  data.CODE_OK and responce[1]["success"] == True

    @allure.testcase('создание пользователя, который уже зарегистрирован')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_create_exist_user(self):
        testcreateuser = UserMethods()
        name = fake.user_name()
        email = fake.email()
        responce = testcreateuser.create_user(name=name, email=email)
        responce = testcreateuser.create_user(name=name, email=email)
        assert responce[0] == data.CODE_USER_EXIST and responce[1]["message"] == data.MSG_USER_EXIST

    @allure.testcase('создание пользователя с не заполненным одним из обязательных полей')
    @allure.issue('Ссылка на баг', 'BUG-007')
    @pytest.mark.parametrize('is_param',
                        [1, 2, 3])
    def test_create_user_empty_one_param(selfr, is_param):
        testcreateuser = UserMethods()
        responce = testcreateuser.create_user(is_param=is_param)
        assert responce[0] == data.CODE_EMPTY_REQUIRED_PARAM and responce[1]["message"] == data.MSG_EMPTY_REQUIRED_PARAM
