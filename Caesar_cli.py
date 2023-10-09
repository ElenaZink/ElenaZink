import Caesar

print("Willkommen zum besten Verschlüsselungsprogramm am BRG16!")
print("="*57)


def do_encrypt():
    msg_clear = input("Was willst du verschlüsseln?")
    key = int(input("Welches Passwort möchtest du verwenden?"))
    msg_hidden = Caesar.encrypt(msg_clear, key)
    print(msg_hidden)

def do_decrypt():
    msg_clear = input("Was willst du entschlüsseln?")
    key = int(input("Welches Passwort möchtest du verwenden?"))
    msg_hidden = Caesar.decrypt(msg_clear, key)
    print(msg_hidden)


while True:
    selection = input("Was möchtest du tun? (e)ncgrypt, (d)ecrypt, (b)rute force, e(x)it")
    if selection == "e":
        do_encrypt()
    elif selection == "d":
        do_decrypt()
    elif selection == "x":
        break
    else:
        print("Funktion ({selection})konnte nicht gefunden werden")
