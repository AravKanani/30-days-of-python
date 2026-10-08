#day 1 of 30 days of python challenge 
# Exercise: Lvel 2

from math import hypot


print(3 + 4) #addition
print(3 - 4) #subtraction
print(3 * 4) #multiplication
print(3 / 4) #division
print(3 ** 4) #exponentials
print(3 // 4) #floor division

#Checking data types

print(type(10)) #int
print(type(9.8)) #float
print(type(4 - 4j)) #complex
print(type('Arav')) #string
print(type(['Asabeneh', 'Python', 'Finland'])) #List
print(type('Kanani')) #string
print(type('India')) #string
print(type('I am enjoying 30 days of python')) #string

#Exercise: Level 3

#Integer

print(2)
print(type(2)) #int

#Float

print(2.5)
print(type(2.5)) #float

#Complex

print(2 + 3j)
print(type(2 + 3j)) #complex

#String
print('Hello, World!')
print(type('Hello, World!')) #string

#Boolean
print(True)
print(type(True)) #boolean

#List
print([1, 2, 3, 4, 5]) #list
print(type([1, 2, 3, 4, 5])) #list

#Tuple
print((1, 2, 3, 4, 5)) #tuple
print(type((1, 2, 3, 4, 5))) #tuple

#Set
print({1, 2, 3, 10, 9}) #set
print(type({1, 2, 3, 10, 9})) #set

#Dictionary
print({'name': 'Arav', 'age': 20, 'country': 'India'}) #dictionary
print(type({'name': 'Arav', 'age': 20, 'country': 'India'})) #dictionary


#Exercise: Level 3.2 --Euclidian distance between two points

p = (2, 3)
q = (10, 8)

distance = hypot(q[0] - p[0], q[1] - p[1])
print(distance) #Euclidian distance between two points