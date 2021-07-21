"""

 CV_IO_utils.py  (author: Anson Wong / git: ankonzoid)

"""
import os
import skimage.io
from multiprocessing import Pool
import numpy as np

# Read image
def read_img(filePath):
    return skimage.io.imread(filePath, as_gray=False)

# Read images with common extensions from a directory
def read_imgs_dir(dirPath, extensions, parallel=True):
    args = [os.path.join(dirPath, filename)
            for filename in os.listdir(dirPath)
            if any(filename.lower().endswith(ext) for ext in extensions)]
    if parallel:
        pool = Pool()
        imgs = pool.map(read_img, args)
        pool.close()
        pool.join()
    else:
        imgs = [read_img(arg) for arg in args]
    return imgs

# Save image to file
def save_img(filePath, img):
    skimage.io.imsave(filePath, img)

def read_imgs_list(detected_images):
    
    images = [np.asarray(img) for img in detected_images] # img : image pillow type
    return images

def read_one_image(selected_image):
    return [np.asarray(selected_image)]
    