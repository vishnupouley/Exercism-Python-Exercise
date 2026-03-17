import random
import string

class Cipher:
    """ Used to encode and decode the Vigenère cipher """
    def __init__(self, key=None):
        key = key if key else "".join(random.choices(string.ascii_lowercase, k=10))
        self.key = key


    def encode(self, text):
        while len(self.key) != len(text):
            self.key = self.key + self.key if len(self.key) < len(text) else self.key[:len(text)]
        return "".join([chr((ord(char) - 97 + (key_value - 97)) % 26 + 97) for char, key_value in zip(text, [ord(letter) for letter in self.key])])


    def decode(self, text):
        while len(self.key) != len(text):
            self.key = self.key + self.key if len(self.key) < len(text) else self.key[:len(text)]
        return "".join([chr((ord(char) - key_value) % 26 + 97) for char, key_value in zip(text, [ord(letter) for letter in self.key])])
