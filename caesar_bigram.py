import re
from itertools import islice
from collections import Counter


def caeser_cipher(text, shift):
    alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ''
    text = text.upper()

    for i in text:
        place = alphabet_RU.find(i)
        new_place = place + shift
        if i in alphabet_RU:
            result += alphabet_RU[new_place]
        else:
            result += i
            
    return result


def make_monogram(message, text):
    #* Подсчитываем монограммы в исходном тексте
    mt = re.findall("\w{1}", text)
    moncounter = Counter(islice(mt, 1, None))
    #print(monr.most_common())
    #* Подсчитываем монограммы в зашифрованном тексте
    mt = re.findall("\w{1}", message)
    s_morcounter = Counter(islice(mt, 1, None))
    for i, y in zip(s_morcounter.most_common(), moncounter.most_common()):
        message = message.replace(i[0], y[0])

    return message


def make_bigram(message, text):
    #* Подсчитываем биграммы в исходном тексте
    mt = re.findall("\w{2}", text)
    bigr = Counter(islice(mt, 1, None))

    #* Подсчитываем биграммы в зашифрованном тексте
    mt = re.findall("\w{2}", message)
    s_bigr = Counter(islice(mt, 1, None))
    #print(s_bigr.most_common())
    for i, y in zip(s_bigr.most_common(), bigr.most_common()):
        message = message.replace(i[0], y[0])

    return message


if __name__ == "__main__":

    #! Считываем главу
    with open("warAndPeace.txt", encoding='utf-8') as text_file:
        result = ''
        for line in text_file:
            result += line


    result = result.upper()
    cipher = caeser_cipher(result, 5)
    m = make_monogram(cipher, result)
    b = make_bigram(cipher, result)
    print("\n\n")
    print('Шифр цезаря: ')
    print(cipher)
    print('\n\n')
    print('Монограммы: ')
    print(m)
    print('\n\n')
    print('Биграммы: ')
    print(b)
