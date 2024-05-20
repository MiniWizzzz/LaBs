from PIL import Image
import sys

image=Image.open('popug.jpg')
image.show()

# задаем новый размер НОВОЙ картинке
new_size = (int(image.width / 3), int(image.height / 3))
resized_image = image.resize(new_size)
resized_image.save('minipopug.jpg')

image = Image.open('minipopug.jpg')
image.show()

try:
    minipopug = Image.open("minipopug.jpg")
except IOError:
    print("Не могу открыть изображение!")
    sys.exit(1)

rotated_180 = minipopug.transpose(Image.ROTATE_180)
rotated_180.save('minipopug_rotated_1.jpg')

rotated_flip = minipopug.transpose(Image.FLIP_LEFT_RIGHT)
rotated_flip.save('minipopug_rotated_2.jpg')