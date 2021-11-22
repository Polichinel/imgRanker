import os
# from itertools import permutations
import numpy as np
import pickle
from tkinter import *
from PIL import ImageTk, Image

# utils ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def getPregenIndexList(cwd):

    """Load a list of pairs to use"""

    # List to store used pairs: should be saved and loaded after first itereation
    if 'pregenerated_indx_list.pkl' in os.listdir(cwd):
        pregen_indx_list = pickle.load(open( "pregenerated_indx_list.pkl", "rb" ) )
        return(pregen_indx_list)

    else:
        print('No pregenerated_indx_list.pkl in folder. Run gen_preGen_pairlist.ipynb.') 
        return(None)

def getImagesNames(images_path):

    """Creates a list of all image names given a flatten dir. Used in gen_preGen_pairList.ipynd, not main.py."""

    name_list = []

    for root, dirs, files in os.walk(images_path):
        for name in files:
            name_list.append(name)

    return(name_list)

def getTwoImages(two_paths):

        """ Open two images given pair of paths"""

        # Load and resize the first pair of images
        img0 = Image.open(two_paths[0]).resize((800, 525), Image.ANTIALIAS)
        img1 = Image.open(two_paths[1]).resize((800, 525), Image.ANTIALIAS)

        # convert pair of image to Tkinter format
        imgTk0 = ImageTk.PhotoImage(img0)
        imgTk1 = ImageTk.PhotoImage(img1)

        return(imgTk0, imgTk1)


def getAttDict(cwd):

    """Get the dict of att_lists or create them"""

    # List to store used pairs: should be saved and loaded after first itereation
    if 'att_dict.pkl' in os.listdir(cwd):
        att_dict = pickle.load( open( "att_dict.pkl", "rb" ) )

    # If it is not there, it is the first round OVERALL, we create the dict.
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
                    'att9':att9_list,'indx_indicator' : 0}

    return(att_dict)
