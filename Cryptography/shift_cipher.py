""" Shift Cipher

brute_force_search(cipher_text) performs a brute-force key search on cipher_text (searching all keys A-Z), where
cipher_text has been encoded using a standard shift-cipher. All 26 possible plain text messages are printed and should
then be checked manually.

"""

def brute_force_search(cipher_text):
    cipher_text = cipher_text.upper()
    for key_numeral in range(0, 26):
        key = chr(key_numeral + 65)
        print(key + ":\t", end="")

        for character in cipher_text:
            character_numeral = ord(character)
            decoded_character_numeral = (((character_numeral - 65) + key_numeral) % 26) + 65
            decoded_character = chr(decoded_character_numeral)
            print(decoded_character, end="")
        print("\n", end="")