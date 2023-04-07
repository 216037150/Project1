import random 
n = random.randrange(1,5)
print(n)

guess = int(input('Enter the number: '))

while n != guess:
    if guess<n:
        print("The number is too low")
        guess = int(input('Enter the number: '))
    elif guess>n:
        print("The number is too big")
        guess = int(input('Enter the number: '))
    else:
        break        

print("Congratulations, you guessed correct!!!")
 
 