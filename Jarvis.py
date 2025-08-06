import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import cv2
import requests
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys
import time
from bs4 import BeautifulSoup
import pyautogui
import pyjokes
import pygame
import wolframalpha
from pywikihow import search_wikihow
import instaloader
from twilio.rest import Client

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)

# Wolfram Alpha API for calculations
app = wolframalpha.Client("UHLRPR-T85W5GRV6T")

# Speak function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Greeting function
def wish():
    hour = int(datetime.datetime.now().hour)
    speak("System initializing, Successfully connected to the satellite")
    
    if hour < 12:
        speak("Good morning sir")
    elif hour < 18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")

    speak("I am Jojo, Heavily programmed by Takki. Please tell me how I can assist you.")

# Voice recognition function
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2  
        r.energy_threshold = 300  
        try:
            audio = r.listen(source, timeout=8, phrase_time_limit=15)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
            return "none"
        except sr.UnknownValueError:
            print("Could not understand the audio. Please speak clearly.")
            return "none"
        except sr.RequestError:
            print("Could not request results, please check your internet connection.")
            return "none"

# Play YouTube video
def play_on_youtube():
    speak("What would you like to play on YouTube?")
    video_query = takecommand()
    if video_query != "none":
        speak(f"Playing {video_query} on YouTube")
        pywhatkit.playonyt(video_query)
    else:
        speak("I didn't catch that. Please try again.")

# Set and trigger alarm
def set_alarm():
    global alarm_time
    speak("For what time should I set the alarm? Format: HH:MM AM/PM")
    alarm_time = takecommand().strip()

    if alarm_time:  
        speak(f"Alarm set for {alarm_time}")
        while True:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            if current_time == alarm_time:
                speak("Time to wake up!")
                os.startfile("C:\\Users\\Dell\\Downloads\\twirling-intime-lenovo-k8-note-alarm-tone-41440.mp3")  # Add your alarm sound file
                break
            time.sleep(30)  # Reduce CPU usage

# Execute tasks based on voice command
def TaskExecution():
    global alarm_time
    alarm_time = None  # Initialize alarm_time to avoid UnboundLocalError
    
    wish()
    
    while True:
        query = takecommand()
        
        if query == "none":
            continue  

        if "open notepad" in query:
            os.startfile("C:\\WINDOWS\\system32\\notepad.exe")
        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")
            speak("Notepad has been closed.")
        elif "what can you do" in query:
            speak("I can do a lot of things, such as telling time, date, weather, sending emails, and launching applications.")
        elif "how are you" in query:
            speak("I am fine. How can I assist you, sir?")
        elif "thank you" in query:
            speak("It's my pleasure, sir. Always ready to help.")
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")
            speak("Command Prompt has been closed.")
        elif "open whatsapp" in query:
            speak("Opening WhatsApp")
            os.system("start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
        elif "temperature" in query:
            speak("Please tell me the city name.")
            city = takecommand()
            if city != "none":
                search = f"temperature in {city}"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp_data = data.find("div", class_="BNeawe iBp4i AP7Wnd")
                if temp_data:
                    temp = temp_data.text
                    speak(f"The current temperature in {city} is {temp}")
                else:
                    speak("Sorry, I couldn't fetch the temperature data.")
        elif "open file explorer" in query:
            os.system("explorer")
        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")
        elif "find location" in query:
            speak("Please tell me the location")
            location = takecommand()
            webbrowser.open(f"https://www.google.com/maps/place/{location}")
        elif "set a reminder" in query:
            speak("What should I remind you about?")
            reminder_text = takecommand()
            speak("In how many minutes should I remind you?") 
            minutes = int(takecommand())
            time.sleep(minutes * 60)
            speak(f"Reminder: {reminder_text}")
        elif "take screenshot" in query:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            speak("Screenshot saved successfully.")
        elif "set alarm" in query:
            set_alarm()  
        elif "send whatsapp message" in query:
            contacts = {
                "raj": "919321380693",
                 "Ali": "918104831507",
                "fardeen": "919372556055"
            }  

            speak("To whom should I send the message?")
            contact_name = takecommand().lower()

            if contact_name in contacts:
                number = contacts[contact_name]
                speak("What is the message?")
                message = takecommand()

        # Send WhatsApp message
                pywhatkit.sendwhatmsg_instantly(f"+{number}", message)
                speak(f"Message sent successfully to {contact_name}.")

        # Close WhatsApp directly
                time.sleep(5)  # Ensure the message is sent before closing
                for process in psutil.process_iter():
                    try:
                        if "WhatsApp" in process.name():
                            process.terminate()
                        speak("WhatsApp has been closed successfully.")
                        break
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass

            else:
                speak("Sorry, I couldn't find that contact in your list.")

        elif "open google" in query:
            speak("Sir, what should I search on Google?")
            search_query = takecommand()
            if search_query != "none":
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif "calculate" in query:
            speak("What should I calculate?")
            calculation_query = takecommand()
            if calculation_query and calculation_query != "none":
                try:
                    res = app.query(calculation_query)
                    speak(next(res.results).text)
                except:
                    speak("Sorry, I couldn't process the calculation.")
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

if __name__ == "__main__":
    TaskExecution()
