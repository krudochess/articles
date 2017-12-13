
FPS = [
    # CENTER <-- BORDER
    (0b00000, +0),    (0b00001, +1),    (0b00010, +5),    (0b00011, +10),
    (0b00100, +30),   (0b00101, -0),    (0b00110, +100),  (0b00111, +120),
    (0b01000, +40),   (0b01001, -0),    (0b01010, -0),    (0b01011, -0),
    (0b01100, +150),  (0b01101, -0),    (0b01110, +150),  (0b01111, +200),
    (0b10000, +10),   (0b10001, -0),    (0b10010, -0),    (0b10011, -0),
    (0b10100, -0),    (0b10101, +50),   (0b10110, -0),    (0b10111, -0),
    (0b11000, +200),  (0b11001, -0),    (0b11010, -0),    (0b11011, +50),
    (0b11100, +275),  (0b11101, -0),    (0b11110, +400),  (0b11111, +450),
]

QPSW = FPS
KPSW = []

def revbin(p):
    return (p & 0b00001) << 4 | (p & 0b00010) << 2 | (p & 0b00100) | (p & 0b01000) >> 2 | (p & 0b10000) >> 4

for p, w in FPS:
    KPSW.append((revbin(p), w))

list = [];
for qp, qw in QPSW:
    for kp, kw in KPSW:
        bi = format(qp| kp  << 3 , '#010b')[2:].replace('0','.')
        ap = int(bi.replace('.', '0'), 2)
        list.append([bi, kw + qw, kw, qw, ap])

list = sorted(list, key=lambda x: x[1], reverse=True)

e = []
t = {
    '0min': 900, '0max': 0,
    '1min': 900, '1max': 0,
    '2min': 900, '2max': 0,
    '3min': 900, '3max': 0,
    '4min': 900, '4max': 0,
    '5min': 900, '5max': 0,
    '6min': 900, '6max': 0,
    '7min': 900, '7max': 0,
    '8min': 900, '8max': 0,
}

kio = [];
for p, w, a, b , d in list:
    if p not in e:
        n = str(p.count('1'))
        if w < t[n+'min']: t[n+'min'] = w
        if w > t[n+'max']: t[n+'max'] = w
        print str(n) + ')  ', p, w, ' ---> ', a, b , 'D',d
        kio.append((p, w, a, b , d))
        e.append(p)

print "---"

for i in range(8, -1, -1):
    print str(i)+')  ', 'min:', t[str(i)+'min'], 'max:', t[str(i)+'max']


print "---"

kio = sorted(kio, key=lambda x: x[4], reverse=False)

print "{"
for p, w, a, b, d in kio:
    if d % 16 is 0:
        print ''
    print w, ',' ,
