#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 15:43:17 2019

@author: mengruding
"""

import sys
import nltk
import os

COMMENT_LINE_STT = "#=="
CONVERSATION_SEP = "==="

def corpus_pre_process(file_dir):
    '''
    Preprocess the training data so that it can be handled by tensorflow TextLineDataSet
    '''
    for data_file in sorted(os.listdir(file_dir)):
        full_path_name = os.path.join(file_dir, data_file)
        if os.path.isfile(full_path_name) and data_file.lower().endswith('.txt'):
            new_name = data_file.lower().replace('.txt', '_new.txt')
            full_new_name = os.path.join(file_dir, new_name)
            
            conversations = []
            with open(full_path_name, 'r') as f:
                samples = []
                for line in f:
                    l = line.strip()
                    if not l or l.startswith(COMMENT_LINE_STT):
                        continue
                    if l == CONVERSATION_SEP:
                        if len(samples):
                            conversations.append(samples)
                        samples = []
                    else:
                        samples.append({"text": l})
            
            with open(full_new_name, 'a') as f_out:
                i = 0
                for conversation in conversations:
                    step = 2
                    for i in range(0, len(conversation) - 1, step):
                        source_tokens = nltk.word_tokenize(conversation[i]['text'])
                        target_tokens = nltk.word_tokenize(conversation[i+1]['text'])
                        
                        source_line = "Q: " + ' '.join(source_tokens[:]).strip()
                        target_line = "A: " + ' '.join(target_tokens[:]).strip()
                    
                        f_out.write('{}\n'.format(source_line))
                        f_out.write('{}\n'.format(target_line))
                        
                    f_out.write('===\n')
                    

if __name__ == "__main__":
    sys.path.append(r'/Users/mengruding/Documents/Study/Chatbot/baseline')
    from settings import PROJECT_ROOT
    
    file_dir = os.path.join(PROJECT_ROOT, 'Data', 'Corpus', 'temp')
    corpus_pre_process(file_dir)