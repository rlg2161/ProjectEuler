#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

import math


def main():
  
  test = 600851475143

  largestFactor = findLargestPrimeFactor(test)

  print largestFactor



def findLargestPrimeFactor(test):
  '''Returns the largest prime factor of the inputted integer'''
  a = 0

  sqrt_test = math.ceil(math.sqrt(test))

  for x in range(1, int(sqrt_test)):
    #print str(test) + "  " + str(x) + "  " + str(test%x)
    if (test%x == 0):
      if(isPrime(x)):
        a = x

  return a

   
   
def isPrime(test):
  '''Checks to see if the inputted value is prime and returns a boolean'''
  sqrt_test = math.ceil(math.sqrt(test))
  prime = True

  for x in range (2, int(sqrt_test)):
    
    if (test%x == 0):
      #print str(test) + "  " + str(x) + "  " + str(test%x)
      prime = False

  #print str(test) + "   " + str(prime)
  return prime










if __name__ == "__main__":
  main()