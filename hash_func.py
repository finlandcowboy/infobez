def hash_func(text):
    hashes = []
    for letter in text:
        hashes.append(ord(letter))

    return hashes

text = 'hi im here'

print('Decrypted: ', "".join(list(map(str, hash_func(text)))))

print('Result:', "".join(list(map(chr, hash_func(text)))))