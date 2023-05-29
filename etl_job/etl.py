import pymongo
import time
import math
from sqlalchemy import create_engine, text
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host='mongodb', port=27017)

print ("hello, etl_job is running")
time.sleep(10)  # seconds

# Select the database you want to use withing the MongoDB server
db = client.reddit

   
#Create a Postgres client
pg = create_engine('postgresql://docker_user:12345@postgresdb:5432/reddit', echo=True)

#Connect to the client to postgres
pg_connect = pg.connect()

#Create Table in Postgres
table = text(

  """
     CREATE TABLE IF NOT EXISTS posts (
     text VARCHAR(500),
     sentiment NUMERIC
);
""")

pg_connect.execute(table)
pg_connect.commit()

# sentiment analyser
s_analyser = SentimentIntensityAnalyzer()

docs = db.posts.find()
for doc in docs:
    #print(doc)
    _text = doc['text'].replace("'", " ")
    _list = s_analyser.polarity_scores(_text)
    score = _list['compound']   		# placeholder value
    #trr= "INSERT INTO posts VALUES (%s, %s);"
    query = text(f"INSERT INTO posts VALUES ('{_text}', {score});")
    pg_connect.execute(query)
    pg_connect.commit()

#time.sleep(2);
#pg_connect.close()
