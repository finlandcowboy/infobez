def hash_func(key=''):
    hash = 0
    mask = 0x0000FFFF
    for idx, value in enumerate(key):
        hash += ord(value) ** idx
        print('1.', hash)
        print('2.', hash << 2)
        hash = (hash << 2) & mask
        
    return hash

if __name__ == '__main__':
    key = 'привет как дела'
    print(hash_func(key))