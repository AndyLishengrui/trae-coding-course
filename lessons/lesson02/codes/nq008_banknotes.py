# NQ008: 钞票
n = int(input())
print(n)
notes = [100, 50, 20, 10, 5, 2, 1]
for note in notes:
    count = n // note
    print(f"{count} nota(s) de R$ {note},00")
    n %= note
