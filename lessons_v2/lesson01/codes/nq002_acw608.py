s = __import__('sys').stdin.read()
nums = []
for tok in s.replace('\r',' ').replace('\n',' ').split(' '):
    tok = tok.strip()
    if tok:
        try: nums.append(int(tok))
        except: pass
a,b,c,d = nums[0], nums[1], nums[2], nums[3]
print(f"DIFERENCA = {a * b - c * d}")
