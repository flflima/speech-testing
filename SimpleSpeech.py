import speech_recognition as sr

r = sr.Recognizer()

harvard = sr.AudioFile('audio/harvard.wav')
with harvard as source:
    audio = r.record(source)

print('Processing...')

result = r.recognize_google(audio)

print(result)