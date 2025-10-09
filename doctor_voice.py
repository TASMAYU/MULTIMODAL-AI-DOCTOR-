# setting up speech to text (gtts and Elevenlabs)
# gTTS(Google text to speech )
import os
from gtts import gTTS

def text_to_speech_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow= False
    )
    audioobj.save(output_filepath)

input_text="hello How are you, I am tasmayu. i will help you. I am the coordinator here."
#text_to_speech_gtts_old(input_text=input_text, output_filepath="gtts_texting.mp3")    


# Now with Elevenlabs
from dotenv import load_dotenv
load_dotenv()
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVEN_LABS_API_KEY= os.environ.get("ELEVEN_LABS_API_KEY")


def text_to_speech_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVEN_LABS_API_KEY)
    audio= client.text_to_speech.convert(
        text=input_text,
        voice_id="mCQMfsqGDT6IDkEKR20a",
        output_format="mp3_22050_32",
        model_id= "eleven_turbo_v2"

    )
    elevenlabs.save(audio, output_filepath)


#text_to_speech_elevenlabs_old(input_text, output_filepath="elevenlabs.mp3")





# Autoplay for text output to voice

import subprocess
import platform

def text_to_speech_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow= False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

input_text="hello How are you, PlexusAI here . i will help you as your personalised doctor. I am just a learning assistant to guide you not a real doctor "
#text_to_speech_gtts(input_text=input_text, output_filepath="gtts_texting.mp3")    



def text_to_speech_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVEN_LABS_API_KEY)
    audio= client.text_to_speech.convert(
        text=input_text,
        voice_id="mCQMfsqGDT6IDkEKR20a",
        output_format="mp3_22050_32",
        model_id= "eleven_turbo_v2"

    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")



text_to_speech_elevenlabs(input_text, output_filepath="elevenlabs.mp3")
