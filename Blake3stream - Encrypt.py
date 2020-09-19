import secrets
from blake3 import blake3, KEY_LEN, OUT_LEN
import base64

class Blake3StreamCipher:

    def __init__(self, key, nonce, hashalg=blake3):
        __call__ = hashalg
        self._h = hashalg(data)
        self._pos = 0

    def keystream(self, n):
        #Return bytes from the keystream
        newpos = self._pos + n
        length = self._pos+newpos
        stream = self._h.digest(length)
        self._pos = newpos
        return stream

    def encrypt(self, plaintextmessage):
        #Encrypt the bytes of the plaintext with the keystream
        stream = self.keystream(len(plaintextmessage))
        try:
            return bytes(x^y for x, y in zip(plaintextmessage, stream))
        except TypeError as e:
            self._pos -= len(plain)
            raise TypeError("argument must be a bytes object") from e

    decrypt = encrypt

#Nonce and key can be manually input. Since this is a stream cipher it needs a unique nonce

randomBitNumber = secrets.token_bytes(32)
print ("Nonce is:", base64.b64encode(randomBitNumber))

randomkeynumber = secrets.token_bytes(32)
print ("Key is:", base64.b64encode(randomkeynumber))

nonce = randomBitNumber
key = randomkeynumber

data = randomBitNumber+randomkeynumber

cipher = Blake3StreamCipher(key=key, nonce=nonce)
plaintext = b"plaintext message"
ciphertext = cipher.encrypt(plaintext)
print ("Cipher text is:",base64.b64encode(ciphertext))

