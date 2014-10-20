# By starting at the top the the triangle below and moving to adjacent numbers on the row 
# below, the maximum total from top to bottom is 23

#       3
#     7   4
#   2   4   6
# 8   5   9   3

# Find the maximum total of the given triangle.

def main():

  in_triangle = importTriangle('problem18input.txt')
  
  while (len(in_triangle) > 1):
    
    for x in range(0 , len(in_triangle[len(in_triangle)-2])):
      in_triangle[len(in_triangle)-2][x] = in_triangle[len(in_triangle)-2][x] \
      + maxAB(in_triangle[len(in_triangle)-1][x], in_triangle[len(in_triangle)-1][x+1])

    in_triangle = in_triangle[0: len(in_triangle) -1]
    print in_triangle
  



def importTriangle(file_name):
  
  triangle = []

  in_file = open(file_name, 'r')

  for line in in_file:
    m_line = line.rstrip('\n')
    #m_line = m_line[0:len(m_line) -1]
    split_line = m_line.split(" ")
    print split_line

    for x in range(0, len(split_line)):
      split_line[x] = int(split_line[x])
    
    triangle.append(split_line)

  return triangle

def maxAB(a, b):
  
  temp = a
  if (b > a):
    temp = b

  return temp



if __name__ == "__main__":
  main()