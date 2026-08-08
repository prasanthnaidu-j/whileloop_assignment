# Problem 1 – Nested while
# What is the problem asking?
# Generate all pairs from 1–5 and print only pairs whose sum is even.
# Things needed for logic:
# • Outer while → first number (i)
# • Inner while → second number (j)
# • Addition: i+j
# • Condition: (i+j)%2==0
# Example dry run:
# i=1, j=1 → sum=2 → print
# i=1, j=2 → sum=3 → skip
# Example output:
# (1,1)
# (1,3)
# (1,5)
# (2,2)...
for i in range(1,6):
    for j in range(1,6):
        sum1=i+j
        if sum1%2!=0:
            continue
        else:
            print((i,j))
        
# Problem 2 – Nested while
# What is the problem asking?
# Generate all pairs from 1–10 and print only pairs whose product is greater than 30. Also count total
# pairs.
# Things needed for logic:
# • Outer while
# • Inner while
# • Multiplication: i*j
# • Condition: i*j > 30
# • Counter variable
# Example output:
# (4,8) → 32
# (4,9) → 36
count=0
for i in range(1,11):
    for j in range(1,11):
        if i*j>30:
            count+=1
            print((i,j))
        else:
            continue
print("total pairs:",count)

# Problem 3 – For inside While
# What is the problem asking?
# Keep asking user for numbers until 0 is entered. For each number, find factors and their sum.
# Things needed for logic:
# • while num!=0
# • for i in range(1,num+1)
# • Factor condition: num%i==0
# • Sum variable
# Example:
# Input:12
# Factors:1 2 3 4 6 12
# Sum:28
n=int(input("enter any number:"))
while n!=0:
    s=0
    for i in range(1,n+1):
        if n%i==0:
            print("factors:",i,end=" ")
            s+=i
    print("sum:",s)
    n=int(input("enter any number:"))

# Problem 4 – While inside For
# What is the problem asking?
# Given numbers=[12,7,20,9], for each number print values from 1 to that number and count evens.
# Things needed for logic:
# • for through list
# • while loop for counting
# • Even condition: i%2==0
# • Counter variable
# Example output:
# 12 → Even count: 6
# 7 → Even count: 3
l=[12,7,20,9]
for num in l:
    i=1
    count=0
    while i<=num:
        print(i)
        if i%2==0:
            count+=1
        i+=1
    print(num,"even count:",count)
