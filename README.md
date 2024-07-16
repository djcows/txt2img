# txt2img - A picture is worth a million words
> insert ascii data into RGB pixel values to achieve lossless compression ratio of up to ~1.5

James King Bible as 1202x1202 image file - 4.3mb(txt) -> 3.1mb(png):
![bible_out](https://github.com/user-attachments/assets/18906f9d-1570-4b77-8696-3dffa8c7536a)

- Reads ascii data from .txt file and writes it to .png file
- calculates smallest perfect square given num of bits in file
- To return back to ascii, use img2txt

Run example.py to reproduce baseline results:
1. ```pip install -r requirements.txt```
2. ```python3 example.py```

```
from txt2img import txt2img, img2txt
import time

# ascii -> rgb
txt2img('bible.txt', 'bible_output_image.png')

# for read/write safety
time.sleep(2)

# read bible image pixel data back to txt file
img2txt('bible_output_image.png', 'bible_output_text.txt')
```
