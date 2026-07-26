def convert(text):
  r = text.replace(":)", "🙂").replace(":(", "🙁")
  return r
  
def main():
  text =  input("")
  print(convert(text))
main()