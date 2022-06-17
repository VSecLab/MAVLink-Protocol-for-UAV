# MAVLink-Protocol-for-UAV
Additional materials for "MAVLink Protocol for Unmanned Aerial Vehicle:  Vulnerabilities Analysis"

# ScriptCyberChef

Script that replicates the operations performed on CyberChef for the encrypting of the initial seed used to sign MAVLink messages.

# getSignature

Script that allows you to create and replicate a valid signature for MAVLink messages, starting from an initial seed and entering all the information necessary for the creation of the signature: Signature = sha256_48 (secret_key + header + payload + CRC + Link ID + timestamp).

#dictionaryKey and dictionarySignature

Scripts that allow you to perform a dictionary attack. The "key" file carries out the attack starting from the secret key recovered in the exchange of messages. The "signature" file carries out the attack starting from the signature exchanged in the messages, without the need for the secret key.

dictionaryKey:

time python3 dizionarioKey.py --type sha256 --string "secretkey" --wordlist wordlist.txt

dictionarySignature:

time python3 dizionarioSignature.py --type sha256 --string "signature" --wordlist wordlist.txt

# wordlist

Wordlist used to carry out the attack.  It contains about 100,000 words including the most used passwords in the world, the most common Italian names and surnames, and finally many terms from the Italian dictionary.

# file.mp4 and .mov

Videos are shown to show the execution of the dictionary attack on the Key, the Signature and finally the actual Injection.

# Software Requirements 

Python 3
Mission Planner
Packet Sender
