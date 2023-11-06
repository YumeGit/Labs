import os
import requests
from bs4 import BeautifulSoup
import time

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
            img_name = str(downloaded_count).zfill(4) + '.jpg'
            img_path = os.path.join(folder_path, 'dataset_' + class_name, img_name)
            
            with open(img_path, 'wb') as img_file:
                img_file.write(img_data)

            downloaded_count += 1
            if downloaded_count >= num_images:
                break

            # Задержка между запросами
            time.sleep(3)   
    return downloaded_count

# URL-ы для поиска изображений зебры и байской лошади на Google Images
zebra_url = 'https://www.google.com/search?q=zebra&tbm=isch'
horse_url = 'https://www.google.com/search?q=bay+horse&tbm=isch'

# Путь к папке, где будут сохранены изображения
folder_path = 'D:/Test/dataset'

# Количество изображений, которые нужно загрузить для каждого класса
num_images = 30

# Загрузка изображений зебры
zebra_count = download_images(zebra_url, folder_path, 'zebra', num_images)

# Загрузка изображений байской лошади
horse_count = download_images(horse_url, folder_path, 'bay_horse', num_images)

# После этого вы можете проверить изображения на соответствие классу и дополнить недостающие, если необходимо.