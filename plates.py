def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
  seen_digit = False
  s = s.upper()
  if not len(s) >= 2 and not len(s) <= 6:
        return False
  if not s.isalnum():
            return False
  if not s[:2].isalpha():
                return False
  for a in s:
        if a.isdigit():
              if not seen_digit and a == "0":
                    return False
              seen_digit = True
        elif seen_digit and a.isalpha():
              return False
              
  return True            
                            

                        
             
        
   


main()
