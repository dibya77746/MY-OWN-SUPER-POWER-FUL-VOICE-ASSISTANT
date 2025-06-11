import speech_recognition as sr
import pyttsx3
import webbrowser  # <-- Add this import

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except Exception as e:
        print("Sorry, I did not catch that.")
        return ""

if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you? hey dibya say how are you")
    while True:
        command = listen()
        
        if "hello" in command:
            speak("Hello! How are you? dibya, iam robo 2.0" )
        elif "your name" in command:
            speak("I am your jarvis voice assistant.")
            if "tell me about your self " in command:
                speak("I am just a program, but thank you for asking!")
                if "are u a robot" in command:
                    speak("Yes, I am a robot designed to assist you.")
        elif "what is your name" in command:
            speak("My name is Jarvis, your voice assistant.")
        elif "what can you do" in command:
            speak("I can assist you with various tasks, answer questions, and provide information.")
        if "tell me a joke" in command:
            speak("Why don't scientists trust atoms? Because they make up everything!")
        elif "play music" in command:
            speak("Sure! Playing your favorite music.")
            
        elif "open youtube" in command:  # <-- Add this block
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")
        elif "open website" in command: 
            speak("Please tell me the name of the website you want to open.")
        elif "search" in command:
            speak("What would you like to search for?")
           
            speak("I am just a program, but thank you for asking! How can I assist you today?")
        elif "who are you" in command:
            speak("I am Jarvis, your voice assistant. Here to help you with anything you need.")
        elif "help" in command:
            speak("I can assist you with various tasks like searching the web, playing music, and answering questions.")
        elif "tell me about yourself" in command:
            speak("I am a voice assistant designed to help you with your daily tasks and provide information.")
        elif "tell me a story" in command:
            speak("Once upon a time, in a land far away, there lived a wise old owl who knew all the secrets of the forest. One day, a curious little mouse asked the owl for advice on how to find happiness. The owl replied, 'Happiness is not found in things, but in the moments we share with others.' And from that day on, the mouse made it a point to cherish every moment with friends and family.")
        
        
            
        elif "thank you" in command:
            speak("You're welcome! If you need anything else, just let me know.")
            
        elif "goodbye" in command or "bye" in command:
            speak("Goodbye! Have a great day!")
            break
        elif "what time is it" in command:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}.")
        elif "what is the date" in command: 
            from datetime import datetime
            current_date = datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {current_date}.")
        elif "weather" in command:
            speak("Please tell me the city for which you want the weather information.")
        elif "set alarm" in command:
            speak("Please tell me the time for the alarm.")
        elif "reminder" in command:         
            speak("What would you like to be reminded about?")
            
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            if "exit" in command:
                speak("Exiting the program. Have a nice day!")
            break
        elif command:
            speak("You said: " + command)