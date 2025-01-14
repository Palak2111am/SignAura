import speech_recognition as sr
import pyttsx3
from PIL import Image
import os

r = sr.Recognizer()


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

word_to_image = {
    "સફરજન": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/apple.jpg",  # Apple
    "કેળુ": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/banana.jpeg",# Banana
    "કેળું": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/banana.jpeg",
    "બિલાડી": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/cat.jpeg",    # Cat
    "કૂતરો": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/dog.jpeg",
    "કુતરો": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/dog.jpeg", # Dog
    # Gujarati Numbers
    "એક":  "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/one.jpg",
    "બે":  "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/two.jpg",
    "ત્રણ": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/three.jpg",
    "ચાર": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/four.jpg",
    "પાંચ": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/five.jpg",
    "પાચ": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/five.jpg",
    "છ": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/six.jpg",
    "સાત": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/seven.jpg",
    "આઠ": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/eight.jpg",
    "નૌ": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/nine.jpg",
    "નવ": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/nine.jpg",
    "નાઉ": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/nine.jpg",
    "શૂન્ય": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/zero.jpg",
    "શુન્ય": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/zero.jpg",
    "શુંય": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/zero.jpg",
    "ક": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/ka.jpg",
    "ખ": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/kha.jpg",
    "ગ": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/ga.jpg",
    "ઘ": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/gha.jpg",
    "ચ": "D:/Krishna/SIGNAURA/SignAura/Speech To Text/images/cha.jpg"
}

def display_image(word):
    if word in word_to_image:
        image_path = word_to_image[word]
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img.show()
        else:
            print(f"Image for {word} not found at {image_path}")
    else:
        print(f"No image mapped for word: {word}")


def log_recognized_text(text):
    with open("recognized_text.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n")


while True:
    try:

        with sr.Microphone() as source2:
            print("Adjusting for ambient noise... Please wait.")
            r.adjust_for_ambient_noise(source2, duration=1)

            print("Listening...")
            audio2 = r.listen(source2)

            print("Recognizing speech...")
            MyText = r.recognize_google(audio2, language='gu-IN')
            MyText = MyText.lower()

            log_recognized_text(MyText)

            print(f"Recognized Text (logged to file): {MyText.encode('utf-8')}")

            SpeakText(MyText)

            words = MyText.split()

            for word in words:
                display_image(word)

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")