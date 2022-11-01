
import feedparser
import pandas as pd
from feed_list import urls
import datetime
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
        df = pd.DataFrame(data)
        # set_index removes the row counters
        df.set_index('title', inplace=True)
    print(df)
    return(df)