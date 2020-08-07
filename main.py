# Libs:
import os
from functions import * # import util functions
from tkinter import *

# paths
cwd = os.getcwd()
image_folder = '/images'
images_path = cwd + image_folder


# Initiate Tkinter window ++++++++++++++++++++++++++++++++++++++++++++++++++++++
root = Tk()
root.title("Image")
root.iconbitmap('@/home/polichinel/Documents/Tkinter/icons/zilla.xbm')


# Function to define and viz +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def defNviz(cwd, images_path, first_round_indicator = 0):

    """Executed when pressing 'next'. Switches the images, clears the boxes, saves both image index and atribute lists"""

    # so they go between 'next' clicks
    global indx_list
    global att_dict

    # When next is pressed (is round is not init) pickle images and choosen atributes
    if first_round_indicator == 0: # not when the program first initiates - only when pressing 'next'

        # index list
        pickle.dump(indx_list, open( "indx_list.pkl", "wb" ))

        # attributes
        att_dict['att0'].append((att0_img0.get(), att0_img1.get()))
        att_dict['att1'].append((att1_img0.get(), att1_img1.get()))
        att_dict['att2'].append((att2_img0.get(), att2_img1.get()))
        att_dict['att3'].append((att3_img0.get(), att3_img1.get()))
        att_dict['att4'].append((att4_img0.get(), att4_img1.get()))
        att_dict['att5'].append((att5_img0.get(), att5_img1.get()))

        # include the indx_list in the dict for ease and safty
        att_dict['indx'] = indx_list #overwrite the whole jazz each time

        pickle.dump(att_dict, open( "att_dict.pkl", "wb" ))

    # If it is the initiail round simply load the list and dict
    else:
        indx_list = getIndexList(cwd)
        att_dict = getAttDict(cwd, indx_list)

    # Window -------------------------------------------------------------------

    # vizualize the image count
    n_pairs_coded = Label(root, text = f'{len(indx_list)}/5000')
    n_pairs_coded.grid(row = 9, column = 1, pady = 5, padx = 20, columnspan = 2)

    # use util functions to get two new paths/images plus initiate or update lists and dict
    two_paths, indx_list = drawTwoPaths(cwd, images_path)

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


# Checkbuttons +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# att0
c00 = Checkbutton(root, text = "att 0", variable = att0_img0, onvalue = 1, offvalue = 0)
c00.deselect()
c00.grid(row = 3, column = 0, pady = 5)

c01 = Checkbutton(root, text = "att 0", variable = att0_img1, onvalue = 1, offvalue = 0)
c01.deselect()
c01.grid(row = 3, column = 1, pady = 5)

# att1
c10 = Checkbutton(root, text = "att 1", variable = att1_img0, onvalue = 1, offvalue = 0)
c10.deselect()
c10.grid(row = 4, column = 0, pady = 5)

c11 = Checkbutton(root, text = "att 1", variable = att1_img1, onvalue = 1, offvalue = 0)
c11.deselect()
c11.grid(row = 4, column = 1, pady = 5)


# att2
c20 = Checkbutton(root, text = "att 2", variable = att2_img0, onvalue = 1, offvalue = 0)
c20.deselect()
c20.grid(row = 5, column = 0, pady = 5)

c21 = Checkbutton(root, text = "att 2", variable = att2_img1, onvalue = 1, offvalue = 0)
c21.deselect()
c21.grid(row = 5, column = 1, pady = 5)


# att3
c30 = Checkbutton(root, text = "att 3", variable = att3_img0, onvalue = 1, offvalue = 0)
c30.deselect()
c30.grid(row = 6, column = 0, pady = 5)

c31 = Checkbutton(root, text = "att 3", variable = att3_img1, onvalue = 1, offvalue = 0)
c31.deselect()
c31.grid(row = 6, column = 1, pady = 5)


# att4
c40 = Checkbutton(root, text = "att 4", variable = att4_img0, onvalue = 1, offvalue = 0)
c40.deselect()
c40.grid(row = 7, column = 0, pady = 5)

c41 = Checkbutton(root, text = "att 4", variable = att4_img1, onvalue = 1, offvalue = 0)
c41.deselect()
c41.grid(row = 7, column = 1, pady = 5)


# att5
c50 = Checkbutton(root, text = "att 5", variable = att5_img0, onvalue = 1, offvalue = 0)
c50.deselect()
c50.grid(row = 8, column = 0, pady = 5)

c51 = Checkbutton(root, text = "att 5", variable = att5_img1, onvalue = 1, offvalue = 0)
c51.deselect()
c51.grid(row = 8, column = 1, pady = 5)

# end space for nice viz
end_space = Label(root, text = ' ')
end_space.grid(row = 9, column = 1, pady = 5, columnspan = 2)

# display first two images
defNviz(cwd, images_path, first_round_indicator = 1)

# Next Button ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

button_next = Button(root, text = 'Next Pair >>', command = lambda: defNviz(cwd,images_path))
button_next.grid(row = 2, column = 0, columnspan = 2)


# Program Loop +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
root.mainloop()
