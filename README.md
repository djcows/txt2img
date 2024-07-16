# txt2img - A picture is worth a million words

> stores ascii data in pixel color values, achieving lossless compression ratio of up to ~1.5


Basic usage
```
from img2txt import txt2img, img2txt

# ascii -> rgb
txt2img('data_in.txt', 'data_out.png')

# rgb -> ascii
img2txt('data_out.png', 'data_in.txt')
```
