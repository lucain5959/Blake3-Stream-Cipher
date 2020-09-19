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

nonce = (base64.b64decode('hCo6oHA6DTNXHgXEWURrgxO3KU/ZlJZbj+znxWun6oM='))
key = (base64.b64decode('13SkygjqiYQ02g2XdatBoHWVvDsMnGpGwxALs4c9UiY='))
data = nonce+key

cipher = Blake3StreamCipher(key=key, nonce=nonce)
ciphertext = (base64.b64decode('w/FfrXEyKuAfkBfmQsEKCSI='))
decryptedtext = cipher.encrypt(ciphertext)
print ("Cipher text is:",(decryptedtext))

