import tkinter as tk
import Caesar


def do_encrypt():
    ergebnis = Caesar.encrypt(clear_textbox.get(), key_slider.get())
    secret_textbox.delete(0, "end")
    secret_textbox.insert(0, ergebnis)


def do_decrypt():
    ergebnis = Caesar.decrypt(secret_textbox.get(), key_slider.get())
    clear_textbox.delete(0, "end")
    clear_textbox.insert(0, ergebnis)


root = tk.Tk()
root.title("Caesar Verschlüsselung")
root.minsize(300, 200)

key_label = tk.Label(root, text="Schlüssel:")
clear_label = tk.Label(root, text="Klartext:")
secret_label = tk.Label(root, text="Geheimtext:")

key_label.grid(row=0, column=0, sticky="ew")
clear_label.grid(row=1, column=0)
secret_label.grid(row=3, column=0, padx=5, pady=5)

key_slider = tk.Scale(root, to=25, orient=tk.HORIZONTAL)
clear_textbox = tk.Entry(root)
secret_textbox = tk.Entry(root)

key_slider.grid(row=0, column=1, columnspan=2, sticky="ew")
clear_textbox.grid(row=1, column=1, columnspan=2, sticky="nsew")
secret_textbox.grid(row=3, column=1, columnspan=2, sticky="nsew")

encrypt_button = tk.Button(root, text="Verschlüsseln", command=do_encrypt)
decrypt_button = tk.Button(root, text="Entschlüsseln", command=do_decrypt)

encrypt_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
decrypt_button.grid(row=2, column=2, padx=5, pady=5, sticky="ew")

root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(3, weight=1)

root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()
