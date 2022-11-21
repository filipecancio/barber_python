import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from nltk import word_tokenize, corpus
import json
import nltk
nltk.download('stopwords')
nltk.download('punkt')

def get_data_settings():
    global microphone
    global stop_word
    global asisstent_name
    global action_list

    microphone = sr.Recognizer()
    stop_word = set(corpus.stopwords.words("portuguese"))

    with open("database.json", "r") as settings_file:
        settings = json.load(settings_file)

        asisstent_name = settings["name"]
        action_list = settings["action_list"]

        settings_file.close()

    

def hear_voice():
    global microphone

    phrase = None

    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)

        frase = 'Diga alguma coisa: '
        print(frase)
        audio = microphone.listen(source, timeout=5, phrase_time_limit=5)
        
        try:
            phrase = microphone.recognize_google(audio,language='pt-BR')
        except Exception as e:
            pass

    return phrase

def hear_audio(audio):
    global microphone

    command = None

    with sr.AudioFile(audio) as source:
        fala = microphone.listen(source)
        try:
            command = microphone.recognize_google(fala, language='pt-BR')
        except Exception as e:
            pass

    return command

def remove_stop_word(phrase):
    global stop_word

    token_list = []
    
    for token in phrase:
        if token not in stop_word:
            token_list.append(token)

    return token_list


def get_tokenized_command(phrase):
    global asisstent_name

    action = None
    target = None

    token_phrase = word_tokenize(phrase, 'portuguese')
    if token_phrase:
        token_phrase = remove_stop_word(token_phrase)

        if len(token_phrase) >= 3:
            if asisstent_name == token_phrase[0].lower():
                action = token_phrase[1].lower()
                target = token_phrase[2].lower()

    return action, target

def run_command(action,target):
    global action_list

    is_valid = False

    if action and target:
        for item in action_list:
            if action == item["name"]:
                if target in item["target"]:
                    is_valid = True
                break

    return is_valid

def send_response(action,target):
    print()
    frase = f"ok vou executar o comando: {action} {target}"
    print(frase)
    cria_audio(frase)

#Funcao responsavel por falar 
def cria_audio(audio):
    tts = gTTS(audio,lang='pt-br')
    #Salva o arquivo de audio
    tts.save('hello.mp3')
    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    playsound('hello.mp3')

if __name__ == "__main__":
    get_data_settings()

    is_alive = True

    while is_alive:
        try:
            command = hear_voice()
            print(f"processando o comando: {command}")

            if command:
                acao, objeto = get_tokenized_command(command)
                valido = run_command(acao, objeto)
                if valido:
                    send_response(acao, objeto)
                else:
                    print("Não entendi o comando. Repita, por favor!")
        except KeyboardInterrupt:
            print("Tchau!")

            continuar = False
