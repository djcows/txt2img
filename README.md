# txt2img - A picture is worth a million words
> Inserts ASCII data into RGB pixel values, potentially achieving lossless compression ratio of ~1.5

- Reads ascii data from .txt file and writes it to .png file
- calculates smallest perfect square given num of bits in file
- To return back to ascii, use img2txt

Run example.py to reproduce baseline results:
1. ```pip install -r requirements.txt```
2. ```python3 example.py```

```
from img2txt import txt2img, img2txt

# ascii -> rgb
txt2img('data_in.txt', 'data_out.png')

# rgb -> ascii
img2txt('data_out.png', 'data_in.txt')
```
