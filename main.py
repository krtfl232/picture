from PIL import Image,ImageFilter
with Image.open('i.webp') as pic:
    other_pic=pic.filter(ImageFilter.BLUR)
    blur_pic=other_pic.filter(ImageFilter.BLUR)
    for i in range(5):
        blur_pic=blur_pic.filter(ImageFilter.BLUR)
    blur_pic.show()
print('a')
