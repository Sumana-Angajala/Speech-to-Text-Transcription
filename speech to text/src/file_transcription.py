"""
Audio file transcription module
Converts audio files to text using Google Speech API
"""

import speech_recognition as sr
from src.utils import save_transcription
from datetime import datetime
import os

def file_to_text(audio_file_path):
    """
    Convert audio file to text
    
    Args:
        audio_file_path (str): Path to audio file (.wav, .flac, .aiff)
    
    Returns:
        str: Transcribed text or None if error occurs
    """
    if not os.path.exists(audio_file_path):
        print(f"\n❌ Error: File not found: {audio_file_path}")
        return None
    
    recognizer = sr.Recognizer()
    
    print(f"\n📂 Loading audio file: {audio_file_path}")
    print("⏳ Processing... This may take a moment.\n")
    
    try:
        # Load audio file
        with sr.AudioFile(audio_file_path) as source:
            # Record the audio data
            audio_data = recognizer.record(source)
            
            print("🔄 Transcribing audio...")
            
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)
            
            print("\n" + "="*50)
            print("TRANSCRIPTION RESULT")
            print("="*50)
            print(f"\n{text}\n")
            print("="*50)
            
            # Statistics
            word_count = len(text.split())
            char_count = len(text)
            print(f"\n📊 Statistics:")
            print(f"   Words: {word_count}")
            print(f"   Characters: {char_count}")
            
            # Ask if user wants to save
            save_choice = input("\n💾 Save transcription? (y/n): ").strip().lower()
            if save_choice == 'y':
                filename = f"transcription_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                if save_transcription(text, filename):
                    print(f"✅ Transcription saved to: output/{filename}")
            
            return text
            
    except sr.UnknownValueError:
        print("\n❌ Could not understand audio in the file.")
        print("   Ensure the audio is clear and in a supported format.")
        return None
    except sr.RequestError as e:
        print(f"\n❌ API Error: {e}")
        print("   Check your internet connection.")
        return None
    except FileNotFoundError:
        print(f"\n❌ File not found: {audio_file_path}")
        return None
    except Exception as e:
        print(f"\n❌ Error processing file: {e}")
        print("   Supported formats: .wav, .flac, .aiff")
        return None