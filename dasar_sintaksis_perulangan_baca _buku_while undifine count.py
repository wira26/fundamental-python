"""
program perulangan  whiel sampai paham
"""
book_count= 10
print("ibu berkata baca semua buku")
read_count= 0

understoot_count = 0
print(f"jumlah buku yang sudah di baca dan di pahami {understoot_count}")

while read_count < book_count * 2:
    read_count = read_count + 1
    if understoot_count == 9:
        print(f"buku ke {understoot_count + 1} belum paham")
    else:
        understoot_count = understoot_count + 1
        print(f"buke ke {understoot_count} sudah di baca dan dipahami")

print(f"jumlah buku yang di baca di pahami {understoot_count}")
if understoot_count == book_count:
    print('Bu,semua buku sudah saya baca')
else:
    print(f'bu,tidak semua buku bisa saya pahami,'
          f'budhi hanya bisa memahami {understoot_count} buku')