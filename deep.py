text = input("what is the answer to the Great Question of Life, the Universe and Everything ? ").lower()
if text == "42":
  print("Yes")
elif text == "forty two":
  print("Yes")
elif text == "forty-two":
  print("Yes")
else:
  print("No")
