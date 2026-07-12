#largest number among 3 numbers
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
if(a>b and a>c):
    print(" a is the largest of 3 numbers")
elif(b>a and b>c):
    print("b is the largest of 3 numbers")
elif(c>a and c>b):
    print("c is the largest of 3 numbers")
else:
        print("there is no larger number")
        
#check whether a character is vowel or a consonant
ch=input("enter a character: ")
if(ch in "aeiouAEIOU"):
    print("this character is a vowel")
else:
    print("it is a consonant")
    
#check whether the student is passed or fail
marks=int(input("enter the marks: "))
if(marks<=35):
    print("FAIL")
else:
    print("PASS")
    
#printing grades
marks=int(input("enter the marks of a: "))
if(marks>90):
    print("Grade A")
elif(marks>75<89):
    print("Grade B")
elif(marks>50<74):
    print("Grade C")
else:
        print("FAIL")

