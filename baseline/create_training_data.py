import sqlite3
import pandas as pd

timeframes = ['2015-05']
path = '../chatdata/reddit_data/'

def writeData(p, df, head):
    with open(p, 'a', encoding = 'utf8') as f:
        for content in df[head].values:
            f.write(str(content) + '\n')

for timeframe in timeframes:
    connection = sqlite3.connect((path + 'database/{}.db').format(timeframe))
    c = connection.cursor()
    limit = 5000 # the size of chunk that we're going to pull on RAM at a time from the database
    last_unix = 0 # help us make pulls from the database
    cur_length = limit # tell us we're done
    counter = 0 # allow us to show some debugging information
    test_done = False # build test data
    
    while cur_length == limit:
        df = pd.read_sql("SELECT * FROM parent_reply WHERE unix > {} and parent NOT NULL and score > 0 ORDER BY unix ASC LIMIT {}".format(last_unix,limit),connection)
        last_unix = df.tail(1)['unix'].values[0]
        cur_length = len(df)
#        print(cur_length)
        
        if not test_done:
            writeData(path+'test/test.from', df, 'parent')
            writeData(path+'test/test.to', df, 'comment')                  
            test_done = True
        
        else:
            writeData(path+'train/train.from', df, 'parent')
            writeData(path+'train/train.to', df, 'comment')
                    
        counter += 1
        if counter % 20 == 0:
            print(counter*limit,'rows completed so far')