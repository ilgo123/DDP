def bilangan(n):
    hasil = []

    for i in range(1, n):
        if i % 2 != 0:
            hasil.append(i)

    print(hasil)

bilangan(20)