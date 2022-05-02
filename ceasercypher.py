ALPHABET_START = ord('A')
ALPHABET_END = ord('Z')

alphabet_start = ord('a')
alphabet_end = ord('z')

def caesar_encrypt(plain_text, key):
  key %=26
  cipher_text = ""
  for c in plain_text:
      if c.isupper():
          c_unicode = ord(c)
          c_index = ord(c) - ALPHABET_START
          new_index = (c_index + key) % 26
          new_unicode = new_index + ALPHABET_START
          new_character = chr(new_unicode)
          cipher_text = cipher_text + new_character
      elif c.islower():
        c_unicode = ord(c)
        c_index = ord(c) - alphabet_start
        new_index = (c_index + key) % 26
        new_unicode = new_index + alphabet_start
        new_character = chr(new_unicode)
        cipher_text = cipher_text + new_character
      else:
        cipher_text += c 
  print(cipher_text)