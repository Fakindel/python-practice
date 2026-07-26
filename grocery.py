from collections import Counter

empty_list = []
while True:
 try:
  items = input("input items ").upper()
  empty_list.append(items)
  a = Counter(empty_list)
  for key, value in sorted(a.items()):
   print(value, key)
 except EOFError:
  pass
