import turtle
star = turtle.Screen()
star.title("START")
star.setup(700, 700)
spiral = turtle.Turtle()
spiral.speed(10)


listColor = list(["#10002b", "#3c096c", "#5a189a", "#7b2cbf", "#7b2cbf", "#9d4edd", "#c77dff",
                  "#e0aaff", "#e3f2fd", "#bbdefb", "#90caf9", "#64b5f6", "#64b5f6", "#2196f3", "#1e88e5",
                  "#1e88e5", "#1976d2", "#1565c0", "#0d47a1"])




c = len(listColor)-1
counterColor = 0
for i in range(50):
    if(counterColor < len(listColor)):
        star.bgcolor(listColor[counterColor])
        counterColor += 1
    if(counterColor == len(listColor)):
        counterColor = 0
    if c == 0:
        c = len(listColor)-1
    spiral.forward(i*10)
    spiral.right(144)
    spiral.color(listColor[c])
    if c == 3:
        c = 0
    else:
        c -= 1
star.bgcolor("black")
star.exitonclick()