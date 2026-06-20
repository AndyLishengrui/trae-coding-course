a, b, c = sorted(map(float, input().split()), reverse=True)
if a >= b + c:
    print("Not a triangle")
else:
    if a*a == b*b + c*c: print("Right")
    if a*a > b*b + c*c: print("Obtuse")
    if a*a < b*b + c*c: print("Acute")
    if a == b == c: print("Equilateral")
    elif a == b or b == c or a == c: print("Isosceles")
