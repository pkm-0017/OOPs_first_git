# # import math


# # # # # # # y = 3 
# # # # # # # print(x + y)
# # # # # # # x= 9 
# # # # # # # print(x + y)
# # # # # # # print( _ + y)

# # # # # # # myname = "Pratik mohanty"
# # # # # # # len(myname)
# # # # # # # nums = [25 , 12 , 36 , 14]
# # # # # # # # print(nums)
# # # # # # # # print(nums[0])
# # # # # # # # print(nums[-1 ])
# # # # # # # names = ['Pratik' , 'Mohanty' , 'john']
# # # # # # # #  values = [9.5 , 'navin' , 25]list can of differnt types
# # # # # # # print(nums.count(14))
# # # # # # # print(nums.insert(1,55))
# # # # # # # print(nums)
# # # # # # # print(nums.remove(12))
# # # # # # # print(nums)
# # # # # # # print(nums.pop(2))
# # # # # # # print(nums)
# # # # # # # print(nums.extend([44,56,67,87]))
# # # # # # # print(nums)
# # # # # # tup = (23,45,67,89)
# # # # # # print(type(tup))
# # # # # # keys = {'pratik' , 'mohanty'  ,'keshar'}
# # # # # # values = {23,45,67}
# # # # # # dict1 = dict(zip(keys, values)) 
# # # # # # print(dict1)
# # # # # a = 'Pratik m'
# # # # # print(id(a))

# # # # # b ='Pratik m' 
# # # # # print(id(b))

# # # # # print(set(range(2,11,2)))
# # # # # print(set(range(2,11,3)))
# # # # ls =[4,5,6]
# # # # tup = (7,8)
# # # # x = list(tup)
# # # # print(x)
# # # """  function bgeinng """
# # # def add(a,b):
 
# # #     c = a + b 
# # #     return c 
    
# # # result = add(6,7)
# # # print(" result is : " , result)

# # # nums = 25 
# # # result =math.sqrt(nums)
# # # print(result)
# # # a = 5
# # # b = 6 
# # # c = a  a = a  + b 
# # # a = b  b  = a - b
# # # b = c   a = a - b f
# # # print("a :" , a)
# # # print("b :" , b)
 
# # x = int(input("enter a number "))
# # y = input("enter a number f")

# num = int(input("enter a number to check whether the number is even or odd  "))
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")    

# num = int(input("enter a number "))
# if num ==1 :
#     print("One")
# elif num ==2 :
#     print("Two")
# elif num ==3 :
#     print("Three")
# elif num ==4 :
#     print("Four")
# elif num ==5 :
#     print("Five")
# else:
#     print("else")

num = int(input("enter a number "))

match num:
    case 1 :
        print("One")
    case 2 :
        print("Two")
    case 3 :
        print("Three")
    case 4 :
        print("Four")
    case 5 :
        print("Five")
    case _:
     print("else")