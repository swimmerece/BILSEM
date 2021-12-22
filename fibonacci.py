z = int(input("Sayi giriniz: "))
sayi1 = 1
sayi2 = 1
fibonacci=[sayi1, sayi2]

for i in range (1, z):
    sayi1 = sayi1+sayi2
    sayi2 = sayi1+sayi2
    fibonacci.append(sayi1)
    fibonacci.append(sayi2)

print(fibonacci[z])
