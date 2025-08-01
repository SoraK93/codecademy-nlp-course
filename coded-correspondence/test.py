def decode(message, offset):
  decrypted = ""
  start = ord("a")
  for char in message:
    if "a" <= char <= "z":
      decrypted += chr((ord(char) + offset - start) % 26 + start)
    else:
      decrypted += char
  return decrypted

def encode(message, offset):
  encrypted = ""
  start = ord("a")
  for char in message:
    if "a" <= char <= "z":
      encrypted += chr((ord(char) - offset - start) % 26 + start)
    else:
      encrypted += char
  return encrypted

encrypted_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
offset = 10

decoded_message = decode(encrypted_message, offset)
encoded_message = encode(decoded_message, offset)
# print(encoded_message == encrypted_message)

print(ord("x"), ord("r"), ord("o"), ord("a"))
