def encrypt(text):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]
        result += chr(ord(char)+1)
    return result


# check the above function
text = "TEST"
print("Text  : " + text)
print("Cipher: " + encrypt(text))