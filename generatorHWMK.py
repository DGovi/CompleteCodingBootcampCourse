def gen_num(n):
    for i in range(n):
        yield i**2


for n in gen_num(4):
    print(n)
