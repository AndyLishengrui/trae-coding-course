import sys
text = sys.stdin.read().strip()
parts = text.split("->")
values = [p for p in parts if p != "NULL"]
values.reverse()
print("->".join(values) + "->NULL")
