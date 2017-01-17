

"""
To open these doors, you will need to reverse engineer the hash function it is using. You already
managed to steal the details of the algorithm used, and with some quiet observation of the guards
you find out the results of the hash (the new digest). Now to break it. 

The function takes a 16 byte input and gives a 16 byte output. It uses multiplication, bit_wise exclusive OR 
(XOR) and modulo (%) to calculate an element of the digest based on the elements of the input message:

digest[i] = ((129*message[i]) XOR message[i-1]) % 256

For the first element, the value of message[-1] is 0.

For example, if message[0] = 1 and message[1] = 129, then:
For digest[0]:
129*message[0] = 129
129 XOR message[-1] = 129
129 % 256 = 129
Thus digest[0] = 129

For digest[1]:
129*message[1] = 16641
16641 XOR message[0] = 16640
16640 % 256 = 0
Thus digest[1] = 0

Write a function answer(digest) that takes an array of 16 integers and returns aother array of 16
that correspond to the unique message that created this digest. Since each value is a single byte,
the values are 0 to 255 for both message and digest.

"""

def hashOut(message):
    digest = []
    for i in range(len(message)):
        if i == 0:
            digest_i = ((129*message[i]) ^ 0) % 256
            digest.append(digest_i)
        else:
            digest_i = ((129*message[i]) ^ message[i-1]) % 256
            digest.append(digest_i)
    return digest

test2 = list(range(0,33))
test3 = list(range(0,33,2))
test4 = list(range(1,34,2))

hashed_test2 = hashOut(test2)
hashed_test3 = hashOut(test3)
hashed_test4 = hashOut(test4)


def answer(digest):
    message = []
    for i in range(len(digest)):
        if i == 0:
            xor = [(x*129)^0 for x in range(256)]
            answers = [x for x in range(256) if (((x*129)^0)%256) == digest[0]]
            message.append(xor.index(xor[answers[0]]))
        else:
            xor = [(x * 129)^message[i-1] for x in range(256)]
            answers = [x for x in range(256) if (((x*129)^message[i-1])%256) == digest[i]]
            message.append(xor.index(xor[answers[0]]))
    return message


print(answer(hashed_test2))
print(answer(hashed_test3))
print(answer(hashed_test4))

print(answer(hashed_test2) == test2)
print(answer(hashed_test3) == test3)
print(answer(hashed_test4) == test4)


