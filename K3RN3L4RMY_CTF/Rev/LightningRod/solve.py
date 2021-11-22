state = [0 for i in range(242)]
ini = 0


def transform(b):
    global state
    global ini
    for i in range(23):
        v4 = state[ini]
        state[ini] = b ^ v4

        if b > v4:
            ini += 11
        else:
            ini += 10

        if (i & 1) == 0:
            v3 = ini - 11 + 21 * (i / -2)
            if v3 == -1:
                ini += 10
            if v3 == 10:
                ini -= 10
        ini %= 242
        b ^= v4

    return b


def encrypt(text):
    cyph = ""
    for i in range(len(text)):
        cyph += chr(transform(ord(text[i])))

    return cyph


print(encrypt("ASDASDASDASDASDasdfhlashfashflhaslfhasldhklasdhfklashdlfhasdklhasdklhklasdfhlkasdhfklshdklfshadklaskldfklsdfkl"))
a = "".join([chr(i) for i in state])
print("=========")
print(a)
