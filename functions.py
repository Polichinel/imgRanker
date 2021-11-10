import os
# from itertools import permutations
import numpy as np
import pickle
from tkinter import *
from PIL import ImageTk, Image

# utils ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def getIndexList(cwd):

    """Creates or load a list of used pairs"""

    # List to store used pairs: should be saved and loaded after first itereation
    if 'indx_list.pkl' in os.listdir(cwd):
        indx_list = pickle.load( open( "indx_list.pkl", "rb" ) )

    else:
        indx_list = []

    return(indx_list)


def getImagesPath(images_path):

    """Creates a list of all paths given a flatten dir"""

    path_list = []

    for root, dirs, files in os.walk(images_path):
        for name in files:
            path = os.path.join(root, name)
            path_list.append(path)

    return(path_list)


def drawTwoPaths(cwd, images_path):

    """Get two random paths from path_list wich are not already in index_list.
    Then add to index_list and update it"""

    # util functions:
    indx_list = getIndexList(cwd)
    path_list = getImagesPath(images_path)

    # for empty indx_list
    if len(indx_list) == 0:
        # get two now paths paths
        two_paths = tuple(np.random.choice(path_list, 2, replace= False))# indx of pairs

    else: 
        img1 = np.random.choice(np.array(indx_list).reshape(-1), 1 , replace= False).item() # one image already in the image list.
        img2 = np.random.choice(path_list, 1, replace= False).item() # one potentially new image

        # the images should not be the same
        while img1 == img2:
            img2 = np.random.choice(path_list, 1, replace= False).item() # one potentially new image

        two_paths = tuple([img1,img2])

    # if the pair have already been compared, draw a new pair
    while two_paths in indx_list:
        rand_int = np.random.randint(0,2)
        img1 = np.random.choice(np.array(indx_list).reshape(-1), 1 , replace= False).item() # one image already in the image list.
        img2 = np.random.choice(path_list, 1, replace= False).item() # one potentially new image
        two_paths = tuple([img1,img2])

    indx_list.append(two_paths) # update index_list

    # return the two_paths and a updated indx_list
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


# ------------------------------------------------------------------------------


def getAttDict(cwd, indx_list):

    """Get the dict of att_lists or create them"""

    # List to store used pairs: should be saved and loaded after first itereation
    if 'att_dict.pkl' in os.listdir(cwd):
        att_dict = pickle.load( open( "att_dict.pkl", "rb" ) )

    else:

        att0_list = []
        att1_list = []
        att2_list = []
        att3_list = []
        att4_list = []
        att5_list = []
        att6_list = []
        att7_list = []
        att8_list = []
        att9_list = []

        att_dict = {'att0':att0_list,'att1':att1_list,'att2':att2_list,
                    'att3':att3_list,'att4':att4_list,'att5':att5_list,
                    'att6':att6_list,'att7':att7_list,'att8':att8_list, 
                    'att9':att9_list,'indx' : indx_list}

    return(att_dict)
