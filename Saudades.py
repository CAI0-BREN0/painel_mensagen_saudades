import math
from turtle import*
pendown()
goto(0, -100)
color("#f73487")
write("Sentiremos sua falta", align="center", font=("Arial", 20, "bold"))
def coracaoa(k):
    return 15 * math.sin(k) ** 3
def coracaob(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)
speed(0)
bgcolor("black")
for i in range(10000):
    goto(coracaoa(i) * 20, coracaob(i) * 20)
    for j in range(5):
        color("#f73487")
    goto(0, 0)
done()