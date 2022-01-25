# QUESTION 1
string1 = "Python is a case sensitive language"
print("(a)The length of the string is ", len(string1))  # Function to find the length of the string
print("(b)The reversed string is ", string1[-1::-1])  # Reversing the string
string2 = string1[10:26]  # Stored 'a case sensitive' in a new string
string2.replace("a case sensitive", "object oriented")  # Replaced "a case sensitive" with "object oriented"
print("(e)The index of substring a is ", string1.find('a'))
print("(f)The original string after removing whitespace is", string1.replace(" ", ""))
print("\n")

# QUESTION 2
Name = input("Enter your Name ")
SID = int(input("Enter your SID "))
Department = input("Enter your Department ")
CGPA = float(input("Enter your CGPA "))
print("Hey %s," % Name, "Here!")
print("My SID is %d" % SID)
print("I am from %s" % Department, "and my CGPA is %f" % CGPA)
print("\n")

# QUESTION 3
a = 56
b = 10
print("a. ", a & b)
print("b. ", a | b)
print("c. ", a ^ b)
print("Left shift both a and b with 2 bits respectively are :", a << 2, b << 2)
print("Right shift a with 2 bits and b with 4 bits respectively are : ", a >> 2, b >> 4)
print("\n")

# QUESTION 4
a=int(input('Enter first number- '))
b=int(input('Enter second number- '))
c=int(input('Enter third number- '))
list1=[a,b,c]
print('The largest number is',max(list1))
print("\n")

# QUESTION 5
i = input("Enter the string-")
if 'name' in i:
    print("Yes")
else:
    print("No")
print("\n")

# QUESTION 6
p = int(input("Enter the first side of a triangle- "))
q = int(input("Enter the second side of a triangle- "))
r = int(input("Enter the third side of a triangle- "))
if ((p + q) > r and (q + r) > p and (r + p) > q and p > 0 and q > 0 and r > 0):
# All sides should be positive and sum of two sides should be greater than third side
    print("Yes")
else:
    print("No")