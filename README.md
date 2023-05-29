# Web-based_API


![](/structure_reddit.svg)


## Data pipeline 

### - Collect reddits through reddits API
### - Add collected posts into MangoDB Database
### - Run sentiment analysis of the reddit posts
#### + Sentiment analysis is based on VADER (Valence Aware Dictionary and sEntiment Reasoner) library
### - Store the post and the resulted sentiment in POSTGRES Database
### - Update posts and Sentiment to Slack through Slackbot

### All jobs are running on Docker Containers
#### + Make it possible to deploy online
