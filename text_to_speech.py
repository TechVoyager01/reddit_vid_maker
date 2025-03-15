from gtts import gTTS
import os

def text_to_speech(text, filename="output/audio.mp3"):
    """Converts text to speech and saves as an MP3 file"""
    tts = gTTS(text=text, lang="en")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    tts.save(filename)
    print(f"Audio saved as {filename}")
    return filename

if __name__ == "__main__":
    text_to_speech("Hello! This is a test for the Reddit bot.")
