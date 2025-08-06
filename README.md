# 🤖 JoJo – Your Personal AI-Powered Virtual Assistant

JoJo is a Python-based voice-activated virtual assistant that can do everything from playing YouTube videos and setting alarms to sending WhatsApp messages, telling jokes, calculating expressions, and more. It's a versatile project combining **NLP, web APIs, automation, and AI integration**.

---

## 🎯 Features

- 🎙️ Voice command recognition using `speech_recognition`
- 🔊 Natural voice output with `pyttsx3`
- 📺 Play videos on YouTube
- ⏰ Set alarms and reminders
- 🌡️ Fetch temperature info using live Google search
- 🧮 Ask mathematical questions (via WolframAlpha API)
- 😂 Get jokes using `pyjokes`
- 📸 Take screenshots with `pyautogui`
- 💬 Send WhatsApp messages using `pywhatkit`
- 📍 Open maps and search locations
- 📚 Get Wikipedia summaries
- 🕰️ Report current time and system info
- 🔐 Modular voice command loop with expansion capabilities

---

## 🛠️ Tech Stack

| Category            | Libraries/Tools                                                                 |
|---------------------|----------------------------------------------------------------------------------|
| Core Language       | Python 3                                                                         |
| Voice Input         | `speech_recognition`, `pyaudio`                                                  |
| Voice Output        | `pyttsx3`                                                                         |
| APIs                | `wikipedia`, `wolframalpha`, `pywhatkit`, `OpenWeather`, `requests`, `Twilio`   |
| Web Parsing         | `BeautifulSoup`                                                                  |
| Automation          | `pyautogui`, `os`, `webbrowser`, `datetime`                                      |
| Entertainment       | `pyjokes`, `instaloader`, `cv2`, `pygame`                                        |

---

## 📷 Demo Screenshot / Video  
> *(Add a screenshot or video of JoJo running in the terminal here)*

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.7 or higher
- Working microphone and speakers
- Internet connection (for APIs and online searches)

### 🧪 Installation

```bash
git clone https://github.com/yourusername/jojo-virtual-assistant.git
cd jojo-virtual-assistant
pip install -r requirements.txt
