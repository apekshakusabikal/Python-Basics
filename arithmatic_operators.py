#addition
a=10
b=20
print(a+b)

#substraction
a=10
b=20
print(a-b)

#multiplication
a=10
b=20
print(a*b)

#division
a=100
b=4
print(a/b)

#to find remainders
a=34
b=2
print(a%b)

#to find quotient
a=45
b=5
print(a//b)

#finf 2 raised to the power 5
a=2
b=5
print(a**b)

#take 2 numbers as input and find their sum
num_1=float(input("enter the first number: "))
num_2=float(input("enter the second number: "))
sum=num_1+num_2
print("sum=",sum)

#take 2 numbers as input and find their difference
num_1=float(input("enter the first number: "))
num_2=float(input("enter the second number: "))
difference=num_1-num_2
print("difference=",difference)

#take 2 numbers as input and find their quotient
num_1=float(input("enter the first number: "))
num_2=float(input("enter the second number: "))
quotient=num_1//num_2
print("quotient=",quotient)

#take 2 numbers as input and find the remainder
num_1=float(input("enter the first number: "))
num_2=float(input("enter the second number: "))
remainder=num_1%num_2
print("remainder=",remainder)

#take 2 numbers as input and perform floor division
num_1=int(input("enter first number: "))
num_2=int(input("enter second number: "))
quotient=num_1//num_2
print("floor division=",quotient)

#take 2 numbers as input and find the first number raised to the power of the second number
num_1=int(input("enter the first number: "))
num_2=int(input("enter the second number: "))
power=num_1**num_2
print("power=",power)

#area of the rectangle using length and breadth
length_of_rectangle=int(input("enter the length of the rectangle: "))
breadth_of_rectangle=int(input("enter the breadth of the rectangle: "))
area=length_of_rectangle*breadth_of_rectangle
print("area of the rectangle=",area)

#perimeter of the rectangle
length=int(input("enter the length of the rectanle: "))
breadth=int(input("enter the breadth of the rectangle: "))
perimeter=2*(length+breadth)
print("perimeter of the rectangle=",perimeter)

#area of the circle
radius=float(input("enter the radius of the circle: "))
pi_value=float(input("enter the pi value: "))
area_of_the_circle=pi_value*radius*radius
print("area of the circle=",area_of_the_circle)

#average of 3 numbers
num_1=int(input("enter the first number: "))
num_2=int(input("enter the second number: "))
num_3=int(input("enter the third number: "))
average=(num_1+num_2+num_3)/3
print("average=",average)

#converting hours into minutes
hour=int(input("enter the hour: "))
minutes=int(input("enter minutes: "))
hour_to_min=hour*minutes
print("hour to minutes=",hour_to_min)

#convert days into hours
days=int(input("enter the number of days: "))
days_into_hours=days*24
print("days into hours=",days_into_hours)

#find the square of the number
num_1=int(input("enter the first number: "))
num_2=int(input("enter the second number: "))
square=num_1**2
print("square of the number=",square)

#simple interest
p=int(input("enter the p value: "))
r=int(input("enter the r value: "))
t=int(input("enter the t value: "))
simple_interest=(p*r*t)/100
print("simple interest=",simple_interest)

#percentage of marks obtained in 5 subjects
eng=int(input("enter english marks: "))
maths=int(input("enter maths marks: "))
kan=int(input("enter kannada marks: "))
sst=int(input("enter sst marks: "))
hindi=int(input("enter hindi marks: "))
sum=eng+maths+kan+sst+hindi
print("sum=",sum)
percentage=(sum*100)/500
print("percentage=",percentage)

