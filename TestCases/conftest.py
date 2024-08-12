import random
import string

import pytest
# from faker.generator import random
from selenium import webdriver

# import faker
# from faker import Faker

chrome_options = webdriver.ChromeOptions()


# chrome_options.add_argument("headless")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "Chrome":
        print("Test Run - Browser Chrome")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Test Run - Browser Firefox")
        driver = webdriver.Firefox()
    elif browser == "Edge":
        print("Test Run - Browser Edge")
        driver = webdriver.Edge()
    else:
        print("Test Run Headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://bankapp.credence.in/")
    driver.implicitly_wait(30)
    yield driver
    driver.quit()


# fake = Faker()


# @pytest.fixture()
# def random_userdata():
# #     return {
#         "username": fake.user_name(),
#         "password": fake.password(),
#
#         "email": fake.email(),
#         "phone": fake.phone_number()
#     }
#
#
# def test_random_user_data(random_user_data):
#     assert len(random_user_data['username']) == 6
#     assert len(random_user_data['password']) == 6
#     assert any(c.isupper() for c in random_user_data['password'])
#     assert any(c.islower() for c in random_user_data['password'])
#     assert any(c.isdigit() for c in random_user_data['password'])
#     assert any(c in string.punctuation for c in random_user_data['password'])
#     assert '@' in random_user_data['email']
#     assert len(random_user_data['phone']) == 10
#     assert any(c.isdigit() for c in random_user_data['phone'])
@pytest.fixture()
def generate_random_username(length=6):
    return 'User{0}'.format(''.join(random.choice(string.ascii_letters + string.digits, k=length)))


def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))


def generate_random_email(domain="gmail.com"):
    return generate_random_username() + "@" + domain


def generate_random_phone_number():
    return ''.join(random.choices(string.digits, k=10))


@pytest.fixture(params=[

    ("Admin", "pass"),
    ("Tushar", "pass"),
    ("Admin420", "fail"),
    ("demo2", "pass"),
    ("demo", "pass")
])
def getDataForSearchUser(request):
    return request.param
