from PIL import Image


img = Image.open('picture.JPG')
img_crop = img.crop((0,550,1600,1183))
img_crop.save('picture_crop.jpg')