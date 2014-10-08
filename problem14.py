# Longest Collatz sequence
# What starting number, under 1,000,000, produces the longest Collatz sequence?


def main():

  max_seq_len = -1
  max_seq_val = -1
  

  for x in range(1, 1000000):
    temp = x
    temp_seq_len = 0

    while (temp != 1):
      temp_seq_len += 1
      temp = calcNextCollatz(temp)

    temp_seq_len += 1 #to account for final value in sequence when temp == 1

    if (temp_seq_len > max_seq_len):
      max_seq_len = temp_seq_len
      max_seq_val = x

  print str(max_seq_val) + " " + str(max_seq_len)




def calcNextCollatz(number):
  if (number ==1):
    return 1
  elif (number % 2 == 0):
    return number/2
  else:
    return ((3*number) + 1)



if __name__ == "__main__":
  main()