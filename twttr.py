text = input("").lower()
new = ""
for char in text:
  if char in ["a", "e", "i", "o", "u"]:
    continue
  new +=char
print(new)
