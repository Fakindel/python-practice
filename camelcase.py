def main(text):
  input = ""
  for char in text:
    if char.isupper():
      input = input + "_" + char.lower()
    else:
      input = input+ char
  return input
print(main("firstName"))