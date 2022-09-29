jumlah_seluruh_bilangan_asli = 0
for i in range (1000):
    if (i%3 == 0 or i%5 == 0):
        jumlah_seluruh_bilangan_asli = jumlah_seluruh_bilangan_asli + i

print ("jumlah seluruh bilangan asli yang merupakan kelipatan 3 atau 5 kurang dari 1000 =", jumlah_seluruh_bilangan_asli)