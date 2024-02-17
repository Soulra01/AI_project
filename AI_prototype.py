import pyautogui as pau
import time
import speech_recognition as sr
from screen_brightness_control import set_brightness, get_brightness

def recognize_audio(device_index):
    recognizer = sr.Recognizer()
    
    with sr.Microphone(device_index=device_index) as source:
        print("Silakan mulai berbicara...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Mengenali teks...")
        text = recognizer.recognize_google(audio, language="id-ID")
        # print(f"Hasil: {text}")
    except sr.UnknownValueError:
        print("Maaf, tidak dapat mengenali suara.")
        text = 'none'
    except sr.RequestError as e:
        print(f"Terjadi kesalahan pada pengenalan suara: {e}")
        text = 'none'
    return text

def get_last_word(sentence):
    words = sentence.split()
    last_word = words[-1]
    return last_word

def get_first_word(sentence):
    words = sentence.split()
    first_word = words[0]
    return first_word


def pemilihan_kata(kata1,kata2):
    if kata1 == 'set':
        int(kata2)
        set_brightness(kata2)
        print('kecerahan layar:', get_brightness())
    else:
        print('ulangi perintah')
    


# new_brightness = input('Enter new brightness level: ') 

# print('Last brightness level:', get_brightness())
# set_brightness(new_brightness)

# current_brightness = get_brightness()
# print("Current screen brightness is:", current_brightness)

if __name__ == "__main__":
    while True:
        last = recognize_audio(5) # 0 is the default device index
        print(get_first_word(last) + ' ' + get_last_word(last))
        pemilihan_kata(get_first_word(last),get_last_word(last))

# cek
        