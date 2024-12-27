import json
import os
from data.test_attributes import MainAttributes, LabelTypes, Links

attribute = MainAttributes
label_type = LabelTypes
link = Links

# TODO расскоментировать, когда код будет отдебажен
# parser = ArgumentParser()
# parser.add_argument(
#     'repdir',
#     type=str,
#     help='Директория с allure-отчётами, на основе которой будет составлена матрица покрытия',
# )
# args = parser.parse_args()

# Получаем директорию с результатами тестов из терминала
# allure_reports_dir = os.path.dirname(args.repdir)

# Для отладки
allure_reports_dir = os.path.dirname('./billing_platform/allure-results/')


# Берём имя директории на 1 уровень выше директории с результатами тестов и называем ей excel-лист
# TODO Возможно, sheet_name нужно брать из эпика
sheet_name = os.path.basename(os.path.dirname(allure_reports_dir))


class PrepareData:
    @staticmethod
    def collect_test_data(allure_reports_path_to_dir: str) -> list:
        """
        Собирает информацию о тестах, которая будет участвовать в матрице покрытия:
        (наименование тест-кейса и id кейса + гиперссылка на кейс) - строки,
        (название фичи) - столбцы,
        статус (зелёный/красный) - в ячейках
        :param allure_reports_path_to_dir:
        :return:
        """
        all_tests_data = []
        for filename in os.listdir(allure_reports_path_to_dir):
            if filename.endswith('result.json'):
                test_info = {}
                filepath = os.path.join(allure_reports_path_to_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    # TODO Реализовать обработку ошибок в случаях, когда не была найдена: ссылка, фича
                    file_data = json.load(file)
                    test_name = file_data[attribute.NAME]
                    test_id = next((i['value'] for i in file_data[attribute.LABELS] if i['name'] == label_type.ID))
                    test_status = file_data[attribute.STATUS]

                    # test_link = file_data[attribute.LINKS][0][link.URL]
                    test_link = file_data.get(attribute.LINKS, [{}])[0].get(link.URL, None)

                    # TODO Подумать, действительно ли нужны эпик и стори. Если да, то как их скомпоновать в excel
                    test_epic = next((i['value'] for i in file_data[attribute.LABELS] if i['name'] == label_type.EPIC), 'Эпик отсутствует')
                    test_feature = next((i['value'] for i in file_data[attribute.LABELS] if i['name'] == label_type.FEATURE))
                    test_story = next((i['value'] for i in file_data[attribute.LABELS] if i['name'] == label_type.STORY), 'Стори отсутствует')
                    test_ierarchy = []
                    test_ierarchy.extend(
                        [
                            {
                                'test_epic': test_epic,
                                'test_feature': test_feature,
                                'test_story': test_story
                            }
                        ]
                    )

                    test_info.update(
                        test_name=test_name,
                        test_id=test_id,
                        test_status=test_status,
                        test_link=test_link,
                        test_ierarchy=test_ierarchy
                    )
                all_tests_data.append(test_info)
        return all_tests_data
