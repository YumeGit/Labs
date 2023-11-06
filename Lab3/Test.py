import os
import requests
from bs4 import BeautifulSoup
import time
import csv
import shutil

# Функция для создания папок и загрузки изображений по URL с задержкой
def download_images(url, folder_path, class_name, num_images):
    os.makedirs(os.path.join(folder_path, 'dataset_' + class_name), exist_ok=True)
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    downloaded_count = 0
    for img_tag in img_tags:
        img_url = img_tag.get('src')
        
        if img_url and img_url.startswith('http'):
            img_data = requests.get(img_url).content
            img_name = class_name + '_' + str(downloaded_count).zfill(4) + '.jpg'
            img_path = os.path.join(folder_path, 'dataset_' + class_name, img_name)
            
            with open(img_path, 'wb') as img_file:
                img_file.write(img_data)

            downloaded_count += 1
            if downloaded_count >= num_images:
                break

            # Задержка между запросами
            time.sleep(3)   
    return downloaded_count

# Функция для создания текстового файла-аннотации
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

# URL-ы для поиска изображений зебры и байской лошади на Google Images
zebra_url = 'https://www.google.com/search?q=zebra&tbm=isch'
horse_url = 'https://www.google.com/search?q=bay+horse&tbm=isch'

# Путь к папке, где будут сохранены изображения
folder_path = 'D:/Test/dataset322223'

# Количество изображений, которые нужно загрузить для каждого класса
num_images = 30

# Загрузка изображений зебры
zebra_count = download_images(zebra_url, folder_path, 'zebra', num_images)

# Загрузка изображений байской лошади
horse_count = download_images(horse_url, folder_path, 'bay_horse', num_images)

# Создание текстового файла-аннотации для изображений зебры
create_annotation_file(folder_path, 'zebra', num_images)

# Создание текстового файла-аннотации для изображений байской лошади
create_annotation_file(folder_path, 'bay_horse', num_images)

# Путь нового датасета
new_dataset_path = 'D:/Test/dataset_new'

# Функция для копирования и переименования файлов и создания аннотации
def copy_and_rename_dataset(original_path, new_path, class_name, num_images):
    os.makedirs(os.path.join(new_path, 'dataset_' + class_name), exist_ok=True)
    
    annotation_file_path = os.path.join(new_path, 'annotations_' + class_name + '.csv')
    
    with open(annotation_file_path, 'w', newline='') as csvfile:
        fieldnames = ['absolute_path', 'relative_path', 'class']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(num_images):
            original_img_name = class_name + '_' + str(i).zfill(4) + '.jpg'
            original_img_path = os.path.join(original_path, 'dataset_' + class_name, original_img_name)
            new_img_path = os.path.join(new_path, 'dataset_' + class_name, original_img_name)
            shutil.copyfile(original_img_path, new_img_path)
            
            # Записываем данные в аннотацию
            absolute_path = os.path.abspath(new_img_path)
            relative_path = os.path.relpath(new_img_path, new_path)
            writer.writerow({'absolute_path': absolute_path, 'relative_path': relative_path, 'class': class_name})

# Копирование и переименование датасета зебры
copy_and_rename_dataset(folder_path, new_dataset_path, 'zebra', num_images)

# Копирование и переименование датасета байской лошади
copy_and_rename_dataset(folder_path, new_dataset_path, 'bay_horse', num_images)