# Using the given names file, sort the names into alphabetical order
# Next, work out the alphabetical value of each name and multiply it by 
# the names' position in the list to get the name score

# What is the total of all name scores in the file?

def main():
  nameList = importNamesList("p22_names.txt")
  nameList.sort()
  #print nameList
  totalNameScore = 0

  for x in range(0, len(nameList)):
    curNameScore = calcNameScore(x+1, nameList[x])
    totalNameScore = totalNameScore + curNameScore

  print "Total Name Score of the list is: " + str(totalNameScore)



def importNamesList(filename):
  names_file = open(filename, 'r')
  names = names_file.readline()
  split_names = names.split(",")
  
  for x in range(0, len(split_names)):
    split_names[x] = split_names[x][1:-1]

  return split_names


def calcNameScore(x, name):
  nameVal = 0
  for char in name:
    nameVal = nameVal + (ord(char) - 64)

  nameScore = nameVal*x

  return nameScore
  


if __name__ == "__main__":
  main()