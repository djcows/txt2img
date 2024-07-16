from txt2img import txt2img, img2txt
import time

# ascii -> rgb
txt2img('bible.txt', 'bible_image.png')

time.sleep(0.25)

# read bible image pixel data back to txt file
img2txt('bible_image.png', 'bible_return.txt')