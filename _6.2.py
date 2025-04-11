# dict.fromkeys(['a', 'd'], 100)
from module1 import *
est = ['koer', 'kass', 'maja', 'auto', 'päike']
rus = ['собака', 'кошка', 'дом', 'машина', 'солнце']
eng = ['dog', 'cat', 'house', 'car', 'sun']
sonastik = []
for e, r, g in zip(est, rus, eng):
    sonastik.append({'est': e, 'rus': r, 'eng': g})
valik = input('Vali keelekood: est, rus, eng: ')

main1()


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
