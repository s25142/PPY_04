import math


def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True

def prime(*numbers):
    for n in numbers:
        if n == 0 or n == 1:
            print(n, "is not prime")
            continue
        p = is_prime(n)
        if p:
            print(n, "is prime number")
        else:
            print(n, "is not prime")


prime(0,1,2,3,4,5,6,7,8,9,10,11,12,13)


