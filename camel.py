name = input("enter name ")
new = ""
for char in name:
  if str.isupper():
   new = new + "_" + char
  else:
   new = new + char
   
print(new.lower())
