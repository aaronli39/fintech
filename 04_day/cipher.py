# Code out your function definitions here

# the offset is 0 if user forgets to input
def encode(inp, off=0):
    ret = ""
    temp = inp.lower()
    for i in temp:
        if i == " ":
            ret += " "
            continue
        if i.isalpha():
            ret += chr((ord(i) + off - 97) % 26 + 97)
        else:
            ret += chr((ord(i) + off - 33) % 30 + 33)
    for i in inp:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

            ret = ret[: inp.index(i)] + ret[inp.index(i)
                                            ].upper() + ret[inp.index(i) + 1:]
    return ret


def decode(inp, off):
    ret = ""
    temp = inp.lower()
    for i in temp:
        if i == " ":
            ret += " "
            continue
        if i.isalpha():
            ret += chr((ord(i) - off - 97) % 26 + 97)
        else:
            # print(i.encode())
            ret += chr((ord(i) - off - 33) % 30 + 33)
    for i in inp:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            # print(ret[inp.index(i)], ret[inp.index(i)].upper())
            ret = ret[: inp.index(i)] + ret[inp.index(i)].upper() + ret[inp.index(i) + 1:]
    return ret


print(encode("Python is fun!)", 8))
print(decode(encode("Python is fun!)", 8), 8))

# 123 * 123
# 1234 * 1234
# 12345 * 12345
# ti84
'''
ti84 plus
pi
e
sin12
factorial 92
mortgage
interest
logarithmn
2^1212312312321
gpa
average
sum
median
std dev
iqr
range
min
max
mode
graphs
box plots
difference
quotient
product
remainder
pythagorean theorem
sqrt
cube root
any root
quadratics
integrals
limits
probability
randint
cotan
secant
secant inv
all trig inverses
graphs of integrals
histogram
derivatives
pi r ^2
'''

gpa 
pythagorean trip

sin12