import speech_recognition as sr
from src.utils import save_transcription
from datetime import datetime

def mic_to_text():
    """
    Capture audio from microphone and convert to text
    
    Returns:
        str: Transcribed text or None if error occurs
    """
    recognizer = sr.Recognizer()
    
    # Adjust for ambient noise
    with sr.Microphone() as source:
        print("\n🔊 Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("✅ Ready! Start speaking...\n")
        
        try:
            # Listen to the microphone
            audio_data = recognizer.listen(source, timeout=None, phrase_time_limit=None)
            print("\n⏳ Processing audio... Please wait.")
            
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
            
        except sr.WaitTimeoutError:
            print("\n❌ No speech detected. Please try again.")
            return None
        except sr.UnknownValueError:
            print("\n❌ Could not understand audio. Please speak clearly.")
            return None
        except sr.RequestError as e:
            print(f"\n❌ API Error: {e}")
            print("   Check your internet connection.")
            return None
        except KeyboardInterrupt:
            print("\n\n⏹️  Recording stopped by user.")
            return None
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            return None

