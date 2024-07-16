# txt2img - A picture is worth a million words
Embeds decimals of text in RGB values of pixels to create data compression with images

Example:
James King Bible as 1202x1202 image file - 4.3mb(txt) -> 3.1mb(png):
![bible_out](https://github.com/user-attachments/assets/18906f9d-1570-4b77-8696-3dffa8c7536a)


Install requirements: pip install -r requirements.txt

## Usage
```
from txt2img import txt2img, img2txt
# insert text data into png image pixels 
txt2img('bible.txt', 'bible_output_image.png')

# extract text data from png image pixels
img2txt('bible_output_image.png', 'bible_output_text.txt')
```
