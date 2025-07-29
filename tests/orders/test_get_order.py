import allure
import pytest
from faker import Faker
fake = Faker()

import data
from methods.order_methods import OrderMethods

from conftest import user
from conftest import authorize_user


class TestGetOreder():

    @allure.title('Получение заказов конкретного пользовател')
    @allure.description('Проверка корректности создания заказа под конкретным пользователем')

    @allure.testcase('заказ под авторизованным пользователем')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_get_autorized_user_orders(self, authorize_user):
        testgetorder = OrderMethods()
        responce = testgetorder.get_user_orders(authorize_user[1]["accessToken"])
        assert responce[0] == data.CODE_OK and responce[1]["success"] == True

    @allure.testcase('заказ под не авторизованным пользователем')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_get_not_autorized_user_orders(self, authorize_user):
        testgetorder = OrderMethods()
        responce = testgetorder.get_user_orders(None)
        assert responce[0] == data.CODE_401 and responce[1]["message"] == data.MSG_GET_ORDERS_NOT_AUTORIZED_USER