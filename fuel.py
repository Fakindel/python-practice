try:
 while True:
  x_y = input("fraction ")
  x, y = x_y.split("/")
  x = int(x)
  y = int(y)
  re = (x / y) * 100
  if re <= 1:
   print("E")
  elif re >=99:
   print("F")
  else:
   print(f"{re:.0f}%")
   break
except ValueError:
 pass
except ZeroDivisionError:
 print("cant divide by 0")


  

