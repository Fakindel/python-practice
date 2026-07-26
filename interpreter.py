x_y_z = input("Expression")
x, y, z = x_y_z.split(" ")
x = float(x)
z = float(z)
if y == "+":
  print(f"{x + z:.1f}")
elif y == "-":
  print(f"{x - z:.1f}")
elif y == "/":
  print(f"{x / z:.1f}")
elif y == "*":
  print(f"{x * z:.1f}")
