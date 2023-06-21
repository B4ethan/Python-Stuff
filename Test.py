import pyttsx3

text = "hello world"

engine = pyttsx3.init()

engine.save_to_file(text, 'test.mp3')

engine.runAndWait()