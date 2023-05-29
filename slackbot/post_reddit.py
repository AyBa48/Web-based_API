import pyjokes
import requests
from sqlalchemy import create_engine, text
import json
import time 
import psycopg2

time.sleep(15)

webhook_url = "https://hooks.slack.com/services/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"

#joke = pyjokes.get_joke()
#data = {'text': joke, '_id': '2'}
#print(requests.post(url=webhook_url, json = data))


#Create a Postgres client
pg = create_engine('postgresql://docker_user:12345@postgresdb:5432/reddit', echo=True)

#Connect to the client to postgres
pg_connect = pg.connect()

new_post = text("SELECT * FROM posts")

r = pg_connect.execute(new_post).fetchall()
pg_connect.commit()

#print(r)

#text_sql=pg_client_connect.execute(query)
# post=text_sql.fetchall()
# print(post)
# data = {'text': str(post)}
# requests.post(url=webhook_url, json = data)
# pg_client_connect.close()

for i in range(len(r)):
  #print(f"This is the object : {r[i]}")
  g=r[i]
  post =g[0]
  sent=float(g[1])
  #_dict={"_title": post , "sentiment": sent}
  #print(g[0])
  #print(_dict)
  data = { "text": f"post: {post}, Sentiment score = {sent}"} 
  #print(data)
  requests.post(url=webhook_url, json = data)
  #print(requests.post(url=webhook_url, json = _dict))
  time.sleep(25)  # seconds
  
#r_j = json.dumps([i for i in r])

#print(f"This is the object : {r_j}")
#print(type(r))



