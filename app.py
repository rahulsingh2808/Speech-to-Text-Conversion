import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

class SpeechToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech to Text Converter")
        self.root.geometry("500x300")
        
        self.label = tk.Label(root, text="Press the button and start speaking", font=("Helvetica", 14))
        self.label.pack(pady=20)
        
        self.text_box = tk.Text(root, height=10, width=50, wrap='word', font=("Helvetica", 12))
        self.text_box.pack(pady=10)
        
        self.button = tk.Button(root, text="Start Recording", command=self.record_audio, font=("Helvetica", 14))
        self.button.pack(pady=20)
    
    def record_audio(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.label.config(text="Listening...")
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                self.text_box.insert(tk.END, text + "\n")
                self.label.config(text="Press the button and start speaking")
            except sr.UnknownValueError:
                messagebox.showerror("Error", "Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                messagebox.showerror("Error", f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechToTextApp(root)
    root.mainloop()
