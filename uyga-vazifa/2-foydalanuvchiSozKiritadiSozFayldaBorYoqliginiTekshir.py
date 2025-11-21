with  open("dars.txt", 'r', encoding='utf-8') as f:
    matn = f.read().lower()
soz = input("Sozni kiriting: ").lower()

if matn.find(soz) != -1:
    print("Siz kiritgan soz faylda bor.")
else:
    print("Siz kiritgan soz faylda yoq.")