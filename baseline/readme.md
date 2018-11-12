# Chatbot Baseline

## 1. Data Process

- The reddit datasets are downloaded from [Reddit](http://files.pushshift.io/reddit/comments/). They are all json objects.

- I just chose one month 'RC_2015-05.bz2' data for baseline, the size of this dataset is 33,46 GB after decompression. But you don't need to decompress it.

- The code of parse and clean the reddit data is in the directory 'baseline/Data/Corpus/RedditData/'.

- The size of cleaned reddit data is 166,2 MB after processing 'RC_2015-05.bz2'. I have uploaded the first 200 lines of cleaned data here. It is in the directory 'baseline/Data/Corpus/RedditData/standard/reddit_cleaned_200.txt'. You can check it.

## 2. Create Training and Testing Data

## 3. Build encoder-decoder model with Attention Mechanism for Chatbot.