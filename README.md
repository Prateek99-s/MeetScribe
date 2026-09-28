# MeetScribe: Offline AI Meeting Intelligence

**Built for the Snapdragon® AI Lab Build & Present Challenge**

## Overview
Cloud-based meeting recorders compromise enterprise privacy and require expensive subscriptions. **MeetScribe** is a 100% offline, local AI meeting assistant built for Snapdragon-powered HP PCs. 

It captures your microphone audio during a meeting, transcribes it locally using **Whisper**, and then instantly generates a summary and action items using **Llama 3** (via Ollama). No internet required.

## Why it Wins
*   **Privacy-First:** All audio processing and language modeling happen on-device. Perfect for confidential corporate meetings on HP business laptops.
*   **Snapdragon Optimized:** Designed to leverage the power of local AI. It runs a speech-to-text pipeline and a Large Language Model (Llama 3) entirely locally, showcasing the massive compute capability of the Snapdragon X Elite/Plus platform.
*   **Enterprise Utility:** Solves a real, daily problem for PC users.

## Architecture
1.  **Audio Capture:** Uses `sounddevice` to capture microphone input.
2.  **Transcription Engine:** Uses `faster-whisper` (Whisper Base) to transcribe the audio into text quickly and efficiently.
3.  **Summarization Engine:** Uses the `ollama` Python library to pipe the transcript into a locally running **Llama 3** model, which extracts the summary and action items.
4.  **UI:** A clean, responsive PyQt6 interface.

## Installation

### 1. Install Ollama & Llama 3
MeetScribe uses Ollama to run Llama 3 locally.
1. Download Ollama from [ollama.com](https://ollama.com/) (if not already installed).
2. Open a terminal and run:
   ```bash
   ollama run llama3
   ```
   *This will download the Llama 3 model (approx. 4.7GB). You can close it once downloaded.*

### 2. Install Python Dependencies
```bash
# Clone or open the repository
cd MeetScribe

# Create a virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

## Running the Application

```bash
python main.py
```

1. Click **Start Meeting** and begin talking.
2. Click **End Meeting & Summarize**. 
3. Watch as the AI transcribes and summarizes your meeting in seconds, entirely offline.

*Developed with ❤️ in 32 Hours.*
