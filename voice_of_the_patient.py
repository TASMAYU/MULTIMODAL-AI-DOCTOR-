#Step1: Setup Audio recorder (ffmpeg & portaudio)
import logging 
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from groq import Groq

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message) s ')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    recognizer= sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting the Noise in the surrounding")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info(" Start your conversation now...")

            # recording the audio for it 
            audio_data= recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info(" Recording the audio completed...")

            # now conversion of that audio file to mp3 file 
            wav_data= audio_data.get_wav_data()
            audio_segment= AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format= "mp3", bitrate="128k")

            logging.info(f"Audio saved to mp3 file {file_path}")


    except Exception as e:
        logging.error(f"An Error occured{e}")

audio_file_path= "voice_test_1.mp3"
record_audio(file_path=audio_file_path)



#Step2: Setup Speech to text-STT-model for transcription (Voice to text using Openai Whisper Model)
import os
from dotenv import load_dotenv

load_dotenv() 


from groq import Groq

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
stt_model="whisper-large-v3"

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client=Groq(api_key=GROQ_API_KEY)
    
    audio_file=open(audio_filepath, "rb")
    transcription=client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )

    return transcription.text


