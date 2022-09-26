import turtle
sc = turtle.Screen()
sc.title("START")
sc.setup(600, 600)
spiral = turtle.Turtle()
spiral.speed(10)
sc.bgcolor("black")

col = list(["#10002b", "#240046", "#3c096c", "#5a189a", "#7b2cbf", "#7b2cbf", "#9d4edd", "#c77dff",
                  "#e0aaff", "#e3f2fd", "#bbdefb", "#90caf9", "#64b5f6", "#64b5f6", "#2196f3", "#1e88e5",
                  "#1e88e5", "#1976d2", "#1565c0", "#0d47a1"])
c = len(col)-1
#def new_func(spiral):
   # spiral.fillcolor('violet')
    #col= turtle.pencolor()
    #spiral.fillcolor(col)
    #spiral.fillcolor(0, .5, 3)
    #return col

#col = new_func(spiral)
for i in range(50):
    if (c == 0):
        c = len(col) - 1
    spiral.forward(i*10)
    spiral.right(144)
    spiral.color(col[c])
    if c == 3:
        c = 0
    else:
        c -= 1

sc.exitonclick()