""" Shift Cipher

Provides operations allowing the encoding and decoding of text using a standard shift cipher. Also includes a method to
perform a brute-force search for a key in the key space of a shift cipher.

"""


def encode(plaintext, key):
    """ Encode a given plaintext string using a shift cipher with the given key. """
    key = key.upper()
    key_numeral = ord(key) - 65
    plaintext = plaintext.upper()
    if key_numeral < 0 or key_numeral > 25:
        raise ValueError("Key must be in range A-Z")

    output = ""
    for character in plaintext:
        character_numeral = ord(character)
        if character_numeral < 65 or character_numeral > 90:
            output += character
        else:
            output += chr((((character_numeral - 65) + key_numeral) % 26) + 65)
    return output


def decode(ciphertext, key):
    """ Decode a given plaintext string using a shift cipher with the given key. """
    key_numeral = ord(key) - 65
    return encode(ciphertext, chr(((26 - key_numeral) % 26) + 65))


def brute_force_search(ciphertext):
    """ Enumerate all possible keys allowing a user to determine the key for a shift cipher and a given ciphertext. """
    ciphertext = ciphertext.upper()
    result = []
    for key in [chr(c+65) for c in range(0, 26)]:
        decoded_ciphertext = decode(ciphertext, key)
        result.append(decoded_ciphertext)
    return result


def print_brute_force_search(search_results):
    """ Prints the result of the above method labelling each item with the key that resulted in it. """
    if not(len(search_results) == 26):
        raise ValueError("Search results must contain 26 entries")
    for i in range(0, 26):
        print(chr(i + 65) + ":\t" + search_results[i])