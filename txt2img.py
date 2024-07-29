'''
 _        _   ____  _                 
| |___  _| |_|___ \(_)_ __ ___   __ _ 
| __\ \/ / __| __) | | '_ ` _ \ / _` |
| |_ >  <| |_ / __/| | | | | | | (_| |
 \__/_/\_\\__|_____|_|_| |_| |_|\__, |
                                |___/

store data in pixels
'''
__author__ = 'djcows'
__version__ = '2.0'
__copyright__ = 'GNU GPLv3'

import os
import math
import sys
import numpy as np
from PIL import Image
from utils import file_to_binary, binary_to_file, compress_data, decompress_data

class Txt2Img:
    def txt2img(self, input_file: str, output_image: str, compression_level=9):
        # protect user from compressing files >500mb while not supported
        if os.path.getsize(input_file) > 500000000:
            ui = input('LARGE FILE WARNING\nLarge filesizes are not supported and are extremely slow.\nProceed? (Y/n)')
            if ui.lower() != 'y':
                print('txt2img operation cancelled')
                sys.exit()

        binary_data = file_to_binary(input_file)
        try:
            compressed_data = compress_data(binary_data, compression_level)
        except Exception as e:
            print(f'compression failed: {str(e)}')
            return 1

        # use RGBA with 8-bit color depth
        rgba_values = np.frombuffer(compressed_data, dtype=np.uint8)
        
        # calculate ideal size of image, perfect square for simplicity
        pixel_count = math.ceil(len(rgba_values) / 4)
        max_size=65536
        dim = min(math.ceil(math.sqrt(pixel_count)), max_size)
        print(f'output image dimensions = {dim}x{dim}')
        
        # create array of ideal size
        image_array = np.full((dim, dim, 4), 255, dtype=np.uint8)
        image_array.flat[:len(rgba_values)] = rgba_values

        # save
        image = Image.fromarray(image_array, 'RGBA')
        image.save(output_image, format='PNG', compress_level=9)

        original_size = os.path.getsize(input_file)
        image_size = os.path.getsize(output_image)
        
        print(f'output file created: {output_image}\ninput size: {original_size} bytes\noutput size: {image_size} bytes\n')
        print(f'filesize delta: {(1 - image_size/original_size) * 100:.2f}%')

    # mirrors file_to_image steps
    def img2txt(self, input_image: str, output_file: str):
        if os.path.getsize(input_image) > 500000000:
            ui = input('LARGE FILE WARNING\nLarge filesizes are not natively supported and are extremely slow.\nProceed? (Y/n)')
            if ui.lower() != 'y':
                print('img2txt operation cancelled')
                sys.exit()

        image = Image.open(input_image)
        rgba_values = np.array(image)
        compressed_data = rgba_values.tobytes()

        try:
            binary_data = decompress_data(compressed_data)
        except Exception as e:
            print(f'decompression failed: {str(e)}')
            return 1

        binary_to_file(binary_data, output_file)
        print(f'output file created: {output_file}')
        return 0
    