from PIL import Image

img = Image.open('popug.jpg')
img.show()

image_info = {
    'Размер': img.size,
    'Формат': img.format,
    'Режим': img.mode
}

for key, value in image_info.items():
    print(f'{key}: {value}')