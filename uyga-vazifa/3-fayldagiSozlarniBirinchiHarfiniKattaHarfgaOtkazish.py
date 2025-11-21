with open("matn.txt", 'r', encoding='utf-8') as f:
    matn = f.read()
yngi_matn = matn.title()
with open("natija.txt", 'w', encoding='utf-8') as f:
    f.write(yngi_matn)
print("Bajarildi! ")
