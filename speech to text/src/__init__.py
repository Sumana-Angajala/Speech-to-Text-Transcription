"""
Speech-to-Text Transcription Package
Initializes the package and exposes main functions
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# Import main functions for easy access
from src.microphone_transcription import mic_to_text
from src.file_transcription import file_to_text
from src.utils import save_transcription, clear_screen, print_header

__all__ = [
    'mic_to_text',
    'file_to_text',
    'save_transcription',
    'clear_screen',
    'print_header'
]


