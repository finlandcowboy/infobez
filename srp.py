import hashlib
import miller_rabin
import primesieve
import random
import math
import string

def generator_mod(N):
    init_set, cur_set = set(), set()
    
    for i in range(1,N):
        if math.gcd(i, N):
            init_set.add(i)
    
    for i in range(1,N):
        for j in range(1,N):
            cur_set.add(pow(i,j) % N)
            
        if init_set == cur_set:
            return i



def SRP(passwd, I, k=3):
    
    '''
    Args: 
    
    passwd - Пароль, который необходимо передать \n
    I - ? \n
    k - множитель (может являться хеш-функцией) \n
    '''
    
    N = 0
    print('Факторы протокола: ')
    
    while not miller_rabin.isPrime(N, 1000):
        if k != 0:
            print('\tСоставное')
        q = primesieve.nth_prime(random.randint(100,1000))
        N = 2 * q + 1
        print(f'q={q}\tN={N}', end = '')
        
    print('\tПростое')
    
    g = generator_mod(N)
    print(f'\nG = {g}')
    print(f'k = {k}\n')
    
    
    print('I. Регистрация\nВ процессе регистрации принимают участие клиент и сервер.')
    
    salt = "".join(random.choice(string.ascii_uppercase) for i in range(12))
    
    print(f'На клиенте генерируется:\nSalt: {salt}')
    
    x = int(hashlib.sha512(salt.encode() + passwd.encode()).hexdigest(), 16)
    
    #! x = H(S,p)
    print(f'x= {x}\t pass = {passwd}')
    
    #! v - password verifier
    v = pow(g,x,N)
    print(f'V = g^x mod N = {v}')
    
    print(f'\nII. Аутентификация.\n\nII.I Фаза 1' + '\n' + \
            '1. Клиент отправляет A и I на сервер\nI={I}')
    
    rand_a = random.randint(2,100)
    
    A = pow(g,rand_a,N)
    print(f'A = {A}')
    
    print('Сервер должен убедится что A!=0')
    if A == 0:
        return False
    
    rand_b = random.randint(2, 100)
    
    B = (k * v + pow(g,rand_b,N) % N)
    
    print(f'B = {B}')
    
    if B == 0:
        return False
    
    print('2. Затем сервер отсылает клиенту s и B\n' + 
          '4. Затем обе стороны вычисляют u = H(A,B)'
          '3. Клиент проверяет, что B != 0\n')
    
    u = int(hashlib.sha512(str(A).encode() + str(B).encode()).hexdigest(), 16)
    
    print(f'u = {u}\nЕсли u = 0, соединение прерывается')
    
    if u == 0: 
        return False

    s_cl = pow((B - k*(pow(g, x, N))), (rand_a + u * x), N)
    print(f'Клиент и сервер вычисляют общий ключ сессии (K)\ns_cl = {s_cl}')

    k_cl = int(hashlib.sha512(str(s_cl).encode()).hexdigest(), 16)
    print(f'{k_cl = }')    

    s_serv = pow(A * pow(v, u, N), rand_b, N)
    print(f'{s_serv = }')

    k_serv = int(hashlib.sha512(str(s_serv).encode()).hexdigest(), 16)
    print(f'k_serv = {k_serv}')
    
    if k_serv != k_cl:
        print(f'ERROR: K клиента и K сервера не совпадают!')
        return False
            
    print(f'K клиента и K сервера совпадают и равно = {k_serv}')
        
    print('\nII.II Фаза 2\nГенерация подтверждения\nСервер и клиент вычисляют M...')
    
    hash_N = int(hashlib.sha512(str(N).encode()).hexdigest(), 16)
    hash_g = int(hashlib.sha512(str(g).encode()).hexdigest(), 16)
    hash_I = int(hashlib.sha512(str(I).encode()).hexdigest(), 16)
    
    M_cl = int(hashlib.sha512(str(hash_N ^ hash_g).encode() + str(hash_I).encode() + str(s_cl).encode() + str(A).encode() + str(B).encode() + str(k).encode()).hexdigest(), 16)
    
    M_serv = int(hashlib.sha512(str(hash_N ^ hash_g).encode() + str(hash_I).encode() + str(s_cl).encode() + str(A).encode() + str(B).encode() + str(k).encode()).hexdigest(), 16)

    if M_cl != M_serv:
        print('М клиента и сервера не совпадают')
        return 'Failed to encypt'
    
    print(f'М клиента и сервера совпадают\nM= {M_serv}')

    print('\nСервер и клиент вычисляют R...')
    
    R_cl = int(hashlib.sha512(str(A).encode() + str(M_cl).encode() + str(k_cl).encode()).hexdigest(), 16)
    R_serv = int(hashlib.sha512(str(A).encode() + str(M_serv).encode() + str(k_serv).encode()).hexdigest(), 16)

    if R_cl != R_serv:
        print('R клиента и сервера не совпадают')
        return 'Failed to encypt'
    
    print('R клиента и сервера совпадают')


if __name__ == '__main__':
    passwd = 'asdbsd'
    I = 'zhashkov'
    k = 3
    SRP(passwd=passwd, I=I, k=k)



