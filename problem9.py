# A pythagorean triplet is a set of 3 nat'l numbers s.t. a<b<c and a^2 + b^2 = c^2

# There exists one pythagorean triplet for which a + b + c = 1000
# What is a*b*c?

import math

def main():
  
  val = 0
   

  for a in range(1, 600):
    
    for b in range(a+1, 600):
      
      c = math.sqrt((a**2) + (b**2))
      
      if ((a + b + c) == 1000):
        val = a*b*c
        print str(a) + " " + str(b) + " " + str(c) + ": " + str(val)
        
        






if __name__ == "__main__":
  main()