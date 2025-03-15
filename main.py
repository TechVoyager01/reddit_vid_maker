from reddit_scraper import fetch_top_post
from text_to_speech import text_to_speech
from video_maker import create_video

if __name__ == "__main__":
    post = fetch_top_post("AskReddit")

    print(f"Creating video for: {post['title']}")

    # Convert title to speech
    audio_file = text_to_speech(post["title"], "output/audio.mp3")

    # Create video
    video_file = create_video(post["title"], audio_file, "output/reddit_video.mp4")

    print("✅ Video creation complete:", video_file)


