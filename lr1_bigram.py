import re
from collections import Counter
import string


def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])


punc = string.punctuation + '\n\xa0«»\t—… '
not_chars = "!\"#$%&'()*+-./:;<=>?@[\]^_`{|}~" + "\xa0,\xa0"

Alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
FrequencyOfLetters = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё'


print("Дешифровка с помощью монограмм\n")



text = input('Введите текст: ')

key = input('Введите ключ шифрации: ')

text = (re.sub('[a-z|A-Z|A-Z|a-z]', '', text)).lower() # .strip()

book = remove_chars_from_text(text, punc)
book = remove_chars_from_text(text, string.digits)


bigrams_mono = Counter(re.findall(r'(?=([а-я]{2}))', text)).most_common(10) #подсчёт 10 самых популярных биграм в оригинальном тексте
print("Биграммы в оригинальном тексте: ")

print(bigrams_mono)
list_of_bigrams_mono = str(bigrams_mono)

list_of_bigrams_mono = remove_chars_from_text(list_of_bigrams_mono, string.digits)
list_of_bigrams_mono = remove_chars_from_text(list_of_bigrams_mono, not_chars).split()
        

from caesar_word import Caesar


caesar = Caesar(message=text, key=key)
new_text = caesar.encrypt()
new_text = (re.sub('[a-z|A-Z|A-Z|a-z]', '', text)).lower()

        

letters_decr = Counter("".join([ch for ch in new_text if ch in Alphabet])) #подсчёт частоты букв
print(letters_decr)
list_of_letters = list(letters_decr.items())
list_of_letters.sort(key=lambda i: i[1])
list_of_letters.reverse()
print(list_of_letters)

Message3 = []

list_of_letters = str(letters_decr)

list_of_letters = remove_chars_from_text(list_of_letters, punc)
list_of_letters = remove_chars_from_text(list_of_letters, string.digits)
list_of_letters = list_of_letters[7:]



with open('texts/monogram.txt', 'rt',encoding='utf8') as text_decrypted2:
            bigrams_mono = text_decrypted2.read()
            bigrams_mono = Counter(re.findall(r'(?=([а-я]{2}))', bigrams_mono)).most_common(10)
            for char_new in new_text:
                try:
                    index_new = list_of_letters.index(char_new)
                    new_char = FrequencyOfLetters[index_new]
                except ValueError:
                    Message3.append(char_new)
                    
            print("Биграммы в расшифрованном тексте с помощью монограмм: ")
            print(bigrams_mono)
            list_of_letters3 = str(bigrams_mono)
            list_of_letters3 = remove_chars_from_text(list_of_letters3, string.digits)
            list_of_letters3 = remove_chars_from_text(list_of_letters3, not_chars).split()
            print(list_of_letters3)

FrequencyOfLettersUpd = FrequencyOfLetters
FrequencyOfLettersUpd = list(FrequencyOfLettersUpd)

for a in range(len(list_of_letters3)):
            if list_of_letters3[a] != list_of_bigrams_mono[a]:
                x = list_of_letters3[a]
                y = list_of_bigrams_mono[a]

                if x[0] != y[0]:
                    index1 = FrequencyOfLetters.index(x[0])
                    FrequencyOfLettersUpd[index1] = y[0]
                    index11 = FrequencyOfLetters.index(y[0])
                    FrequencyOfLettersUpd[index11] = x[0]
                if x[1] != y[1]:
                    index2 = FrequencyOfLetters.index(x[1])
                    FrequencyOfLettersUpd[index2] = y[1]
                    index22 = FrequencyOfLetters.index(x[1])
                    FrequencyOfLettersUpd[index22] = y[1]
                


q = open('texts/monogram.txt', 'r',encoding='utf8')
qq = q.read()
Message4 = []
with open('texts/bigram.txt', 'wt',encoding='utf8') as text_decrypted3:

            for charr in qq:
                try:
                    index1 = FrequencyOfLetters.index(charr)
                    index2 = FrequencyOfLettersUpd.index(charr)
                    if index1 != index2:
                        character2 = FrequencyOfLettersUpd[index1]
                        Message4.append(character2)
                    else:
                        Message4.append(charr)
                except ValueError:
                    Message4.append(charr)

            text_decrypted3.write(''.join(Message4))

text_original.close()
text_encrypted.close()
text_decrypted2.close()
text_decrypted3.close()