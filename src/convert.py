import pyperclip as pc


def convert():
    text = pc.paste().replace("\r", "\n")
    text = text.replace("\n\n- ", " - ")
    text2 = text.split(" - ")

    res = []
    for sub in text2:
        res.append(sub.replace("\n", ""))

    return "\n".join(res)


input("Please copy the text and press enter to convert: ")
val = convert()
pc.copy(val)
