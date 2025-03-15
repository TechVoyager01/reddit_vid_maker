import os
import requests
from moviepy import *

ASSETS_DIR = "assets/"
VIDEO_DIR = os.path.join(ASSETS_DIR, "videos/")
DEFAULT_VIDEO_PATH = os.path.join(VIDEO_DIR, "background.mp4")


def list_existing_videos():
    """Lists available videos in the assets directory."""
    if not os.path.exists(VIDEO_DIR):
        os.makedirs(VIDEO_DIR, exist_ok=True)
    return [f for f in os.listdir(VIDEO_DIR) if f.endswith(('.mp4', '.mov', '.avi'))]


def download_video(url, save_path):
    """Downloads a video from a URL and saves it in the assets folder."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    print(f"📥 Downloading video from {url}...")
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"✅ Video downloaded to {save_path}")
    else:
        print("❌ Failed to download video!")
        return None

    return save_path


def get_video_choice():
    """Asks the user if they want to use an existing video or download a new one."""
    videos = list_existing_videos()

    if videos:
        print("\n🎥 Existing videos in assets:")
        for i, video in enumerate(videos, start=1):
            print(f"{i}. {video}")

        choice = input("\nDo you want to use an existing video? (yes/no): ").strip().lower()

        if choice == "yes":
            selected_index = int(input("Enter the number of the video you want to use: ").strip()) - 1
            return os.path.join(VIDEO_DIR, videos[selected_index])

    # If no existing videos or user chooses to download a new one
    video_url = input("\nEnter the video URL to download: ").strip()
    video_name = input("Enter a name for the video file (without extension): ").strip() + ".mp4"
    save_path = os.path.join(VIDEO_DIR, video_name)

    return download_video(video_url, save_path)


def create_video(text, audio_file="output/audio.mp3", output_file="output/reddit_video.mp4"):
    """Creates a video using user-selected background video and voiceover."""

    # Ask user for video selection
    video_file = get_video_choice()

    if not video_file or not os.path.exists(video_file):
        print("❌ No valid video found. Exiting.")
        return

    print(f"\n🎬 Using video: {video_file}")

    # Load selected video
    clip = VideoFileClip(video_file).subclip(0, 10)

    # Add text overlay
    txt_clip = TextClip(text, fontsize=50, color="white", size=(1280, 720))
    txt_clip = txt_clip.set_position("center").set_duration(10)

    # Add audio
    audio = AudioFileClip(audio_file)
    clip = clip.set_audio(audio)

    # Merge everything
    final_clip = CompositeVideoClip([clip, txt_clip])
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    final_clip.write_videofile(output_file, fps=24)

    print(f"✅ Video saved as {output_file}")


if __name__ == "__main__":
    create_video("This is a Reddit video bot test!")
