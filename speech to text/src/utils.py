"""
Utility functions for Speech-to-Text Tool
Includes file operations, screen management, and helper functions
"""

import os
from datetime import datetime

def save_transcription(text, filename=None):
    """
    Save transcription to a text file
    
    Args:
        text (str): Transcription text to save
        filename (str): Output filename (optional, auto-generated if None)
    
    Returns:
        bool: True if saved successfully, False otherwise
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs("output", exist_ok=True)
        
        # Generate filename if not provided
        if filename is None:
            filename = f"transcription_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        filepath = os.path.join("output", filename)
        
        # Write transcription to file with formatting
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("="*60 + "\n")
            f.write("SPEECH-TO-TEXT TRANSCRIPTION\n")
            f.write("="*60 + "\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Filename: {filename}\n\n")
            f.write("="*60 + "\n")
            f.write("TRANSCRIPTION:\n")
            f.write("="*60 + "\n\n")
            f.write(text)
            f.write("\n\n" + "="*60 + "\n")
            f.write(f"Word Count: {len(text.split())}\n")
            f.write(f"Character Count: {len(text)}\n")
            f.write("="*60 + "\n")
        
        return True
    except Exception as e:
        print(f"\n❌ Error saving file: {e}")
        return False


def clear_screen():
    """
    Clear terminal screen (works on Windows, Linux, macOS)
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """
    Print application header with branding
    """
    print("\n" + "="*60)
    print(" "*15 + "🎤 SPEECH-TO-TEXT TOOL 🎤")
    print("="*60)
    print(" "*10 + "Convert Speech to Text with Python")
    print("="*60 + "\n")


def get_audio_files():
    """
    Get list of audio files in the audio directory
    
    Returns:
        list: Sorted list of audio filenames
    """
    audio_dir = "audio"
    
    # Create audio directory if it doesn't exist
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)
        return []
    
    # Supported audio formats
    supported_formats = ('.wav', '.flac', '.aiff', '.mp3')
    
    # Get all audio files
    audio_files = [f for f in os.listdir(audio_dir) 
                   if f.lower().endswith(supported_formats)]
    
    return sorted(audio_files)
