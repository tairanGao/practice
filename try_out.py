def mark(a):
    count = 0
    while True:
        count += 1
        if count > 10:
            break
        yield a + count




gen_a = mark(0)
gen_b = mark(5)
while True:
    print(next(gen_a))
    print(next(gen_b))