import sounddevice
from scipy.io.wavfile import write

fs=44100 #sample_rate
sound= int(input("Enter the time duration in second:")) #enter your required time ...
print("Recording....\n")
recod_voice= sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.wav",fs,recod_voice)
print("Finished...\nPlease Check it...")