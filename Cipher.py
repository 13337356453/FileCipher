class Cipher:
    key = ""

    def __init__(self, key):
        self.key = key

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def parseKey(self, key):
        # 处理密钥
        if key != "":
            o = 0
            for k in key:
                n = 0
                i = str(ord(k))
                for t in i:
                    n += int(t)
                o += n
            # 使密钥范围控制在10-100之间
            while True:
                if o < 10:
                    o = int(o * 2)
                elif o > 100:
                    o = int(o / 2)
                else:
                    return o
        return

    def getOdd(self, max):
        return [i for i in range(1, max + 1) if i % 2 == 1]

    def encrypt(self, data):
        # 加密算法
        if data == "":
            return
        result = ""
        length = len(data)  # 获取数据长度
        a = [ord(x) for x in data]
        # 判断是否为4的倍数
        remainder = length % 4  # 余数
        if remainder != 0:
            b = 4 - remainder
            for c in range(b):
                a.append(0)
        # 第一次分组
        groups = []
        d = len(a) // 2
        e1 = a[:d]
        e2 = a[d:]
        indexs = self.getOdd(d)
        groups.append([e1[i - 1] for i in indexs])
        groups.append([e1[i] for i in indexs])
        groups.append([e2[i - 1] for i in indexs])
        groups.append([e2[i] for i in indexs])
        # 第二次分组
        f1 = groups[0] + groups[3]
        f2 = groups[1] + groups[2]
        # 第一次加密
        keycode1 = self.parseKey(self.getKey())
        g = []
        for h in f1:
            i = h + keycode1
            j = chr(i)
            g.append(i)
            result += j
        # 第二次获取keycode
        k = str(sum(g))
        keycode2 = self.parseKey(k)
        # 第二次加密
        for l in f2:
            m = l + keycode2
            n = chr(m)
            result += n
        # 加密完成
        return result

    def decrypt(self, data):
        # 解密算法
        if data == "":
            return
        result = ""
        # 获取keycode1
        keycode1 = self.parseKey(self.getKey())
        # 第一次解密
        a = len(data) // 2
        b1 = data[:a]
        b2 = data[a:]
        c = [ord(d) for d in b1]
        e = [f - keycode1 for f in c]
        # 获取keycode2
        g = str(sum(c))
        keycode2 = self.parseKey(g)
        # 第二次解密
        h = [ord(i) for i in b2]
        j = [k - keycode2 for k in h]
        # f1对应e , f2对应j
        # 第一次分组
        k = len(e) // 2
        group1 = e[:k]
        group4 = e[k:]
        group2 = j[:k]
        group3 = j[k:]
        # 第二次分组
        datalength = len(group1) + len(group2) + len(group3) + len(group4)  # 数据长度
        l = datalength // 4
        m = []
        for n in range(l):
            m.append(group1[n])
            m.append(group2[n])
        o=[]
        for p in range(l):
            o.append(group3[p])
            o.append(group4[p])
        # 数据拼接
        q=m+o
        for r in q:
            result+=chr(r)
        # 返回结果
        return result


