# Find the sum of all primes less than 2,000,000

import problem3 as p3

def main():
  
  summation = 0

  for x in range (1, 2000000):
    if (x%10000 ==0):
      # Allows rough watching of progress of program
  	  print x
    
    if (p3.isPrime(x)):
      summation = summation + x
      


  print summation





if __name__ == "__main__":
  main()