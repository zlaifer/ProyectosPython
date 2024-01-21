import moviepy.editor as mp

name = "./Video/Junta_2023-12-04 21-02-46.mp4"

#Cargamos el fichero .mp4
clip = mp.VideoFileClip(name)

#Lo escribimos como audio y `.mp3`
clip.audio.write_audiofile("./Mp3/Junta_2023-12-04 21-02-46.mp3")