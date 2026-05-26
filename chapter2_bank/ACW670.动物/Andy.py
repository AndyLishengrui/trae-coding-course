a, b, c = input(), input(), input()
if a == "vertebrado":
    if b == "ave":
        print("aguia" if c == "carnivoro" else "pomba")
    else:
        print("homem" if c == "onivoro" else "vaca")
else:
    if b == "inseto":
        print("pulga" if c == "hematofago" else "lagarta")
    else:
        print("sanguessuga" if c == "hematofago" else "minhoca")
