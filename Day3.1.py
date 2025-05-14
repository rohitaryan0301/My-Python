# today i learnt typecasting 
a=10.74
b=int(a)
print(b)

a=23.88
b=15
c=a+b
print(c)  # implicit typecasting

# explicit

string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)

#implicit

# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))