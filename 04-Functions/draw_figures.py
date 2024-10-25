import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Side length
side_length = 150

# Draw figures
pen.penup()
pen.goto(-300, 100)
pen.pendown()
figures.draw_square(side_length, pen)
pen.penup()
pen.goto(-100, 100)
pen.pendown()
figures.draw_triangle(side_length, pen)
pen.penup()
pen.goto(100, 100)
pen.pendown()
figures.draw_rectangle(side_length, side_length * 0.8, pen)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()