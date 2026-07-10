#1
a=10
b=10
print(a is b)

#2
x=[1,2,3]
y=[1,2,3]
print(x is y)

#3
x=[1,2,3]
y=x
print(x is y)

#4
a="Python"
b="Python"
print(a is b)

#5
a=50
b=100
print(a is b)

#6
a='none'
print(a is a)

#7
a= True
b=False
print(a is not b)

#8
a=5
b='5'
print(a is b)
print(a is not b)
print(id(a))
print(id(b))