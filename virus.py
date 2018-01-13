def R():
    n = 1
    while True:
        yield n
        n = n + 1

list(R())
