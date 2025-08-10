import allure
import requests
from faker import Faker
fake = Faker()

import data


class OrderMethods():

    @allure.step('создание заказа')
    def create_order(self, ingredients):
        data_param = {"ingredients": ingredients}
        responce = requests.post(f'{data.BASE_URL}{data.ORDER_CREATE_URL}', data=data_param)
        try:
            return responce.status_code, responce.json()
        except Exception:
            return responce.status_code, responce.text

    @allure.step('создание заказа с авторизацией')
    def create_order_autorized_user(self, ingredients, accesstoken):
        data_param = {"ingredients": ingredients}
        responce = requests.post(f'{data.BASE_URL}{data.ORDER_CREATE_URL}', data=data_param, headers={'Authorization': accesstoken})
        try:
            return responce.status_code, responce.json()
        except Exception:
            return responce.status_code, responce.text

    @allure.step('получение информации про ингридиенты')
    def get_ingredients_info(self):
        responce = requests.get(f'{data.BASE_URL}{data.GET_INGREDIENT_INFO_URL}')
        try:
            return responce.status_code, responce.json()
        except Exception:
            return responce.status_code, responce.text

    @allure.step('получение информации про заказы конкретного пользователя')
    def get_user_orders(self, accesstoken):
        responce = requests.get(f'{data.BASE_URL}{data.GET_USER_ORDERS}', headers={'Authorization': accesstoken})
        try:
            return responce.status_code, responce.json()
        except Exception:
            return responce.status_code, responce.text
