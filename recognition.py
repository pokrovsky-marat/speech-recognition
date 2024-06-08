#Перед тем как начать использовать программу не забудь установить:
#pip install SpeechRecognition pyperclip PyAudio

import speech_recognition as sr
#Для сохранения в клипборд
import pyperclip
#Для дачи звукового сигнала
import winsound

# Инициализация распознавателя
recognizer = sr.Recognizer()
# Звуковой сигнал перед началом записи
# Функция распознавания речи
def recognize_speech():
    with sr.Microphone() as source:
        #winsound.Beep(frequency, duration) После сигнала начинается запись
        winsound.Beep(400, 200)
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Распознаю...")
        # Используем русское API Google для распознавания речи
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Вы сказали:", text)     
        #Сохраняем расшифровку в клипборд
        pyperclip.copy(text)
        #Даем сигнал что запись закончена
        winsound.Beep(400, 200)
    except sr.UnknownValueError:
        print("Не удалось распознать аудио")
        winsound.Beep(400, 200)
        winsound.Beep(400, 200)
    except sr.RequestError as e:
        print("Ошибка при получении результатов от службы распознавания речи Google; {0}".format(e))
        winsound.Beep(400, 200)
        winsound.Beep(400, 200)
        winsound.Beep(400, 200)
# Вызов функции распознавания речи
recognize_speech()






