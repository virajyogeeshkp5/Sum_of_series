"""
Find sum of series given below:
1+2+3+.....+n
"""
n=int(input("Enter the number of terms in series: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("This is sum of series",sum)

"""
Find sum of series given below:
2+5+8+.....+n
"""
n=int(input("Enter the number of terms in series: "))
lni,sum=2,0
for i in range(1,n+1):
    sum=sum+lni
    lni+=3
print("This is sum of series",sum)

"""
Find sum of series given below:
2+5+8+.....+n
"""
n=int(input("Enter the number of terms in series: "))
lni=int(input("Enter the initial value: "))
D=int(input("Enter the difference: "))
for i in range(1,n+1):
    print(lni,end=" ")
    lni+=D
"""
Find sum of series given below:
1+4+9+16.....+n
"""
n=int(input("Enter the number of terms in series: "))
sum=0
for i in range(1,n+1):
    sum+=i*i
print("Enter the sum of series",sum)

"""
Find sum of series given below:
1/x+2/x+3/x+4/x.....+n/x
"""

n=int(input("Enter the number of terms in series: "))
x=int(input("Enter the x value: "))
sum=0
for i in range(1,n+1):
    sum+=i/x
print("sum fo value",sum)

"""
Find sum of series given below:
x/1+x/2+x/3+x/4.....+x/n
"""

n=int(input("Enter the number of terms in series: "))
x=int(input("Enter the x value: "))
sum=0
for i in range(1,n+1):
    sum+=x/i
print("sum fo value",sum)

"""
Find sum of series given below:
2/x+4/2x+6/3x.....+n/x
"""

n=int(input("Enter the number of terms in series: "))
x=int(input("Enter the x value: "))
sum=0
for i in range(1,n+1):
    sum+=(i*2)/(i*x)
print("sum fo value",sum)

"""
Find sum of series given below:
x^2/1 + x^2/2 + x^2/3 +.....+x^2/n
"""

n=int(input("Enter the number of terms in series: "))
x=int(input("Enter the x value: "))
sum=0
for i in range(1,n+1):
    sum+=(x**2)/i
print("sum fo value",sum)

"""
Find sum of series given below:
x/1 - x^2/2 + x^3/3 -.....+x^n/n
"""
n=int(input("Enter the number of terms in series: "))
x=int(input("Enter the x value: "))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum-=(x**i)/i
    else:
        sum+=(x**i)/i
print("sum of value",sum)
