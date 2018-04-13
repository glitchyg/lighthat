from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def test_text():

    print("Testing")

    img = Image.new('RGB', (64, 8), (100, 0, 0))


    rgb_img = img.convert('RGB')
    r, g, b = rgb_img.getpixel((0, 0))

    print(r, g, b)


def get_text_image(text, width, height):
    print("Testing")

    img = Image.new('RGB', (width, height), (100, 0, 0))

    # font = ImageFont.truetype("arial.ttf", 1)

    fnt = ImageFont.truetype('8bit.ttf', 8)

    d = ImageDraw.Draw(img)
    # d.text((0, 0), text, font=fnt, fill=(0, 255, 0))

    img.save('temp.png')

    rgb_img = img.convert('RGB')

    return rgb_img


get_text_image("HELLO", 64, 8)
