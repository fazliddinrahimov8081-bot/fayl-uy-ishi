matn = open("ascii.txt").read().split()
gap = "".join(chr(int(k)) for k in matn)
open("natija.txt", 'w').write(gap)