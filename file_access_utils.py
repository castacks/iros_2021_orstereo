# coding=utf-8

# Author: Yaoyu Hu <yaoyuh@andrew.cmu.edu>
# Date: 2021-03-13

import cv2
import numpy as np
import os

def read_lu1_disparity(fn):
    '''Read the disparity file with a suffix _lu1 in the file name.
    Arguments:
    fn (string): The file name with full path.

    Returns:
    A single-channel disparity with dtype == np.float32.
    '''
    assert( os.path.isfile(fn) ), \
        f'{fn} does not exist. '
    
    # Read the raw data from a 4-channel PNG file.
    d = cv2.imread(fn, cv2.IMREAD_UNCHANGED)
    assert(d.dtype == np.uint8)
    assert(d.shape[2] == 4), \
        f'{fn} has a shape of {d.shape}, not suitable for disparity/depth conversion. '

    # Conver the data to float32.
    d = d.view('<f4')

    # Squeeze the redundant dimension.
    d = np.squeeze(d, axis=-1)

    return d

def read_occlusion(fn):
    '''Read an occlusion file.
    Arguments:
    fn (string): The input filename with full path.

    Returns:
    A single-channel boolean image. True pixels are occlusions.
    '''
    assert( os.path.isfile(fn) ), \
        f'{fn} does not exist. '

    # Read the raw image.
    m = cv2.imread(fn, cv2.IMREAD_UNCHANGED)

    # The pixels with a value other than 255
    # are considered as occlusion (including 
    # out-of-view).
    return m != 255