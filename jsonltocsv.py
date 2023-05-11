import pandas as pd
import numpy as np
import json
import sys

# Specify the input and output file names
input = sys.argv[1]
output = sys.argv[2]

# Define a list to store the extracted values from each JSON object
data = []

# Open the .jsonl file and iterate over each line
with open(input, 'r') as f:
    for line in f:
        # Load the JSON object
        tweet = json.loads(line.strip())

        # Check if the JSON object is a tweet
        if tweet['_type'] == 'snscrape.modules.twitter.Tweet':
            # Extract the relevant values
            url = tweet['url']
            date = tweet['date']
            raw_content = tweet['rawContent'].replace("\n","").replace('"','doublequote')
            rendered_content = tweet['renderedContent'].replace("\n","").replace('"','doublequote')
            tweet_id = tweet['id']
            reply_count = tweet['replyCount']
            retweet_count = tweet['retweetCount']
            like_count = tweet['likeCount']
            quote_count = tweet['quoteCount']
            conversation_id = tweet['conversationId']
            hashtags = str(tweet['hashtags'])

            # Append the extracted values to the list
            data.append([url, date, raw_content, rendered_content, tweet_id, reply_count, retweet_count, like_count, quote_count, conversation_id, hashtags])

# Convert the list into a pandas DataFrame
df = pd.DataFrame(data, columns=['url', 'date', 'raw_content', 'rendered_content', 'tweet_id', 'reply_count', 'retweet_count', 'like_count', 'quote_count', 'conversation_id', 'hashtags'])

# Write the DataFrame to a CSV file
df.to_csv(path_or_buf=output, sep=';', quotechar='"', index=False)