# Given the input file (saved as proble8data.txt), find the 13 adjacent digits
# in the given file that have the greatest product.

# Return the value of this product

def main():
  
  num = ""
  data_file = open('problem8data.txt', 'r')
  
  for line in data_file:
    num = num + line.strip("\n")

  temp = 1
  cur_max = -1

  for x in range(0, len(num)-13):
    # loops through the array to give the starting point of the sequence
    temp = 1
    for y in range(0, 13):
      # provides the values of the 13 digits to be pointed at
      temp = temp * int(num[x+y])
    if (temp > cur_max):
      # saves the current product if greater than saved product
      cur_max = temp

  print cur_max





if __name__ == "__main__":
  main()