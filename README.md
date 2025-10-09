🩺 PlexusAI — The Multimodal AI Doctor
💡 Overview
PlexusAI is an experimental AI-powered multimodal medical assistant that listens, sees, and speaks like a real doctor.
It combines audio, vision, and language understanding into one seamless interface — built for learning and demonstration purposes only.
⚙️ Core Features
🧠 Multimodal Intelligence — Accepts both voice and image inputs.
🗣️ Voice Understanding (Groq + Whisper) — Converts patient speech to text using Groq’s Whisper large-v3 model, enabling fast and accurate transcription.
👁️ Visual Diagnosis (LLaMA Vision) — Analyzes uploaded medical images via Meta LLaMA-4 Vision (Scout 17B) to simulate a medical opinion.
🧏 Doctor-Like Reasoning — Generates a natural, human-like diagnostic response with brief explanations and suggested remedies.
🔊 Voice Output (ElevenLabs) — Converts the AI doctor’s response back into lifelike speech using ElevenLabs TTS.
Interactive Gradio UI — A simple yet elegant web interface that lets users talk, upload, and hear results instantly.
## Tech Stack
Component	Technology
Speech-to-Text	Groq API (Whisper Large v3)
Vision + Language Model	Meta LLaMA-4 Scout-17B-16E-Instruct
Text-to-Speech	ElevenLabs API
Interface	Gradio
Environment Management	Python + dotenv
🚀 How It Works
🎙️ The user records their voice describing symptoms.
🩻 The user uploads a medical image (e.g., skin rash, X-ray).
⚗️ The model analyzes both inputs using Groq (for STT) and LLaMA-4 Vision (for image reasoning).
🩺 PlexusAI generates a professional doctor-like response — short, conversational, and informative.
🔊 Finally, ElevenLabs TTS delivers the answer in natural voice.
