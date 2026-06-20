# NQ1-13: 面积
# 计算三个图形面积: 直角三角形、圆、梯形，各保留3位小数。

PI = 3.14159
a, b, c = map(float, input().split())

print(f"TRIANGULO: {a * c / 2.0:.3f}")   # 直角三角形: A*C/2
print(f"CIRCULO: {PI * c * c:.3f}")       # 圆: pi*C^2
print(f"TRAPEZIO: {(a + b) * c / 2.0:.3f}")  # 梯形: (A+B)*C/2
