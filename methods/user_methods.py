import allure
import requests
from faker import Faker
fake = Faker()

import data


class UserMethods():

    @allure.step('создание пользователя')
    def create_user(self, name=None, email=None, password=None, is_param=0):
        if is_param == 0:
            if not name: name = fake.user_name()
            if not email: email = fake.email()
            if not password: password = fake.password()
        elif is_param == 1:
            name = None
            if not email: email = fake.email()
            if not password: password = fake.password()
        elif is_param == 2:
            if not name: name = fake.user_name()
            email = None
            if not password: password = fake.password()
        elif is_param == 3:
            if not name: name = fake.user_name()
            if not email: email = fake.email()
            password = None
        data_param = {
            "email": email,
            "password": password,
        "name": name
        }
        responce = requests.post(f'{data.BASE_URL}{data.USER_CREATE_URL}', data=data_param)
        try:
            return responce.status_code, responce.json(), [email, password, name]
        except Exception:
            return responce.status_code, responce.text, [email, password, name]

    @allure.step('логин под пользователем')
    def login_user(self, email=None, password=None):
        data_param = {
            "email": email,
            "password": password
        }

        responce = requests.post(f'{data.BASE_URL}{data.USER_LOGIN_URL}', data=data_param)
        try:
            return responce.status_code, responce.json(), email, password
        except Exception:
            return responce.status_code, responce.text, email, password

    @allure.step('логаут пользователя')
    def logout_user(self, p_refreshtoken):
        data_param = '{"token": "{{' + p_refreshtoken + '}}"}'

        responce = requests.post(f'{data.BASE_URL}{data.USER_LOGOUT_URL}', data=data_param)
        try:
            return responce.status_code, responce.json()
        except Exception:
            return responce.status_code, responce.text

    @allure.step('удаление пользователя')
    def delete_user(self, email = None, password = None):
        responce = self.login_user(email, password)
        p_accesstoken = responce[1]["accessToken"]
        responce = requests.delete(f'{data.BASE_URL}{data.USER_DELETE_URL}', headers={'Authorization': p_accesstoken})
        return responce

    @allure.step('изменение данных пользователя')
    def edit_autorized_user_data(self, data_param, accesstoken):
        responce = requests.patch(f'{data.BASE_URL}{data.USER_EDIT_DATA_URL}', data=data_param, headers={'Authorization': accesstoken})
        try:
            return responce.status_code, responce.json()
        except Exception:
            return responce.status_code, responce.text

    @allure.step('получение данных авторизованного пользователя')
    def get_autorized_user_data(self, accesstoken):
        responce = requests.get(f'{data.BASE_URL}{data.USER_EDIT_DATA_URL}', headers={'Authorization': accesstoken})
        try:
            return responce.status_code, responce.json()
        except Exception:
            return responce.status_code, responce.text


