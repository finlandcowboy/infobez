
#* Вводим смещение (offset) и ключ (key)
offset = 3
key = 'приветик'


#* Записываем в result главу Войны и Мира
with open("warAndPeace.txt", encoding='utf-8') as text_file:
    result = ''
    for s in text_file:
        result += s


#* Генерируем русский алфавит
a = ord('а')
alphabet = ''.join([chr(i) for i in range(a, a+32)])

print('Алфавит:', alphabet, '\n')

#* Делаем ключ неуязвимым в пробелам
key = key.replace(' ', '')

#* удаляем из алфавита символы из ключа и добавляем вначало ключ на каждой итерации
for sym in key:
    alphabet = alphabet.replace(sym, '')
    alphabet = key + alphabet

#* Смещаем алфавит на offset
for i in range(offset):
    alphabet = alphabet[-1] + alphabet[:-1]

print('Новый алфавит:', alphabet, '\n')

text = ''

#* Если символ "алфавитный", то вычисляем его значение
for symbol in result:
    if symbol.isalpha():
        #* Вычисляем символ в алфавите
        text += alphabet[(ord(symbol) - 224) % 32]
    else:
        #* Просто добавляем символ
        text += symbol


if __name__ == "__main__":
    print(f"Результат шифрации\n{text}")
