
# Exercise: Convert a camelCase variable name to snake_case.
# Example:
# firstName -> first_name
# preferredFirstName -> preferred_first_name

def main(text):
  input = ""
  for char in text:
    if char.isupper():
      input = input + "_" + char.lower()
    else:
      input = input+ char
  return input
print(main("firstName"))