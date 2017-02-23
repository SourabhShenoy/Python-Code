
def  decrypt(encrypted_message):
#    endSig = "Your friend, Alice"
#    encodedEndSig = encrypted_message[encrypted_message.rfind('-')+1:]
    key = [8,2,5,1,2,2,0]
    return decryptMsg(key,encrypted_message)

def decryptMsg(key,msg):
    runner = 0
    answer = []
    for letter in msg:
        enc = ord(letter)
        if enc < 65 or enc > 122 or enc > 90 and enc < 97:
            answer.append(letter)
            continue
        origin = enc - int(key[runner])
        if letter.islower() and origin < ord('a') or origin < ord('A'):
            origin += 26
        runner  += 1
        if runner >= len(key):
            runner = 0
        answer.append(chr(origin))
    return "".join(answer)

