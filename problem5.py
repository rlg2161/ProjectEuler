# 2520 is the smallest number that can be divided by each of the numbers from 1-10 
# without any remainder. 

# What is the smallest positive number that is evenly divisible by all numbers
# from 1-20?

def main():
'''Tests if value is divisible by desired numbers. Counter iterates by 20 b/c 
   number must be divisible by 20'''
     
  a = None
  test = 0

  while (a == None):

    test = test + 20
    
    if (test%20 ==0 and test%19 == 0 and test%18 ==0 and test%17==0 and test%16==0 \
      and test%15==0 and test%14 ==0 and test%13==0 and test%12 ==0 and test%11 == 0):
      print "Success " + str(test)
      a = test


  print a



if __name__ == "__main__":
  main()