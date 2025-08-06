from string import ascii_lowercase

ENC = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])

def encode(plain_text: str) -> str:
    transformed = "".join(ch for ch in plain_text.lower() if ch.isalnum()).translate(ENC)
    return " ".join(transformed[i:i+5] for i in range(0, len(transformed), 5))
    

def decode(ciphered_text: str) -> str:
    return "".join(ch for ch in ciphered_text.lower() if ch.isalnum()).translate(ENC)
