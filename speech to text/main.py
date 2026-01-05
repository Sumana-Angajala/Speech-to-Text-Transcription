from src.microphone_transcription import mic_to_text
from src.file_transcription import file_to_text
from src.utils import clear_screen, print_header, get_audio_files
import os

def main():
    clear_screen()
    print_header()
    
    while True:
        print("\n" + "="*50)
        print("SPEECH-TO-TEXT TRANSCRIPTION TOOL")
        print("="*50)
        print("\n[1] Microphone Input (Real-time)")
        print("[2] Audio File Input")
        print("[3] View Available Audio Files")
        print("[4] Exit")
        print("\n" + "="*50)
        
        choice = input("\nChoose option (1-4): ").strip()
        
        if choice == "1":
            print("\n🎤 Starting Microphone Transcription...")
            print("Speak clearly into your microphone.")
            print("Press Ctrl+C to stop recording.\n")
            mic_to_text()
            
        elif choice == "2":
            audio_files = get_audio_files()
            if audio_files:
                print("\n📁 Available audio files:")
                for i, file in enumerate(audio_files, 1):
                    print(f"  [{i}] {file}")
                
                file_choice = input("\nEnter file number or full path: ").strip()
                
                if file_choice.isdigit() and 1 <= int(file_choice) <= len(audio_files):
                    filepath = os.path.join("audio", audio_files[int(file_choice) - 1])
                else:
                    filepath = file_choice
                
                if os.path.exists(filepath):
                    file_to_text(filepath)
                else:
                    print(f"\n❌ Error: File not found: {filepath}")
            else:
                filepath = input("\nEnter audio file path: ").strip()
                if os.path.exists(filepath):
                    file_to_text(filepath)
                else:
                    print(f"\n❌ Error: File not found: {filepath}")
        
        elif choice == "3":
            audio_files = get_audio_files()
            if audio_files:
                print("\n📁 Audio files in 'audio/' folder:")
                for i, file in enumerate(audio_files, 1):
                    size = os.path.getsize(os.path.join("audio", file)) / 1024
                    print(f"  [{i}] {file} ({size:.2f} KB)")
            else:
                print("\n📁 No audio files found in 'audio/' folder.")
                print("   Place .wav, .mp3, or .flac files there.")
        
        elif choice == "4":
            print("\n👋 Thank you for using Speech-to-Text Tool!")
            break
        
        else:
            print("\n❌ Invalid choice. Please enter 1-4.")
        
        input("\nPress Enter to continue...")
        clear_screen()

if __name__ == "__main__":
    main()

