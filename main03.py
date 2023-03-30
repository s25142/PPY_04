import string


english_alphabet = list(string.ascii_lowercase)
def change_letter(letter, key, alphabet):
    alphabet = tuple(alphabet)

    start_index = alphabet.index(letter)
    end_index = (start_index + key) % len(alphabet)

    letter = alphabet[end_index]
    return letter
def cesear_cipher(text, key, alphabet=english_alphabet):
    alphabet = tuple(alphabet)
    text = str(text).casefold()
    encrypted = ''
    for c in text:
        if c not in alphabet:
            encrypted += c
        else:
            c = change_letter(c, key, alphabet)
            encrypted += c

    return encrypted


msg = "The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll"

print(cesear_cipher(msg, 5))
print(cesear_cipher(msg, 3, ["a", "B"]))

