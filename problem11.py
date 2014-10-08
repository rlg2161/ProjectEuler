# In the problem11data.txt grid, find the combination of four consecutive numbers
# vertically, horizontally or diagonally with the largest product


def main():
  
  line_list = []

  data_file = open('problem11data.txt', 'r')

  # for loop reads in data, converts to ints and adds line to a list
  # each line is then added to line_list to get a 20x20 2d array
  for line in data_file:
    vals = []
    line = line.strip("\n")
    line = line.split(" ")
    for item in line:
      item = int(item)
      vals.append(item)
    line_list.append(vals)

  horiz_max = testHorizontal(line_list)
  vert_max = testVertical(line_list)
  fwdDiag_max = testFwdDiagonal(line_list)
  bkwdDiag_max = testBkwdDiagonal(line_list)

  results = [horiz_max, vert_max, fwdDiag_max, bkwdDiag_max]
  results.sort()

  print results[3]
    

def testHorizontal(line_list):
  '''tests horizonal sequences of numbers'''
  cur_max = -1
  
  for x in range(0, len(line_list)):
    cur_list = line_list[x]
    for y in range(0, len(cur_list)-4):
      temp = cur_list[y]*cur_list[y+1]*cur_list[y+2]+cur_list[y+3]
      if (temp > cur_max):
        cur_max = temp
        #print cur_max


  return cur_max

def testVertical(line_list):
  '''tests vertical sequences of numbers'''
  cur_max = -1

  for x in range(0, len(line_list)-4):
    for y in range(0, len(line_list)):
      temp = line_list[x][y]*line_list[x+1][y]*line_list[x+2][y]*line_list[x+3][y]
      if (temp > cur_max):
        cur_max = temp
        #print cur_max

  return cur_max

def testFwdDiagonal(line_list):
  ''' tests downward sloping diagonals
  #
    #
      #
        #
  '''
  cur_max = -1

  for x in range(0, len(line_list)-4):
    for y in range(0, len(line_list)-4):
      temp = line_list[x][y]*line_list[x+1][y+1]*line_list[x+2][y+2]*line_list[x+3][y+3]
      if (temp > cur_max):
        cur_max = temp
        #print cur_max

  return cur_max

def testBkwdDiagonal(line_list):
  '''tests upward sloping diagonals
          #
        #
      #
    #
  '''
  cur_max = -1

  for x in range(len(line_list)-1, 2, -1):
    for y in range(0, len(line_list)-4):
      temp = line_list[x][y]*line_list[x-1][y+1]*line_list[x-2][y+2]*line_list[x-3][y+3]
      if (temp > cur_max):
        cur_max = temp
        #print cur_max

  return cur_max


if __name__ == "__main__":
  main()