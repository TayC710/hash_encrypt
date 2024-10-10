# coding = utf-8
import os
import time
import hashlib
from gmssl.sm3 import sm3_hash
from subkey import get_Kn

 
def read_file(filename):
    """
    读取文件
    :param filename: 文件完整路径
    :return: 文件内信息
    """
    try:
        print(filename)
        f = open(filename, "r", encoding='utf-8')
        message = f.read()
        f.close()
        return message
    except:
        print("Open file error!")


def write_file(message, fileHash, filename):
    """
    写入到文件
    :param message: 写入文件的信息
    :param filename: 文件完整路径
    :return: 成功状态码0
    """
    try:
        f = open(filename, 'w', encoding='utf-8')
        f.write("[ciphertext " + fileHash + "]\n")
        f.write(message)
        f.close()
        return 0
    except:
        print("Write file error!")


def int2bin(x, n):
    """
    将十进制整数转换为二进制
    :param x: 十进制整数
    :param n: 二进制位数
    :return: n位二进制
    """
    x = str(bin(x)[2:])
    result = "0" * (n - len(x)) + x
    return result


def str2bit(string):
    """
    字符串转化为比特流
    :param string: 字符串
    :return: 01比特流
    """
    bits = ""
    for i in string:
        asc2i = bin(ord(i))[2:]  # bin将十进制数转二进制返回带有0b的01字符串
        # 为了统一每一个字符的01bit串位数相同，将每一个均补齐8位
        for j in range(8 - len(asc2i)):
            asc2i = '0' + asc2i
        bits += asc2i
    return bits


def bit2str(bits):
    """
    比特流转化为字符串
    :param bits: 01比特流
    :return: 字符串
    """
    string = ""
    for i in range(len(bits) // 8):
        string += chr(int(bits[i * 8:(i + 1) * 8], 2))
    return string


def xor(x, k):
    """
    x与k的异或运算
    """
    bits_xor = ""
    for i in range(len(x)):
        if x[i] == k[i]:
            bits_xor += '0'
        else:
            bits_xor += '1'
    return bits_xor


def mad(x, k):
    """
    x与k的模加运算
    """
    x = int(x, 2)
    k = int(k, 2)
    n1 = x ^ k
    n2 = (x & k) << 1
    while n2 != 0:
        temp = n1 ^ n2
        n2 = (n1 & n2) << 1
        n1 = temp
    return int2bin(n1, 256)


def rotateLeft(k, r):
    """
    将256位子密钥k向左循环移位r位
    """
    n = 256
    k = int(k, 2)
    r = r % n
    result = ((k << r) % (2 ** n)) ^ ((k >> (n - r)) % (2 ** n))
    return int2bin(result, n)


def process_key(key):
    key_bits = ""
    for i in key:
        count = 0
        asc2i = bin(ord(i))[2:]
        # 将每一个ascii均补齐7位,第8位作为奇偶效验位
        for j in asc2i:
            count += int(j)
        if count % 2 == 0:
            asc2i += '0'
        else:
            asc2i += '1'

        for j in range(7 - len(asc2i)):
            asc2i = '0' + asc2i
        key_bits += asc2i
    if len(key_bits) > 64:
        return key_bits[0:64]
    else:
        for i in range(64 - len(key_bits)):
            key_bits += '0'
        return key_bits


def divide(bits, k):
    """
    将bits按k位一组进行分组
    :return: 分组得到的列表
    """
    m = len(bits) // k
    N = ["" for i in range(m)]
    for i in range(m):
        N[i] = bits[i * k:(i + 1) * k]
    if len(bits) % k != 0:
        N.append(bits[m * k:])
        for i in range(k - len(N[m])):
            N[m] += '0'
    return N


def get_hash(bits, t):
    """
    计算hash值
    :param bits: 256位比特串
    :param t: 使用hash算法的类型
    :return: 256位hash值
    """
    s = bit2str(bits).encode()
    # MD5
    if t == 2:
        md = hashlib.md5()
        md.update(s)
        h = md.hexdigest()
        return str2bit(h) * 2
    # SHA3
    elif t == 1:
        sh = hashlib.sha3_256()
        sh.update(s)
        h = sh.hexdigest()
        return str2bit(h)
    # SM3
    elif t == 0:
        h = sm3_hash(bytearray(s))
        return str2bit(h)
    else:
        print("Hash type error!")


def F(x, k, r):
    """
    轮函数
    :param x: 256位比特串
    :param k: 256位子密钥
    :param r: 循环左移位数
    :return: 256位比特串
    """
    bits = mad(x, k)
    k = rotateLeft(k, r)
    bits = xor(bits, k)
    return bits


def encrypt(bits, key, type):
    """
    bits : 分组512bit01明文字符串
    key : 256bit01密钥
    return : 加密得到512bit 01密文序列
    """
    # 切片分成两个256bit
    L = bits[0:256]
    R = bits[256:]
    key_list = get_Kn(key, hex(int(R, 2))[2:18])  # 4个子密钥
    for i in range(4):
        L_next = xor(R, key_list[i])
        h = get_hash(F(R, key_list[i], i % 2 + 1), type)
        print("第%d轮生成的hash为：" %i)
        print(hex(int(h,2)))
        R = xor(L, h)
        L = L_next
    result = R + L
    return result


def main_encrypt(message, key, type):
    """
    message : 读入明文字符串
    key : 读入密钥串
    type : 哈希算法类型
    returns : 密文01序列
    """
    message = str2bit(message)
    key = process_key(key)
    mess_div = divide(message, 512)
    result = ""
    for i in mess_div:
        result += encrypt(i, key, type)
    return result

def integrity(message, t):
    """
    生成文件哈希
    :param message: 文件内容
    :param t: 使用hash算法的类型
    :return: 128/256位hash值
    """
    # MD5
    if t == 2:
        md = hashlib.md5()
        md.update(message.encode())
        h = md.hexdigest()
        return h
    # SHA3
    elif t == 1:
        sh = hashlib.sha3_256()
        sh.update(message.encode())
        h = sh.hexdigest()
        return h
    # SM3
    elif t == 0:
        h = sm3_hash(bytearray(message.encode()))
        return h
    else:
        print("Hash type error!")

def main(filename_path,encode_path,oriKey,Hash):
    file = filename_path
    message = read_file(file)
    print("Plaintext:  " + message)
    # print("Plaintext 01bits:   " + str2bit(message))
    key =oriKey

    start = time.time()
    result = main_encrypt(message, key, Hash)
    end = time.time()
    print('Running time: %s Seconds' % (end - start))
    # print("\nCiphertext 01bits:  " + result)
    result_str = bit2str(result)
    print(result_str)

    savepath = encode_path
    filepath, filename = os.path.split(file)
    cfile = os.path.join(savepath, "c_" + filename)
    fileHash = integrity(message,Hash) #获取文件hash
    resultFlag = write_file(result_str,fileHash,cfile)
    # print("Ciphertext:  " + result_str)

    return resultFlag

'''
if __name__ == '__main__':
    while True:
        if main():
            break
'''
