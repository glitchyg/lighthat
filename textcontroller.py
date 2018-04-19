from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

last_image_file = None
last_image_data = None

last_gif_file = None
last_gif_data = None
last_gif_frame_data = None
last_gif_frame = 0


# for frame in range(0,imageObject.n_frames):
#
#     imageObject.seek(frame)
#
#     imageObject.show()


def get_gif(file, frame):
    global last_gif_file, last_gif_data, last_gif_frame, last_gif_frame_data

    # img = None

    if file == last_gif_file:
        img = last_gif_data
    else:
        img = Image.open(file)
        last_gif_data = img

    last_gif_file = file

    if frame == last_gif_frame:
        return last_gif_frame_data

    if img.is_animated:
        frame = frame % img.n_frames
        img.seek(frame)
        img.show()

    rgb_img = img.convert('RGB')

    last_gif_frame_data = rgb_img

    return rgb_img


def get_image(file):
    global last_image_data, last_image_file

    if file == last_image_file:
        return last_image_data

    last_image_file = file

    img = Image.open(file)
    rgb_img = img.convert('RGB')

    last_image_data = rgb_img

    return rgb_img


def get_text_image(text, width, height, offset=0, wrap=False, saveImage=False, text_color=(255, 0, 0),
                   bg_color=(0, 0, 0)):
    # print(text_color)
    TOP_OFFSET = 0

    img = Image.new('RGB', (width, height), bg_color)

    fnt = ImageFont.truetype('8bit.ttf', 7)

    # Create the drawer to place the text
    d = ImageDraw.Draw(img)

    # Get the size of the text we are going to draw
    size = d.textsize(text, font=fnt)

    # Wrap the offset if we need to
    if offset >= width:
        offset = offset % width

    if offset <= -width:
        offset = (offset % width)

    d.text((offset, TOP_OFFSET), text, font=fnt, fill=text_color)

    if wrap:
        # Check if we even need to wrap forward.
        if offset + size[0] > width:
            wrap_offset = 0 - (width - offset)
            d.text((wrap_offset, TOP_OFFSET), text, font=fnt, fill=text_color)

        if offset < 0:
            wrap_offset = (width - abs(offset))
            # print(size[0], width, offset, wrap_offset)
            d.text((wrap_offset, TOP_OFFSET), text, font=fnt, fill=text_color)

    if saveImage:
        img.save('temp1.png')

    rgb_img = img.convert('RGB')

    return rgb_img


get_text_image("HELLO WORLD", 64, 8, -10, True, True)
