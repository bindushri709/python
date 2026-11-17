

a='Good morning good afternoon'   #sclicing
print(a[-17:-21-1:-2])
print(a[-14:-10])
print(a[-14:-21:-2])
print(a[-27:-23])

s=eval(input("enter the string:"))#printing the string
print(s)
n=eval(input("enter the tuple:"))#checking the tuple
if type(n)==tuple:
    print("input is tuple")
else:
    print("input is not a tuple")
    
n=eval(input("enter the number:"))#checking even or odd
if  n%2 == 0:
     print("even")
else:
    print("odd")
    
s=eval(input("enter the tuple:"))#checking the tuple
if type(s)==tuple:
        print("it is tuple")
else:
        print("it is not a tuple")

print(ord('A'))#printing the ascii value of character

ch=input("enter character:")#checking the character is upper case or not
if 'A'<=ch<='Z':
    print("True")
else:
    print("False")
    
num=int(input("enter the number:")) #checking the number is two digit or not
if 10<=num<=99:
    print("two digit number")
else:
    print("not a two digit number")
    
num1=int(input("enter the number:")) #comparing two digits
num2=int(input("enter the number:"))
if num1<num2:
    print(f'{num1} is lesser than {num2}')
elif num1>num2:
    print(f'{num1} is greater than {num2}')
else:
    print(f'{num1} is equal to {num2}')
    
s=eval(input("enter a string:"))#checking the input is upper,lower or digit,special character
if 'A'<=s<='Z':
    print("Upper")
elif 'a'<=s<='z':
    print("Lower")
elif '0'<=s<='9':
    print("Digit")
else:
    print("Special character")
    
ch=eval(input("enter a string:"))  #checking by using inbuilt funtions
if ch.isupper():
    print("it is upper")
elif ch.islower():
    print("it is lower")
elif ch.isdigit():
    print("it is digit")
else:
    print("it is spl character")
    
ch=input("enter character:")  #performing nested if to check ch is vowel or not
if ch.isalpha():
    if ch in 'aeiouAEIOU':
        print("it is vowel")
    else:
        print("it is consonent")
else:
    print("it is number")
    
n=eval(input("Enter list:")) #checking the input is list or not and checking the length of list is even or odd by using nested if
if type(n)==list:
    if len(n)%2==0:
        print("even")
    else:
        print("odd")
else:
    print("not a list")
    
i=1
while i<=10:#printing 1 to 10 
    print(i)
    i+=1
    
s=eval(input("enter a list:"))#printing the elements in the list
i=0
while i<len(s):
    print(s[i])
    i+=1
s=[1,2,3,4]#printing the elements in the list
i=0
while i<len(s):
    print(s[i])
    i+=1
n=int(input("enter a number"))  #printing last digit

rev=0
while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
    print(rev)
for i in range(1,11): #printing 1 to 20
    print(i)
for i in range(1,6): #printing hello 5 times 
    print("hello")

s=input("enter:")#converting upper to lower
out=''
for i in s:
    if 'A'<=i<='Z':
        out=out+chr(ord(i)+32)
    else:
        out+=i
print(out)
print(chr(104))
s=input("enter:")#converting lower to upper and upper to lower
out=''
for i in s: 
    if 'a'<=i<='z':
        out=out+chr(ord(i)-32)
    elif 'A'<=i<='Z':
        out=out+chr(ord(i)+32)
    else:
        out+=i
    
print(out)

s=[12,10,'hello','Good',5j,'Bye']#converting list to dictionary
out={}
for i in s:
    if type(i)==str:
        out[i]=i[0]+i[-1]
print(out)
for i in range(1,6):#pattern printing
    for j in range(1,6):
        print('*',end=' ')
    print()
for i in range(1,6):
    for j in range(1,6):
            print('*',end=' ')
    print()
    
def convert(s):          #converting lower to upper and vice versa by using function with arguments and return
    out=''                          
    for i in s: 
        if 'a'<=i<='z':
            out=out+chr(ord(i)-32)
        elif 'A'<=i<='Z':
            out=out+chr(ord(i)+32)
        else:
            out+=i
    return out
print(convert(input("enter:")))

def convert(s):         #with args without return
    out=''                          
    for i in s: 
        if 'a'<=i<='z':
            out=out+chr(ord(i)-32)
        elif 'A'<=i<='Z':
            out=out+chr(ord(i)+32)
        else:
            out+=i
    print(out)
convert(input("enter:")) #no args  no return
def convert():
    s=input("entger:")         
    out=''                          
    for i in s: 
        if 'a'<=i<='z':
            out=out+chr(ord(i)-32)
        elif 'A'<=i<='Z':
            out=out+chr(ord(i)+32)
        else:
            out+=i
    print(out)
convert()
def convert():       #no args with return
    s=input("enter:")         
    out=''                          
    for i in s: 
        if 'a'<=i<='z':
            out=out+chr(ord(i)-32)
        elif 'A'<=i<='Z':
            out=out+chr(ord(i)+32)
        else:
            out+=i
    return(out)
print(convert())
    
    
    
    
