import os
from music_midi import transcribe_audio

class MUSIC_SHEET:
    def __init__(self, file_path:str) -> None:
        self.file_path = file_path
        self.transcribed_path = None
        self.check_file_type()
        
    def check_file_type(self):
        _, ext = os.path.splitext(self.file_path)
        ext = ext.lower()
        
        if ext=='.mp3':
            print('mp3 type')
            self.process_mp3()
        else:
            print('wrong type')
            raise ValueError(f"Unsupported file type: {ext}")
        return self.transcribed_path
    
    def process_mp3(self):
        self.transcribed_path = transcribe_audio(self.file_path)