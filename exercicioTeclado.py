import keyboard
import time

def minhafuncao():
    print("executei essa função aqui")

while True:
    key_pressed = keyboard.read_key()
    if(key_pressed != ""):
        print(f"a tecla digitada foi: {key_pressed}")
        if(key_pressed == "f1"): minhafuncao()
        if(key_pressed == "esc"): break
    time.sleep(0.3)