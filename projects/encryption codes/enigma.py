def enigma_machiene(text:str):
    covertion_key = {
        "a":"d",
        "b":"e",
        "c":"f",
        "d":"a",
        "e":"b",
        "f":"c",
        "g":"j",
        "h":"k",
        "i":"l",
        "j":"g",
        "k":"h",
        "l":"i",
        "m":"p",
        "n":"q",
        "o":"r",
        "p":"m",
        "q":"n",
        "r":"o",
        "s":"v",
        "t":"w",
        "u":"x",
        "v":"s",
        "w":"t",
        "x":"u",
        "y":"z",
        "z":"y",
        "0":"9",
        "1":"8",
        "2":"7",
        "3":"6",
        "4":"5",
        "5":"4",
        "6":"3",
        "7":"2",
        "8":"1",
        "9":"0",
        "!":"?",
        "?":"!",
        ".":",",
        ",":".",
        ":":";",
        ";":":",
        "(":"[",
        "[":"(",
        ")":"]",
        "]":")",
        " ":" "
            }
    try:
        text = text.lower()
        list_of_new_chars = []
        for i in text:
            list_of_new_chars.append(covertion_key.get(i,"#"))
        return "".join(list_of_new_chars)
    except AttributeError:
         return ("this program only takes in strings")

print(enigma_machiene("jbopdqz lv exoqlqj,"))