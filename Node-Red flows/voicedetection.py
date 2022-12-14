#!/usr/bin/env python3

import struct
import pyaudio
import pvporcupine

porcupine = None
pa = None
audio_stream = None

access_key="aHvAPloBcuhvv4zgC8eXdexQYWHugvR3HYCshyy1+mKfC2wC6mSchw=="
keyw="jarvis"

try:
	porcupine = pvporcupine.create(access_key, keywords=[keyw])

	pa = pyaudio.PyAudio()

	audio_stream = pa.open(
		rate=porcupine.sample_rate,
		channels=1,
		format=pyaudio.paInt16,
		input=True,
		frames_per_buffer=porcupine.frame_length)

	
	while True:
	
		pcm = audio_stream.read(porcupine.frame_length)
		pcm= struct.unpack_from("h" * porcupine.frame_length, pcm)
	
		keyword_index = porcupine.process(pcm)

		if keyword_index >= 0:

			print("Hotword Detected, "+keyw)
			break
finally:
    if porcupine is not None:
        porcupine.delete()
   
    if audio_stream is not None:
        audio_stream.close()

    if pa is not None:
        pa.terminate()
