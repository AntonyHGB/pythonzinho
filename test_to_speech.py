import os
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

voice_id = "hindi"
newVoiceRate = 120
engine.setProperty('voice', voice_id)
engine.setProperty('rate', newVoiceRate)

engine.say("Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...")
engine.save_to_file("Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...", 'test.wav')
engine.runAndWait()
