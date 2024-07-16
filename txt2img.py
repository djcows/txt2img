'''
img2txt - convert decimal values of ASCII characters into RGB values'
eads RGB values from .png and convts into ascii string, then stores string in a .txt file

Basic usage:
from img2txt import txt2img, img2txt

ascii -> rgb
txt2img('./txt/bible_in.txt', './img/bible_out.png')

rgb -> ascii
img2txt('./img/bible_out.png', './txt/bible_back_in.txt')
'''
__version__ = '1.0'
__author__ = 'x.com/djcows'
__copyright__ = '(C)2024 djcows. GNU GPLv3.'

from PIL import Image
import math

'''convert ascii characters to decimal'''
def txt2img(txt_path, img_path, max_size=65536):
    ascii_values = _txt_to_ascii(txt_path)
    if not ascii_values:
        return 1
    
    while len(ascii_values) % 3 != 0:
        ascii_values.append(0)
    
    # calculate ideal square image dimension (we love x^2 in this house)
    pixel_count = len(ascii_values) // 3
    a = min(math.ceil(math.sqrt(pixel_count)), max_size)
    
    print(f'total ascii values: {len(ascii_values)}')
    print(f'image dimensions: {a}x{a}')
    
    # create image object in rgb mode
    image = Image.new('RGB', (a, a), color='black')
    pixels = image.load()
    
    # insert op
    ascii_index = 0
    for y in range(a):
        for x in range(a):
            if ascii_index < len(ascii_values) - 2:
                r = ascii_values[ascii_index]
                g = ascii_values[ascii_index + 1]
                b = ascii_values[ascii_index + 2]
                pixels[x, y] = (r, g, b)
                ascii_index += 3
            else:
                pixels[x, y] = (0, 0, 0)  # fill with black pixels if no data
    # save image
    image.save(img_path)

    print('text written to image')

# extract ascii from png
def img2txt(img_path, txt_path):
    image = Image.open(img_path)
    pixels = image.load()
    width, height = image.size

    ascii_values = []
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            ascii_values.extend([r, g, b])
    
    # convert ascii decimal to string
    text = ''.join(chr(value) for value in ascii_values)

    text = text.rstrip('\x00')

    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(text)
    
    print('image written to text')

def _txt_to_ascii(txt_path):
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            data = file.read()
        list_of_decimals = [ord(char) for char in data]
        return list_of_decimals
    except IOError as e:
        print(f'error reading .txt file: {e}')
        return []
    except Exception as e:
        print(f'unexpected error converting .txt file to ascii decimal: {e}')
        return []