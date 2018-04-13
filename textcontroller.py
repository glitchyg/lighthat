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


def get_text_image(text, width, height, offset=0, wrap=False, saveImage=False):
    TOP_OFFSET = 1

    img = Image.new('RGB', (width, height), (0, 0, 0))

    fnt = ImageFont.truetype('munro.ttf', 7)

    # Create the drawer to place the text
    d = ImageDraw.Draw(img)

    # Get the size of the text we are going to draw
    size = d.textsize(text, font=fnt)

    # Wrap the offset if we need to
    if offset >= width:
        offset = offset % width

    if offset <= -width:
        offset = (offset % width)

    d.text((offset, TOP_OFFSET), text, font=fnt, fill=(0, 255, 0))

    if wrap:
        # Check if we even need to wrap forward.
        if offset + size[0] > width:
            wrap_offset = 0 - (width - offset)
            d.text((wrap_offset, TOP_OFFSET), text, font=fnt, fill=(0, 255, 0))

        if offset < 0:
            wrap_offset = (width - abs(offset))
            # print(size[0], width, offset, wrap_offset)
            d.text((wrap_offset, TOP_OFFSET), text, font=fnt, fill=(0, 255, 0))

    if saveImage:
        img.save('temp1.png')

    # # Flip the image
    # flipped_image = img.transpose(Image.FLIP_TOP_BOTTOM)
    # flipped_image.save('temp2.png')
    #

    return_image = Image.open('calibrate.png')

    rgb_img = img.convert('RGB')

    return rgb_img


get_text_image("HELLO WORLD", 64, 8, -10, True, True)

