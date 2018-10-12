1. Create Database

The reddit datasets are all json objects.

Produce comment-reply pairs from reddit datasets. I just chose one month 'RC_2015-05' data for code test, the size of this dataset is 33,46 GB after decompression but before processing it.

I should probably have only 1 reply per comment, even though many single comments might have many replies, I should really just go with one. I can go with the top-voted one(the reply with the best score).

The database(table name: parent_reply) stores the parent_id, comment_id, the parent comment, the reply, subreddit, the time and the score(votes) for the comment.

Just insert the comment whose score is more than 1(>1).

Just insert the comment whose length is less than 50.

The size of database for 'RC_2015-05'(2015-05.db) which has been processed is 2,58 GB. There are 54,500,000 rows of original data(RC_2015-05) and 3,339,233 comment-reply(one-turn) pairs after processing. It takes about one 70 minutes to achieve database '2015-05.db' from original data by running on my own mac book.

Delete the rows which have no parent content. The size of database(2015-05.db) is 908 MB.

2. Create Training and Testing Data

Create files that are basically ‘comment(parent)’ and ‘reply’ text files, where each line is the sample.

In the ‘train’ file, there are two files, ’train.from’ and ‘train.to’, which correspond to each other line by line.

In the ‘test’ file, there are two files, ‘test.from’ and ‘test.to’, which correspond to each other line by line.