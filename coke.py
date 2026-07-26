amount_due = 50
while amount_due > 0:
  print(f"amount due:{amount_due}")
  money = int(input("insert coin "))
  if not money == 25 or money == 10 or money == 5:
    continue
  amount_due = amount_due - money
print(f"change owed: {abs(amount_due)}")




 


    


