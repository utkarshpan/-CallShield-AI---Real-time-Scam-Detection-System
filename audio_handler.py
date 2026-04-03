# audio_handler.py

import speech_recognition as sr
import tempfile
import os
from pydub import AudioSegment

class AudioProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        # Optimize for Hinglish
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        
    def transcribe_audio_file(self, audio_path: str, chunk_seconds: int = 3):
        """Process audio file in chunks for real-time simulation"""
        # Load audio
        audio = AudioSegment.from_wav(audio_path)
        
        # Calculate chunk size in milliseconds
        chunk_ms = chunk_seconds * 1000
        
        # Process each chunk
        for i, start_ms in enumerate(range(0, len(audio), chunk_ms)):
            end_ms = min(start_ms + chunk_ms, len(audio))
            chunk = audio[start_ms:end_ms]
            
            # Save temp chunk
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp:
                chunk.export(tmp.name, format='wav')
                tmp_path = tmp.name
            
            # Transcribe chunk
            text = self.transcribe_audio(tmp_path)
            
            # Cleanup
            os.unlink(tmp_path)
            
            yield {
                'chunk_index': i,
                'start_time': start_ms / 1000,
                'end_time': end_ms / 1000,
                'text': text
            }
    
    def transcribe_audio(self, audio_path: str) -> str:
        """Transcribe audio to text"""
        try:
            with sr.AudioFile(audio_path) as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio_data = self.recognizer.record(source)
                
                # Use Google Speech Recognition (works with Hinglish)
                text = self.recognizer.recognize_google(audio_data)
                return text.lower()
                
        except sr.UnknownValueError:
            return "[unintelligible]"
        except sr.RequestError as e:
            return f"[error: {e}]"
        except Exception as e:
            return f"[error: {str(e)}]"
    
    def transcribe_mic(self, duration: int = 5):
        """Live mic transcription (for bonus demo)"""
        try:
            with sr.Microphone() as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=duration)
                
            text = self.recognizer.recognize_google(audio)
            return text.lower()
            
        except sr.WaitTimeoutError:
            return "[timeout]"
        except sr.UnknownValueError:
            return "[could not understand]"
        except Exception as e:
            return f"[error: {str(e)}]"