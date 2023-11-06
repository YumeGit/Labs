
import os
import requests
from bs4 import BeautifulSoup
import time
import csv
import shutil
import random

folder_path = 'D:/Test/dataset322223'
new_dataset_path = 'D:/Test/dataset_new_new'

def create_annotation_file(folder_path, class_name, num_images):
    annotation_file_path = os.path.join(folder_path, 'annotations_' + class_name + '.csv')
    
    with open(annotation_file_path, 'w', newline='') as csvfile:
        fieldnames = ['absolute_path', 'relative_path', 'class']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(num_images):
            img_name = class_name + '_' + str(i).zfill(4) + '.jpg'
            absolute_path = os.path.join(folder_path, 'dataset_' + class_name, img_name)
            relative_path = os.path.relpath(absolute_path, folder_path)
            writer.writerow({'absolute_path': absolute_path, 'relative_path': relative_path, 'class': class_name})

# Создание аннотаций для зебры и байской лошади
num_images = 20
create_annotation_file(folder_path, 'zebra', num_images)
create_annotation_file(folder_path, 'bay_horse', num_images)

def copy_and_rename_with_random_numbers(original_path, new_path):
    for class_name in os.listdir(original_path):
        class_path = os.path.join(original_path, class_name)
        if os.path.isdir(class_path):
            os.makedirs(os.path.join(new_path, class_name), exist_ok=True)
            annotation_file_path = os.path.join(new_path, 'annotations_' + class_name + '.csv')
            
            with open(annotation_file_path, 'w', newline='') as csvfile:
                fieldnames = ['absolute_path', 'relative_path', 'class']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for filename in os.listdir(class_path):
                    random_number = random.randint(0, 10000)
                    _, file_extension = os.path.splitext(filename)
                    new_filename = str(random_number) + file_extension
                    original_file_path = os.path.join(class_path, filename)
                    new_file_path = os.path.join(new_path, class_name, new_filename)
                    shutil.copyfile(original_file_path, new_file_path)
                    
                    absolute_path = os.path.abspath(new_file_path)
                    relative_path = os.path.relpath(new_file_path, new_path)
                    writer.writerow({'absolute_path': absolute_path, 'relative_path': relative_path, 'class': class_name})

# Копирование и переименование файлов с случайными номерами
copy_and_rename_with_random_numbers(folder_path, new_dataset_path)

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
csv_file_path = os.path.join(folder_path, 'annotations_bay_horse.csv')
load_data_from_csv(csv_file_path)

class_label = 'bay_horse'
next_instance = get_next_instance(class_label)

if next_instance is not None:
    print(f'Следующий экземпляр класса {class_label}: {next_instance}')
else:
    print(f'Для класса {class_label} больше нет доступных экземпляров.')
