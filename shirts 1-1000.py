number_of_shirts= int(input("enter the number of shirts being purchaced: "))

if 1 <= number_of_shirts <= 50:

 print("cost per shirt = $20.00")

elif 50 <= number_of_shirts <= 100:

 print("cost per shirt = $17.50")

elif 100 <= number_of_shirts <= 250:

 print("cost per shirt = $15.00")

elif 250 <= number_of_shirts <= 500:

 print("cost per shirt = $12.50")

elif 500 <= number_of_shirts <= 1000:

 print("cost per shirt = $10.00")

else:

    print("error")
