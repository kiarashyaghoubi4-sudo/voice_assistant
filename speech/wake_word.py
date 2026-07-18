from sounddevice import InputStream
from openwakeword.model import Model
from threading import Event
from utils.paths import MODELS

wake_event = Event()


SAMPLE_RATE = 16000
CHUNK_SIZE = 1280
WAKEWORD_NAME = "hey_jarvis"

model = Model(
    inference_framework= "onnx",
    wakeword_models=[MODELS / WAKEWORD_NAME])

def callback(indata, frames, time, status):
    audio = indata.flatten()

    prediction = model.predict(audio)

    score = prediction.get(WAKEWORD_NAME, 0)
    
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