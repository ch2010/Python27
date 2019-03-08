import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile('audio (1).wav') as source:
    audio = r.record(source)

try:
    s = r.recognize_google(audio)
    print("Saida: "+s)
except Exception as e:
    print("Exception: "+str(e))
