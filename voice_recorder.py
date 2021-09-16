import sounddevice
from scipy.io.wavfile import write

fs = 44100
second =int(input("Quantos segundos deseja gravar? "))

print("\n Gravando ....................\n")

record_voice = sounddevice.rec(int(second * fs), samplerate= fs, channels= 2)
sounddevice.wait()

write("gravação.mp3", fs, record_voice)

print("Gravação finalizada")