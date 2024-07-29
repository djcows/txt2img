from Txt2Img import Txt2Img
# beware of usage with large files, only tested on <1gb files

# initialize Txt2Img() object
t = Txt2Img()

# call txt2img to write data to pixel values. any file format works as input. compression level is optional, from min to max compression: 0 to 9
t.txt2img('bible.txt', 'bible.png', compression_level=9)
 
# call img2txt to read data from pixel values file (any format)
t.img2txt('bible.png', 'bible_original.txt')
