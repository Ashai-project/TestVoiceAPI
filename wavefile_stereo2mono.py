from pydub import AudioSegment

sound = AudioSegment.from_wav("C:\\Users\\akiko\\TestVoice\\240.wav")
sound = sound.set_channels(1)
sound.export("C:\\Users\\akiko\\TestVoice\\240_mono.wav", format="wav")
