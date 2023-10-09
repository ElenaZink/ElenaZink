import Caesar

print("Servus! Willkommen zum besten Verschlüsselungsprogramm am BRG16!")
print("=" * 57)


def get_key():
    while True:
        try:
            key = int(input("Welches Passwort möchtest du verwenden?"))
            break
        except ValueError:
            print("Hey du Dodl, du musst eine ganze Zahl eingeben!")
    return key


def do_encrypt():
    msg_clear = input("Was willst du verschlüsseln?")
    key = get_key()
    msg_hidden = Caesar.encrypt(msg_clear, key)
    print(msg_hidden)


def do_decrypt():
    msg_hidden = input("Was willst du entschlüsseln?")
    key = get_key()
    msg_clear = Caesar.decrypt(msg_hidden, key)
    print(msg_clear)


def do_bruteforce():
    msg_hidden = input("Was willst du entschlüsseln?")
    for key in range(26):
        msg_clear = Caesar.decrypt(msg_hidden, key)
        print(f"{key:02d}: {msg_clear}")


while True:
    selection = input("Was möchtest du tun? (e)ncgrypt, (d)ecrypt, (b)rute force, e(x)it")
    if selection == "e":
        do_encrypt()
    elif selection == "d":
        do_decrypt()
    elif selection == "b":
        do_bruteforce()

    elif selection == "x":
        break
    else:
        print("Funktion ({selection}) konnte nicht gefunden werden")
