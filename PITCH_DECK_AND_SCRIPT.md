# MeetScribe: Pitch Deck & Video Script

## 📊 Presentation Deck (5 Slides)

**Slide 1: The Problem**
*   **Title:** The Corporate Privacy Nightmare
*   **Points:**
    *   AI meeting tools are incredibly useful for productivity.
    *   However, 99% of them (Otter.ai, Fireflies, Zoom AI) upload sensitive corporate audio to the cloud.
    *   Enterprises forbid uploading confidential meetings to third-party servers.

**Slide 2: The Solution - MeetScribe**
*   **Title:** MeetScribe: 100% Offline AI Intelligence
*   **Points:**
    *   A desktop app built specifically for Snapdragon-powered HP PCs.
    *   Captures audio, transcribes it, and generates action items—**entirely locally**.
    *   No internet connection required. Absolute privacy.

**Slide 3: Why Snapdragon & HP?**
*   **Title:** Unlocking the NPU
*   **Points:**
    *   Running dual AI models (Speech-to-Text + Large Language Model) traditionally melts laptop batteries.
    *   By leveraging the **Snapdragon X Elite/Plus platform**, we can run these complex inference tasks efficiently at the edge.
    *   Perfect synergy with HP's enterprise-focused Omnibook lineup.

**Slide 4: Technical Architecture**
*   **Title:** Under the Hood
*   **Points:**
    *   **Audio Capture:** Direct microphone/system audio piping.
    *   **Transcription:** `faster-whisper` (Whisper Base) for near real-time, low-latency speech recognition.
    *   **Intelligence:** `Llama 3 8B` (via Ollama) processes the raw text to extract high-quality summaries and action items locally.

**Slide 5: Future Roadmap**
*   **Title:** Next Steps
*   **Points:**
    *   Deeper integration with Qualcomm AI Hub SDK for maximum NPU TOPS utilization.
    *   Speaker diarization (detecting *who* is speaking).
    *   Auto-drafting emails in Outlook based on action items.

---

## 🎬 2-Minute Demo Video Script

**[0:00 - 0:15] Intro & Hook**
*(Camera on you, holding or sitting at your HP laptop)*
> "Hi, I'm [Your Name]. Enterprise workers love AI meeting summaries, but they hate sending confidential company audio to the cloud. So, I built **MeetScribe**—a 100% offline AI meeting assistant powered by the Snapdragon NPU on this HP PC."

**[0:15 - 0:45] The Live Demo**
*(Screen recording of the MeetScribe app)*
> "Let's do a live test. I'm completely disconnected from the internet. I click 'Start Meeting'."
> *(Speak clearly into the mic)*
> "Hey team, great quarter. Next week, Sarah, please finalize the Q3 marketing budget. John, I need you to push the code update by Friday. Let's get this done."
> "Now, I click 'End & Summarize'."

**[0:45 - 1:15] The AI Magic**
*(Zoom in on the UI as text populates)*
> "Instantly, the audio is processed locally using the Whisper AI model to generate the transcript. Then, that transcript is fed into a locally running Llama 3 model which extracts a clean summary and bulleted action items for Sarah and John."

**[1:15 - 2:00] The Value Proposition & Outro**
*(Camera back on you)*
> "Running an LLM and an audio transcription model simultaneously usually destroys battery life. But because this is built for the Snapdragon architecture, it runs flawlessly and efficiently on the edge. This is the future of enterprise privacy on HP PCs. Thank you."
