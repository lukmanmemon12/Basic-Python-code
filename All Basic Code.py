# program 1
a=int(input("enter a no:"))

if a==10:
    print("A value is 10")
elif a<10:
        print("A is < 10")
else:
        print("A is > 10")
               
# program 2               

a=int(input("Enter nu1:"))
if a<0:
    print("Plz Enter positive number")
else:
     if a>10:
            print("Enter value <10")
     else:
            print("Thank you for number")

# program 3

a  = int(input("Enter no1:"))
b  = int(input("Enetr no 2"))
c  = int(input("Enter no3:"))
if a==b==c:
    print("Both are same")
elif a>b and a>c:
    print("A  is Bigger")
elif b>a and b>c:
    print("B is Bigger")
elif c>b and c>a:
    print("C is bigger")
else:
    print("technical error")    
    
    #program 4

    x = 10
y =5

# addition
print("sum:", x+y)

#subtraction

print("subtration: ",x -y)

#multiplication

print("multiplication:", x * y)

# division

print("division:",x / y)

#floor division
print("floor division:", x//y)

#modulo

print("odulo:",x%y)

#  x to the power y
print("Powern: ", x**y)

#program 5

ch = input("Enter a character")

if (ch =='a' or ch =='e' or ch =='i' or  ch=='o' or ch =='u'):
        print(ch, "is a vowel")
else:
            print(ch, "is a consonant") 
                   
#program 6

x =int(input("Enter no1:"))

print(not(x> 1 and x < 10))

# program 7

mylist = [10,20.5, "Hello"]
n1 = 10
n2 = 100

print(n1 in mylist)

print(n2 in mylist)

print(n2 not in mylist)

# program 8

mylist1 =[10,20]
mylist2 =[10,20]
mylist3 =mylist1 

print(mylist1 is mylist3)

print(mylist1 is mylist2)


print(mylist1 == mylist2) 


print(mylist1 is not mylist2)

# program 9

name = "Akash technolabs"
print(name[0])
print(name[0:5])
print(name[6:])
print(name*2)

# program 10

n1 = 10
n2 = 20.5
n3 = 10+5j

print(n1, type(n1))
print(n2, type(n2))
print(n3, type(n3))
print(n1+n2)
print()


n1 = str(n1)
n2 = str(n2)
n3 = str(n3)

print(n1, type(n1))
print(n2, type(n2))
print(n3, type(n3))
print(n1+n2)

#program 11

value = [10,20,30.5, "hello","world"]

print("List values")
print(value)

ans = tuple(value)

print("Tuple1 values")
print(ans)
print(type(ans))

#program 12

a  = 33
b  = 200
if b > a:
    print("B is greate than A")
print('Bye')

# program 13

no1 = int(input("Enter no:"))

if no1==10:
    print("no1 is 10")
elif no1<10:
    print("no1 is <10")
else:
    print("no1 is >10") 

# program 14    

a = 10
match a:
    case 1:
        print("one")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("select 1-3")    

# program 15

        ch = int(input("Enter choice:"))
match ch:
    case 1:
        print("This is one")
    case 2:
        print("This is two")
    case 3:
        print("This is three")
    case _:
        print("invalid value") 

# program 16

n1 = 11
if n1>0:
    if n1==10:
        print("n1 is 10")
    elif n1>10:
        print("n1 is >10")
    else:
        print("n1 is <10")
else:
    print("ENter Positive value")  

# program 17

mystring = f"The price is {20*59}dollars"
print(mystring)

price = 59
tax = 0.25
tax = f"The price is {price +(price + tax)} dollars"
print(tax)

Name ='Ap'
age = 22
print(f"HEllo, My Name is {Name} and my age is {age} years old.")

# program 18

no1 = input("ENter No1:")
no2 = input("ENter NO2:")
c = int(no1) +int(no2)
# method 1
print("A value is ", no1,"B value is",no2,"Sum is",c)
#method 2
print("A value is {} b value is {} sum is {}".format(no1,no2,c))
#method 3
print(f"A value is {no1} b value is {no2} sum is {c}")

# program 19

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if a>b:

    print("maximum=",a)
    print("minimum=",b)
else:
    print("maximum=",b)
    print("minimum=",a)

# program 20

a = 10
b = 20.50
c = a+b
print(" A Type is ", type(a),"Value is", a)
print(" B Type is ", type(b),"Value is", b)
print(" C Type is ", type(c),"Value is", c)    
                                      