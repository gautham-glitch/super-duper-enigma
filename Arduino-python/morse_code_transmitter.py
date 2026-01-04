import time
from pyfirmata2 import Arduino, util
def morse_code_translator(text):
    original = {
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
        "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
        "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
        "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
        "y": "-.--", "z": "--..",

        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",

        ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--",
        "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.",
        "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-", "\\": ".-..-.",
        "$": "...-..-", "@": ".--.-.", " ": "/"
    }
    updated = {k: [v] for k, v in original.items()}


    morse_pre_con = list(text.lower())

    list_of_chars = []

    for i in morse_pre_con:
        list_of_chars.extend(updated.get(i, "#"))

    return(" ".join(list_of_chars))

# 🔌 Connect to Arduino
board = Arduino('COM3')  # Make sure this matches your port
#led_pin = board.get_pin('d:8:o')  # Digital pin 8 as output
buzzer = board.get_pin("d:12:o")

# 💡 Blink LED based on Morse code
def blink_led(morse_code):
    for symbol in morse_code:
        match symbol:
            case '.':
                #led_pin.write(1)
                buzzer.write(1)
                time.sleep(0.2)
            case '-':
                #led_pin.write(1)
                buzzer.write(1)
                time.sleep(0.6)
            case '/':
                time.sleep(1)
            case _:  # space between letters
                time.sleep(0.4)
        #led_pin.write(0)
        buzzer.write(0)
        time.sleep(0.2)  # brief pause between blinks

# 🔤 Message to convert
message = str_to_con = str(input("Input some charecters: "))
code = morse_code_translator(message)
print("Morse Code:", code)

blink_led(code)