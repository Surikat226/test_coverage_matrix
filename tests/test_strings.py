import pytest
import allure


@allure.feature("Сервис со строками")
@pytest.mark.strings
class TestStrings:
    @allure.story("Конкатенация строк")
    @allure.testcase('https://ratata.com/tc1')
    def test_hello_world(self):
        text = 'Hello world'
        assert text + '!' == 'Hello world!'

    @allure.story("Конкатенация строк")
    @allure.testcase('https://ratata.com/tc2')
    def test_say_my_name(self):
        name = 'Walter White'
        text = f'And {name} said: "Say my name..."'
        assert text == 'And Walter White said: "Say my name"'
