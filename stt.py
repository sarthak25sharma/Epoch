from vosk import Model, KaldiRecognizer
import wave
from pydub import AudioSegment

model_path = r"C:\Users\ASUS\Desktop\STT\vosk-model-small-en-us-0.15"
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

audio_file_path = r"C:\Users\ASUS\Desktop\STT\audio_extract.mp3"
audio = AudioSegment.from_mp3(audio_file_path)

wav_audio_file_path = "audio_extract.wav"

# Export audio to WAV format with the sample rate set to 16 kHz
audio.export(wav_audio_file_path, format="wav", parameters=["-ac", "1", "-ar", "16000"])

with wave.open(wav_audio_file_path, 'rb') as wave_file:
    while True:
        data = wave_file.readframes(4096)
        print("Working..")
        if len(data) == 0:
            break
        recognizer.AcceptWaveform(data)

result = recognizer.FinalResult()
print("Final Result:", result)

with open('output.txt', 'a') as f:
    f.write(result)
    f.write("\n")
