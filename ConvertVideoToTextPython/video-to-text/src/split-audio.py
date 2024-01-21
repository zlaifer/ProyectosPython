from pydub import AudioSegment
from pydub.utils import make_chunks

FOLDER_AUDIO_PATH = "../audio"
FOLDER_AUDIO_TO_SAVE_PATH = "../audio-split"
FILE_AUDIO = "SecureCodingPractices"
FILE_AUDIO_EXT = ".wav"
FILE_AUDIO_CHUNK = 60000

myaudio = AudioSegment.from_file(f"{FOLDER_AUDIO_PATH}/{FILE_AUDIO}{FILE_AUDIO_EXT}" , "wav") 
chunk_length_ms = FILE_AUDIO_CHUNK # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

#Export all of the individual chunks as wav files
for i, chunk in enumerate(chunks):
    chunk_name = f"{FILE_AUDIO}{i}{FILE_AUDIO_EXT}"
    print(f"exporting => [{chunk_name}]")
    chunk.export(f"{FOLDER_AUDIO_TO_SAVE_PATH}/{chunk_name}", format="wav")