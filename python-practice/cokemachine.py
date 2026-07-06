# Exercise: Simulate a Coke vending machine.

# Accept only 25¢, 10¢, and 5¢ coins.

# Keep prompting until 50¢ is paid, then output the change owed.

def coke_machine(amount):
    while amount > 0:
       print(f"Amount due: {amount}")
       coin = int(input("Insert Coin "))
       if coin == 25 or coin == 10 or coin == 5:
        amount = amount - coin
    print(f"change owned: {-amount}")
  
   
coke_machine(50)
 