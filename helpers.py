import firebasescrypt

import base64

#Password Hash parameters
SALT_SEPARATOR = "Bw=="
SIGNER_KEY = "nZAII/QUzx+GU/dmQz7BoyRqoenaBRmEOgJhwjMWXjC3hB1KLFoXDi+ZtYdfIDmse3bYE1VWqLCsYqtKonYJBQ=="
ROUNDS = 8
MEM_COST = 14

class FirebaseHasher:

    @staticmethod
    def hash_password(password, salt):

        derived_key: bytes = firebasescrypt.generate_derived_key(password, salt, SALT_SEPARATOR, ROUNDS, MEM_COST)
        signer_key: bytes = base64.b64decode(SIGNER_KEY)

        result = firebasescrypt.encrypt(signer_key, derived_key)

        password_hash = base64.b64encode(result).decode('utf-8')

        return password_hash



if __name__ == '__main__':
        print(FirebaseHasher.hash_password("Se300799#","Hz2SNS3OvaJV8w=="))
