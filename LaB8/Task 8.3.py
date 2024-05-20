from PIL import Image, ImageDraw, ImageFont


img = Image.open('picture.JPG')
img_crop = img.crop((0,550,1600,1183))
img_crop.save('picture_crop.jpg')

name = input("Кого поздравим? ")
full_text = str(name)+ ", поздравляю!"
draw_text = ImageDraw.Draw(img_crop)
font = ImageFont.truetype('./Styrene A LC-Black.otf', size=100)
draw_text.text(
    (100,100),
    full_text,
    font=font,
    fill=('#000000')
    )
img_crop.show()
