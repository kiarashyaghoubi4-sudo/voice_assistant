from sounddevice import InputStream
from openwakeword.model import Model
from threading import Event
from utils.paths import MODELS
from time import sleep

wake_event = Event()


SAMPLE_RATE = 16000
CHUNK_SIZE = 1280
MODEL_NAME = "hey_jarvis_v0.1"

def create_model():
    return Model(
        wakeword_models=
        [f"{MODELS}\\hey_jarvis_v0.1.onnx"],
        inference_framework="onnx"
    )

model = create_model()

def callback(indata, frames, time, status):


    audio = indata.flatten()

    prediction = model.predict(audio)
    
    score = prediction.get(MODEL_NAME, 0)

    if score > 0.5:
        wake_event.set()

def wait_for_wake_word():

    wake_event.clear()

    with InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
        blocksize=CHUNK_SIZE,
        callback=callback
    ):
        wake_event.wait()

    model.reset()