#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:21:40 2018

@author: mengruding
"""

'''
    Knowledge:
        1, tf.test.gpu_device_name(): 
           Returns the name of a GPU device if available or the empty string.
        2, warnings.warn('string'): output self-defined warning information
           https://python3-cookbook.readthedocs.io/zh_CN/latest/c14/p11_issuing_warning_messages.html
        3, 
'''

import tensorflow as tf
import warnings

# Check Tensorflow Version
print('TensorFlow Version: {}'.format(tf.__version__))

# Check for a GPU
if not tf.test.gpu_device_name(): 
    warnings.warn('No GPU found. Pleasse use a GPU to train your Neural Network.')
else:
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
    
# Hyper-parameters settings
data_path = '../chatdata/reddit_data/'
source_path = data_path + 'train/train.from'
target_path = data_path + 'train/train.to'
batch_size = 256
num_units = 64
max_gradient_norm = 5.0
learning_rate = 0.001
epoch = 8

