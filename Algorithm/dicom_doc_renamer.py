import os


def list_file_to_dcm(path_to_files: str) -> list:
    """
    Создаем список с файлами для переименования
    :param path_to_files: путь к папке с файлами
    :return: список с названиями файлов
    """
    for directs, direct, files in os.walk(path_to_files):
        print(files)
        return files


def rename_file(current_path: str, list_file: list):
    """
    Переименовываем файлы добавляя .dcm
    :param current_path: путь к папке с файлами
    :param list_file: список исходных имен файлов
    :return: None
    """
    for file in list_file:
        if file.endswith(".dcm"):
            pass
        else:
            print(file)
            os.renames(current_path + file, current_path + file + '.dcm')
