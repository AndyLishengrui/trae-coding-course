s = input()
from collections import Counter
cnt = Counter(s)
for c in s:
    if cnt[c] == 1:
        print(c)
        break
else:
    print("no")
