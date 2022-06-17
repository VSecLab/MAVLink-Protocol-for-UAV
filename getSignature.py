import hashlib
import binascii
import base64
from hashlib import sha256

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def calculate_secretkey(seed):
    print("Seed: ", seed)
    hashed_seed = (sha256(seed.encode('utf-8')).hexdigest())
    print("SHA256: ", hashed_seed)
    hex_seed = bytes.fromhex(hashed_seed)
    print("From HEX: ", hex_seed)
    base64_bytes = base64.b64encode(hex_seed)
    base64_seed = base64_bytes.decode('ascii')
    print("To base64: ", base64_seed)
    print("Signature = sha256_48(secret_key + header + payload + CRC + Link ID + timestamp)")
    header = input("Enter Header: ")
    payload = input("Enter Payload: ")
    crc = input("Enter CRC: ")
    linkid = input("Enter Link ID: ")
    timestamp = input("Enter Timestamp: ")
    signaturecompleta = hashed_seed+header+payload+crc+linkid+timestamp
    print( signaturecompleta)
    signature = sha256(bytes.fromhex(signaturecompleta))
    stampa_signature = signature.hexdigest()
    print("Signature: ", stampa_signature)
    print("Signature_48 bit: ", bcolors.OKGREEN + stampa_signature[:12] + bcolors.ENDC)

seed = input("Enter the password to sign messages: ")
calculate_secretkey(seed)
