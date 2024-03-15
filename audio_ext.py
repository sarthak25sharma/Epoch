import moviepy.editor 
cvt_video=moviepy.editor.VideoFileClip(r"C:\Users\ASUS\Desktop\STT\RIISE 2022 final video.mp4")

audio_clip = cvt_video.audio
audio_path=r"C:\Users\ASUS\Desktop\STT\audio_extract.mp3"
audio_clip.write_audiofile(audio_path, codec='mp3')

audio_clip.close()
