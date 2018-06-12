#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:00:05 2017

@author: pqzhuang
"""

import os
from scipy.io import loadmat as sio
import numpy as np
import PIL.Image as Image


os.chdir('/home/king/Documents/deeplab_v2/exper/rgbd/features/deeplab_largeFOV/val/fc8')
path=os.getcwd()
files=os.listdir(path)
labels_path=os.path.join(path,'labels')


palette=[]
for i in range(256):
    palette.extend((i,i,i))
palette[:3*21]=np.array([[0, 0, 0],   # 0,0,0
                            [128, 0, 0],    # plane
                            [0, 128, 0],    # bicyle
                            [128, 128, 0],  # bird
                            [0, 0, 128],    # boat
                            [128, 0, 128],  # bottle
                            [0, 128, 128],  # bus
                            [128, 128, 128],# car
                            [64, 0, 0],     # cat
                            [192, 0, 0],    # chair
                            [64, 128, 0],   # cow
                            [192, 128, 0],  # table
                            [64, 0, 128],   # dog
                            [192, 0, 128],  # horse
                            [64, 128, 128], # motobike
                            [192, 128, 128],# person
                            [0, 64, 0],     # pottled-plant
                            [128, 64, 0],   # sheep
                            [0, 192, 0],    # sofa
                            [128, 192, 0],  # train
                            [0, 64, 128]],  # tv/monitor 
                            dtype='uint8').flatten()



for afile in files:
    file_path=os.path.join(path,afile)
    if os.path.isfile(file_path):
        if os.path.getsize(file_path)==0:
            continue
        mat_idx=afile[:afile.find('.mat')]
        mat_file=sio(file_path)
        mat_file=mat_file['data']
        labels=np.argmax(mat_file,axis=2).astype(np.uint8)
        label_img=Image.fromarray(labels.reshape(labels.shape[0],labels.shape[1]))
        label_img.putpalette(palette)
        label_img=label_img.transpose(Image.FLIP_LEFT_RIGHT)
        label_img = label_img.rotate(90)
        dst_path=os.path.join(labels_path,mat_idx+'.png')
        label_img.save(dst_path)
