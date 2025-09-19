
def vigenere_encrypt(text, key):
    encrypted_chars = []
    key_shifts = [ord(c.lower()) - ord('a') for c in key]
    for idx, ch in enumerate(text):
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = key_shifts[idx % len(key_shifts)]
            encrypted_chars.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            encrypted_chars.append(ch)
    return "".join(encrypted_chars)

def vigenere_decrypt(ciphertext, key):
    decrypted_chars = []
    key_shifts = [ord(c.lower()) - ord('a') for c in key]
    for idx, ch in enumerate(ciphertext):
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = key_shifts[idx % len(key_shifts)]
            decrypted_chars.append(chr((ord(ch) - base - shift) % 26 + base))
        else:
            decrypted_chars.append(ch)
    return "".join(decrypted_chars)

if __name__ == "__main__":
    plaintext = "Network Security"
    key = "key"
    encrypted = vigenere_encrypt(plaintext, key)
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
