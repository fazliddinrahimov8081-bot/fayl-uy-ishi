with open ("sonlar.txt", 'r') as f:
    sonlar = f.read(). split()
    sonlar = [int(s) for s in sonlar]
    ortacha = sum(sonlar) / len (sonlar)
    print(round(ortacha))