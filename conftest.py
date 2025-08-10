import pytest

from methods.user_methods import UserMethods


@pytest.fixture()
def user():
    responce = UserMethods().create_user()
    yield responce
    UserMethods().delete_user(responce[2][0], responce[2][1])

@pytest.fixture()
def authorize_user(user):
    responce = UserMethods().login_user(email=user[2][0], password=user[2][1])
    return responce
