# import turtle
#
#
# timmy = turtle.Turtle()
# my_screen = turtle.Screen()
# timmy.shape("turtle")
# timmy.color("LightSlateBlue")
# timmy.begin_fill()
# while True:
#     timmy.forward(200)
#     timmy.left(170)
#     if abs(timmy.pos()) < 1:
#         break
# timmy.end_fill()
#
# my_screen.exitonclick()

from  prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Drikachu"])
table.add_column("Pokemon Type", ["Electric", "Water"])
table.align = "l"
print(table)

