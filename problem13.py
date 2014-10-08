# Find the first ten digits of the sum of the one hundred 50-digit numbers 
# in problem13data.txt


def main():
  
  data_file = open('problem13data.txt', 'r')
  
  firstTenSum = 0

  for line in data_file:
    # slice the first 10 values and round up if the 11th value is > 4
    rounding_digit = int(line[10])
    first_ten = int(line[:10])

    if (rounding_digit > 4):
      first_ten = first_ten + 1
    
    #print str(line) + ": " + "first 10: " + str(first_ten)
    
    firstTenSum = firstTenSum + first_ten

  # Cast firstTenSum to string and slice it to the 10 most sig-digs
  firstTenSum = str(firstTenSum)
  print firstTenSum[:10]








if __name__ == "__main__":
  main()