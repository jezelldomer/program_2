money = input("Enter the amount of money you have:")
amount = input("Enter the price of the apple:")

result = (float(money) / float(amount)) 
result_2 = (int(result) * int(amount))
result_3 = (float(money)) - (float(result_2)) 

print ("You can buy", int(result), "apples", "And your change is ", (result_3))

