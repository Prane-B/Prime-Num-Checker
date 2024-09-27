num = int(input('Enter a number'))
for i in range(0,num):
    if num % i == 0:
        print('is not a prime number can be divided with',i)
        break
    else:
        print("is a prime number")

