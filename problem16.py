# 2^15 = 32768; the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
# What is the sum of the digits of the nubmer 2 ^ 1000

def main():
  
  n = 2**1000
  str_n = str(n)
  sum_place = 0

  for x in range (0, len(str_n)):
    sum_place = sum_place + int(str_n[x:x+1])

  print sum_place


if __name__ == "__main__":
  main()