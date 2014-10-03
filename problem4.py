# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91x99

# Find the largest palindrome made from the product of two 3-digit ints


import math

def main():
  stack = []
  temp_max = 0

  
  for x in range(100,1000):
  	for y in range(100, 1000):
  	  #loops through all possible number combinations and tests if they are pal's
  	  test = x*y
  	  if (checkPalindrome(str(test))):
  	    if(temp_max < test):
  	      temp_max = test

  print temp_max



def checkPalindrome(in_string):
  '''Checks if an inputted string is a palindrome'''
  fwdStack = []
  revStack = []
  pal = True

  for x in range(0, len(in_string)):
    fwdStack.append(in_string[x])
    revStack.append(in_string[x])

  revStack.reverse()

  while (len(fwdStack) != 0):
    a = fwdStack.pop()
    b = revStack.pop()

    if (a != b):
      pal = False

  return pal


if __name__ == "__main__":
  main()