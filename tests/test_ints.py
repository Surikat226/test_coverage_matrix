import pytest
import allure


@allure.epic("Сервис с числами")
@pytest.mark.ints
class TestInts:
    @allure.feature("Сложение строк и чисел")
    @allure.story("Сложение хелловорлд и числа")
    @allure.id("3")
    @allure.testcase('https://ratata.com/tc3')
    def test_hello_number(self):
        num = 5
        text = 'Hello, '
        assert text + str(num) == 'Hello, 5'
