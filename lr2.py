import random


if __name__=='__main__':
    P = 29
    G = 9
    alice_key = 4
    bob_key = 3
    
    gen_key_x = int(pow(G, alice_key, P))
    gen_key_y = int(pow(G, bob_key, P))
    
    ka = int(pow(gen_key_y,alice_key,P))
    kb = int(pow(gen_key_x,bob_key,P))
    print(ka, kb)