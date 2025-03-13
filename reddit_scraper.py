import praw
import config

# To get sign-in data from reddit scrapper
reddit = praw.Reddit(
    client_id=config.REDDIT_CLIENT_ID,
    client_secret=config.REDDIT_CLIENT_SECRET,
    user_agent=config.REDDIT_USER_AGENT,
    username=config.REDDIT_USERNAME,
    password=config.REDDIT_PASSWORD
)

def fetch_top_post(subreddit_name):
    """Fetch the top post from a subreddit"""
    subreddit = reddit.subreddit(subreddit_name)
    post = next(subreddit.top("day", limit=1))
    return post.title, post.selftext

if __name__ == "__main__":
    title, body = fetch_top_post("AskReddit")
    print("Title:", title)
    print("Body:", body)

