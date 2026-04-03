# create_audio.py
import os
import pyttsx3
from pydub import AudioSegment

print("🎤 Creating audio files...")

# Create folder
os.makedirs("sample_calls", exist_ok=True)

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

# ========== SCAM CALL ==========
print("📞 Creating scam call...")

scam_phrases = [
    "Hello sir, I am calling from your bank.",
    "Your account will be blocked today.",
    "Please share the OTP immediately."
]

scam_audio = AudioSegment.empty()
for i, phrase in enumerate(scam_phrases):
    print(f"   Creating: {phrase}")
    temp_file = f"sample_calls/temp_scam_{i}.wav"
    engine.save_to_file(phrase, temp_file)
    engine.runAndWait()
    
    audio = AudioSegment.from_wav(temp_file)
    scam_audio += audio
    scam_audio += AudioSegment.silent(duration=1000)  # 1 sec pause
    
    os.remove(temp_file)

scam_audio.export("sample_calls/scam_call.wav", format="wav")
print("✅ Created: sample_calls/scam_call.wav")

# ========== NORMAL CALL ==========
print("\n📞 Creating normal call...")

normal_phrases = [
    "Hello, this is a reminder for your appointment tomorrow.",
    "Please confirm your availability.",
    "Thank you, have a great day."
]

normal_audio = AudioSegment.empty()
for i, phrase in enumerate(normal_phrases):
    print(f"   Creating: {phrase}")
    temp_file = f"sample_calls/temp_normal_{i}.wav"
    engine.save_to_file(phrase, temp_file)
    engine.runAndWait()
    
    audio = AudioSegment.from_wav(temp_file)
    normal_audio += audio
    normal_audio += AudioSegment.silent(duration=1000)
    
    os.remove(temp_file)

normal_audio.export("sample_calls/normal_call.wav", format="wav")
print("✅ Created: sample_calls/normal_call.wav")

print("\n✅ ALL DONE! Audio files ready.")
print("📁 Files created:")
print("   - sample_calls/scam_call.wav")
print("   - sample_calls/normal_call.wav")