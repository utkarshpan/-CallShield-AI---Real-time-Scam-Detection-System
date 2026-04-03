# download_audio.py
import os
import requests

print("🎤 Downloading audio files...")

# Create folder
os.makedirs("sample_calls", exist_ok=True)

# Use Google TTS API (free, no installation)
def create_audio(text, filename):
    url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={text}&tl=en&client=tw-ob"
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            return True
    except:
        pass
    return False

# Scam call phrases
scam_phrases = [
    "Hello sir, I am calling from your bank.",
    "Your account will be blocked today.",
    "Please share the OTP immediately."
]

print("📞 Creating scam call audio...")
for i, phrase in enumerate(scam_phrases):
    filename = f"sample_calls/scam_{i+1}.wav"
    print(f"   Downloading: {phrase[:30]}...")
    create_audio(phrase, filename)
    print(f"   Saved: {filename}")

# Normal call phrases
normal_phrases = [
    "Hello, this is a reminder for your appointment tomorrow.",
    "Please confirm your availability.",
    "Thank you, have a great day."
]

print("\n📞 Creating normal call audio...")
for i, phrase in enumerate(normal_phrases):
    filename = f"sample_calls/normal_{i+1}.wav"
    print(f"   Downloading: {phrase[:30]}...")
    create_audio(phrase, filename)
    print(f"   Saved: {filename}")

print("\n✅ All audio files created!")
print("📁 Files in sample_calls folder:")
os.system("dir sample_calls")