import pytest
import allure


@allure.epic("Сервис со строками")
@pytest.mark.strings
class TestStrings:
    @allure.feature("Сложение строк")
    @allure.story("Сложение хелловорлд")
    @allure.testcase('https://ratata.com/tc1')
    def test_hello_world(self):
        text = 'Hello world'
        assert text + '!' == 'Hello world!'

    @allure.feature("Сложение строк")
    @allure.story("Сложение строк брейкинг бэд")
    @allure.testcase('https://ratata.com/tc2')
    def test_say_my_name(self):
        name = 'Walter White'
        text = f'And {name} said: "Say my name..."'
        assert text == 'And Walter White said: "Say my name"'
