from PIL import Image, ImageFilter

def LaB_7_3():
    # Задаем фильтры
    applied_filters = [
        ImageFilter.CONTOUR,
        ImageFilter.SMOOTH,
        ImageFilter.SHARPEN,
        ImageFilter.EMBOSS,
        ImageFilter.EDGE_ENHANCE,
    ]

    # Применяем фильтры на изображения и сохраняем
    for index, filter in enumerate(applied_filters):
        with Image.open(f"pic/{index + 1}.jpg") as image:
            new_image = image.filter(filter)
            new_image.save(f"pic/new_pic/{index+1}_filtered.jpg")
LaB_7_3()