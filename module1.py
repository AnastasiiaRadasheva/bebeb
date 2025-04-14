

#     create_dictionary() - создает словарь из трех языков

#  search_dictionary() - ищет слово на любом языке и показывает другие переводы

#  add_dictionary() - добавляет новое слово в три языка

#  correct_dictionary() - исправляет существующее слово

#  display_dictionary() - отображает весь словарь

#  select_languages_dictionary() - спрашивает у пользователя, с какого языка на какой он хочет перевести

#  test_knowledge() - проверка знаний с помощью случайных слов

#  display_result() - отображение конечного результата теста

#  ask_user_speech() - запрос ввода и проверка на пустоту

#  text_to_speech() - произнесение слова громким голосом

#  display_menu() - отображение меню и руководство пользователя

#  select_explanation() - программа приветствует пользователя в начале теста

# Переведено с помощью DeepL.com (бесплатная версия)
#1
def create_dictionary():
    est = ['koer', 'kass', 'maja', 'auto', 'päike']
    rus = ['собака', 'кошка', 'дом', 'машина', 'солнце']
    eng = ['dog', 'cat', 'house', 'car', 'sun']
    sonastik = []
    for e, r, g in zip(est, rus, eng):
        sonastik.append({'est': e, 'rus': r, 'eng': g})
    return sonastik
#2
def search_dictionary(dictionary, word):
   for entry in dictionary:
        if word in entry.values():
            return entry
   return None
#3
def add_dictionary(dictionary, est_word, rus_word, eng_word):
    new_entry = {'est': est_word, 'rus': rus_word, 'eng': eng_word}
    dictionary.append(new_entry)
    return dictionary
#4
def correct_dictionary(dictionary, word, new_word):
    for entry in dictionary:
        if word in entry.values():
            entry['est'] = new_word
            return dictionary
    return None
#5
def display_dictionary(dictionary):
    print(Entry)
#6
def select_languages_dictionary():
    languages = ['est', 'rus', 'eng']
    print("Available languages:")
    for i, lang in enumerate(languages):
        print(f"{i + 1}. {lang}")
    choice = int(input("Select a language (1-3): "))
    return languages[choice - 1]
#7
def test_knowledge():
    dictionary = create_dictionary()
    score = 0
    for entry in dictionary:
        print(f"Translate '{entry['est']}' to Russian:")
        answer = input("Your answer: ")
        if answer.lower() == entry['rus']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is '{entry['rus']}'")
    return score
#8
def display_result(score, total):
    print(f"Your score: {score}/{total}")
    if score == total:
        print("Excellent!")
    elif score >= total / 2:
        print("Good job!")
    else:
        print("Keep practicing!")
#10
def text_to_speech(word):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()
#11
def kuva_menuu():
    print("Tere tulemast sõnastiku programmi!")
    print("1. Otsi sõna")
    print("2. Lisa uus sõna")
    print("3. Paranda sõna")
    print("4. Kuvage kogu sõnastik")
    print("5. Testi teadmisi")
    print("6. Kuula sõna hääldust")
    print("7. Välju")


def main():
    sonad = sonastik.loo_sonastik()
    
    while True:
        kuva_menuu()
        valik = input("Sisesta oma valik: ").strip()
        
        if valik == '1':
            allikas, siht = vali_keelte_suund()
            sona = input(f"Sisesta sõna ({allikas} -> {siht}): ").strip().lower()
            tulemus = sonastik.tolkija(sonad, allikas, siht, sona)
            print(f"Tõlge: {tulemus}")
        
        elif valik == '2':
            sonastik.lisa_sona(sonad)
        
        elif valik == '3':
            sonastik.paranda_sona(sonad)
        
        elif valik == '4':
            sonastik.kuva_sonad(sonad)
        
        elif valik == '5':
            sonastik.testi_teadmisi(sonad)
        
        elif valik == '6':
            sona = input("Sisesta sõna, mida soovid kuulda: ").strip().lower()
            sonastik.text_to_speech(sona)
        
        elif valik == '7':
            print("Head aega!")
            break
        
        else:
            print("Vale valik, proovige uuesti!")


def select_explanation():
    print("Tere tulemast sõnastiku programmi!")
    print("See programm aitab teil õppida kolme keele sõnavara.")
    print("Valige menüüst soovitud tegevus.")
    print("Sõnastik sisaldab eesti, vene ja inglise keelt.")
    print("Loodame, et naudite õppimist!")

def main1():
    sonad = create_dictionary()
    
    while True:
        kuva_menuu()
        valik = input("Sisesta oma valik: ").strip()
        
        if valik == '1':
            word = input("Sisesta sõna (eesti, vene või inglise keeles): ").strip().lower()
            result = search_dictionary(sonad, word)
            if result:
                print(f"Tõlge: {result}")
            else:
                print("Sõna ei leitud!")
        
        elif valik == '2':
            est_word = input("Sisesta eesti sõna: ").strip().lower()
            rus_word = input("Sisesta vene sõna: ").strip().lower()
            eng_word = input("Sisesta ingliskeelne sõna: ").strip().lower()
            sonad = add_dictionary(sonad, est_word, rus_word, eng_word)
            print("Sõna on lisatud!")
        
        elif valik == '3':
            word = input("Sisesta sõna, mida soovid parandada: ").strip().lower()
            new_word = input("Sisesta uus eesti sõna: ").strip().lower()
            sonad = correct_dictionary(sonad, word, new_word)
            if sonad:
                print("Sõna on parandatud!")
            else:
                print("Sõna ei leitud!")
        
        elif valik == '4':
            display_dictionary(sonad)
        
        elif valik == '5':
            score = test_knowledge(sonad)
            display_result(score, len(sonad))
        
        elif valik == '6':
            word = input("Sisesta sõna, mida soovid kuulda: ").strip().lower()
            text_to_speech(word)
        
        elif valik == '7':
            print("Head aega!")
            break
        
        else:
            print("Vale valik, proovige uuesti!")
