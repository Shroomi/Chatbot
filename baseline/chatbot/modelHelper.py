#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 18:26:31 2019

@author: mengruding
"""

import tensorflow as tf

def get_initializer(init_op, seed = None, init_weight = None):
    # Create an initializer. init_weight is only for uniform.
    if init_op == 'uniform':
        