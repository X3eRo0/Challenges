from z3 import *
import pwn

from Crypto.Util.number import long_to_bytes

NUM_MODELS = 1000000
INP_LENGTH = 20 
BITLEN = 64
inp = [BitVec(f'inp{i}', BITLEN) for i in range(INP_LENGTH)]
S = Solver()

constraints = [
    inp[0] == 102,
    inp[1] & 1337 == 1057,
    inp[1] | 1337 == 28025,
    inp[1] ^ 1337 < 269700,
    # inp[1] & 0xff == ord('l'),
    # inp[2] ^ inp[3] == 28,
    # inp[2] & inp[3] == 99,
    inp[2] == ord('g'),
    inp[3] == ord('{'),
    inp[4] == 3713,
    inp[6] - inp[5] == 489139534831,
    inp[6] & 4294967040 == 892362496,
    inp[7] - inp[8] == 18446743885531466769,
    inp[7] * inp[11] == 10593957610752,
    inp[9] + inp[7] - inp[8] == 118730899270,
    inp[7] + inp[8] + inp[9] + inp[10] == 1346493052268,
    inp[10] | inp[11] == 409991082872,
    inp[10] - inp[9] == 103082098739,
    inp[12] == 30001,
    inp[13] == 25695,
    inp[14] == 26419,
    inp[15] == 928999216,
    inp[16] == 62003745337707,
    inp[17] == 13151,
    inp[18] == 27955,
    inp[19] == 125,
    # (inp[5] >> 32) & 0xff == ord('N'),
    (inp[5] >> 0) & 0xff == ord('t'),
    (inp[5] >> 8) & 0xff <= 0x7f,
    (inp[5] >> 16) & 0xff <= 0x7f,
    (inp[5] >> 24) & 0xff <= 0x7f,
    # (inp[5] >> 32) & 0xff <= 0x7f,
    (inp[5] >> 40) & 0xff <= 0x7f,
    (inp[5] >> 48) & 0xff <= 0x7f,
    (inp[5] >> 54) & 0xff <= 0x7f,

    (inp[5] >> 0) & 0xff >= 0x2e,
    (inp[5] >> 8) & 0xff >= 0x2e,
    (inp[5] >> 16) & 0xff >= 0x2e,
    (inp[5] >> 24) & 0xff >= 0x2e,
    (inp[5] >> 32) & 0xff >= 0x2e,
    (inp[5] >> 40) & 0xff >= 0x2e,
    (inp[5] >> 48) & 0xff >= 0x2e,
    (inp[5] >> 54) & 0xff >= 0x2e,

    (inp[6] >> 0) & 0xff <= 0x7f,
    (inp[6] >> 8) & 0xff <= 0x7f,
    (inp[6] >> 16) & 0xff <= 0x7f,
    (inp[6] >> 24) & 0xff <= 0x7f,
    (inp[6] >> 32) & 0xff <= 0x7f,
    (inp[6] >> 40) & 0xff <= 0x7f,
    (inp[6] >> 48) & 0xff <= 0x7f,
    (inp[6] >> 54) & 0xff <= 0x7f,

    (inp[6] >> 0) & 0xff >= 0x2e,
    (inp[6] >> 8) & 0xff >= 0x2e,
    (inp[6] >> 16) & 0xff >= 0x2e,
    (inp[6] >> 24) & 0xff >= 0x2e,
    (inp[6] >> 32) & 0xff >= 0x2e,
    (inp[6] >> 40) & 0xff >= 0x2e,
    (inp[6] >> 48) & 0xff >= 0x2e,
    (inp[6] >> 54) & 0xff >= 0x2e,
]


# constraints for ascii chars
# constraints.extend([
#     Or(
#         inp[i] & 0xff <= 0x7e,
#     )
#     for i in range(INP_LENGTH)])


def get_models(constraints,num_models: int) -> list:
    result = []
    solver = Solver()
    solver.add(constraints)
    while len(result) < num_models and solver.check() == sat:
        model = solver.model()
        result.append(model)
        # print(model)
        Input = bytes(b"".join([long_to_bytes(model[inp[i]].as_long()) for i in range(INP_LENGTH)]))
        print("".join([chr(i) for i in long_to_bytes(model[inp[5]].as_long())]), end="")
        # print("".join([chr(i) for i in long_to_bytes(model[inp[6]].as_long())]), hex(model[inp[5]].as_long()))
        # print(Input)
        pwn.context.log_level = 'critical'
        io = pwn.process(["./Recurso", "./leFlag.recc"])
        io.sendline(Input)
        resp = io.recvline()
        print(resp, Input)
        io.close()
        if resp != b'0\n':
            print(resp, Input)
            input("FOUND")
        block = []
        for declaration in model:
            c = declaration()
            block.append(c != model[declaration])
        solver.add(Or(block))
    return result


models = get_models(constraints, NUM_MODELS)
