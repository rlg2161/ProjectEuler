# The Fibonacci sequence is defined by the recurrence relation:
# F(n) = F(n-1) + F(n-2) where F(1) = 1 and F(2) = 1

# What is the first term in the Fibonacci sequence to contain 1000 digits


def main():
  
  lessThan1000 = True
  first = 1
  second = 1
  counter = 2 # first 2 terms are already defined

  while (lessThan1000):
    nxt = calcNextFibNumber(first, second)
    counter = counter + 1

    if (len(str(nxt)) == 1000):
      lessThan1000 = False

    first = second
    second = nxt

  print "The first term in the sequence to contain 1000 digits is: " + str(counter)
  print "That number is: " + str(second)



def calcNextFibNumber(a, b):
  c = a + b
  return c

if __name__ == "__main__":
  main()