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
```


## Refenrence
- [Opennmt-tf Tool Document](http://opennmt.net/OpenNMT-tf/quickstart.html)