# prime number 

number=int(input("Ple Entwewer prime number:"))

def prime(num):
    is_prime=True
    for i in range(2,num):
        if num % i==0:
            is_prime=False
    if is_prime:
            print("prime number")
    else:
         print("not prime")    

prime(num=number)