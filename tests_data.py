import json
import os

# Сделать ввод директории с тестами через терминал
allure_results_dir = './tests/allure-results'


def get_test_results_info():
    tests_info = []
    for filename in os.listdir(allure_results_dir):
        test_info = {}
        with open(allure_results_dir + '/' + filename, 'r') as file:
            file_data = json.load(file)

            test_name = file_data['name']
            test_info.update(test_name=test_name)

            test_status = file_data['status']
            test_info.update(test_status=test_status)
        tests_info.append(test_info)


get_test_results_info()
