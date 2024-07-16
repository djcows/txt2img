from txt2img import txt2img, img2txt

# ascii -> rgb
txt2img('data_in.txt', 'data_out.png')

# rgb -> ascii
img2txt('data_out.png', 'data_back_in.txt')
