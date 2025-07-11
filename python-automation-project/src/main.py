import speech_recognition as sr
import pyttsx3
from playsound3 import playsound
import os
import subprocess
import webbrowser
import urllib.parse
import time

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("How can I help you?")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def find_spotify():
    # Common install locations for Spotify on Windows
    possible_paths = [
        os.path.expandvars(r"%APPDATA%\Spotify\Spotify.exe"),
        os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WindowsApps\Spotify.exe"),
        os.path.expandvars(r"%PROGRAMFILES%\Spotify\Spotify.exe"),
        os.path.expandvars(r"%PROGRAMFILES(X86)%\Spotify\Spotify.exe"),
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    # Search entire C: drive (slow, but thorough)
    for root, dirs, files in os.walk("C:\\"):
        for file in files:
            if file.lower() == "spotify.exe":
                return os.path.join(root, file)
    return None

def play_song_on_spotify(song_name):
    spotify_path = find_spotify()
    if spotify_path:
        speak(f"Opening Spotify and searching for {song_name}.")
        subprocess.Popen([spotify_path])
        time.sleep(5)  # Give Spotify time to open
        query = urllib.parse.quote(song_name)
        webbrowser.open(f"https://open.spotify.com/search/{query}")
    else:
        speak("Spotify is not available. Opening the download page.")
        webbrowser.open("https://www.spotify.com/download/")

def main():
    command = listen()
    if command.startswith("play "):
        song_name = command.replace("play ", "", 1).strip()
        if song_name:
            play_song_on_spotify(song_name)
        else:
            speak("Please specify the song name.")
    else:
        speak("Command not recognized.")

if __name__ == "__main__":
    main()