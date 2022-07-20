"""
semua sintaksis dasar bahasa pemrograman adalah:
sekuensial:langkah berurutan
percobaan:langkah melompat jikah kondisi terpenuhi
perulangan:mengulang langkah berkali-kali selama/sampai kondisi terpenuhi
"""

#SEKUENSIAL
print('Ibu berkata,"Pergi ke toko"')
print('Budhi menjawab,"Baik,apa yang harus saya lakukan di toko?"')
print('ibu menjawab'"beli 1 botol susu")
print("Maka Budhi berangkat ke toko")
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu= 173
jumlah_telor= 1587
print(f"jumlah botol susu {jumlah_botol_susu}botol")
print(f"jumlah telur {jumlah_telor}butir")

if jumlah_botol_susu > 0:
    print("Budhi mengecek harganya,dan ternyata uangnya cukup")
    if jumlah_telor==0:
       print("Budhi membeli 1 botol susu")
    else:
        print("Budhi  membeli 6 botol susu")

else:
    print("Budhi tidak jadi membeli 1 botol susu")

print("Budhi pulang kerumah")
print("Menyampaikan hasilnya kepada ibu")