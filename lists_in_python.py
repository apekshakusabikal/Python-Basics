#creating list of 5 fruits
fruits=['mango','orange','banana','strawberry']
print(fruits)

numbers=[1,2,3,3,4,56,7,89,45]

#printing last number
print(numbers[6])

#print 3rd number of the list
print(numbers[3])

#length of the list
print(len(numbers))

#adding new itm at the end of the list
numbers.append(23)
print(numbers)

#inserting element at the beginning of the list
numbers.insert(0,12)
print(numbers)

#removing last element
numbers.pop()
print(numbers)

#clearing all elements from list


#replacing 2nd value with new number
numbers[2]=14
print(numbers)

#change the last element of the list
numbers[7]=9
print(numbers)

# printing only first 3 elements
print(numbers[0:3])

#printing list in reverse order
numbers.reverse()
print(numbers)

#checking whether the number exists in lists


#counting the number
print(numbers.count(3))

#finding largest number in a list
print(max(numbers))

#finding smallest number in list
print(min(numbers))

#sum of all numbers in list
print(sum(numbers))

#taking 5 numbers as input and print the largest number
numbers1=(input("enter the numbers: "))
print(max(numbers1))

#taking 5 numbers as input and print the smallest number
numbers2=(input("enter the numbers: "))
print(min(numbers2))

#for inserting many numbers
numbers.extend([3,45,46,47,48])
print(numbers)

#sorting
numbers.sort()

print(numbers[-1])
print(numbers[0])
print(numbers[-4])
print(numbers[3:4])
print(numbers[1:3])
print(numbers[0:6])
print(numbers[0:6:8])
