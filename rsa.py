import math
import primesieve
import random


def RSA(p, q):
    n = p * q
    print(f'{n = }')
    z = (p - 1) * (q - 1)
    print(f'{z = }')
    e = 0
    print('Гененируем такое число e, что наибольший общий делитель e и z = 1...')
    for i in range(2, z):
        print(f'gcd = {math.gcd(i, z)}')
        if math.gcd(i, z) == 1:
            e = i
            break


    print(f'{e = }')
    d = 0

    print(f'Генерируем такое число d...')
    for i in range(z):
        x = 1+(i*z)
        if x % e == 0:
            d = int(x / e)
            break

    print(f'{d = }')

    return [e, n], [d, n]


def encrypt(message, public_key):
    encrypt_message = []
    for m in message:
        encrypt_message.append(pow(ord(m), public_key[0], public_key[1]))
    print(f'\nEncrypted message: ', "".join(list(map(str,encrypt_message))))
    return encrypt_message


def decrypt(message, private_key):
    decrypt_message = ''
    print('\nDecryption...')
    for m in message:
        decrypt_message += chr(pow(m, private_key[0], private_key[1]))
        print(f'Initial message: {m}\tDecrypted message: {decrypt_message}')
    return decrypt_message


message = input()


p = primesieve.nth_prime(random.randint(50, 150))
q = primesieve.nth_prime(random.randint(50, 150))

public_key, private_key = RSA(p, q)

p2 = primesieve.nth_prime(random.randint(50, 150))
q2 = primesieve.nth_prime(random.randint(50, 150))

public_key2, private_key2 = RSA(p2, q2)

print('Public Key:', ", ".join(list(map(str, public_key))))

print('Private Key:', ", ".join(list(map(str, private_key))))

print('Public Key:', ", ".join(list(map(str, public_key))))

print('Private Key:', ", ".join(list(map(str, private_key))))


msg = encrypt(message, public_key)
print('Message:', decrypt(msg, private_key))
