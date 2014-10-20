# Calculate the sum of the digits in 100!

def main():
  
  x = factorial(100)
  str_x = str(x) # Cast to string to make it easier to iterate through numbers in x  
  
  s = 0

  for y in range(0, len(str_x)):
    s = s + int(str_x[y])

  print s


def factorial(num):
  n = 1
  while (num >= 1):
    n = n * num
    num = num -1
  return n
  

if __name__ == "__main__":
  main()