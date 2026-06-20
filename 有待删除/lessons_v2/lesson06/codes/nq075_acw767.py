r = []
for c in input():
    if "a" <= c <= "z":
        r.append(chr((ord(c) - 97 + 1) % 26 + 97))
    elif "A" <= c <= "Z":
        r.append(chr((ord(c) - 65 + 1) % 26 + 65))
    else:
        r.append(c)
print("".join(r))
