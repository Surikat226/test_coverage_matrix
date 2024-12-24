import pytest
import allure


@allure.epic("Сервис со строками")
@pytest.mark.strings
class TestStrings:
    @allure.feature("Сложение строк")
    @allure.story("Сложение хелловорлд")
    @allure.id("1")
    @allure.link('https://ratata.com/tc1')
    @allure.title("Проверка сложения воскл. знака и хелловорлд")
    def test_hello_world(self):
        text = 'Hello world'
        assert text + '!' == 'Hello world!'

    @allure.feature("Сложение строк")
    @allure.story("Сложение строк брейкинг бэд")
    @allure.id("2")
    @allure.link('https://ratata.com/tc2')
    @allure.title("Проверка сложения имени В. Уайта и его фразы")
    def test_say_my_name(self):
        name = 'Walter White'
        text = f'And {name} said: "Say my name..."'
        assert text == 'And Walter White said: "Say my name"'
