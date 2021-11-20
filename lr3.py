import math
import primesieve
import random


def RSA(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    e = 0
    for i in range(2, z):
        if math.gcd(i, z) == 1:
            e = i
            break
    d = 0
    for i in range(z):
        x = 1+(i*z)
        if x % e == 0:
            d = int(x / e)
            break
    return [e, n], [d, n]


def encrypt(message, public_key):
    encrypt_message = []
    for m in message:
        encrypt_message.append(pow(ord(m), public_key[0]) % public_key[1])
    return encrypt_message


def decrypt(message, private_key):
    decrypt_message = ''
    for m in message:
        decrypt_message += chr(pow(m, private_key[0]) % private_key[1])
    return decrypt_message


p = primesieve.nth_prime(random.randint(50, 150))
q = primesieve.nth_prime(random.randint(50, 150))

public_key, private_key = RSA(p, q)


print('Public Key:', ", ".join(list(map(str, public_key))))

print('Private Key:', ", ".join(list(map(str, private_key))))

msg = encrypt('Hi, Bob! asd', public_key)
print('Message:', decrypt(msg, private_key))
