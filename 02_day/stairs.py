# Code your functions here!

def downstairs(num):
    if num == 0: return ""
    ret = []
    for i in range(1, num + 1):
        ret.append(("#" * i) + "\n")
    return "".join(ret)
    
# print(downstairs(4))

def upstairs(num):
    if num == 0: return ""
    ret = []
    for i in range(1, num + 1):
        ret.append((" " * (num - i + 1)) + ("#" * i) + "\n")
    return "".join(ret)
    
# print(upstairs(6))

def pyramid(num):
    if num == 0: return ""
    ret = []
    for i in range(1, num + 1):
        ret.append((" " * (num - i + 1)) + ("#" * i) + " " + ("#" * i) + "\n")
    return "".join(ret)
        
print(pyramid(9))