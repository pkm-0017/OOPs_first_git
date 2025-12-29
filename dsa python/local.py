# a = 10 
# def something():
#     print( "Inside :" , a)
# something()
# print("outside :" ,a)



# def fact(n): 
#     if n == 0 or n == 1 :
#         return 1
#     return n * fact( n - 1 )
# n = int(input("Enter a number"))
# print("factorial =" ,fact(n))

def square(n):
    return n * n
def cube(n):
    return n * n * n
def operate(n , operation):
    for i in n :
        result = operation(i)
        print(result)
    
value = [5,6,7]
result = operate(value , square)
print(result)
