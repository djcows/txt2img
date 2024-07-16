# txt2img - A picture is worth a million words
Embeds decimals of ascii in RGB values of pixels for lossless data compression

Example:
James King Bible stored in a 1202x1202 image file, reducing disk size from 4.3mb to 3.1mb.

![bible_out](https://github.com/user-attachments/assets/18906f9d-1570-4b77-8696-3dffa8c7536a)

## Usage
1. ```pip install -r requirements.txt```
2. ```import txt2img```
3. ```txt2img.txt2img('data_in.txt', 'data_out.png')```
4. ```txt2img.img2txt('data_out.png', 'data_back_in.txt')```
