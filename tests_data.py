import json
import os
from argparse import ArgumentParser
from data.attributes import MainAttributes, LabelTypes, Links

# Сделать ввод директории с тестами через терминал
default_allure_results_dir = './tests/allure-results'

attribute = MainAttributes
label_type = LabelTypes
link = Links


# parser = ArgumentParser()
# parser.add_argument(
#     'repdir',
#     type=str,
#     help='Директория с allure-отчётами, на основе которой будет составлена матрица покрытия'
# )
# args = parser.parse_args()
# print(args.repdir)


class TestsData:
    def collect_test_data(
        self,
        allure_reports_dir: str = default_allure_results_dir
    ):
        """
        Собирает информацию о тестах, которая будет участвовать в матрице покрытия:
        (наименование тест-кейса и id кейса + гиперссылка на кейс) - строки,
        (название фичи) - столбцы,
        статус (зелёный/красный) - в ячейках
        :param allure_reports_dir:
        :return:
        """
        all_tests_data = []
        for filename in os.listdir(allure_reports_dir):
            test_info = []
            with open(allure_reports_dir + '/' + filename, 'r', encoding='utf-8') as file:
                file_data = json.load(file)

                test_name = file_data[attribute.NAME]
                test_id = next((i['value'] for i in file_data[attribute.LABELS] if i['name'] == label_type.ID))
                test_status = file_data[attribute.STATUS]
                test_link = file_data[attribute.LINKS][0][link.URL]

                test_ierarchy = []
                test_epic = next((i['value'] for i in file_data[attribute.LABELS] if i['name'] == label_type.EPIC))
                test_feature = next((i['value'] for i in file_data[attribute.LABELS] if i['name'] == label_type.FEATURE))
                test_story = next((i['value'] for i in file_data[attribute.LABELS] if i['name'] == label_type.STORY))
                test_ierarchy.extend([test_epic, test_feature, test_story])

                test_info.extend([test_name, test_id, test_status, test_link, test_ierarchy])
            all_tests_data.append(test_info)
        return all_tests_data

    def prepare_coverage_data_for_matrix(self, service_name: str = None):
        pass