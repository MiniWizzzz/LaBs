from PIL import Image, ImageFilter
import os

# Путь к папке с изображениями
images_folder = 'Исходные'

# Загружаем все изображения из папки
images = os.listdir(images_folder)

# Применяем фильтр к каждому изображению
for image_name in images:
    image_path = os.path.join(images_folder, image_name)
    image = Image.open(image_path)

    # Применяем фильтр к изображению
    filtered_image = image.filter(ImageFilter.BLUR)
    filtered_image.save(f"Отфильтрованные/filtered_{image_name}")
