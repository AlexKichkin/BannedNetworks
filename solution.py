class Vertex:
    def __init__(self):
        self.next = {}
        self.leaf = False


# реализуем класс Бор, который релизует одноименную структуру данных
class Bor:
    def add_string(self, s):
        ver = self.t
        length = len(s)
        for i in range(0, length):
            if ver.next.get(s[i]) is None:
                ver.next.update({s[i]: Vertex()})
            ver = ver.next[s[i]]
            if i == length-1:
                ver.leaf = True

    def __init__(self):
        self.t = Vertex()

    def in_bor(self, s):
        ver = self.t
        length = len(s)
        for i in range(0, length):
            if ver.next.get(s[i]) is None:
                return False
            ver = ver.next[s[i]]
            if ver.leaf ==  True:
                return True
            if i == length-1:
                return False


def ip_tostr(ip): #подготовка айпи для записи в бор
    a = ip.split('/')
    ip_addr = a[0]
    rez = ''
    for i in ip_addr.split('.'):
        s = str(bin(int(i))).replace("0b","")
        rez += '0'*(8-len(s))+s
    n = int(a[1])
    mask = '1'*n+'0'*(32-n)
    mask = int(mask, 2)
    rez = int(rez, 2)
    rez = str(bin(rez & mask)).replace("0b",'')
    l = len(rez)
    rez = '0'*(32-l)+rez

    return rez


def ip_tostr1(ip): #подготовка айпи для проверки
    ip_addr = ip
    rez = ''
    for i in ip_addr.split('.'):
        s = str(bin(int(i))).replace("0b",'')
        rez += '0'*(8-len(s))+s
    return rez

# отрезаем нули в конце
def chomp_zeros(ip):
    k = len(ip)-1
    while ip[k] == '0' and (k > 0):
        k -= 1
    return ip[0:k+1]


class RKN:
    def __init__(self, list):
        self.ip_bor = Bor()
        for i in list:
            self.ip_bor.add_string(chomp_zeros(ip_tostr(i)))

    def is_banned(self, ip):
        return self.ip_bor.in_bor(ip_tostr1(ip))

#попытался написать тесты)
if __name__ == "__main__":
    test0 = RKN(['10.0.0.0/8', '8.8.8.8/32'])
    assert test0.is_banned('10.1.2.3'), 'Zero test not passed'
    assert not test0.is_banned('127.0.0.1'), 'Zero test not passed'
    assert test0.is_banned('8.8.8.8'), 'Zero test not passed'
    assert not test0.is_banned('7.8.8.7'), 'Zero test not passed'

    test1 = RKN(['127.127.127.127/1', '1.1.1.1/7'])
    assert test1.is_banned('65.0.0.0'), 'First test not passed'
    assert test1.is_banned('65.127.127.127'), 'First test not passed'
    assert test1.is_banned('64.0.0.0'), 'First test not passed'
    assert test1.is_banned('64.127.127.127'), 'First test not passed'
    assert test1.is_banned('1.1.1.1'), 'First test not passed'
    assert test1.is_banned('0.1.1.1'), 'First test not passed'
    assert test1.is_banned('1.127.127.127'), 'First test not passed'
    assert test1.is_banned('0.127.127.127'), 'First test not passed'

    test2 = RKN(['135.168.13.2.1/30', '192.168.1.1/11'])
    assert not test2.is_banned('135.168.255.255'), 'Second test not passed'

