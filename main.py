import sys
import threading
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import tempfile
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QTextEdit, QLabel)
from PyQt6.QtCore import Qt, pyqtSignal, QObject
from PyQt6.QtGui import QFont

from faster_whisper import WhisperModel
import ollama

class WorkerSignals(QObject):
    status_update = pyqtSignal(str)
    transcription_complete = pyqtSignal(str)
    summary_complete = pyqtSignal(str)
    finished = pyqtSignal()

class MeetScribeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MeetScribe: Local AI Meeting Intelligence")
        self.setMinimumSize(800, 600)
        
        self.is_recording = False
        self.audio_data = []
        self.sample_rate = 16000
        self.stream = None
        
        self.signals = WorkerSignals()
        self.signals.status_update.connect(self.update_status)
        self.signals.transcription_complete.connect(self.show_transcription)
        self.signals.summary_complete.connect(self.show_summary)
        self.signals.finished.connect(self.reset_ui)
        
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("MeetScribe")
        header.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)
        
        subtitle = QLabel("100% Offline AI Meeting Summarizer (Built for Snapdragon)")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle)
        
        # Buttons
        btn_layout = QHBoxLayout()
        
        self.btn_start = QPushButton("🔴 Start Meeting")
        self.btn_start.setMinimumHeight(50)
        self.btn_start.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; font-size: 16px;")
        self.btn_start.clicked.connect(self.start_recording)
        
        self.btn_stop = QPushButton("⏹️ End Meeting & Summarize")
        self.btn_stop.setMinimumHeight(50)
        self.btn_stop.setStyleSheet("background-color: #f44336; color: white; font-weight: bold; font-size: 16px;")
        self.btn_stop.setEnabled(False)
        self.btn_stop.clicked.connect(self.stop_recording)
        
        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_stop)
        layout.addLayout(btn_layout)
        
        # Status
        self.lbl_status = QLabel("Ready.")
        self.lbl_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_status.setStyleSheet("color: #555; font-style: italic; font-size: 14px;")
        layout.addWidget(self.lbl_status)
        
        # Output Areas
        self.txt_transcript = QTextEdit()
        self.txt_transcript.setReadOnly(True)
        self.txt_transcript.setPlaceholderText("Transcription will appear here...")
        layout.addWidget(QLabel("📝 Transcript:"))
        layout.addWidget(self.txt_transcript)
        
        self.txt_summary = QTextEdit()
        self.txt_summary.setReadOnly(True)
        self.txt_summary.setPlaceholderText("AI Summary and Action Items will appear here...")
        layout.addWidget(QLabel("✨ AI Summary & Action Items (via Llama 3):"))
        layout.addWidget(self.txt_summary)
        
        central_widget.setLayout(layout)

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.audio_data.append(indata.copy())

    def start_recording(self):
        self.is_recording = True
        self.audio_data = []
        self.txt_transcript.clear()
        self.txt_summary.clear()
        
        self.btn_start.setEnabled(False)
        self.btn_stop.setEnabled(True)
        self.update_status("🔴 Recording meeting... (Speak now)")
        
        self.stream = sd.InputStream(samplerate=self.sample_rate, channels=1, callback=self.audio_callback)
        self.stream.start()

    def stop_recording(self):
        self.is_recording = False
        self.btn_stop.setEnabled(False)
        self.update_status("⏹️ Recording stopped. Processing audio...")
        
        if self.stream:
            self.stream.stop()
            self.stream.close()
            
        # Run AI processing in background thread
        threading.Thread(target=self.process_audio, daemon=True).start()

    def process_audio(self):
        try:
            # 1. Save audio to temp file
            self.signals.status_update.emit("Saving audio data...")
            audio_np = np.concatenate(self.audio_data, axis=0)
            
            temp_dir = tempfile.gettempdir()
            wav_path = os.path.join(temp_dir, "meetscribe_audio.wav")
            write(wav_path, self.sample_rate, audio_np)
            
            # 2. Transcribe
            self.signals.status_update.emit("Transcribing audio using Whisper...")
            model = WhisperModel("base", device="cpu", compute_type="int8")
            segments, info = model.transcribe(wav_path, beam_size=5)
            
            transcript_text = ""
            for segment in segments:
                transcript_text += segment.text + " "
                
            self.signals.transcription_complete.emit(transcript_text.strip())
            
            if not transcript_text.strip():
                self.signals.status_update.emit("No audio detected.")
                self.signals.finished.emit()
                return

            # 3. Summarize using local Ollama (Llama 3)
            self.signals.status_update.emit("Generating summary using Llama 3...")
            prompt = f"""
            You are an AI meeting assistant. Below is the transcript of a meeting.
            Please provide:
            1. A brief summary of the meeting.
            2. A bulleted list of Action Items (who needs to do what).
            
            Transcript:
            {transcript_text}
            """
            
            response = ollama.chat(model='llama3', messages=[
                {'role': 'user', 'content': prompt}
            ])
            
            summary = response['message']['content']
            self.signals.summary_complete.emit(summary)
            self.signals.status_update.emit("✅ Processing complete.")
            
        except Exception as e:
            self.signals.status_update.emit(f"Error: {str(e)}")
        finally:
            self.signals.finished.emit()

    def update_status(self, text):
        self.lbl_status.setText(text)

    def show_transcription(self, text):
        self.txt_transcript.setPlainText(text)

    def show_summary(self, text):
        self.txt_summary.setPlainText(text)

    def reset_ui(self):
        self.btn_start.setEnabled(True)

def main():
    app = QApplication(sys.argv)
    window = MeetScribeApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
