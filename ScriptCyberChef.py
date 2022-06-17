import hashlib
import binascii
import base64
from hashlib import sha256

def calculate_secretkey(seed):
    print("Seed: ", seed)
    hashed_seed = (sha256(seed.encode('utf-8')).hexdigest())
    print("SHA256: ", hashed_seed)
    hex_seed = bytes.fromhex(hashed_seed)
    print("From HEX: ", hex_seed)
    base64_bytes = base64.b64encode(hex_seed)
    base64_seed = base64_bytes.decode('ascii')
    print("To base64: ", base64_seed)

seed = input("Enter the seed: ")
calculate_secretkey(seed)
