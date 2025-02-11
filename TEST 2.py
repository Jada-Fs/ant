
#TEST 2

# QUESTION 2 
for i in range(1,7):
    for j in range(1,7):
        product=i*j
        print(f"{i}*{j}={product}")
        
        
        
# QUESTION 3
secret_num=13
guess=int(input("Enter the number"))
if guess==secret_num:
    print("You are welcome")
elif  guess<secret_num:
    print("Your guess is lower than the secret number")
else:
     print("Your guess is higher than the secret number")
     
     

#QUESTION 4
for i in range(0,10):
    if i==4 or i==8:
        continue
    print(f"The expected output is {i}")
    
    
    
#QUESTION 5
def km_to_miles(km):
    return 
km*0.621371
def find_smallest_value(a,b,c):
    return 
min(a,b,c)