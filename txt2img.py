'''
img2txt - convert decimal values of ASCII characters into RGB values
Reads RGB values from .png and converts them into an ASCII string, then stores the string in a .txt file

Usage:
from txt2img import txt2img, img2txt

# ascii -> rgb
txt2img('data_in.txt', 'data_out.png')

rgb -> ascii
img2txt('data_out.png', 'data_back_in.txt')
'''
__version__ = '1.0'
__author__ = 'x.com/djcows'
__copyright__ = '(C)2024 djcows. GNU GPLv3.'

from utils import txt_to_ascii
from PIL import Image
import math

def txt2img(txt_path, img_path, max_size=65536):
    ascii_values = txt_to_ascii(txt_path)
    if not ascii_values:
        return 1
    
    # pad with zeroes to make length a multiple of 3
    ascii_values += [0] * ((3 - len(ascii_values) % 3) % 3)

    # calculate best fit square given data size
    pixel_count = len(ascii_values) // 3
    dim = min(math.ceil(math.sqrt(pixel_count)), max_size)

    print(f'image dimension set: {dim}x{dim}')

    # create and populate image array
    image = Image.new('RGB', (dim, dim), color='black')
    pixels = image.load()
    
    for idx in range(0, len(ascii_values), 3):
        x = (idx // 3) % dim
        y = (idx // 3) // dim
        if y < dim:
            r, g, b = ascii_values[idx:idx+3]
            pixels[x, y] = (r, g, b)
    
    # save image
    image.save(img_path)
    print(f'txt2img complete: {img_path}') 

def img2txt(img_path, txt_path):
    image = Image.open(img_path)
    pixels = image.load()
    width, height = image.size

    ascii_values = [pixels[x, y][i] for y in range(height) for x in range(width) for i in range(3)]
    ascii_values = [val for val in ascii_values if val != 0]

    # convert ascii decimal values to string
    text = ''.join(chr(value) for value in ascii_values)
    
    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(text)
    
    print(f'img2txt complete {txt_path}')
