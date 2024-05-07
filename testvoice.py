from google.cloud import speech
import io
import wave

def transcribe_file(voice_file_path):

    # サンプリングレートを確認
    with wave.open(voice_file_path, 'rb') as f:
        fr = f.getframerate()

    # 音声ファイルの読み込み
    with io.open(voice_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=fr,
        language_code="ja-JP"
    )

    # APIの呼び出し
    client = speech.SpeechClient()
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print(u"Transcript: {}".format(result.alternatives[0].transcript))

transcribe_file("C:\\Users\\akiko\\TestVoice\\240_mono.wav")