import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def get_path_to_resource():
    return f'{Path(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))}/Resource/'


def get_path_to_answer():
    return f'{get_path_to_resource()}answer.png'


def create_image_answer(time, cases, recovered, dead, rate):
    image = Image.open(f'{get_path_to_resource()}image_template.jpg')
    font_head = ImageFont.truetype(f'{get_path_to_resource()}/Fonts/amatic.ttf', 48)
    font_regular = ImageFont.truetype(f'{get_path_to_resource()}/Fonts/amatic.ttf', 45)
    d = ImageDraw.Draw(image)
    d.text((50, 90), f"Статистика на {time} UTC:", font=font_head, fill=(0, 0, 0))
    d.text((50, 150), f"Заразилось: {cases}", font=font_regular, fill=(0, 0, 0))
    d.text((50, 190), f"Выздоровело: {recovered}", font=font_regular, fill=(0, 0, 0))
    d.text((50, 230), f"Умерло: {dead}", font=font_regular, fill=(0, 0, 0))
    d.text((50, 270), f"Общая смертность: {rate}%", font=font_regular, fill=(0, 0, 0))
    image.save(f'{get_path_to_resource()}answer.png')
