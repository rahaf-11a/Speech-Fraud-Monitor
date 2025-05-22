
## Project Description

This project is a simple desktop application that captures speech from the microphone, converts it to text using the Google Speech Recognition service, and then scans the text for keywords indicating potential financial fraud. If any of these keywords are detected, the application alerts the user; otherwise, it confirms that the call is normal.

The interface is built with Tkinter, and the code adjusts the audio sensitivity before listening. It also handles errors such as unclear speech or failure to connect to Google’s service.

## Features

- Real-time speech recognition from microphone input  
- Detection of potential financial fraud keywords  
- User alerts through pop-up messages  
- Simple and user-friendly graphical interface with Tkinter

## Requirements

- Python 3.x  
- speech_recognition library  
- tkinter (usually included with Python)  
- internet connection for Google Speech Recognition API

## How to Run

1. Install the required libraries if not already installed:  
   ```bash
   pip install SpeechRecognition
