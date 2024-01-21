import speech_recognition as sr 

FOLDER_AUDIO_PATH = "../audio-split"
FILE_AUDIO = "SecureCodingPractices"
FILE_AUDIO_EXT = ".wav"
FOLDER_TEXT_PATH = "../text"
FILE_TEXT_EXT = ".txt"

# Initialize recognizer 
r = sr.Recognizer() 

# Load the audio file 
with sr.AudioFile(f"{FOLDER_AUDIO_PATH}/{FILE_AUDIO}0{FILE_AUDIO_EXT}") as source: 
	data = r.record(source) 

# Convert speech to text 
text = r.recognize_google(data) 

# Print the text 
with open(f'{FOLDER_TEXT_PATH}/{FILE_AUDIO}{FILE_TEXT_EXT}', 'a') as f:
    f.write(text)
