disk = 1.44
pages = 100
stri = 50
letter = 25
code = 4

book_byte = pages*stri*letter*code
disk_byte = disk*1024*1024
print("Количество книг, помещающихся на дискету:", int(disk_byte//book_byte))