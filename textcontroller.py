from PIL import Image



def test_text():

    print("Testing")

    img = Image.new('RGB', (64, 8), (100, 0, 0))


    rgb_img = img.convert('RGB')
    r, g, b = rgb_img.getpixel((0, 0))

    print(r, g, b)


def get_text_image(text, width, height):
    print("Testing")

    img = Image.new('RGB', (width, height), (100, 0, 0))

    rgb_img = img.convert('RGB')

    return rgb_img

test_text()
