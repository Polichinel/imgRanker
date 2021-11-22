# Libs:
import os
from functions import * # import util functions
from tkinter import *
import numpy as np

# paths
cwd = os.getcwd()
image_folder = '/images'
images_path = cwd + image_folder

# Initiate Tkinter window ++++++++++++++++++++++++++++++++++++++++++++++++++++++
root = Tk()
root.title("Image")

# Function to define and viz +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def defNviz(cwd, images_path, first_round_indicator = 0): 

    """Executed when pressing 'next'. Switches the images, clears the boxes, saves both image index and atribute lists"""

 # Now you need to infere where you where via the attribute dict. still important that you go through the network in order.
    
    # so they go between 'next' clicks
    global att_dict

    # Allways load the pregenerated indexlist
    pregen_indx_list = getPregenIndexList(cwd)

    # When next is pressed (is round is not after startup) pickle images and choosen atributes
    if first_round_indicator == 0: # not when the program first startup - only when pressing 'next'

        # attributes
        att_dict['att0'].append((att0_img0.get(), att0_img1.get()))
        att_dict['att1'].append((att1_img0.get(), att1_img1.get()))
        att_dict['att2'].append((att2_img0.get(), att2_img1.get()))
        att_dict['att3'].append((att3_img0.get(), att3_img1.get()))
        att_dict['att4'].append((att4_img0.get(), att4_img1.get()))
        att_dict['att5'].append((att5_img0.get(), att5_img1.get()))
        att_dict['att6'].append((att6_img0.get(), att6_img1.get()))
        att_dict['att7'].append((att7_img0.get(), att7_img1.get()))
        att_dict['att8'].append((att8_img0.get(), att8_img1.get()))
        att_dict['att9'].append((att9_img0.get(), att9_img1.get()))

        # Next round
        att_dict['indx_indicator'] += 1 # we move up on round.

        # Save the att_dict as a pickle
        pickle.dump(att_dict, open( "att_dict.pkl", "wb" ))

    # If it is the first round after startup round simply load the list and dict
    else:
        att_dict = getAttDict(cwd)

    # Window -------------------------------------------------------------------

    # vizualize the image count
    pair_number = att_dict['indx_indicator'] # Which pair are we at. also important below.
    pair_total = len(pregen_indx_list)
    n_pairs_coded = Label(root, text = f'{pair_number}/{pair_total}') # CHANGE
    # placement of image count
    n_pairs_coded.grid(row = 13, column = 1, pady = 5, padx = 20, columnspan = 2)
    
    # get two paths from the pregenerated list - in order.
    two_names = pregen_indx_list[pair_number]
    two_paths = (os.path.join(images_path, two_names[0]), os.path.join(images_path, two_names[1]))

    # get the two new images
    image0, image1 = getTwoImages(two_paths)

    # Rinse the grid if needed
    try:
        img0.grid_forget()
        img1.grid_forget()
    except:
        pass

    # define the elements
    img0 = Label(image  = image0)
    img1 = Label(image = image1)

    # keep reference, becuase tkinter image thing
    img0.image = image0
    img1.image = image1

    # visualize the difened images and their paths
    img0.grid(row=0, column = 0, columnspan = 1)
    img1.grid(row=0, column = 1, columnspan = 1)

    img0_label = Label(root, text = f'{two_paths[0]}')
    img0_label.grid(row = 1, column = 0, pady = 5)

    img1_label = Label(root, text = f'{two_paths[1]}')
    img1_label.grid(row = 1, column = 1, pady = 5)

    # Rinse checkboxes
    c00.deselect()
    c01.deselect()
    c10.deselect()
    c11.deselect()
    c20.deselect()
    c21.deselect()
    c30.deselect()
    c31.deselect()
    c40.deselect()
    c41.deselect()
    c50.deselect()
    c51.deselect()
    c60.deselect()
    c61.deselect()
    c70.deselect()
    c71.deselect()
    c80.deselect()
    c81.deselect()
    c90.deselect()
    c91.deselect()


# tkinter vars  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
att0_img0 = IntVar()
att0_img1 = IntVar()

att1_img0 = IntVar()
att1_img1 = IntVar()

att2_img0 = IntVar()
att2_img1 = IntVar()

att3_img0 = IntVar()
att3_img1 = IntVar()

att4_img0 = IntVar()
att4_img1 = IntVar()

att5_img0 = IntVar()
att5_img1 = IntVar()

att6_img0 = IntVar()
att6_img1 = IntVar()

att7_img0 = IntVar()
att7_img1 = IntVar()

att8_img0 = IntVar()
att8_img1 = IntVar()

