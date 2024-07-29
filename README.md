# txt2img - lossless data compression using pixels
Embeds binary data to pixel values of images

Example:
bible.txt (4.3mb) ---> bible.png (1.0mb)

![bible_out](https://github.com/user-attachments/assets/18906f9d-1570-4b77-8696-3dffa8c7536a)

## Usage
1. install requirements: ```pip install -r requirements.txt```
2. import package: ```from Txt2Img import txt2img```
3. initialize object: ```t = Txt2Img()```
4. write data to pixel values: ```t.txt2img('data_in.txt', 'data_out.png', compression_level=9) # compression_level optional, min 0, max 9```
5. read data from pixel values: ```txt2img.img2txt('data_out.png', 'data_back_in.txt')```