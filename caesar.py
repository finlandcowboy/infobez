import re
from collections import Counter
from itertools import islice


class Caesar:
    text: str = None
    shift: int = None
    
    def __init__(self, text, shift=0):
        self.alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.text = text.upper()
        self.shift = shift

    def encrypt(self):
        result = ''
        for char in self.text:
            idx = self.alphabet.find(char) + self.shift
            if char in self.alphabet:
                result += self.alphabet[idx]
            else:
                result += char

        return result

    def decrypt(self, result):
        decrypted = ''
        for char in result:
            idx = self.alphabet.find(char) - self.shift
            
            if char in self.alphabet:
                decrypted += self.alphabet[idx]

            else:
                decrypted += char

        return decrypted

    def grams(self, result, mono=1):
        if mono:
            monograms = list(self.text)
            monc = Counter(islice(monograms, 1, None))
            
            mres = re.findall("\w{1}", result)
            resc = Counter(islice(mres, 1, None))

            

            for i, y in zip(resc.most_common(), monc.most_common()):
                result = result.replace(i[0], y[0])

            return result
        
        else:
            monograms = re.findall("\w{2}", self.text)
            monc = Counter(islice(monograms, 1, None))
            
            mres = re.findall("\w{2}", result)
            resc = Counter(islice(mres, 1, None))


            for i, y in zip(resc.most_common(), monc.most_common()):
                result = result.replace(i[0], y[0])

            return result
            


if __name__ == '__main__':
    text = open('warAndPeace.txt', 'r', encoding='utf-8').read()

    # text = input('Введите текст\n')

    # text = 'привет как дела как дела'

    c = Caesar(text, shift=2)
    encrypted = c.encrypt()


    print(f'Расшифрока: {c.decrypt(encrypted)}')

    print('--------------------\n')

    print("Шифр Цезаря:", encrypted)
    print('--------------------')

    bi = c.grams(encrypted, mono=0)
    mono = c.grams(encrypted, mono=1)

    print('Монограммы:', mono)
    print('--------------------')
    print('Биграммы:', bi)
    print('--------------------')
