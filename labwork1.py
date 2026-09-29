#Ex1
r= float(input("Enter circle radius?"))
print("Circle area=",3.14*r*r)


#Ex2
c= float(input('Enter the temperature in Celcius:'))
f=1.8*c+32
print(c, "(C) =", f, "(F)")

#Ex3
n= int(input('Enter a number? '))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
            print(n,'is a prime number')
else:
            print(n,'is a NOT prime number')

#Ex4
n=int(input('Enter a number: '))
sum=0
for i in range(1, n):
    if n%i==0:
        sum= sum+ i

if sum==n:
    print(n,' is a perfect number')
else:
    print(n,' is a NOT perfect number')

#Ex5
color = ['yellow', 'red', 'white', 'purple', 'black']
opt = str(input('What is your favorite color? '))
if (opt in color):
      print('Your color is at index ', color.index(opt),'in my list')
else:
      print('Sory,I could not find your color')

#Ex6
numbs1 = range(0,7)
numbs2 = range (1,12,3)
numbs3= range(5,1,-1)
numbs4= range(6,-4,-2)
for i in numbs1:
    print(i, end=' ')
print()
for i in numbs2:
    print(i, end=' ')
print()
for i in numbs3:
    print(i, end=' ')
print()
for i in numbs4:
    print(i, end=' ')

#Ex7
def remove_dollar_sign(s):
    result = " "
    for char in s:
        if char !="$":
             result+= char
    return result
s= input("enter a sentence:")
print(remove_dollar_sign(s))

#Ex8
l=[1, 4, 5, -1, 10]
def extract_even(l):
    result= [num for num in l if num%2==0]
    return result
print(extract_even(l))

#Ex9
f=input("Enter a non-negative number:")
while f<0:
     print("Enter a non-negative number:")
def factorial_of_numbs(f):
    for i in range(1,f+1):
        result*=i
    return result
print(factorial_of_numbs(f))

#Ex10
d=int(input("Enter a number: "))
def divisors_number (d):
    div_list=[]
    for i in range (1,d+1):
         if d%i==0:
            div_list.append(i)
    return div_list
print(divisors_number(d))

#Ex11
import math
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Enter coordinates for Point 1:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("Enter coordinates for Point 2:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

result = calculate_distance(x1, y1, x2, y2)
print("The distance between the two points is:",result)

#Ex12
m = int(input("Number of rows: "))
n = int(input("Number of columns: "))
def asterisk_square(m, n):
    for row in range(m):
        if row== 0 or row== m-1:
            print("* "*n)
        else:
             print("* "," "*(n-2),"* ")
print(asterisk_square(m,n))