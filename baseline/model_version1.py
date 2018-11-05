#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:21:40 2018

@author: mengruding
"""

'''
    Knowledge to Learn:
        1, tf.test.gpu_device_name(): 
           Returns the name of a GPU device if available or the empty string.
        2, warnings.warn('string'): output self-defined warning information
           https://python3-cookbook.readthedocs.io/zh_CN/latest/c14/p11_issuing_warning_messages.html
        3, tf.contrib.lookup.index_table_from_file():
           Returns a lookup table that converts a string tensor into int64 IDs.
        4, tf.contrib.lookup.index_to_string_table_from_file():
           Returns a lookup table that maps a Tensor of indices into strings.
        5, tf.data.TextLineDataset():
           A Dataset comprising lines from one or more text files.
           Read the text from the file.
        6, map and lambda in Python:
           https://blog.csdn.net/u013944212/article/details/55095687
        7, 

'''

import tensorflow as tf
import warnings

#%%
# Check Tensorflow Version
print('TensorFlow Version: {}'.format(tf.__version__))

# Check for a GPU
if not tf.test.gpu_device_name(): 
    warnings.warn('No GPU found. Pleasse use a GPU to train your Neural Network.')
else:
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))

#%% Hyper-parameters settings
data_path = '../chatdata/reddit_data/'
source_path = data_path + 'train/train.from' # input sentences
target_path = data_path + 'train/train.to' # output sentences
batch_size = 256
num_units = 64
max_gradient_norm = 5.0
learning_rate = 0.001
epoch = 8

#%% Generate words
##########!!!!!!!!!! have not cleaned text !!!!!!!!!############
# Read the input sentences and generate unique words
# These words are wild, maybe with URLs, with Japanese words and etc.
print('generating encoder words and decoder words...')
words = []
with open(source_path, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        words += line.split()
f.close()
unique_words_src = ['eos'] + list(set(words))
print('\n')
print('# encoder words: {}\n # encoder unique words: {}'.format(len(words),len(unique_words_src)))

with open(data_path+'train/words_encoder', 'w', encoding='utf-8') as f:
    for word in unique_words_src:
        f.write(word + '\n')
f.close()

# Read the output sentences and generate unique words
# These words are wild, maybe with URLs, with Japanese words and etc.
words = []
with open(target_path, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        words += line.split()
f.close()
unique_words_tar = ['sos'] + ['eos'] + list(set(words))
print('# decoder words: {}\n # decoder unique words: {}'.format(len(words),len(unique_words_tar)))

with open(data_path+'train/words_decoder', 'w', encoding='utf-8') as f:
    for word in unique_words_tar:
        f.write(word + '\n')
f.close()

#%% Build lookup table
# lookup_encoder: words ---> id
# lookup_decoder: words ---> id
# lookup_chat: id ---> words
lookup_encoder = tf.contrib.lookup.index_table_from_file(data_path+'train/words_encoder')
lookup_decoder = tf.contrib.lookup.index_table_from_file(data_path+'train/words_decoder')
lookup_chat = tf.contrib.lookup.index_to_string_table_from_file(data_path+'train/words_decoder')

src_eos_id = lookup_encoder.lookup(tf.constant('eos')) # 0 in source vocab
tar_sos_id = lookup_decoder.lookup(tf.constant('sos')) # 0 in target vocab
tar_eos_id = lookup_decoder.lookup(tf.constant('eos')) # 1 in target vocab

#%% Data preprocessing for Tensorflow model
# source(encoder) dataset: change text into word ids
source_dataset = tf.data.TextLineDataset(source_path)
source_dataset = source_dataset.map(lambda string: tf.string_split([string]).values) # without input arguments
source_dataset = source_dataset.map(lambda words: (words, tf.size(words)))# without input arguments
source_dataset = source_dataset.map(lambda words, size: (lookup_encoder.lookup(words), size))# without input arguments
# target(decoder) dataset: change text into word ids and add 'sos'
target_dataset = tf.data.TextLineDataset(target_path)
target_dataset = target_dataset.map(lambda string: tf.string_split([tf.string_join([tf.constant('sos'), string], separator=' ')]).values)
target_dataset = target_dataset.map(lambda words: (words, tf.size(words)))
target_dataset = target_dataset.map(lambda words, size: (lookup_decoder.lookup(words), size))
# padding and batch
