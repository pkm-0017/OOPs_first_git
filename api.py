# sum = 0 
# n = int(input("enter a number :"))
# for i in range(1,n+1):
#     sum += i 
# print(f"The sum of first {n} natural numbers is : {sum}")

# even = []
# odd = []
# n = int(input("enter a number :"))
# for i in range (2, n+1 , 1):
#     if i % 2 == 0 :
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"The even numbers are : {even}")
# print(f"The odd numbers are : {odd}")
# for i in even:
#     even = even + i

# n = int(input("enter a number :"))
# sum = 0 
# for i in  range (1, n + 1 ):
#     if n % i == 0 :
#         print(i)
#         sum +=i
# print(f" The factors of a {n} is : {i} and the sum is : {sum}" )
# n = int(input("enter a number :"))
# temp = n 
# sum = 0 
# for i in range (1,n):
#     if n % i == 0 :
#         print(i)
#         sum +=i
# print(f" The factors of a {n} is : {i} and the sum is : {sum}" )
# if temp == sum :
#     print(f"The number {n} is a perfect number")
# else:
#     print(f"The number {n} is not a perfect number")

# n = int(input("enter a number :"))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0 :
#         count += 1
# if count == 2 :
#     print(f"The number {n} is a prime number")
# else:
#     print(f"The number {n} is not a prime number")
# import random
# n = random.randint(1,11)
# tries = 0 
# while tries < 3:
#     guess = int(input("enter a number between 1 to 10 :"))
#     if n == guess :
#         print("Congratulations! You guessed it right.")
#         break
#     elif n<guess:
#         print("Go a little lower")
#         tries += 1
#     elif n>guess:
#         print("Go a little higher")
#         tries += 1
#     else:
#         print(f"Sorry, the correct number was {n}. Better luck next time!") 
#         tries += 1
# print("The game is over : The number of tries is :",tries)
# str = input("enter a word :") 
# temp = str
 
# def pallidrome(str):
#      rev = "" 
#      for i in range(len(str)-1 , -1 , -1):
#          rev += str[i]
# if temp == str :
#     print(f"The  word {str} is a pallidrome ")
# else:
#     print(f"The word  {str} is not a pallidrome")
# def hello():
#     print("hello world")
# hello()  
# l = [12,13,14,15,19]
# largest = l[0]
# second_largest = l[0]
# for i in l :
#     if i > largest :
#         second_largest = largest
#         largest = i 
#     elif i > second_largest :
#         second_largest = i    
# print(f"The largest number is : {largest}") 
# print(f"The second largest number is : {second_largest}")
# d = {10:100 , 20:200 , 30:300 , 40 :400}
# for i in d :#for i in d.values():print(i)
#     print(d[i])
# d1 = {10:100 , 20:200   , 40:300 }
# d2 = {40:400 , 50:500   , 60:600 }
# for i in d2 :
#     d1[i] = d2[i]
# print(d1)
# print(d1|d2)
# a = [1,1,1,1,2,2,2,33,33,7,8,7,8,1,9,9]
# d = {}
# for i in a :
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)
# a = int(input("enter a number :"))
# try :
#     print(10/a)
# except exception as err:
#     print("division by zero is not allowed")    
# else:
#     print("the operation is successful")
# finally:
#     print(" I will run no matter what")  
# p = open( r'api.py')
# print(p.read())
# n = int()
# r= open("keshar.txt" , "a")
# r.write("there was nothing in a file and i have created it and overwrited")
# r.close()
# class factory : 
#     def __init__(self , name , maal  , naam):
#         self.name = name 
#         self.maal = maal
#         self.naam = naam
#     def show(self):
#         print(f"the object details are {self.name} , {self.maal} , {self.naam}")
# keshar = factory("pratik" , 3 , 4 )
# keshar.show()
# class amimal :
#     name = "lion" # class attribute
#     def __init__(self ,age):
#         self.age = age  # instance attribute
        
#     def show (self):
#         print(f"How are you {self.age}") # instance method
#     @classmethod
#     def hello(cls):
#         print("how are you brother")
# Inheritance

# class mumbai:
#     a = "i am a factory from mumbai"
#     def hello(self):
#         print("Heli i am memtioned inside mumbai")
# class pune(mumbai):
#     pass
# obj = mumbai()
# obj2 = pune()
# obj2.hello()

# constuctor in inheritance  # Single inheritance
# class animal:
#     def __init__(self , name):
#         self.name = name

#     def show(self):
#         print(f"hello your name is {self.name} ")

# class Human(animal):
#     def __init__(self , name , age):
#         super().__init__(name)
#         self.age = age
#         print(f"hello your name is {self.name} , and your age is {self.age}") # method overiding
# person = Human("Pratik" , 24)
# person.show()
# from abc import ABC , abstractmethod
# class animal:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"Your name is {self.name}"
    
#     def __add__(self , other):
#         sum = 0 
#         for i in other:
#             sum += i.age
#         return f"your sum of ages are {self.age + sum}"
# obj = animal("Pratik" , 12)
# obj2 = animal("dolphin" , 14)
# obj3 = animal("dhello" , 18)
# print(obj+ (obj2,obj3))

# def decorate(func):
#     def wrapper():
#         print("I will print before the function")
#         func()
#         print("I will call after the function")
#     return wrapper
    
# @decorate
# def hello():
#     print("Hello I am Pratik Mohanty")
# hello()

# def add(*args ):
#     sum = 0 
#     for i in args:
#         sum = sum + i
#     print(sum)
# add(4,5 , 6, 7 , 8 )
# def info(**kwargs):
#     print("Your info is ")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]} ")
# info(name = "Pratik" , age = 23 , des = "Ai/Ml")
# l = [i for i in range(1,21) if i % 2==0]
# print(l)
# l = {i  : i**2 for i in range(1,11)}
# print(l)
# def add(a,b):
#     print(a+b)
# add(12,13)
# add = lambda a :"even" if a%2== 0 else "odd"
# print(add(12,13))

#MAP
# a = [1,2,3,4,5]
# result = map(lambda x : x**2 , a)
# print(list(result))
#filter   filter works only on true and false
def even(x):
     if x % 2 == 0 :
         return True
     else :
         return False
a = [1,2,3,4,5,5,6,7,89,10,90]
result = filter(even,a)
print(list(result))
# hello