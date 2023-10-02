import Caesar

print("Willkommen zum besten Verschlüsselungsprogramm am BRG16!")
print("="*57)

while True:
    msg_clear = input("Was willst du verschlüsseln? (lass leer um zu beenden)")
    if msg_clear == "":
        break
    key = int(input("Welches Passwort möchtest du verwenden?"))
    msg_hidden = Caesar.encrypt(msg_clear, key)
    print(msg_hidden)
