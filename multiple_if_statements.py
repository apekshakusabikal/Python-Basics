#movie ticket booking
ticket=0
age=int(input("enter the age of the person: "))
if(age<12):
    ticket=100
    print("pay rs 100")
elif (age<=18):
        ticket=150
        print("pay rs 150")
else:
        ticket=250
        print("pay rs 250")
want_popcorn=input("Do you want popcorn(Y/N)?: ")
if(want_popcorn=='Y' or want_popcorn=='y'):
    ticket=ticket+80
    print(f"total ticket is {ticket}")
print("thank you!!")

#Amusement Park ride
height=int(input("enter your height: "))
bill=0
if(height>=4):
    print("can ride")
    age=int(input("enter the age: "))
if(age<12):
            bill=200
            print("pay rupees 200")
elif(age<=18):
            bill=300
            print("pay ruppes 300")
else:
            bill=500
            print("pay rupees 500")
fast_pass=input("do you want a fast pass(Y/N): ")
if(fast_pass=='Y' or fast_pass=='y'):
    bill=bill+100
    print(f"your total bill is rs {bill}")
else:
    print("can't ride")
print("thankyou!! Enjoy the movie")

#pizza order
size=input("enter the size of the pizza(S/M/L): ")
bill=0
if(size =='S' or size=='s'):
    bill=150
    print("pay rs 150")
elif(size=='M' or size=='m'):
        bill=250
        print("pay rs 250")
elif(size=='L' or size=='l'):
            bill=350
            print("pay rs 350")
extra_cheese=input("do you want extra cheese(Y/N): ")
if(extra_cheese=='Y' or extra_cheese=='y'):
    bill=bill+30
    print(f"toatal bill rs {bill}")
toppings=input("do you want toppings(Y/N): ")
if(toppings=='Y' or toppings=='y'):
    bill=bill+50
    print(f"toatal bill rs {bill}")
else:
    print("INVALID PIZZA")
print("Thankyou!!")

        
