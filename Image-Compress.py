import os
import sys
import shutil

from PIL import Image
import numpy as np

#Directory path from which image has to be taken
from_path = "/Users/leenathomas/Documents/Clinic-Site/clinic-site/src/images/"

#Directory path to which image has to be saved
to_path = "/Users/leenathomas/Documents/compressed-images/"

#function to compress the image
def compress_image(from_path,to_path,each_image):
    #To remove all hidden files
    if not each_image.startswith('.'):
        size=os.path.getsize(f'{from_path}{each_image}')
        image_name_no_extension =  os.path.splitext('each_image')[0]

        #if size greater than 14KB
        if size > 140000:
            edit_image = Image.open(f'{from_path}{each_image}')
            image_convert = edit_image.convert('RGB')
            #if size between 14KB to 17KB
            if size > 140000 and size < 170000:
                image_convert.save(f'{to_path}'+each_image,optimize=True,quality=80)

            #if size between 17KB to 25KB
            elif size > 170000 and size < 250000:
                image_convert.save(f'{to_path}'+each_image,optimize=True,quality=70)

            #if size between 25KB to 1MB
            elif size > 250000 and size < 1000000:
                image_convert.save(f'{to_path}'+each_image,optimize=True,quality=60)

            #if size between greater than 1MB
            elif size > 1000000 :
                image_convert.save(f'{to_path}'+each_image,optimize=True,quality=10)

        #if size less than 14KB
        else:
            shutil.copy(f'{from_path}{each_image}',to_path)

def call_for_each_image(from_path,to_path):
    if not os.path.exists(to_path):
        os.makedirs(to_path)
    for each_image in os.listdir(from_path):
        #if an image file
        if not os.path.isdir(f'{from_path}{each_image}'):
            compress_image(from_path,to_path,each_image)
        #If a subfolder
        elif os.path.isdir(f'{from_path}{each_image}'):
            call_for_each_image(f'{from_path}{each_image}{"/"}',f'{to_path}{each_image}{"/"}')

#main function
call_for_each_image(from_path,to_path)
