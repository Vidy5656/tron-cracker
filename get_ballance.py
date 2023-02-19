
import hashlib
import base58
import requests

def get_balance(seed_phrase):
    # Generate the master private key from the seed phrase
    seed = hashlib.pbkdf2_hmac('sha512', seed_phrase.encode('utf-8'), b'mnemonic', 2048)
    master_private_key = seed[:32]
    
    # Generate the Bitcoin address from the master private key
    public_key = hashlib.sha256(master_private_key).digest()
    extended_public_key = base58.b58encode_check(b'\x04\x88\xb2\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00') + public_key
    address = base58.b58encode_check(extended_public_key).decode('utf-8')
    
    # Query the blockchain to get the balance of the address
    url = f'https://blockchain.info/q/addressbalance/{address}'
    response = requests.get(url)
    balance = int(response.text)
    
    return balance

with open('list.txt') as f:
    for seed_phrase in f:
        seed_phrase = seed_phrase.strip()
        balance = get_balance(seed_phrase)
        print(f'{seed_phrase}: {balance} satoshis')
