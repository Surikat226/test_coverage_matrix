import json
import os
from argparse import ArgumentParser
from data.attributes import TestAttributes, TestLabels

# Сделать ввод директории с тестами через терминал
default_allure_results_dir = './tests/allure-results'

attribute = TestAttributes
label = TestLabels

# parser = ArgumentParser()
# parser.add_argument(
#     'repdir',
#     type=str,
#     help='Директория с allure-отчётами, на основе которой будет составлена матрица покрытия'
# )
# args = parser.parse_args()
# print(args.repdir)


class TestsData:
    def collect_test_data(self, allure_reports_dir: str = default_allure_results_dir):
        all_tests_data = []
        for filename in os.listdir(allure_reports_dir):
            test_info = []
            with open(allure_reports_dir + '/' + filename, 'r') as file:
                file_data = json.load(file)

                test_name = file_data[attribute.NAME]
                test_info.append(test_name)

                test_status = file_data[attribute.STATUS]
                test_info.append(test_status)
            all_tests_data.append(test_info)
        return all_tests_data

