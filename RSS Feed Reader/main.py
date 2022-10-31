# Goal is to read RSS feeds 


############# To be Added #############


# UI to read through it in a better way
# Add Extra Feeds - Possibly Database

# Integrate with the discord bot and post in te RSS channel 

# Have automatic updates instead of needing to be run

# Let this be called when it is setup

#######################################
import feedparser
import pandas as pd
from feed_list import urls
node = 'https://n-o-d-e.net/rss/rss.xml'

 
feed = feedparser.parse(node)
feed.entries[0].keys()


# Create function to call 

def feed_parse():
    feed = feedparser.parse(node)
    feed.entries[0].keys()


    data = {}
    # Parsing through entries and listing them
    for entry in feed.entries:
        data.setdefault('title', [])
        data.setdefault('published', [])
        data.setdefault('link', [])
        data['title'].append(entry.title)
        data['published'].append(entry.published)
        data['link'].append(entry.link)
        # feed = [entry.title, entry.published, entry.link] 
    df = pd.DataFrame(data)
    df.head()
    print(df)
    return(df)