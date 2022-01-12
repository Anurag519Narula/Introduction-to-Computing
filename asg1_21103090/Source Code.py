#Assignment 1

#Soln 1
#Calculating average of three numbers
print("Question 1")
a=int(input("Enter first number-"))
b=int(input("Enter second number-"))
c=int(input("Enter third number-"))
d=(a+b+c)/3
print("The average of the entered numbers is-",d)

#Soln 2
#Finding a person's income tax
print("Question 2")
x=int(input("Enter your Gross Income (in nearest penny)- $ "))  #input of gross income by user
y=int(input("Enter the number of Dependents- "))  #number of dependents
z=x-10000-(y*3000)  #calculating tax income
t=z*0.2  #Total tax
print("Your tax is $ ",t)

#Soln 3
#Storing data of students
print("Question 3")
SID=int(input("Enter your SID- "))
Name=str(input("Enter your Name- "))
Gender=str(input("Enter your Gender (M/F/U)- "))
Course_Name=str(input("Enter your Engineering Course- "))
CGPA=float(input("Enter your CGPA- "))
Profile=[SID,Name,Gender,Course_Name,CGPA]
print(Profile)

#Soln 4
#Taking input and arranging them
std1=int(input("Enter marks of 1st student- "))
std2=int(input("Enter marks of 2nd student- "))
std3=int(input("Enter marks of 3rd student- "))
std4=int(input("Enter marks of 4th student- "))
std5=int(input("Enter marks of 5th student- "))
#presenting these marks in a list and sorting them
marks_list=[std1,std2,std3,std4,std5]
marks_list.sort()
print("Marks list (increasing order)")
print(marks_list)
marks_list.reverse()
print("Marks list (decreasing order)",)
print(marks_list)

#Soln 5(a)
#Make a list after removing 4th element
print("Question 5 (a)")
color_list = ['Red','Green','White','Black','Pink','Yellow']
color_list.remove('Black')  #Since black is at the 4th position
print(color_list)

#Soln 5(b)
#Replace black and pink to purple
print("Question 5 (b)")
color_list = ['Red','Green','White','Black','Pink','Yellow']
color_list[3:5]=['Purple']  #Replacing black and pink to purple
print(color_list)
