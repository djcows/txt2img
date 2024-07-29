# txt2img - lossless data compression using pixels
Embeds binary data to pixel values of images

Example:
king_james_bible.txt (4.3mb) ---> king_james_bible.png (1.0mb)
![bible_small](https://github.com/user-attachments/assets/9d47be7d-2c6d-4dd8-89c8-c90871dcd5fd)

## Usage
1. install requirements: ```pip install -r requirements.txt```
2. import package: ```from Txt2Img import txt2img```
3. initialize object: ```t = Txt2Img()```
4. write data to pixel values: ```t.txt2img('data_in.txt', 'data_out.png', compression_level=9) # compression_level optional, min 0, max 9```
5. read data from pixel values: ```txt2img.img2txt('data_out.png', 'data_back_in.txt')```
