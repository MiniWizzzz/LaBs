from PIL import Image, ImageFilter
import os

valid_img = ("jpg", "jpeg")

def lab_9_1():
    # Получить список файлов из папки
    source_path_dir = os.path.join(os.getcwd(), "pic_1")
    output_path_dir = os.path.join(os.getcwd(), "pic_2")

    if not os.path.exists(output_path_dir):
        os.makedirs(output_path_dir)

    source_imgs_name = [
        f for f in os.listdir(source_path_dir) if not f.endswith("_filtered.jpg")
    ]

    for img_name in source_imgs_name:
        img_name, img_ext = os.path.splitext(img_name)
        if img_ext in valid_img:
            with Image.open(os.path.join(source_path_dir, img_name)) as image:
                filtered_image = image.convert("RGB").filter(ImageFilter.BLUR)
                filtered_image.save(os.path.join(output_path_dir, f"{img_name}_filtered.{img_ext}"))
#lab_9_1()