# # # data = [2 , 'Pratik' , 4,5  , 4.5 , 'Mohanty']
# # # # i = 0 
# # # # while i <= 5 :
# # # #     print(data[i])
# # # #     i += 1
# # # for value in range(10):
# # #     if value % 3 == 0:
# # #         continue
# # #     print(value )
# # """"  copying of one array to another is possible , if u want to chnage in 1st array  """
# from array import * 
# arr1 = array("i" , [33,45,56,67,78])
# # arr2 = array(arr1.typecode , arr1.tolist())
# arr2 = array(arr1.typecode , (n for n in arr1))
# arr1[2] = 54
# print(arr1)
# print(arr2) 
# def add (num1 , num2  = 0):# default argument                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
#     return num1+ num2
# def add (num1 , *num2):# varibale length argument                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
#     sum = num1 
#     for n in num2:
#         sum += n 
#     return sum
# result = add(4 ,5 ,6 , 7)
# print(result)
# def person(name , **subject ): # keyword arguments
#     print("name  :" , name)
#     for k  , v in subject.items():
#         print(k , "  : " ,v)
    
# person( name ='Navin' , age = 16 , loc = 'Jk' , tech = 'java')
# def alg(name , ** subject):
#     print("Name :" , name)
#     for k , v in subject.items():
#         print(k, " : " ,  v)
        
# alg(name = 'Pratik' , loc = 'jha' , city = 'jamshedpur' , fl = 'Python')

