import praw
import unicodedata

def create_word_list(subreddit_name, words = []):
    reddit = praw.Reddit(client_id = '0iwmtGkjvYPrwg',
                     client_secret = 'Xmt7N6YBaxHwK9wbutqZac3xP5E',
                     user_agent = 'DataCrawler')

    subreddit = reddit.subreddit(subreddit_name)

    hot = subreddit.hot();

    for post in hot:
        comment_queue = post.comments[:]
        while comment_queue:
            comment = comment_queue.pop(0)
            if 'body' in dir(comment):
                sanitized_body = ''.join(c for c in unicodedata.normalize('NFC', comment.body) if c <= '\uFFFF')
                split_comment = sanitized_body.split(' ')
                for word in split_comment:
                    word = word.replace('\n','')
                    words.append(word)
            if 'replies' in dir(comment):
                comment_queue.extend(comment.replies)
    return words


words = []
subreddit_name = 'Jokes'
print(create_word_list(subreddit_name))
