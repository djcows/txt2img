# txt2img - lossless data compression using pixels
Embeds binary data to pixel values of images

Example:
king_james_bible.txt (4.3mb) ---> king_james_bible.png (1.0mb)
![bible_small](https://github.com/user-attachments/assets/9d47be7d-2c6d-4dd8-89c8-c90871dcd5fd)

## Usage
1. Install packages: ```pip install -r requirements.txt```
2. run example.py
```
from Txt2Img import Txt2Img
# beware of usage with large files, only tested on <1gb files

# initialize Txt2Img() object
t = Txt2Img()

# call txt2img to write data to pixel values. any file format works as input. compression level is optional, from min to max compression: 0 to 9
t.txt2img('bible.txt', 'bible.png', compression_level=9)
 
# call img2txt to read data from pixel values file (any format)
t.img2txt('bible.png', 'bible_return.txt')```
