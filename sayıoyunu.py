tahmin=5
while True:
    sayi=int(input("1 ile 10 arasında tahmin gir: "))

    if sayi == tahmin:
        print("Doğru tahmin ettiniz.")
        break

    elif sayi>tahmin:
        print("Sayıyı küçült.")

    sayi=int(input("Tahmin gir: "))

    elif sayi<tahmin:
        print("Sayıyı büyüt.")

    sayi=int(input("Tahmin gir: "))

