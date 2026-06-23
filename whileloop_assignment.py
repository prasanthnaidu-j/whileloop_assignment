#Create a simple program that uses a while loop to iterate over a range of numbers from 1 to 10.
i=1
while i<=10:
    print(i)
    i+=1

#Implement a condition to print only the even numbers within this range using the continue statement.
i=1
while i <=10:
    i+=1
    if i%2==1:
        continue
    print(i)
        
#Add another condition that stops the loop when it encounters the number 8, utilizing the break statement.
i=1
while i <=10:
    i+=1
    if i%2==1:
        continue
    if i==8:
        break
    print(i)
#Ensure your program includes comments explaining the purpose of each segment, especially where break and continue are used.

i=1   		#first i value is 1
while i <=10:  	#while check the condition i.e i<=10 untill the i value becomes 10
    i+=1     	# for every iteration i value increase by 1
    if i%2==1:  	#if check for the odd numbers 
        continue 	#continue skip the odd numbers
    if i==8:  
        break  	# break stops the loop when i reaches 8
print(i)

# Execute your program and document the output to verify it meets the expected behavior.
# Output Explanation:
# continue statement skip all odd numbers. So, only even numbers are printed.
# break statement stops the loop when i becomes 8.
# Program prints the even numbers before 8 and then stops.
