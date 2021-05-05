import random


def generate_key_stream(n):
    return bytes([random.randrange(0, 256) for i in range(n)])


def xor_bytes(Key_stream, message):
    length = min(len(Key_stream), len(message))
    return bytes([Key_stream[i] ^ message[i] for i in range(length)])


# done by sender
message = "Do attack"
message = message.encode()
Key_stream = generate_key_stream(len(message))
cipher = xor_bytes(Key_stream, message)
print(Key_stream)
print(cipher)
print(xor_bytes(Key_stream, cipher))

# done by enemy trying to break the cypher
print(cipher)
message = "No attack"  # enemy input
message = message.encode()
guess_key_stream = xor_bytes(message, cipher)
print(xor_bytes(guess_key_stream, cipher))
# result: Even with an educated guess with the same cipher, the one time pad is still unbreakable.
