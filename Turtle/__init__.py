import time
import turtle
length = 20
lengthNegative = -20
angle = -25
turtle.setup(1366, 769)
turtle.bgcolor('#000000')
listColor = list(["#10002b", "#3c096c", "#5a189a", "#7b2cbf", "#7b2cbf", "#9d4edd", "#c77dff",
                  "#e0aaff", "#e3f2fd", "#bbdefb", "#90caf9", "#64b5f6", "#64b5f6", "#2196f3", "#1e88e5",
                  "#1e88e5", "#1976d2", "#1565c0", "#0d47a1"])
index = 0
turtle.speed(15)
for i in range(len(listColor)):
    turtle.circle(length, 360)
    turtle.circle(lengthNegative, 360)
    turtle.color(listColor[index])
    length += 20
    lengthNegative += -20
    if index <= len(listColor):
        index += 1
    else:
        index = 0
turtle.color(listColor[len(listColor)-1])
turtle.forward(length)
turtle.color(listColor[len(listColor)-2])
turtle.forward(lengthNegative+lengthNegative)
index = 5
turtle.speed(4)
for i in range(3):
    turtle.color(listColor[index])
    turtle.begin_fill()
    turtle.right(-45)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(135)
    turtle.forward(length / 2)
    index += 4
    turtle.end_fill()
time.sleep(5)
for i in range(39):
    turtle.undo()
turtle.exitonclick()