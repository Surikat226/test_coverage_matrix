import pytest
import allure


@allure.feature("Сервис со строками")
@pytest.mark.ints
class TestInts:
    @allure.story("Сложение строк и чисел")
    @allure.testcase('https://ratata.com/tc1')
    def test_hello_number(self):
        num = 5
        text = 'Hello, '
        assert text + str(num) == 'Hello, 5'
