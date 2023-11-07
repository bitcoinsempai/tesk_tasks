import json
import sys


def update_values(test_structure, values_dict):
    if isinstance(test_structure, dict):
        # Если это элемент с id и value, обновляем value
        if "id" in test_structure and "value" in test_structure:
            test_id = test_structure["id"]
            test_structure["value"] = values_dict.get(test_id, "")
        # Рекурсивно обновляем все подструктуры
        for key, value in test_structure.items():
            if isinstance(value, (dict, list)):
                update_values(value, values_dict)
    elif isinstance(test_structure, list):
        # Применяем функцию ко всем элементам списка
        for item in test_structure:
            update_values(item, values_dict)


def main(tests_filepath, values_filepath):
    report_filepath = 'report.json'  # Имя файла для вывода отчета
    try:
        # Загружаем данные из файлов
        with open(tests_filepath, 'r', encoding='utf-8') as file:
            tests_data = json.load(file)
        with open(values_filepath, 'r', encoding='utf-8') as file:
            values_data = json.load(file)

        # Создаем словарь для значений с id в качестве ключей
        values_dict = {item['id']: item['value'] for item in values_data['values']}

        # Обновляем структуру tests_data значениями из values_dict
        update_values(tests_data, values_dict)

        # Сохраняем обновленные данные в report.json
        with open(report_filepath, 'w', encoding='utf-8') as file:
            json.dump(tests_data, file, indent=4, ensure_ascii=False)

        print(f"Report saved to {report_filepath}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Проверяем, что скрипт вызван с корректным количеством аргументов
if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Usage: task3.py tests.json values.json")
