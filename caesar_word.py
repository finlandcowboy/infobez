class Caesar():
    message: str = None
    key: str = None

    def __init__(self, message: str = "", key: str = ""):
        self.message = message
        self.key = key
        self._letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzабвгдеёжзикламнопрстуфхцчщъыьэюяАБВГДЕЁЖЗИКЛАМНОПРСТУФХЦЧЩЪЫЬЭЮЯ"
        self.index = 0

    def encrypt(self):
        translated_message = ''
        for char in self.message:
            if char in self._letters:
                number = self._letters.find(char)
                number += (ord(self.key[self.index]))

                self.index += 1
                self.index %= len(key)

                if number >= len(self._letters):
                    number -= len(self._letters)

                elif number < 0:
                    number += len(self._letters)

                translated_message += self._letters[number]

        else:
            translated_message += char
        
        return translated_message 

    def decrypt(self):
        translated_message = ''
        for char in self.message:
            if char in self._letters:
                number = self._letters.find(char)
                number -= (ord(self.key[self.index]))

                self.index += 1
                self.index %= len(key)

                if number >= len(self._letters):
                    number -= len(self._letters)

                elif number < 0:
                    number += len(self._letters)

                translated_message += self._letters[number]

            else:
                translated_message
        
        return translated_message

# message = 'hi mom im here how are you'
# key = 'wowshit'

# c = Caesar(message, key)

# print(c.encrypt())
# print(c.decrypt())