# Libs:
import os
from functions import * # import util functions
from tkinter import *
# from variables import *
# getVars()

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

    # use util functions
    indx_list = getIndexList(cwd)
    path_list = getImagesPath(images_path)
    two_paths, indx_list = drawTwoPaths(path_list, indx_list)
    image0, image1 = getTwoImages(two_paths)
    att_dict = getAttDict(cwd)

    # update pickeled index list
    if first_round_indicator == 0: # not when the program first initiates - only when pressing 'next'
        pickle.dump(indx_list, open( "indx_list.pkl", "wb" ))

    # Rinse the grid if needed
    try:
        img0.grid_forget()
        img1.grid_forget()
    except:
        pass

    # define
    img0 = Label(image  = image0)
    img1 = Label(image = image1)

    # keep reference, becuase tkinter image thing
    img0.image = image0
    img1.image = image1

    # viz
    img0.grid(row=0, column = 0, columnspan = 1)
    img1.grid(row=0, column = 1, columnspan = 1)

    if first_round_indicator == 0: # not when the program first initiates - only when pressing 'next'
    # # save to lists, collect in dict and pickle
        att_dict['att0'].append((att0_img0.get(), att0_img1.get()))
        att_dict['att1'].append((att1_img0.get(), att1_img1.get()))
        att_dict['att2'].append((att2_img0.get(), att2_img1.get()))
        att_dict['att3'].append((att3_img0.get(), att3_img1.get()))
        att_dict['att4'].append((att4_img0.get(), att4_img1.get()))
        att_dict['att5'].append((att5_img0.get(), att5_img1.get()))

    #     att_dict = {'att0':att0_list,'att1':att1_list,'att2':att2_list,'att3':att3_list,'att4':att4_list,'att5':att5_list}
        pickle.dump(att_dict, open( "att_dict.pkl", "wb" ))

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

# Checkbuttons -----------------------------------------------------------------
#so in your indx_list you already have the pairs (tuple, ordered).
# so for each atribute you simple want a list of tuples [(0,1),..,(0,1)]
# with one denoting the image have "most" of said atrribute.
# most be saved when you press next, so it goes in the defNviz.
# prob its own nested function. And then pickle dump the


# vars
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
c00.grid(row = 2, column = 0, pady = 5)

c01 = Checkbutton(root, text = "att 0", variable = att0_img1, onvalue = 1, offvalue = 0)
c01.deselect()
c01.grid(row = 2, column = 1, pady = 5)

# att1
c10 = Checkbutton(root, text = "att 1", variable = att1_img0, onvalue = 1, offvalue = 0)
c10.deselect()
c10.grid(row = 3, column = 0, pady = 5)

c11 = Checkbutton(root, text = "att 1", variable = att1_img1, onvalue = 1, offvalue = 0)
c11.deselect()
c11.grid(row = 3, column = 1, pady = 5)


# att2
c20 = Checkbutton(root, text = "att 2", variable = att2_img0, onvalue = 1, offvalue = 0)
c20.deselect()
c20.grid(row = 4, column = 0, pady = 5)

c21 = Checkbutton(root, text = "att 2", variable = att2_img1, onvalue = 1, offvalue = 0)
c21.deselect()
c21.grid(row = 4, column = 1, pady = 5)


# att3
c30 = Checkbutton(root, text = "att 3", variable = att3_img0, onvalue = 1, offvalue = 0)
c30.deselect()
c30.grid(row = 5, column = 0, pady = 5)

c31 = Checkbutton(root, text = "att 3", variable = att3_img1, onvalue = 1, offvalue = 0)
c31.deselect()
c31.grid(row = 5, column = 1, pady = 5)


# att4
c40 = Checkbutton(root, text = "att 4", variable = att4_img0, onvalue = 1, offvalue = 0)
c40.deselect()
c40.grid(row = 6, column = 0, pady = 5)

c41 = Checkbutton(root, text = "att 4", variable = att4_img1, onvalue = 1, offvalue = 0)
c41.deselect()
c41.grid(row = 6, column = 1, pady = 5)


# att5
c50 = Checkbutton(root, text = "att 5", variable = att5_img0, onvalue = 1, offvalue = 0)
c50.deselect()
c50.grid(row = 7, column = 0, pady = 5)

c51 = Checkbutton(root, text = "att 5", variable = att5_img1, onvalue = 1, offvalue = 0)
c51.deselect()
c51.grid(row = 7, column = 1, pady = 5)

end_space = Label(root, text = ' ')
end_space.grid(row = 8, column = 1, pady = 5, columnspan = 2)

# display first two images
defNviz(cwd,images_path, first_round_indicator = 1)

# Buttons ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

button_next = Button(root, text = 'Next Pair >>', command = lambda: defNviz(cwd,images_path))
button_next.grid(row = 1, column = 0, columnspan = 2)


# Program Loop +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
root.mainloop()
