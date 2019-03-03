# Chatbot Baseline

## 1. Data Process

### (1) Parse and Clean Data

- The reddit datasets are downloaded from [Reddit](http://files.pushshift.io/reddit/comments/). They are all json objects.

- I just chose one month 'RC_2015-05.bz2' data for baseline, the size of this dataset is 33,46 GB after decompression. But you don't need to decompress it.

- The code of parsing and cleaning the reddit data is in the directory 'baseline/Data/Corpus/RedditData/'.

- The size of cleaned reddit data is 166,2 MB after processing 'RC_2015-05.bz2'. I have uploaded the first 200 lines of cleaned data here. It is in the directory 'baseline/Data/Corpus/RedditData/standard/reddit_cleaned_200.txt'. You can check it.

### (2) Preprocess Data and Generate Vocabulary

- Preprocess the data so that it can be handled by tensorflow TextLineDataSet. The code of preprocessing reddit data is in the directory 'baseline/Data/Corpus/preprocessor.py'. The generated file should be called 'reddit_cleaned_new.txt'.

- Generate vocabulary. The code is in 'baseline/Data/Corpus/vocabgenerator.py'. The size of vocabulary for reddit data 'RC_2015-05' is 228349.

## 2. Build the Model

### (1) Use OpenNMT-tf Tool to Build the Transformer Model

- Install OpenNMT-tf
```linux
  virtualenv --system-site-package -p python3 ./transformerenv
  source transformerenv/bin/activate
  pip install OpenNMT-tf[tensorflow-gpu]
```

- Prepare the data for OpenNMT tool
  - Split the questions and answers in two different files, and generate train, eval and test data by using the code 'baseline/Data/Corpus/splitQA.py'.

  - Build the source and target word vocabularies from the training files
  ```linux
    cd baseline/Data/Corpus/Augment0
    onmt-build-vocab --size 5000 --save_vocab src-vocab.txt src-train.txt
    onmt-build-vocab --size 5000 --save_vocab tgt-vocab.txt tgt-train.txt
  ```

  - Create YAML configuration file, let's name it data.yml. More details are in [OpenNMT-tf Configuration](http://opennmt.net/OpenNMT-tf/configuration.html)
  ```linux
    model_dir: run/

    data:
    	train_features_file: src-train.txt
    	train_labels_file: tgt-train.txt
    	eval_features_file: src-val.txt
    	eval_labels_file: tgt-val.txt
    	source_words_vocabulary: src-vocab.txt
    	target_words_vocabulary: tgt-vocab.txt
  ```

- Train the model
```linux
  CUDA_VISIBLE_DEVICES=? onmt-main train_and_eval --model_type Transformer --config data.yml --auto_config
```


## Refenrence
- [Opennmt-tf Tool Document(Quickstart)](http://opennmt.net/OpenNMT-tf/quickstart.html)