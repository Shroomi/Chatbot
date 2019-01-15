#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 18:44:05 2019

@author: mengruding
"""

import os
import sys

AUG0_FOLDER = "Augment0"

VOCAB_FILE = "vocab.txt"
REDDIT_DATA_FILE = "reddit_cleaned_part.txt"
EXCLUDED_FILE = "excluded.txt"

def generate_vocab_file(corpus_dir):
    """
    Generate the vocab.txt file for the training and prediction/inference.
    Manually remove the empty bottom line in the generated file.
    """
    vocab_list = []
    
    # Special tokens, with IDs: 0, 1, 2
    for t in ['_unk_', '_bos_', '_eos_']:
        vocab_list.append(t)
        
    # The word following this punctuation should be capitalized in the prediction output.
    for t in ['.', '!', '?']:
        vocab_list.append(t)
        
    # The word following this punctuation should not precede with a space in the prediction output.
    for t in ['(', '[', '{', '``', '$']:
        vocab_list.append(t)
    
    temp_dict = {}    
    reddit_file = os.path.join(corpus_dir, AUG0_FOLDER, REDDIT_DATA_FILE)
    if os.path.exists(reddit_file):
        with open(reddit_file, 'r') as f_reddit:
            line_cnt = 0
            for line in f_reddit:
                line_cnt += 1
                if line_cnt % 200000 == 0:
                    print('{:,} lines of reddit data file scanned.'.format(line_cnt))
                ln = line.strip()
                if not ln:
                    continue
                if ln.startswith("Q:") or ln.startswith("A:"):
                    tokens = ln[2:].strip().split(' ')
                    for token in tokens:
                        if len(token) and token != ' ':
                            t = token.lower()
                            if t not in vocab_list:
                                if ln.startswith("A:"): # keep all for responses
                                    vocab_list.append(t)
                                else:
                                    if t not in temp_dict:
                                        temp_dict[t] = 1
                                    else:
                                        temp_dict[t] += 1
                                        if temp_dict[t] >=2:
                                            if t.startswith('.') or t.startswith('-') \
                                                or t.endswith('..') or t.endswith('-'):
                                                continue
                                            vocab_list.append(t)
                                            
    with open(VOCAB_FILE, 'a') as f_voc:
        for v in vocab_list:
            f_voc.write('{}\n'.format(v))
            
    print('The final vocab file generated. Vocab size: {}'.format(len(vocab_list)))
    
    with open(EXCLUDED_FILE, 'a') as f_excluded:
        for k, _ in temp_dict.items():
            if k not in vocab_list:
                f_excluded.write('{}\n'.format(k))
    
                                    

if __name__ == "__main__":
    sys.path.append(r'/Users/mengruding/Documents/Study/Chatbot/baseline')
    from settings import PROJECT_ROOT
    
    corp_dir = os.path.join(PROJECT_ROOT, 'Data', 'Corpus')
    generate_vocab_file(corp_dir)
    