att9_img0 = IntVar()
att9_img1 = IntVar()


# Checkbuttons +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# att0
c00 = Checkbutton(root, text = "negative emotions t1", variable = att0_img0, onvalue = 1, offvalue = 0)
c00.deselect()
c00.grid(row = 3, column = 0, pady = 5)

c01 = Checkbutton(root, text = "negative emotions t1", variable = att0_img1, onvalue = 1, offvalue = 0)
c01.deselect()
c01.grid(row = 3, column = 1, pady = 5)

# att1
c10 = Checkbutton(root, text = "negative emotions t2", variable = att1_img0, onvalue = 1, offvalue = 0)
c10.deselect()
c10.grid(row = 4, column = 0, pady = 5)

c11 = Checkbutton(root, text = "negative emotions t2", variable = att1_img1, onvalue = 1, offvalue = 0)
c11.deselect()
c11.grid(row = 4, column = 1, pady = 5)


# att2
c20 = Checkbutton(root, text = "mass protest", variable = att2_img0, onvalue = 1, offvalue = 0)
c20.deselect()
c20.grid(row = 5, column = 0, pady = 5)

c21 = Checkbutton(root, text = "mass protest", variable = att2_img1, onvalue = 1, offvalue = 0)
c21.deselect()
c21.grid(row = 5, column = 1, pady = 5)


# att3
c30 = Checkbutton(root, text = "damaged property/infra.", variable = att3_img0, onvalue = 1, offvalue = 0)
c30.deselect()
c30.grid(row = 6, column = 0, pady = 5)

c31 = Checkbutton(root, text = "damaged property/infra.", variable = att3_img1, onvalue = 1, offvalue = 0)
c31.deselect()
c31.grid(row = 6, column = 1, pady = 5)


# att4
c40 = Checkbutton(root, text = "privatly/homely", variable = att4_img0, onvalue = 1, offvalue = 0)
c40.deselect()
c40.grid(row = 7, column = 0, pady = 5)

c41 = Checkbutton(root, text = "privatly/homely", variable = att4_img1, onvalue = 1, offvalue = 0)
c41.deselect()
c41.grid(row = 7, column = 1, pady = 5)


# att5
c50 = Checkbutton(root, text = "public", variable = att5_img0, onvalue = 1, offvalue = 0)
c50.deselect()
c50.grid(row = 8, column = 0, pady = 5)

c51 = Checkbutton(root, text = "public", variable = att5_img1, onvalue = 1, offvalue = 0)
c51.deselect()
c51.grid(row = 8, column = 1, pady = 5)

# att 6
c60 = Checkbutton(root, text = "militarized", variable = att6_img0, onvalue = 1, offvalue = 0)
c60.deselect()
c60.grid(row = 9, column = 0, pady = 5)

c61 = Checkbutton(root, text = "militarized", variable = att6_img1, onvalue = 1, offvalue = 0)
c61.deselect()
c61.grid(row = 9, column = 1, pady = 5)

# att 7
c70 = Checkbutton(root, text = "rural", variable = att7_img0, onvalue = 1, offvalue = 0)
c70.deselect()
c70.grid(row = 10, column = 0, pady = 5)

c71 = Checkbutton(root, text = "rural", variable = att7_img1, onvalue = 1, offvalue = 0)
c71.deselect()
c71.grid(row = 10, column = 1, pady = 5)

# att 8
c80 = Checkbutton(root, text = "urban", variable = att8_img0, onvalue = 1, offvalue = 0)
c80.deselect()
c80.grid(row = 11, column = 0, pady = 5)

c81 = Checkbutton(root, text = "urban", variable = att8_img1, onvalue = 1, offvalue = 0)
c81.deselect()
c81.grid(row = 11, column = 1, pady = 5)

# att 9
c90 = Checkbutton(root, text = "staged/formal", variable = att9_img0, onvalue = 1, offvalue = 0)
c90.deselect()
c90.grid(row = 12, column = 0, pady = 5)

c91 = Checkbutton(root, text = "staged/formal", variable = att9_img1, onvalue = 1, offvalue = 0)
c91.deselect()
c91.grid(row = 12, column = 1, pady = 5)


# end space for nice viz
end_space = Label(root, text = ' ')
end_space.grid(row = 13, column = 1, pady = 5, columnspan = 2)

# display first two images
defNviz(cwd, images_path, first_round_indicator = 1)


# Next Button ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

button_next = Button(root, text = 'Next Pair >>', command = lambda: defNviz(cwd,images_path))
button_next.grid(row = 2, column = 0, columnspan = 2)


# Program Loop +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
root.mainloop()
