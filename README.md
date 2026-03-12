# 🎧 AI Call Analyzer

A powerful AI-driven tool that transcribes, diarizes, and analyzes customer support calls using Whisper + PyAnnote + Mistral-7B locally!

![Banner](https://img.shields.io/badge/LLM-Mistral%207B-purple?style=for-the-badge) ![Whisper](https://img.shields.io/badge/Transcription-Whisper-blue?style=for-the-badge) ![FastAPI](https://img.shields.io/badge/API-FastAPI-teal?style=for-the-badge)

---

## 🔍 Features

- 🎙️ **Speaker Diarization** – Identify who said what using PyAnnote.
- 📝 **Transcription** – Convert audio to text using Whisper.
- 🧠 **LLM Analysis** – Analyze conversation tone, category & generate summaries using Mistral-7B.
- 🎧 **Beautiful Frontend** – Upload `.wav` files and see the analysis in an aesthetic UI.
- 🖥️ **Runs Locally** – No external APIs needed (perfect for private data analysis).

---

## 🚀 How It Works

1. Upload a `.wav` call recording.
2. Backend transcribes it using Whisper.
3. Speakers are diarized via PyAnnote.
4. Local Mistral-7B analyzes the transcript and categorizes the call.
5. Results are shown beautifully on the web interface.

---

## 💻 Tech Stack

- 🧠 Mistral-7B (via `ctransformers`)
- 🔊 Whisper (OpenAI)
- 🗣️ PyAnnote (Speaker Diarization)
- ⚡ FastAPI
- 🌐 HTML + CSS + JS (with Lottie animations!)

---

## 🛠️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/rizzlingDuck/ai-call-analyzer.git
   cd ai-call-analyzer
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn python-multipart openai-whisper ctransformers pyannote.audio
   ```

3. Download the Mistral-7B GGUF model and place it in `models/`:
   ```
   models/mistral-7b-instruct-v0.1.Q4_K_M.gguf
   ```

4. Set your HuggingFace token and run:
   ```bash
   export HF_TOKEN="your_huggingface_token"
   uvicorn main:app --reload
   ```

5. Open `http://127.0.0.1:8000` in your browser.

---

## 📄 License

MIT
