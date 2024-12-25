import pytest
import allure


@allure.epic("Сервис с float-числами")
@pytest.mark.floats
class TestFloats:
    @allure.feature("Числа и float-числа")
    @allure.story("Сложение числа и float-числа")
    @allure.id("4")
    @allure.testcase('https://ratata.com/tc4')
    @allure.title("Проверка сложения числа и float-числа")
    def test_int_and_float_sum(self):
        int_num = 10
        float_num = 45.55
        assert int_num + float_num == 55.55

    @allure.feature("Числа и float-числа")
    @allure.story("Вычитание числа и float-числа")
    @allure.id("5")
    @allure.testcase('https://ratata.com/tc5')
    @allure.title("Проверка вычитания числа и float-числа")
    def test_int_and_float_diff(self):
        int_num = 33
        float_num = 3.33
        assert int_num - float_num == 30
