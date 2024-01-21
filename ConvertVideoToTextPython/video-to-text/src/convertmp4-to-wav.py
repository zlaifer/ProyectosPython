import moviepy.editor as mp 

# Load the video 
video = mp.VideoFileClip("../videos/SecureCodingPractices.mp4") 

# Extract the audio from the video 
audio_file = video.audio 
audio_file.write_audiofile("../audio/SecureCodingPractices.wav") 
