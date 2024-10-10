import time
import random

hex_bin_box = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
    'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111',
}
hex2bin = lambda hexstr: ''.join(hex_bin_box[i] for i in hexstr)  # 用于16进制字符串转二进制字符串

# 矩阵转换lambda表达式
translation = lambda item, box: ''.join(item[i - 1] for i in box)

# 秘钥的PC1矩阵
K64_56 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4,
]

# 秘钥的PC2矩阵
K56_48 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

Kleft_shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def encryption(mw, ned):
    # 密文B = 明文A的e次方 模 n， ned为公钥
    # mw就是明文A，ned【1】是e， ned【0】是n
    M = pow(mw, ned[1]) % ned[0]
    return M


# 获取轮秘钥
def get_Kn(Key, P):  # 生成Ki(共16轮密钥)
    Key = eval('0x' + Key)
    P = eval('0x' + P)
    C1 = str(hex(Key ^ P)[2:])

    new_C = []
    if len(C1) < 16:
        C1 = '0' * (16 - len(C1)) + C1
    for i in C1:
        if i in num:
            new_C.append(int(i))
        else:
            new_C.append(ord(i) - ord('a') + 10)
    Key = str(hex(Key))[2:]
    if len(Key) < 16:
        Key = '0' * (16 - len(Key)) + Key

    B = int(random.randint(1, 10))
    # print("B: ",str(B))
    Kn = []
    for i in Key:
        if i in num:
            Kn.append(int(i))
        else:
            Kn.append(ord(i) - ord('a') + 10)
    for i in range(16):
        mid = Kn[(B * i + new_C[i]) % 16]
        Kn[(B * i + new_C[i]) % 16] = Kn[i]
        Kn[i] = mid

    Kn = [bin(i)[2:] for i in Kn]
    for i in range(0, 16):
        if len(Kn[i]) < 4:
            Kn[i] = '0' * (4 - len(Kn[i])) + Kn[i]
    M = [encryption(int(i), [33, 3]) for i in Kn]
    Kn = "".join(Kn)
    # M = encryption(int(Kn), [33,3])
    # print("rsa Kn:",(M))

    # K64 = str(hex2bin(Key))  #转bit串

    # for i in str(C1)
    # # print(K64[41])
    # # print(K64[57])
    # # Step1  64bits Key -> 56bits Key：

    K56 = translation(Kn, K64_56)
    # print(K56)
    # Step2  circulate left draft

    Cn = [K56[:28]]
    Dn = [K56[28:]]
    for i in range(16):
        # 出错位置，虽然Cn中有17个数，但是我们这里的i是从0开始的，且Kleft_draft[i]对应着Ki+1，
        Cn.append(Cn[-1][Kleft_shift[i]:] + Cn[-1][:Kleft_shift[i]])
    for i in range(16):
        Dn.append(Dn[-1][Kleft_shift[i]:] + Dn[-1][:Kleft_shift[i]])
    # for i in range(17):
    #     print("{:<2}   {}   {}".format(i,Cn[i],Dn[i]))

    # Step3 Ci(56)->Ki(48)
    Kn = [translation(Cn[i] + Dn[i], K56_48) for i in range(1, 5)]
    for i in range(4):
        Kn[i] = Kn[i] * 5 + Kn[i][:16]
    # for i in range(4):
    #     print('K{:<3}      {}'.format(i + 1, Kn[i]))
    return Kn


# P = '02468aceeca86420'
# Key = '0f1571c947d9e859'
# print(get_Kn(Key, P))