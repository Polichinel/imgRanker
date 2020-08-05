# Libs:
import os
from functions import *
from tkinter import *


# paths
cwd = os.getcwd()
image_folder = '/images'
images_path = cwd + image_folder


# Initiate Tkinter window ++++++++++++++++++++++++++++++++++++++++++++++++++++++
root = Tk()
root.title("Image")
root.iconbitmap('@/home/polichinel/Documents/Tkinter/icons/zilla.xbm')

# display first two images
defNviz(cwd,images_path)

# Buttons ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

button_next = Button(root, text = 'Next Pair >>', command = lambda: defNviz(cwd,images_path))
button_next.grid(row = 1, column = 0, columnspan = 2)

# Checkbuttons -----------------------------------------------------------------

#so in your indx_list you already have the pairs (tuple, ordered).
# so for each atribute you simple want a list of tuples [(0,1),..,(0,1)]
# with one denoting the image have "most" of said atrribute.
# most be saved when you press next, so it goes in the defNviz.
# prob its own nested function. And then pickle dump the



# Program Loop +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
root.mainloop()
