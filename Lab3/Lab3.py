import os
import requests
from bs4 import BeautifulSoup
import time
import csv
import shutil
import csv
import random

folder_path = 'D:/Test/dataset322223'

# Количество изображений, которые нужно загрузить для каждого класса
num_images = 20

# Путь нового датасета
new_dataset_path = 'D:/Test/dataset_new'

# Функция для копирования и переименования файлов и создания аннотации
def copy_and_rename_dataset(original_path, new_path, class_name):
    os.makedirs(new_path, exist_ok=True)
    
    annotation_file_path = os.path.join(new_path, 'annotations_' + class_name + '.csv')
    
    with open(annotation_file_path, 'w', newline='') as csvfile:
        fieldnames = ['absolute_path', 'relative_path', 'class']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        i = 0
        for file in os.listdir(os.path.join(original_path, 'dataset_' + class_name)):
            original_img_name = class_name + '_' + str(i).zfill(4) + '.jpg'
            original_img_path = os.path.join(original_path, 'dataset_' + class_name, original_img_name)
            new_img_path = os.path.join(new_path, original_img_name)
            shutil.copyfile(original_img_path, new_img_path)
            
            # Записываем данные в аннотацию
            absolute_path = os.path.abspath(new_img_path)
            relative_path = os.path.relpath(new_img_path, new_path)
            writer.writerow({'absolute_path': absolute_path, 'relative_path': relative_path, 'class': class_name})
            i += 1

# Копирование и переименование датасета зебры
copy_and_rename_dataset(folder_path, new_dataset_path, 'zebra')

# Копирование и переименование датасета байской лошади
copy_and_rename_dataset(folder_path, new_dataset_path, 'bay_horse')

new_dataset_path = 'D:/Test/dataset_new_new'
def copy_and_rename_with_random_numbers(original_path, new_path):
    for class_name in os.listdir(original_path):
        class_path = os.path.join(original_path, class_name)
        if os.path.isdir(class_path):
            os.makedirs(new_path, exist_ok=True)
            for filename in os.listdir(class_path):
                # Генерируем случайное число для имени файла
                random_number = random.randint(0, 10000)
                # Получаем расширение файла
                _, file_extension = os.path.splitext(filename)
                # Формируем новое имя файла с случайным номером и оригинальным расширением
                new_filename = str(random_number) + file_extension
                original_file_path = os.path.join(class_path, filename)
                new_file_path = os.path.join(new_path, new_filename)
                # Копируем и переименовываем файл
                shutil.copyfile(original_file_path, new_file_path)

# Копирование и переименование файлов с случайными номерами
copy_and_rename_with_random_numbers(folder_path, new_dataset_path)



# Словарь, содержащий экземпляры классов
class_instances = {
    'bay_horse': ['D:\\Test\dataset322223\dataset_bay_horse', 'D:\\Test\\dataset_new\\_bay_horse_'],
    'zebra': ['D:\\Test\dataset322223\\dataset_zebra', 'D:\\Test\\dataset_new\\zebra_', 'obamna']
}


# Словарь, содержащий экземпляры классов
class_instances = {}

# Функция для чтения данных из CSV файла и заполнения словаря
def load_data_from_csv(csv_file_path):
    with open(csv_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            class_label = row['class']
            instance_path = row['relative_path']
            if class_label not in class_instances:
                class_instances[class_label] = []
            class_instances[class_label].append(instance_path)

# Функция для получения следующего экземпляра класса
def get_next_instance(class_label):
    if class_label in class_instances and class_instances[class_label]:
        # Извлекаем случайный экземпляр класса
        instance = random.choice(class_instances[class_label])
        # Удаляем из списка выбранный экземпляр
        class_instances[class_label].remove(instance)
        return instance
    else:
        # Если список экземпляров пуст, возвращаем None
        return None

# Пример использования функций
csv_file_path = 'D:\\Test\\dataset322223\\annotations_bay_horse.csv'
load_data_from_csv(csv_file_path)

class_label = 'bay_horse'
next_instance = get_next_instance(class_label)

if next_instance is not None:
    print(f'Следующий экземпляр класса {class_label}: {next_instance}')
else:
    print(f'Для класса {class_label} больше нет доступных экземпляров.')
