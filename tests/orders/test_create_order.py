import allure
from faker import Faker
fake = Faker()

import data
from methods.order_methods import OrderMethods


class TestCreateOreder():

    @allure.title('Создание заказа')
    @allure.description('Проверка корректности создания заказа под конкретным пользователем')

    @allure.testcase('Создание заказа с авторизацией')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_create_order_autorized_user(self, authorize_user, user):
        testcreateorder = OrderMethods()
        responce = testcreateorder.get_ingredients_info()
        ingredients = responce[1]["data"][0]["_id"]
        responce = testcreateorder.create_order_autorized_user(ingredients, authorize_user[1]["accessToken"])
        assert responce[0] == 200 and responce[1]["success"] == True and "owner" in responce[1]["order"].keys()

    @allure.testcase('Создание заказа без авторизации')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_create_order_not_autorized_user(self):
        testcreateorder = OrderMethods()
        responce = testcreateorder.get_ingredients_info()
        ingredients = responce[1]["data"][0]["_id"]
        responce = testcreateorder.create_order(ingredients)
        assert responce[0] == 200 and responce[1]["success"] == True  and "owner" not in responce[1]["order"].keys()

    @allure.testcase('Создание заказа с ингредиентами')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_create_order_with_ingredients_user(self):
        testcreateorder = OrderMethods()
        responce = testcreateorder.get_ingredients_info()
        ingredients = responce[1]["data"][0]["_id"]
        responce = testcreateorder.create_order(ingredients)
        assert responce[0] == data.CODE_CREATE_ORDER_WITH_INGREDIENTS and responce[1]["success"] == data.MSG_CREATE_ORDER_WITH_INGREDIENTS

    @allure.testcase('Создание заказа без ингредиентов')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_create_order_without_ingredients_user(self):
        testcreateorder = OrderMethods()
        responce = testcreateorder.get_ingredients_info()
        ingredients = None
        responce = testcreateorder.create_order(ingredients)
        assert responce[0] == data.CODE_CREATE_ORDER_WITHOUT_INGREDIENTS and responce[1]["message"] == data.MSG_CREATE_ORDER_WITHOUT_INGREDIENTS

    @allure.testcase('Создание заказа с неверным хешем ингредиентов')
    @allure.issue('Ссылка на баг', 'BUG-007')
    def test_create_order_fake_ingredients_user(self):
        testcreateorder = OrderMethods()
        responce = testcreateorder.get_ingredients_info()
        ingredients = fake.text()
        responce = testcreateorder.create_order(ingredients)
        assert responce[0] == data.CODE_CREATE_ORDER_FAKE_INGREDIENTS

