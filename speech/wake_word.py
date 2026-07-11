from sounddevice import InputStream
from openwakeword.model import Model
from threading import Event

wake_event = Event()


SAMPLE_RATE = 16000
CHUNK_SIZE = 1280

model = Model(inference_framework= "onnx")

def callback(indata, frames, time, status):
    audio = indata.flatten()

    prediction = model.predict(audio)

    score = prediction["hey_jarvis"]
    
    if score > 0.5:
        wake_event.set()

def wait_for_wake_word():

    wake_event.clear()

    stream = InputStream(
    samplerate = SAMPLE_RATE,
    channels = 1,
    dtype = "int16",
    blocksize= CHUNK_SIZE,
    callback = callback
    )

    with stream:
        wake_event.wait()