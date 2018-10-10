The reddit datasets are all json objects.

Produce comment-reply pairs from reddit datasets. I just chose one month 'RC_2015-05' data for code test, the size of this dataset is 33,46 GB after decompression but before processing it.

I should probably have only 1 reply per comment, even though many single comments might have many replies, I should really just go with one. I can go with the top-voted one(the reply with the best score).

The database(table name: parent_reply) stores the parent_id, comment_id, the parent comment, the reply, subreddit, the time and the score(votes) for the comment.

Just insert the comment whose score is more than 1(>1).

Just insert the comment whose length is less than 50.