import os
# from itertools import permutations
import numpy as np
import pickle
from tkinter import *
from PIL import ImageTk, Image

# utils ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def getIndexList(cwd):

    """Creates a list of used pairs"""

    # List to store used pairs: should be saved and loaded after first itereation
    if 'indx_list.pkl' in os.listdir(cwd):
        indx_list = pickle.load( open( "indx_list.pkl", "rb" ) )

    else:
        indx_list = []

    return(indx_list)


def getImagesPath(flat_dir_path):

    """Creates a list of all paths given a flatten dir"""

    path_list = []

    for root, dirs, files in os.walk(flat_dir_path):
        for name in files:
            path = os.path.join(root, name)
            path_list.append(path)

    return(path_list)


def drawTwoPaths(path_list, indx_list):

    """Get two random paths from path_list wich are not already in index_list.
    Then add to index_list and update it"""

    two_paths = tuple(np.random.choice(path_list, 2, replace= False))# indx of pairs

    while two_paths in indx_list:
        two_paths = tuple(np.random.choice(path_list, 2, replace= False))# insure new indx of pairs

    indx_list.append(two_paths) # update index_list

    return(two_paths, indx_list)


def getTwoImages(two_paths):

        """ Open two images given pair of paths"""

        # Load and resize the first pair of images
        img0 = Image.open(two_paths[0]).resize((800, 525), Image.ANTIALIAS)
        img1 = Image.open(two_paths[1]).resize((800, 525), Image.ANTIALIAS)

        # convert pair of image to Tkinter format
        imgTk0 = ImageTk.PhotoImage(img0)
        imgTk1 = ImageTk.PhotoImage(img1)

        return(imgTk0, imgTk1)


# define and viz +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def defNviz(cwd,images_path):

    # use util functions
    indx_list = getIndexList(cwd)
    path_list = getImagesPath(images_path)
    two_paths, indx_list = drawTwoPaths(path_list, indx_list)
    image0, image1 = getTwoImages(two_paths)

    # update pickeled index list
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
