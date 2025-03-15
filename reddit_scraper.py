import praw
import config

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=config.REDDIT_CLIENT_ID,
    client_secret=config.REDDIT_CLIENT_SECRET,
    user_agent=config.REDDIT_USER_AGENT,
    username=config.REDDIT_USERNAME,
    password=config.REDDIT_PASSWORD
)


def fetch_top_post(subreddit_name="AskReddit"):
    """Fetches the top post from a subreddit"""
    subreddit = reddit.subreddit(subreddit_name)
    post = next(subreddit.top(time_filter="day", limit=1))

    return {
        "title": post.title,
        "body": post.selftext if post.selftext else "No text available",
        "comments": [comment.body for comment in post.comments[:5]]
    }


if __name__ == "__main__":
    post = fetch_top_post("AskReddit")
    print("Title:", post["title"])
    print("Body:", post["body"])
    print("Comments:", post["comments"])
