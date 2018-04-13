from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def test_text():
    print("Testing")

    img = Image.new('RGB', (64, 8), (100, 0, 0))

    rgb_img = img.convert('RGB')
    r, g, b = rgb_img.getpixel((0, 0))

    print(r, g, b)


def get_image(file):
    img = Image.open(file)
    rgb_img = img.convert('RGB')
    return rgb_img


def get_text_image(text, width, height, offset=0, wrap=False):
    img = Image.new('RGB', (width, height), (0, 0, 0))

    fnt = ImageFont.truetype('munro.ttf', 7)

    # Create the drawer to place the text
    d = ImageDraw.Draw(img)

    # Wrap the offset if we need to
    if offset >= width:
        offset = 0

    d.text((offset, 0), text, font=fnt, fill=(0, 255, 0))

    # Get the size of the text we are going to draw
    size = d.textsize(text, font=fnt)

    # img.save('temp1.png')

    # # Flip the image
    # flipped_image = img.transpose(Image.FLIP_TOP_BOTTOM)
    # flipped_image.save('temp2.png')
    #

    return_image = Image.open('calibrate.png')

    rgb_img = img.convert('RGB')

    return rgb_img


get_text_image("HELLO", 64, 8)

