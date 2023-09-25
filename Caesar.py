
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt(msg_clear: str, key: int):
    msg_hidden = ""
    for c in msg_clear:
        i = abc.index(c)
        new_i = i + key
        new_c =  abc[new_i]
        msg_hidden += new_c
    return msg_hidden

print(encrypt("hai", 1))
print(encrypt("wo", 2))
print(encrypt("fff", 3))