from PIL import Image

# Открываем 2 изображения (главное изображение и водную марку)
original_image = Image.open("test1.jpg")
watermark = Image.open("watermark.png")

# Уровень прозрачности
transparency = 70

# Регулировка альфа-каналов
watermark = watermark.convert('RGBA')
watermark_with_transparency = Image.new('RGBA', watermark.size)
for x in range(watermark.width):
    for y in range(watermark.height):
        r, g, b, a = watermark.getpixel((x, y))
        if not (r == 0 and g == 0 and b == 0):
            watermark_with_transparency.putpixel((x, y), (r, g, b, transparency))

# Прописываем расположение водной марки
position = (10, 10)

# Добавляем марку
original_image.paste(watermark_with_transparency, position, watermark_with_transparency)

# Сохраняем
original_image.save("popug_v_kletke.jpeg")