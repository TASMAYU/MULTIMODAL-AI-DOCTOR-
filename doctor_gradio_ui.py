'''import os 
import gradio as gr
from dotenv import load_dotenv
load_dotenv()


from doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from doctor_voice import text_to_speech_elevenlabs


system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Do not add any numbers or special characters in 
            your response. Your response should be in points in a sructured way. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Don't respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer brief (max 5 sentences). No preamble, start your answer right away please and explanation should be good"""


def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
                                                 audio_filepath=audio_filepath,
                                                 stt_model="whisper-large-v3")

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(query=system_prompt+speech_to_text_output, encoded_image=encode_image(image_filepath), model="meta-llama/llama-4-scout-17b-16e-instruct") #model="meta-llama/llama-4-maverick-17b-128e-instruct") 
    else:
        doctor_response = "No image provided to analyze"

    voice_of_doctor = text_to_speech_elevenlabs(input_text=doctor_response, output_filepath="final.mp3") 

    return speech_to_text_output, doctor_response, voice_of_doctor



gradio = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio("Temp.mp3")
    ],
    title="PlexusAI"
)

gradio.launch(debug=True)'''







import os
import gradio as gr
from dotenv import load_dotenv
load_dotenv()

from doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from doctor_voice import text_to_speech_elevenlabs


system_prompt = """You have to act as a professional doctor, I know you are not but this is for learning purpose. 
What's in this image? Do you find anything wrong with it medically? 
If you make a differential, suggest some remedies for them. Do not add any numbers or special characters in 
your response. Your response should be in paragraph. Also always answer as if you are answering to a real person.
Do not say 'In the image I see' but say 'With what I see, I think you have ....'
Don't respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot. 
Keep your answer brief (max 5 sentences). No preamble, start your answer right away please and explanation should be good."""


def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )

    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = "No image provided to analyze."

    voice_of_doctor = text_to_speech_elevenlabs(
        input_text=doctor_response, 
        output_filepath="final.mp3"
    )

    return speech_to_text_output, doctor_response, voice_of_doctor


#Custom Themed Layout 
with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="slate",
        neutral_hue="gray",
    ),
    css="""
        body { background-color: #0b172a; }
        .gradio-container { color: white !important; }
        button.primary { background-color: #2563eb !important; color: white !important; }
        .gr-button { border-radius: 10px !important; padding: 10px 16px !important; }
        h1 { text-align: center; color: #38bdf8; }
    """
) as app:
    
    gr.Markdown("# 🩺 PlexusAI - Vision & Voice Doctor")
    gr.Markdown("### Speak, show, and get an instant medical opinion.")

    with gr.Row():
        with gr.Column(scale=1):
            audio_input = gr.Audio(sources=["microphone"], type="filepath", label="🎙️ Record your symptoms")
            image_input = gr.Image(type="filepath", label="🩻 Upload or drop a medical image")
            submit_btn = gr.Button("🧠 Analyze", variant="primary")
        
        with gr.Column(scale=1):
            speech_output = gr.Textbox(label="🗣️ Speech to Text", interactive=False)
            doctor_output = gr.Textbox(label="💬 Doctor's Response", interactive=False)
            voice_output = gr.Audio(label="🎧 Doctor's Voice", type="filepath")

    submit_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[speech_output, doctor_output, voice_output]
    )

app.launch(debug=True)


