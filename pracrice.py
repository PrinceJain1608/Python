'''
print("prince jain");
a=4;
b=6;
c=a+b;
print(a+b);
print("Addition =",a+b);
print("Addition of ",a,"&" ,b, "is",c)
Name=input("Enter your name:");
print(Name);
c=int(input("enter number 1st:"));
d=int(input("enter number 2nd:"));
Add=c+d;
print(Add);
print(2**-100);
print(5//-2);
a=4;
b=3;
c=5.3;
print(not(a>b) or (b>a));
print(type(c));
if(type(c) is not int):
    print("true");
else:
    print("tata");

a=5;
b=3;
r=2;
print("addition =",a+b);
print("subtraction =",a-b);
print("multiplication =",a*b);
print("division =",a/b);
print("area of rectangle =",a*b);
print("perimater of rectangle =",2*(a+b));
print("area of square =",a*a);
print("perimeter of square =",4*a);
print("area of circle =",3.14*r*r);
print("circumference of circle =",2*3.14*r);

electricity=int(input("enter electricity unit consumption:"));
total_price=electricity*5;
price_to_be_given=total_price-(total_price*10)/100;
print("total bill is of amount: ",price_to_be_given);

a=int(input("enter marks of 1st subject:"));
b=int(input("enter marks of 2st subject:"));
c=int(input("enter marks of 3st subject:"));
d=int(input("enter marks of 4st subject:"));
e=int(input("enter marks of 5st subject:"));
total_marks=a+b+c+d+e;
percentage=(total_marks*100)/500;
print("percentage =",percentage);

sales=int(input("enter total sales:"));
profit=(sales*5)/100;
print("total profit =",profit);

a=5;
b=3;
print("original values are ",a,"and",b);
c=a;
a=b;
b=c;
print("swapped values are ",a,"and",b);

age=int(input("enter your age:"));
if age>=18:
     print("eligible for voting");
else:
    print("not eligible for voting");

a=int(input("enter 1st number:"));
b=int(input("enter 2nd number:"));
if a>b:
      print(a,"is max number");
else:
    print(b,"is max number");

a=int(input("enter 1st number:"));
b=int(input("enter 2nd number:"));
c=int(input("enter 3rd number:"));
if a>b and a>c:
      print(a,"is max number");
elif b>a and b>c:
    print(b,"is max number");
else:
    print(c,"is max number");

    print(b,"is max number");

a=int(input("enter number:"));
if a>0:
    print("positive");
elif a<0:
    print("negative");
else:
    print("zero");

a=int(input("enter 1st number:"));
b=int(input("enter 2nd number:"));
c=int(input("enter 3rd number:"));
if (a>b and a<c) or (a<b and a>c):
    print(a,"is middle number");
elif (b>a and b<c) or (b<a and b>c):
    print(b,"is middle number");
else:
    print(c,"is middle number");

a=int(input("enter marks of 1st subject:"));
b=int(input("enter marks of 2st subject:"));
c=int(input("enter marks of 3st subject:"));
d=int(input("enter marks of 4st subject:"));
e=int(input("enter marks of 5st subject:"));
total_marks=a+b+c+d+e;
percentage=(total_marks*100)/500;
print("percentage =",percentage);
if percentage>=80:
    print("grade A");
elif percentage>=60:
    print("grade B");
elif percentage>=40:
    print("grade C");
else:
    print("grade D");

i=1;
for i in range(1,11):
    print(i);

i=1;
n=int(input("enter number"));
while(i<=n):
    print(i);
    i=i+1;

i=int(input("enter number:"));
while(i>=1):
    print(i);
    i=i-1;

n=int(input("enter number:"));
i=1;
sum=0;
while(i<=n):
    sum=sum+i;
    i=i+1;
print(sum);

n=int(input("enter number:"));
i=1;
sum=0;
j=1;
while(i<=n):
    j=i*i;
    sum=sum+j;
    i=i+1;
print(sum);

n=int(input("enter number:"));
i=1;
sum=0;
j=1;
while(i<=n):
    j=i*i*i;
    sum=sum+j;
    i=i+1;
print(sum);

n=int(input("enter number:"));
i=0;
sum=0;
while(i<=n):
    sum=sum+i;
    i=i+2;
print(sum);

n=int(input("enter number:"));
i=1;
sum=0;
count=0;
while(count<n):
    if i%2==0:
        sum=sum+i;
        count=count+1;
    i=i+1;
print(sum);

n=int(input("enter number:"));
sum=0;
while(n>0):
    sum=sum+ n%10;
    n=n//10;
print("sum of digits is:",sum);

n=int(input("enter number:"));
sum=0;
while(n>0):
    digit=n%10;
    j=digit*digit;
    sum=sum+j;
    n=n//10;
print(sum);

n=int(input("enter number:"));
sum=0;
while(n>0):
    digit=n%10;
    j=digit*digit*digit;
    sum=sum+j;
    n=n//10;
print(sum);

n=int(input("enter number:"));
orig=n;
sum=0;
while(n>0):
    digit=n%10;
    j=digit*digit*digit;
    sum=sum+j;
    n=n//10;
if(sum==orig):
    print("armstrong number");
else:
    print("not armstrong number");

n=int(input("enter number:"));
count=0;
i=n;
while(i>0):
    i=i//10;
    count=count+1;
sum=0;
i=n;
while(i>0):
    digit=i%10;
    prod=1;
    x=1;
    while(x<=count):
        prod=prod*digit;
        x=x+1;
    sum=sum+prod;
    i=i//10;
if(sum==n):
    print("armstrong number");
else:
    print("not armstrong number");

n=int(input("enter number;"));
prod=1;
while(n>0):
    prod=prod*(n%10);
    n=n//10;
print("product of digits:",prod);

n=int(input("enter number:"));
rev=0;
while(n>0):
    rev=(rev*10) + (n%10);
    n=n//10;
print("reverse number is:",rev);

n=int(input("enter number:"));
rev=0;
z=n;
while(n>0):
    rev=(rev*10) + (n%10);
    n=n//10;
if(rev==z):
    print("palindrome");
else:
    print("not palindrome");

n=int(input("enter number:"));
count=0;
i=1;
while(i<=n):
    if(n%i==0):
        count=count+1;
    i=i+1;
if(count==2):
    print("prime");
else:
    print("not prime");

n=int(input("enter number:"));
fac=1;
i=1;
while(i<=n):
    fac=fac*i;
    i=i+1;
print("factorial:",fac);

n=int(input("enter number:"));
a=0;
b=1;
z=0;
while(z<=n):
    print(z);
    a=b;
    b=z;
    z=a+b;

n=int(input("enter number:"));
i=1;
while i<n:
    j=1;
    while j<=i:
        print(i,end=" ");
        j=j+1;
    print();
    i=i+1;

n=int(input("enter number:"));
i=1;
while i<n:
    j=1;
    while j<=i:
        print("*",end=" ");
        j=j+1;
    print();
    i=i+1;

for i in range(1,11):
    print(i);

for i in range(1,101,5):
    print(i);

for i in range(2,21,2):
    print(i);
else:
    print("program terminated");

n=int(input("enter number:"));
i=1;
while(i<=10):
    print(n,"*",i,"=",n*i);
    i=i+1;

def message():
    print("prince jain");
message();

def calc():
    a=int(input("enter 1st number:"));
    b=int(input("enter 2nd number:"));
    c=a+b;
    print("sum =",c);
calc();
calc();
calc();

def sum(a,b):
    c=a+b;
    print("addition =",c);
sum(88,12);

def oddev():
    n=int(input("enter any number:"));
    if n%2==0:
        print("even number");
    else:
        print("odd number");
oddev();

def oddev(n):
    if n%2==0:
        print("even number");
    else:
        print("odd number");
n=int(input("enter number:"));
oddev(n);

def sum(a,b):
    c=a+b;
    return c;
a=int(input("enter 1st number:"));
b=int(input("enter 2nd number:"));
x=sum(a,b);
print("sum =",x);

def sum(a,b,c=2):
    print("addition =",a+b+c);
sum(2,3,7);

i=1;
while(i<=5):
    if i==3:
        break;
    print(i);
    i=i+1;

i=0;
while(i<=5):
    i=i+1;
    if i==3:
        continue;
    print(i);

name="Prince Jain";
for i in name:
    print(i,end="");

print("namaste "+"duniya");
print("Prince"*3);
name="prince";
print("q" in name);

name="prince";
print(name[2]);

str="prince jain";
a=str[2:-3];
print(a);

name="prince jain";
a=name.capitalize();
print(a);

name="prince jain";
a=len(name);
print(a);

str="prince jain";
for i in range(0,len(str)):
    print(str[i],end="");

str="prince jain";
print(str[-1::-1]);

a="prince hello";
for i in range((len(a)-1),-1,-1):
    print(a[i],end="");

name=input("enter name:");
vowel=0;
consonant=0;
for i in range(0,len(name)):
    if name[i]=="a" or name[i]== "e" or name[i]=="i" or name[i]=="o" or name[i]=="u" or name[i]=="A" or name[i]== "E" or name[i]=="I" or name[i]=="O" or name[i]=="U":
        vowel=vowel+1;
    else:
        consonant=consonant+1;
print("total vowels are:",vowel);
print("total consonants are:",consonant);

a="prince";
b=a.capitalize();
a=b;
print(a);

a="hello bro my name is prince";
b="is";
print(a.find(b,0,len(a)-1));

a=int(input("enter number:"));
b=int(input("enter number:"));
c=a+b;
print("addition:",c,sep="",end="");

a=input();
b=input("likes",);
print(a,b);

def table(n, i):
    if (i > 10):
        return;
    print(n,"*",i,"=",n*i);
    return table(n,i+1);
n = 5;
table(n,1);

name=input("enter string:");
a=name[-1::-1];
if a==name:
    print("palindrome string");
else:
    print("not a palindrome string");

name="o";
print(name.isalnum());

name="54";
print(name.isdigit());

name=" bi  ";
print(name.isspace());

a=["prince",100,"jain",9.47];
print(a);
print(a[1]);
print(a[-1]);
print(a[2]);
a[0]="hello";
print(a);

a=["prince",100,"jain",9.47,"okay"];
print(a[::-1]);

a=["prince",100,"jain",9.47];
del(a[1]);
print(a);

a=["prince",100,"jain",9.47];
for i in a:
    print(i);

a=["prince",100,"jain",9.47];
for i in range(0,len(a)):
    print(a[i]);

a=[34,22,55,12,32];
b=max(a);
print(b);
a=["prince","okay","jain","anna"];
b=min(a);
print(b);

l1=[1,5,3,2];
l2=[1,4,3,2];
print(cmp(l1,l2));

p=10000;
r=5;
t=2;
si=(p*r*t)/100;
print("simple interest is",si);

a=int(input("enter 1st number:"));
b=int(input("enter 2nd number:"));
c=int(input("enter 3rd number:"));
d=int(input("enter 4th number:"));
avg=(a+b+c+d)/4;
print("average=",avg);

r=int(input("enter radius:"));
peri=2*3.14*r;
print("perimeter of circle=",peri);

n=int(input("enter number:"));
sum=0;
while(n>0):
    sum=sum+(n%10);
    n=n//10;
print("sum of digits=",sum);

l=int(input("enter length:"));
b=int(input("enter breadth:"));
area=l*b;
print("area of rectangle=",area);

list=["hello","bye","tata","namaste"];
list.append("bonne nuit");
print(list);

a=[];
for i in range(3):
    x=input("enter name:");
    a.append(x);
print(a);

list=["hello","bye","tata","namaste","bye"];
a=list.count("bye");
print(a);

a=[];
for i in range(5):
    x=input("enter name:");
    a.append(x);
f=input("enter name of which you want to count:");
b=a.count(f);
print(b);

a=[];
for i in range(5):
    x=input("enter name:");
    a.append(x);
print(a);
f=input("enter name of which you want to count:");
b=a.index(f);
print(b);

a=[];
for i in range(4):
    x=input("enter name:");
    a.append(x);
print(a);
f=input("enter name to add in the list:");
p=int(input("enter position:"));
a.insert(p,f);
print(a);

a=[];
for i in range(4):
    x=input("enter name:");
    a.append(x);
print(a);
p=input("enter element which you want to delete the element:");
a.remove(p);
print(a);

a=[];
for i in range(4):
    x=input("enter string:");
    a.append(x);
print(a);
a.reverse();
print(a);

a=[];
for i in range(4):
    x=int(input("enter number:"));
    a.append(x);
print(a);
a.sort();
print(a);

a=[];
for i in range(5):
    x=input("enter name:");
    a.append(x);
print(a);
p=int(input("enter index which you want to remove:"));
a.pop(p);
print(a);

a=[];
x=int(input("enter total values:"));
for i in range(x):
    b=int(input("enter numbers:"));
    a.append(b);
print(a);
sum=0;
for i in range(len(a)):
    sum=sum+a[i];
    i=i+1;
print("sum of numbers =",sum);

a=[];
x=int(input("enter total values:"));
for i in range(x):
    b=int(input("enter numbers:"));
    a.append(b);
print(a);
eve=0;
odd=0;
for i in range(len(a)):
    if(a[i]%2==0):
        eve=eve+1;
    else:
        odd=odd+1;
print("total even numbers =",eve);
print("total odd numbers =",odd);

a=[];
x=int(input("enter total values:"));
for i in range(x):
    b=int(input("enter numbers:"));
    a.append(b);
print(a);
eve=0;
odd=1;
for i in range(len(a)):
    if(a[i]%2==0):
        eve=eve+a[i];
    else:
        odd=odd*a[i];
print("sum of even numbers =",eve);
print("product of odd numbers =",odd);

a=[];
x=int(input("enter total values:"));
for i in range(x):
    b=int(input("enter numbers:"));
    a.append(b);
print(a);
key=int(input("enter element you want to search:"))
s=0;
e=len(a)-1;
while(s<=e):
    
    if(a[i]==key):
        print("key is present");
        break;
    else:
        print("key is absent");
        break;

a=[];
x=int(input("enter total values:"));
for i in range(x):
    b=int(input("enter numbers:"));
    a.append(b);
print(a);
key=int(input("enter number:"));
freq=0;
for i in range(len(a)):
    if(a[i]==key):
        freq=freq+1;
print("frequency of a given number is ",freq);

a=2 and 5;
print(a);


a=[];
for i in range(5):
    x=int(input("enter number:"));
    a.append(x);
print(a);
x=min(a);
print(x);

a=[];
for i in range(5):
    x=int(input("enter number:"));
    a.append(x);
print(a);
x=max(a);
print(x);

a=[1,2,3,4,5];
a.insert(2,"hello");
print(a);


a=[1,2,3,4,5];
a.remove(4);
print(a);

a=[];
x=int(input("enter total values:"));
for i in range(x):
    b=int(input("enter numbers:"));
    a.append(b);
print(a);
key=int(input("enter element you want to search:"));
flag=0;
for i in range(x):
    if(a[i]==key):
        flag=1;
        pos=i+1;
        break;
if(flag==1):
    print("key is present");
else:
    print("key is absent");


a=[];
b=int(input("enter total values:"));
for i in range(b):
    x=int(input("enter numbers:"));
    a.append(x);
print(a);
max=a[0];
for i in range(b):
    if(a[i]>max):
        max=a[i];
print("max number is ",max);
print(ord("a"));

a=[];
b=int(input("enter total values:"));
for i in range(b):
    x=int(input("enter numbers:"));
    a.append(x);
print(a);
min=a[0];
for i in range(b):
    if(a[i]<min):
        min=a[i];
print("min number is ",min);

a=[];
x=int(input("enter values:"));
for i in range(x):
    p=int(input("enter numbers"));
    a.append(p);
print(a);
a.reverse();
print(a);

a=[1,2,3,4,5];
a.sort(reverse=True)
print(a);
maxx=a[1];
print("second max value is ",maxx);

import sys
l=[1,2,3,4,5];
t=(1,2,3,4,5);
s=("hello");
print("space occupied by list is ",sys.getsizeof(l));
print("space occupied by tuple is ",sys.getsizeof(t));
print("space occupied by string is ",sys.getsizeof(s));

import timeit
listtime=timeit.timeit(stmt="[1,2,3,4,5]",number=1000000);
tupletime=timeit.timeit(stmt="(1,2,3,4,5)",number=1000000);
print("list time is ",listtime);
print("tuple time is ",tupletime);

t1=(2);
print(type(t1));
t2=(2,);
print(type(t2));
list1="prince";
tuple1=tuple(list1);
print(tuple1);

tuple1=(1,2,3,4,5);
for i in range(len(tuple1)):
    print(tuple1[i]);
tuple2=(6,7,8);
tuple3=tuple1+tuple2;
print(tuple3);
ind=tuple1.index(3);
cou=tuple1.count(1);
print(ind);
print(cou);

t1=("prince","jain","hai",5,7,9);
l1=list(t1);
print(l1);
l1[3]=8;
t1=tuple(l1);
print(t1);
if "prince" in t1:
    print("yes");
else:
    print("no");
print(t1);
del t1;
print(t1);

dict1={1:"hello",2:"prince",3:"jain"};
print(dict1);
x=dict1[2];
print(x);
for i in dict1:
    print(dict1[i]);

dict1={1:"hello",2:"prince",3:"jain"};  
for i in dict1.values():
    print(i);

dict1={1:"hello",2:"prince",3:"jain",4:"henamontena",5:"acha"};
for x,y in dict1.items():
    print(x,y);
dict1.pop(1);
print(dict1);
dict1.popitem();
print(dict1);
dict1.clear();
print(dict1);

dict1={1:"hello",2:"prince",3:"jain",4:"henamontena",5:"acha"};
x=dict1.copy();
print(x);
for i in dict1.items():
    print(i);

dict1=(1,2,3,4);
dict2=(234,34,12,687);
dict3=dict.fromkeys(dict1,dict2);
print(dict3);

dict1={1:"hello",2:"prince",3:"jain",4:"henamontena",5:"acha"};
x=dict1.setdefault(0,"bro");
print(x);
print(dict1);
dict1.update({6:"yellow"});
print(dict1);

dict1={1:"hello",2:"prince",3:"jain",4:"henamontena",5:"acha"};
x=dict1.keys();
print(x);
key=int(input("enter key to search:"));
if key in dict1:
    print("key=",key,"and value=",dict1[key]);
else:
    print("no");

print("prince \"jain\" hello")
print("this is a \"book\"")
print("don\'t do this");

a="jain";
print("hello",a);
  # app=hello prince
  #    how are you
  #    are you good
for i in range(0,len(app)):
    print(app[i]);

a=int(input("enter number:"));
b=float(input("enter number:"));
c=complex(input("enter number"));
print(a,"is type of",type(a));
print(b,"is type of",type(b));
print(c,"is type of",type(c));

a=int(input("enter 1st number:"));
b=int(input("enter 2nd number:"));
print("addition=",a+b);
print("subtraction=",a-b);
print("multiplication=",a*b);
print("division=",a/b);
print("remainder=",a%b);
print("floor division=",a//b);
print("exponential=",a**b);

import random
a=random.randint(1,6);
print(a);

a=int(input("enter 1st number:"));
b=int(input("enter 2nd number:"));
print("numbers before swapping are:",a,b);
a,b=b,a;
print("numbers after swapping are:",a,b);

r=float(input("enter radius of sphere:"));
vol=(4*3.14*r*r*r)/3;
print("volume of sphere is ",vol);

l=[55,67,6,28,8]
m=l.copy();
m.insert(0,100)
print(m)

import phonenumbers
from phonenumbers import carrier,geocoder,timezone
mobileNo=input("Mobile no. with country code:")
mobileNo=phonenumbers.parse(mobileNo)
print(timezone.time_zones_for_number(mobileNo))
print(carrier.name_for_number(mobileNo,"en"))
print(geocoder.description_for_number(mobileNo,"en"))
print("Valid Mobile Number:",phonenumbers.is_valid_number(mobileNo))
print("Checking possibility of Number:",phonenumbers.is_possible_number(mobileNo))

a="!!! hello !!!";
print(a.rstrip("!"));
print(a.lstrip("!"));
print(a.strip("!"));
print(a.replace("hello","prince"));
print(a.split());
b="hello HOW ARE  are are You";
print(b.capitalize());
print(b.center(50));
print(b.count("o"));
print(a.endswith("!"));
print(b.find("are"));
print(b.index("are"));
print(a.isalnum());
print(b.isupper());
print(b.isprintable());
c="Hii Bro";
print(c.istitle());
print(b.swapcase());
print(b.title());

n=float(input("enter time:"));
if(n>=4 and n<=11.59):
    print("good morning");
elif(n>=12 and n<=15.59):
    print("good afternoon");
elif(n>=14 and n<=21.59):
    print("good evening");
else:
    print("good night");

n=int(input("enter number:"));
match n:
    case 0:
        print("zero");
    case 1:
        print("namaste");
    case _ if(n!=90):
        print("not 90");
    case _ if(n!=80):
        print("not 80");
    case _:
        print(x);

n=["prince","jain"];
for name in n:
    print(name);
    for hallo in name:
        print(hallo);

i=1;
n=int(input("enter number:"));
while(i<=n):
    p=i*i;
    print(p);
    i=i+1;

a="Ujjwal Is Very Nalayak Londa";
up=0;
lo=0;
for i in a:
    if(i.isupper()):
        up=up+1;
    elif(i.islower()):
        lo=lo+1;
    else:
        pass;
print("uppercase=",up);
print("lowercase=",lo);

lst=[2*i for i in range(5)];
print(lst);

lst=[i for i in range(11) if(i%2==0)];
print(lst);

str="hello my name is {} and i am from {}";
name="prince jain";
country="India";
print(str.format(name,country));

name="prince jain";
country="India";
str=(f"hello my name is {name} and i am from {country}");
print(str);

str=(f"hello my name is {{name}} and i am from {{country}}");
print(str);

import this

def hii():
    this is the hii function;
    print("hello");
print(hii.__doc__);
hii();

def fac(n):
    if(n==0 or n==1):
        return 1;
    else:
        return n*fac(n-1);
print(fac(5));

def fib(n):
    if(n==0):
        return 0;
    elif(n==1):
        return 1;
    else:
        return fib(n-1)+fib(n-2);
print(fib(2));

a=set();
print(type(a));
b={12,12,3,4,4,3};
print(b);

a={1,2,3,4,4};
b={3,5,7,5};
print(a.union(b));
print(a.intersection(b));
a.update(b);
print(a,b);
print(a.symmetric_difference(b));

dict={509:"siddharth",510:"khushi",517:"ujjwal",567:"prince"};
print(dict);
print(dict.keys());
print(dict.values());
for key in dict.keys():
    print(dict[key]);

dict={509:"siddharth",510:"khushi",517:"ujjwal",567:"prince"};
for i in dict.items():
    print(i);

a=input("enter number:");
b=input("enter number:");
try:
    c=a/b;
    print(c);
except:
    print("sorry some error occured");

try:
    n=int(input("enter number:"));
    for i in range(1,11):
        print(n,"*",i,"=",n*i);
except Exception as e:
    print(e);

n=int(input("enter year:"));
if(n%400==0) or (n%4==0 and n%100 != 0):
   # print(n,"is a leap year");
    print(n," is leap yr");
else:
    print(n,"is not a leap year"); 
    
a=int(input("enter 1st number:"));
b=int(input("enter 2nd number:"));
c=int(input("enter 3rd number:"));
if(a>b and a>c):
    print(a,"is max number");
elif(b>c):
    print(b,"is max number");
else:
    print(c,"is max number");

n=int(input("enter number:"));
l=len(str(n));
s=0;
i=n;
while(i!=0):
    digit=i%10;
    s=s+digit**l;
    i=i//10;
if(n==s):
    print("armstrong number");
else:
    print("not an armstrong number");

n=int(input("enter number:"));
if(n>0):
    print(n,"is positive");
elif(n<0):
    print(n,"is negative");
else:
    print("zero");

marks=int(input("enter marks:"));
if(marks>=80):
    print("excellent");
elif(marks>=65 and marks<80):
    print("good");
elif(marks>=50 and marks<65):
    print("pass");
else:
    print("fail");

n=int(input("enter number:"));
count=0;
i=1;
while(i<=n):
    if(n%i==0):
        count=count+1;
    i=i+1;
if(count==2):
    print("prime number");
else:
    print("not a prime number");
    
a=int(input("enter starting number"));
b=int(input("enter ending number:"));
for num in range(a,b+1):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break;
        else:
            print(num);

n=int(input("enter number:"));
fac=1;
while(n>=1):
    fac=fac*n;
    n=n-1;
print(fac);  

a=int(input("enter number:"));
b=int(input("enter number:"));
for num in range(a,b+1):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break;
        else:
            print(num);

n=int(input("enter number:"));
i=1;
while(i<=10):
    print(n,"*",i,"=",n*i);
    i=i+1;

n=int(input("enter number:"));
z=n;
rev=0;
while(n!=0):
    rev=rev*10 + n%10;
    n=n//10;
if(rev==z):
    print("palindrome number");
else:
    print("not palindrome number");

n=int(input("enter number:"));
a=0;
b=1;
c=0;
while(c<=n):
    print(c);
    a=b;
    b=c;
    c=a+b;

for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=" ");
    print();

n=int(input("enter number:"));
for p in range(0,n):
    for q in range(0,p+1):
        print("*",end=" ");
    print();
for i in range(0,n):
    for j in range(0,n-i):
        print("*",end=" ");
    print();

a=int(input("enter number:"));
b=int(input("enter number:"));
for num in range(a,b+1):
    if num>1:
        for j in range(2,num):
            if(num%j==0):
                break;
        else:
            print(num);
          
a = int(input("enter number:"));
b = int(input("enter number:"));
for i in range(a,b+1):
   odr = len(str(i))
   sum = 0
   tem = i
   while tem > 0:
       digit = tem % 10
       sum += digit ** odr
       tem //= 10
   if i == sum:
       print("The Armstrong numbers are: ",i)
       
n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ");
    print();

n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(j,end=" ");
    print();

n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ");
    print();

n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("*",end=" ");
    print();

n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+64),end=" ");
    print();

n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(chr(j+64),end=" ");
    print();

n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ");
    for j in range(1,i+1):
        print(j," ",end=" ");
    print();

n=int(input("enter number:"));
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end=" ");
    for j in range(1,i+1):
        print(j," ",end=" ");
    print();

n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ");
    for j in range(1,i+1):
        print("*",end=" ");
    print();

n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("",end=" ");
    for j in range(1,i+1):
        print("*",end=" ");
    print();
    
n=int(input("enetr number:"));
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print("",end=" ");
    for j in range(1,i+1):
        print("*",end=" ");
    print();
    
n=int(input("enetr number:"));
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print("",end=" ");
    for j in range(1,i+1):
        print(chr(j+64),end=" ");
    print();
    
n=int(input("enetr number:"));
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("",end=" ");
    for j in range(1,i+1):
        print(chr(j+64),end=" ");
    print();
    
n=int(input("enetr number:"));
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end= " " );
    for j in range(1,i+1):
        print(j,end=" ");
    print();

n=int(input("enetr number:"));
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end= " " );
    for j in range(1,i+1):
        print(j,end=" ");
    print();
    
n=int(input("enetr number:"));
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end= " " );
    for j in range(1,i+1):
        print("*",end=" ");
    print();

n=int(input("enetr number:"));
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end= " " );
    for j in range(1,i+1):
        print("*",end=" ");
    print();
    
n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end= " " );
    for j in range(1,i+1):
        print(chr(j+64),end=" ");
    print();

n=int(input("enter number:"));
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end= " " );
    for j in range(1,i+1):
        print(chr(j+64),end=" ");
    print();
    
n=int(input("enetr number:"));
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(j,end= " ");
    for j in range(1,i+1):
        print(" ",end=" ");
    print();
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(j,end= " ");
    for j in range(1,i+1):
        print(" ",end=" ");
    print();

n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(j,end=" ");
    print();
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ");
    print();

n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end=" ");
    for j in range(1,n-i+2):
        print(j,end=" ");
    print();
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(" ",end=" ");
    for j in range(1,i+1):
        print(j,end=" ");
    print();

n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end=" ");
    for j in range(1,n-i+1):
        print(j,end= " ");
    print();
    
n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ");
    for j in range(1,i+1):
        print(j,sep=" ",end=" ");
    print();
    
n=int(input("enter number:"));
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end=" ");
    for j in range(1,i+1):
        print(j," ",end=" ");
    print();
for i in range(2,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ");
    for j in range(1,i+1):
        print(j," ",end=" ");
    print();
    
ch=input("enter charcter:");
if(ch=='a' or ch=='e' or ch=='i'or ch=='o'or ch=='u'or ch=='A'or ch=='E'or ch=='I'or  ch=='O'or ch=='U'):
    print("it's vowel");
else:
    print("not vowel");
    
st=input("enter string:");
vowel=0;
consonant=0;
for ch in st:
    if(ch=='a' or ch=='e' or ch=='i'or ch=='o'or ch=='u'or ch=='A'or ch=='E'or ch=='I'or  ch=='O'or ch=='U'):
        vowel=vowel+1;
    else:
        consonant=consonant+1;
print("total vowels in string are ",vowel);
print("total consonants in string are ",consonant);

ch=input("enter character:");
if(ch.isupper()):
    print("uppercase character");
elif(ch.islower()):
    print("lowercase character");
elif(ch.isnumeric()):
    print("number");
else:
    print("symbol");
    
n=int(input("enter number:"));
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end= " ");
    print();
    
# 1. Write a Program to count number of words in a file

f = open("s.txt", "rt")

text = f.read()

words = text.split()

print("Number of words in the file : ", len(words))



print()









# 2. Write a Program to find out longest word from a file

import re

f1 = open('text.txt', 'rt')

text = f1.read()

words = re.findall(r'\w+', text)

longest_word = max(words, key = len)

print(f"The longest word in the file is '{longest_word}' with length = {len(longest_word)}.")



print()










# 3. Write a Program to count total number of uppercase and lowercase characters in file

import re

f2 = open("text.txt", 'rt')

text = f2.read()

upper_case_count = 0
lower_case_count = 0

# for char in text :
#     if char.isupper() :
#         upper_case_count += 1
#     elif char.islower() :
#         lower_case_count += 1

upper_case_characters = re.findall("[A-Z]", text)
lower_case_characters = re.findall("[a-z]", text)

print("The upper case count is : ", len(upper_case_characters))
print("The lower case count is : ", len(lower_case_characters))

print()










# 4. Write a Program to read all the contents of CSV file and display only specific columns

import csv
with open('kh.csv', newline='') as csvfile:
  data = csv.DictReader(csvfile)
  print("ID Department Name")
  print("---------------------------------")
  for row in data:
    print(row['department_id'], row['department_name'])


print()











# 5. Write a Program to write python list to CSV file and display the contents

import csv
data = [[10,'a1', 1], [12,'a2', 3], [14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]
with open("temp.csv", "w", newline="") as f:
   writer = csv.writer(f)
   writer.writerows(data)
with open('temp.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ')
 for row in data:
   print(', '.join(row))
   
#program1
count = 0;   
file = open("s.txt", "r")   
for line in file:    
    words = line.split(" ");  
    count = count + len(words);  
print("Number of words present in given file: ",count);  
file.close();  

#program2
file=open("s.txt","r")
for line in file:
  words=line.split(" ")
  max_len=len(max(words,key=len))
a=[word for word in words if len(word)==max_len]
print("lomgest word:",a)
file.close()

#progarm3
import re
file=open("s.txt","r")
s=file.read()
uppercase=re.findall("[A-Z]", s)
lowercase=re.findall("[a-z]",s)
print("total uppercase words:",len(uppercase))
print("total lowercase words:",len(lowercase))
file.close()

#program4
import csv
with open('departments.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("ID Department Name")
 print("---------------------------------")
 for row in data:
   print(row['department_id'], row['department_name'])

#program5
import csv
data = [[10,'a1', 1], [12,'a2', 3], [14, 'a3', 5], [16, 'a4', 7], [18, 'a5', 9]]
with open("temp.csv", "w", newline="") as f:
   writer = csv.writer(f)
   writer.writerows(data)
with open('temp.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ')
 for row in data:
   print(', '.join(row))

# logic.py to be
# imported in the 2048.py file

# importing random package
# for methods to generate random
# numbers.
import random

# function to initialize game / grid
# at the start
def start_game():

	# declaring an empty list then
	# appending 4 list each with four
	# elements as 0.
	mat =[]
	for i in range(4):
		mat.append([0] * 4)

	# printing controls for user
	print("Commands are as follows : ")
	print("'W' or 'w' : Move Up")
	print("'S' or 's' : Move Down")
	print("'A' or 'a' : Move Left")
	print("'D' or 'd' : Move Right")

	# calling the function to add
	# a new 2 in grid after every step
	add_new_2(mat)
	return mat

# function to add a new 2 in
# grid at any random empty cell
def add_new_2(mat):

# choosing a random index for
# row and column.
	r = random.randint(0, 3)
	c = random.randint(0, 3)

	# while loop will break as the
	# random cell chosen will be empty
	# (or contains zero)
	while(mat[r] != 0):
		r = random.randint(0, 3)
		c = random.randint(0, 3)

	# we will place a 2 at that empty
	# random cell.
	mat[r] = 2

# function to get the current
# state of game
def get_current_state(mat):

	# if any cell contains
	# 2048 we have won
	for i in range(4):
		for j in range(4):
			if(mat[i][j]== 2048):
				return 'WON'

	# if we are still left with
	# atleast one empty cell
	# game is not yet over
	for i in range(4):
		for j in range(4):
			if(mat[i][j]== 0):
				return 'GAME NOT OVER'

	# or if no cell is empty now
	# but if after any move left, right,
	# up or down, if any two cells
	# gets merged and create an empty
	# cell then also game is not yet over
	for i in range(3):
		for j in range(3):
			if(mat[i][j]== mat[i + 1][j] or mat[i][j]== mat[i][j + 1]):
				return 'GAME NOT OVER'

	for j in range(3):
		if(mat[3][j]== mat[3][j + 1]):
			return 'GAME NOT OVER'

	for i in range(3):
		if(mat[i][3]== mat[i + 1][3]):
			return 'GAME NOT OVER'

	# else we have lost the game
	return 'LOST'

# all the functions defined below
# are for left swap initially.

# function to compress the grid
# after every step before and
# after merging cells.
def compress(mat):

	# bool variable to determine
	# any change happened or not
	changed = False

	# empty grid
	new_mat = []

	# with all cells empty
	for i in range(4):
		new_mat.append([0] * 4)
		
	# here we will shift entries
	# of each cell to it's extreme
	# left row by row
	# loop to traverse rows
	for i in range(4):
		pos = 0

		# loop to traverse each column
		# in respective row
		for j in range(4):
			if(mat[i][j] != 0):
				
				# if cell is non empty then
				# we will shift it's number to
				# previous empty cell in that row
				# denoted by pos variable
				new_mat[i][pos] = mat[i][j]
				
				if(j != pos):
					changed = True
				pos += 1

	# returning new compressed matrix
	# and the flag variable.
	return new_mat, changed

# function to merge the cells
# in matrix after compressing
def merge(mat):
	
	changed = False
	
	for i in range(4):
		for j in range(3):

			# if current cell has same value as
			# next cell in the row and they
			# are non empty then
			if(mat[i][j] == mat[i][j + 1] and mat[i][j] != 0):

				# double current cell value and
				# empty the next cell
				mat[i][j] = mat[i][j] * 2
				mat[i][j + 1] = 0

				# make bool variable True indicating
				# the new grid after merging is
				# different.
				changed = True

	return mat, changed

# function to reverse the matrix
# means reversing the content of
# each row (reversing the sequence)
def reverse(mat):
	new_mat =[]
	for i in range(4):
		new_mat.append([])
		for j in range(4):
			new_mat[i].append(mat[i][3 - j])
	return new_mat

# function to get the transpose
# of matrix means interchanging
# rows and column
def transpose(mat):
	new_mat = []
	for i in range(4):
		new_mat.append([])
		for j in range(4):
			new_mat[i].append(mat[j][i])
	return new_mat

# function to update the matrix
# if we move / swipe left
def move_left(grid):

	# first compress the grid
	new_grid, changed1 = compress(grid)

	# then merge the cells.
	new_grid, changed2 = merge(new_grid)
	
	changed = changed1 or changed2

	# again compress after merging.
	new_grid, temp = compress(new_grid)

	# return new matrix and bool changed
	# telling whether the grid is same
	# or different
	return new_grid, changed

# function to update the matrix
# if we move / swipe right
def move_right(grid):

	# to move right we just reverse
	# the matrix
	new_grid = reverse(grid)

	# then move left
	new_grid, changed = move_left(new_grid)

	# then again reverse matrix will
	# give us desired result
	new_grid = reverse(new_grid)
	return new_grid, changed

# function to update the matrix
# if we move / swipe up
def move_up(grid):

	# to move up we just take
	# transpose of matrix
	new_grid = transpose(grid)

	# then move left (calling all
	# included functions) then
	new_grid, changed = move_left(new_grid)

	# again take transpose will give
	# desired results
	new_grid = transpose(new_grid)
	return new_grid, changed

# function to update the matrix
# if we move / swipe down
def move_down(grid):

	# to move down we take transpose
	new_grid = transpose(grid)

	# move right and then again
	new_grid, changed = move_right(new_grid)

	# take transpose will give desired
	# results.
	new_grid = transpose(new_grid)
	return new_grid, changed

# this file only contains all the logic
# functions to be called in main function
# present in the other file


for i in range(6):
#   if(i==3):
#     break
  print(i)
else:
  print("hello")
  
n=int(input("enter number:"))
i=1
count=0
while(i<=n):
  if(n%i==0):
    count+=1
  i+=1
if(count==2):
  print("prime")
else:
  print("not prime")

n=int(input("enter number:"))
if(n%400==0 and n%100==0):
  print("leap year")
elif(n%4==0):
  print("leap year")
else:
  print("not a leap year")
  
n=int(input("enter number:"))
rev=0
z=n
while(n>0):
  rev=rev*10+n%10
  n=n//10
if(z==rev):
  print("palindrome number");
else:
  print("not palindrome number")
  
n=int(input("enter number:"))
z=n
arm=0
l=len(str(n))
while(n>0):
  digit=n%10
  arm=arm+digit**l
  n=n//10
if(z==arm):
  print("armstrong number");
else:
  print("not armstrong number")
  
sum=0
def fun():
    while(True):
        n=input("enter number:")
        if(n==""):
            return 0.0
        else:
            return float(n)+fun()
x=fun()
print("sum:",x)

sum=0
def fun():
  n=input("enter number:")
  if(n==""):
    return 0.0
  else:
    return float(n)+fun()
sum=fun()
print("sum:",sum)

def fact(n):
  if(n==0):
    return 0
  if(n==1):
    return 1
  else:
    return n*fact(n-1)
x=int(input("enter number:"))
print("factorial:",fact(x))

def fib(n):
  if(n==0):
    return 0
  if(n==1):
    return 1
  else:
    return fib(n-1)+fib(n-2)
x=int(input("enter number:"))
for i in range(x):
    print(fib(i),end=" ")
    
def binarysearch(list,start,end,key):
  if(start<=end):
    mid=(start+end)//2
    if(list[mid]==key):
      return mid
    elif(list[mid]<key):
      return binarysearch(list,mid+1,end,key)
    else:
      return binarysearch(list,start,mid-1,key)
  else:
    return -1
list=[34,23,45,2,156,54]
key=int(input("enter key:"))
x=binarysearch(list,0,len(list)-1,key)
if(x!=-1):
  print("key is present")
else:
  print("key is absent")  
  
class overload:
  result=0
  def add(self,instanceOf=None,*args):
    if(instanceOf=="int"):
      self.result=0
    if(instanceOf=="str"):
      self.result=" "
    for i in args:
      self.result=self.result + i
    return self.result
o=overload()
print(o.add("int",33,44,22,4,1))
print(o.add("str","my","name","is","prince"))

class override:
  def hello(self):
    print("prince jain")
class python(override):
  def hello(self):
    print("khushi sharma")
    super().hello()
o=python()
o.hello()

n=int(input("enter number:"))
fac=1
while(n>=1):
  fac=fac*n
  n-=1
print(fac)

n=int(input("enter numbers:"))
for n in range(1,n):
    i=1
    count=0
    while(i<=n):
        if(n%i==0):
            count+=1
        i+=1
    if(count==2):
        print(n,end= " ")

n=int(input("enter numbers:"))
for i in range(1,n):
  for j in range(1,i+1):
    print("*",end=" ")
  print()
for i in range(n,0,-1):
  for j in range(1,i+1):
    print("*",end=" ")
  print()
  
n=input("enter reg no:")
sum=0
count=0
for i in n:
  if(i.isdigit()):
    count+=1
    sum+=int(i)
print("sum:",sum)
print("avg:",sum/count)

l=[1,2,3,4,5,6]
l1=[]
for i in l:
  if(i%2==0):
    l1.append(i)
print(l1)

l=[1,2,3,4,4,5,6]
count=0
for i in l:
  if(l.count(i)>1):
    count+=1
if(count>1):
  print("all elements are not unique")
else:
  print("all elements are unique")
  
l=[1,2,3,4,5,6]
print(l)
old=int(input("enter old value:"))
new=int(input("enter new value:"))
for i in range(len(l)):
    if(l[i]==old):
        l[i]=new
print(l)  

l=[224,24,64,2,66]
maxi=max(l)
mini=min(l)
print("maximum number at:",l.index(maxi))
print("minimum number at:",l.index(mini))

l=[]
while True:
  n=int(input("enter number:"))
  if(n==0):
    break
  l.append(n)
l.reverse()
for i in l:
  print(i)
  
l=(1,2,3,4,5)
s=[]
for i in l:
  s.append(i*i*i)
z=list(zip(l,s))
print(z)

t=(32,43,45,1,5,6666,32)
k=int(input("enter number:"))
l=len(t)
l=list(t)
l.sort()
t=tuple(l)
print("minimum",k,"elements are:",t[:k])
print("maximum",k,"elements are:",t[-k:])

l=[1,2,3,4,5]
dic={items:items for items in l}
print(dic)

l=[1,2,3,4,5]
dic={i:i*i for i in l}
print(dic)

st=input("enter string:")
dic={items:st.count(items) for items in st}
print(dic)

def swap(a,b):
  print("numbers before swapping:",a,b)
  a,b=b,a
  print("numbers are swapping:",a,b)
a=int(input("enter number:"))
b=int(input("enter number"))
swap(a,b)

def median(a,b,c):
  l=[a,b,c]
  l.sort()
  return l[1]
def main():
  a=int(input("enter number:"))
  b=int(input("enter number:"))
  c=int(input("enter number:"))
  result=median(a,b,c)
  print("median value:",result)
if(__name__=="__main__"):
    main()
    
import random
def passwd():
  x=random.randint(7,10)
  st=""
  for i in range(x):
    st+=chr(random.randint(33,126))
  return st
passwd=passwd()
print("password:",passwd)

l=[1,2,3,4,5,6]
even=list(filter(lambda x:x%2==0,l))
print(even)

l=[1,2,3,4,5,6]
s=lambda x:sum(y for y in x)
print(s(l))

a=int(input("enter number:"))
b=int(input("enter number:"))
mini=lambda a,b: a if a<b else b
print("smaller number:",mini(a,b))

def fun():
  n=input("enter number:")
  if(n==""):
    return 0.0
  else:
    return float(n)+fun()
x=fun()
print(x)

class prince:
  def __init__(self):
    print("this is constructor")
  def __del__(self):
    print("this is destructor")
p=prince()
del p

class prince:
  def __init__(self,age=0):
    self.__age=age
  def getter(self):
    return self.__age
  def setter(self,a):
    self.__age=a
p=prince()
p.setter(19)
print(p.getter())
# print(p.__age)

def binarysearch(arr,start,end,key):
  if(start<=end):
    mid=(start+end)//2
    if(arr[mid]==key):
        return mid
    elif(arr[mid]<key):
        return binarysearch(arr,mid+1,end,key)
    else:
        return binarysearch(arr,start,mid-1,key)
  else:
     return -1
arr=[22,44,2,4,1,4555,3]
key=int(input("enter key:"))
x=binarysearch(arr,0,len(arr)-1,key)
if(x!=-1):
   print("key is present")
else:
   print("key is absent")
   
import turtle
turtle.showturtle()
for i in range(4):
  turtle.forward(100)
  turtle.left(90)
  turtle.forward(100)
turtle.hideturtle()
turtle.done()

import turtle
turtle.showturtle()
for i in range(6):
  turtle.forward(50)
  turtle.left(60)
  turtle.forward(50)
turtle.hideturtle()
turtle.done()

import turtle
turtle.showturtle()
turtle.speed(10)
turtle.begin_fill()
turtle.circle(150)
turtle.fillcolor("red")
turtle.end_fill()
turtle.penup()
turtle.goto(-50,150)
turtle.pendown()
turtle.write("JECRC University",font=20)
turtle.hideturtle()
turtle.done()

import turtle
turtle.showturtle()
turtle.right(90)
for i in range(1,11):
  turtle.pendown()
  turtle.write(i)
  turtle.penup()
  turtle.forward(30)
turtle.done()
'''
import turtle
turtle.showturtle()
start_x=-200
start_y=200
x=start_x
y=start_y
for i in range(1,6):
  for j in range(i):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write("*")
    x+=20
  x=start_x
  y-=30
turtle.hideturtle()
turtle.done()