#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:36:14 2019

@author: mengruding

This file was used to split the questions and answers in two different files.
And generate train, eval and test data. They will be used for Opennmt tools(Transformer).
"""
import sys
import os

AUG0_FOLDER = "Augment0"
REDDIT_DATA_FILE = "reddit_cleaned_part.txt"
SOURCE_FILE = "src.txt"
TARGET_FILE = "tgt.txt"

def split_file(corp_dir):
    questions = []
    answers = []
    
    reddit_file = os.path.join(corp_dir, AUG0_FOLDER, REDDIT_DATA_FILE)
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
                if ln.startswith('Q:'):
                    questions.append(ln[2:].strip())
                if ln.startswith('A:'):
                    answers.append(ln[2:].strip())
    
    src_file = os.path.join(corp_dir, AUG0_FOLDER, SOURCE_FILE)
    tgt_file = os.path.join(corp_dir, AUG0_FOLDER, TARGET_FILE)
    
    with open(src_file, 'w') as f_src:
        for q in questions:
            f_src.write('{}\n'.format(q))
    
    with open(tgt_file, 'w') as f_tgt:
        for a in answers:
            f_tgt.write('{}\n'.format(a))
            
def write_file(file, content):
    with open(file, 'w') as f:
        for c in content:
            f.write('{}\n'.format(c))
            
def train_eval_test(origin_file, train_per=0.64, eval_per=0.19, flag='src'):
    train = []
    val = []
    test = []
    
    file = open(origin_file, 'r')
    lines_cnt = len(file.readlines())
    file.close()
    
    with open(origin_file, 'r') as f_origin:
        train_end_line = int(lines_cnt * train_per)
        eval_end_line = train_end_line + int(lines_cnt * eval_per)
        
        line_cnt = 0
        for line in f_origin:
            ln = line.strip()
            if not ln:
                continue
            if line_cnt <= train_end_line:
                train.append(ln)
            if line_cnt > train_end_line and line_cnt <= eval_end_line:
                val.append(ln)
            if line_cnt > eval_end_line:
                test.append(ln)
            line_cnt += 1

    augment_dir = origin_file[0:-7]
    train_file = os.path.join(augment_dir, flag+'-train.txt')
    val_file = os.path.join(augment_dir, flag+'-val.txt')
    test_file = os.path.join(augment_dir, flag+'-test.txt')
    write_file(train_file, train)
    write_file(val_file, val)
    write_file(test_file, test)

if __name__ == '__main__':
    sys.path.append(r'/Users/mengruding/Documents/Study/Chatbot/baseline')
    from settings import PROJECT_ROOT
    
    corp_dir = os.path.join(PROJECT_ROOT, 'Data', 'Corpus')
    src_file = os.path.join(corp_dir, AUG0_FOLDER, SOURCE_FILE)
    tgt_file = os.path.join(corp_dir, AUG0_FOLDER, TARGET_FILE)
    split_file(corp_dir)
    train_eval_test(src_file)
    train_eval_test(tgt_file, flag='tgt')