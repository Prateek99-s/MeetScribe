# MeetScribe: Offline AI Meeting Intelligence
**Snapdragon® AI Lab Build & Present Challenge**

## 1. The Problem
In the modern corporate world, AI meeting tools are essential for productivity. However, existing solutions (like Otter.ai or built-in video conferencing AI) require uploading highly sensitive, confidential corporate audio to third-party cloud servers. For many enterprises, this is a severe privacy violation and a security risk.

## 2. The Solution: MeetScribe
MeetScribe is a 100% offline, privacy-first AI meeting assistant built specifically for Snapdragon-powered HP PCs. It acts as an always-on desktop application that records meeting audio, transcribes it, and generates intelligent summaries and action items—entirely on the edge.

Because no data ever leaves the local machine, enterprise workers can use MeetScribe for confidential meetings without violating data privacy policies.

## 3. How It Works (Technical Architecture)
MeetScribe leverages the massive AI compute capabilities (TOPS) of the Snapdragon architecture to run heavy machine learning workloads without draining the laptop's battery.
*   **Audio Capture:** The app captures microphone and system audio seamlessly in the background.
*   **Speech-to-Text:** It utilizes `faster-whisper` (based on OpenAI's Whisper model) to transcribe the audio locally with near real-time latency.
*   **Intelligence:** The raw transcript is passed into a locally running **Llama 3** Large Language Model (via Ollama). Llama 3 parses the conversation, understands context, and extracts a concise summary and a bulleted list of action items.

## 4. Alignment with Snapdragon & Qualcomm AI Hub
Running an Automatic Speech Recognition (ASR) model and a Large Language Model (LLM) simultaneously is traditionally impossible on standard laptop CPUs without severe thermal throttling and battery drain. 

By designing MeetScribe for the Snapdragon X Elite/Plus platform, we harness the power of the NPU to run these open-source models (compatible with Qualcomm AI Hub optimizations) highly efficiently. This proves that Snapdragon HP PCs are not just thin-and-light laptops, but powerful edge-AI workstations.
