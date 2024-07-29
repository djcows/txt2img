# txt2img - store files inside PNG pixels
1. Binary data of input file is read into memory
2. Data is compressed using LZMA
3. Compressed data is inserted into a numpy array
4. Numpy array is saved as a .png image using pillow

This process is completely lossless and reversible using img2txt.
##

#### How-To
Install required modules (currently numpy and pillow) ```pip install -r requirements.txt```
```
from Txt2Img import Txt2Img
pixels = Txt2Img()
pixels.txt2img('bible.txt', 'bible.png', compression_level=9)
pixels.img2txt('bible.png', 'bible_return.txt')
```
txt2img has optional parameter compression_level to select values in domain [0,9].


##
Data with many repeating patterns will naturally have a higher compression ratio as run-length encoding and dictionary encoding.
- bible.txt (4.3MB) -> bible.png (1.0MB)

![bible_small](https://github.com/user-attachments/assets/9d47be7d-2c6d-4dd8-89c8-c90871dcd5fd)

##

Data such as MP3 have a much lower compression ratio because they are already compressed, but songs can nonetheless be stored as pixels and converted back to MP3 as desired.
- Daft Punk - Harder, Better, Faster, Stronger.mp3  (3.6MB) -> Daft Punk - Harder, Better, Faster, Stronger.png (3.5 MB)
![Daft Punk - Harder, Better, Faster, Stronger](https://github.com/user-attachments/assets/65eb60fd-ea63-4f66-8868-c368fbdb0902)

## 

This is part of a passion project of mine to create new wireless data transfer method. I order to merge with AI successfully, we should make wireless transfer much, much faster.
