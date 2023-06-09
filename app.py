from google.cloud import speech
import os, io

client = speech.SpeechClient()

# filename=os.path.join(os.path.dirname(__file__), 'test.wav')
filename=r"C:\Users\dnila\OneDrive\Documents\NilavyaDasPersonal\SpeechText\audio.wav"
with io.open(filename, "rb") as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content) 

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,audio_channel_count=1,language_code="en-US",
)
response = client.recognize(request={"config":config, "audio":audio})

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
