# If the numbers 1 to five are written out in words: one, two, three, four, five, then there
# are 3 + 3 + 5 + 4 + 4 = 19 letters used in total

# If all the unumbers from 1 to 1000 inclusive were written out in words, how many 
# letters would be used?


def main():

  total = 0

  for x in range(1, 1001):
    total = total + getLetterCount(x)
    print "current total: " + str(total)

  print "final total is: " + str(total)


def getLetterCount(number):
  i = str(number)
  j = len(str(number))
  num_letters = 0

  if (j == 4):
    #print "thousands"
    if (number == 1000):
      num_letters = getThousandsPlace(i[0])
    else:
      num_letters = getThousandsPlace(i[0]) + getHundredsPlace(i[1]) + getTensPlace(i[2:4])
      if (number % 100 != 0):
        num_letters = num_letters + 3

  elif (j == 3):
    #print "hundreds"
    
    if (number % 100 != 0):
      num_letters = getHundredsPlace(i[0]) + getTensPlace(i[1:3]) 
      num_letters = num_letters + 3

    else:
      num_letters = getHundredsPlace(i[0]) + 4

  elif (j == 2):
    #print "tens   " + i
    num_letters = getTensPlace(number)

  elif (j == 1):
    #print "ones"
    num_letters = getOnesPlace(i[0])

  
  #print (number, num_letters)
  return num_letters



def getOnesPlace(number):
  return numLetters(number)


def getTensPlace(number):
  n = str(number)
  num_letters = 0
  if(number >19):
    test_number = int(n[0])*10
    num_letters = numLetters(test_number)
    num_letters = num_letters + numLetters(int(n[1]))
    #print (number, num_letters)
  else:
    num_letters = numLetters(number)
    #print (number, num_letters)

  return num_letters

def getHundredsPlace(number):
  #print getOnesPlace(number)
  return getOnesPlace(number) + 7

def getThousandsPlace(number):  
  return getOnesPlace(number) + 8

def numLetters(n):
  
  number = int(n)
  num_let = 0

  if (number == 1 or number == 2 or number == 6 or number == 10):
    num_let = 3

  elif (number == 4 or number == 5 or number == 9):
    num_let = 4
  
  elif (number == 3 or number == 7 or number == 8 or number == 40 or number == 50 \
    or number == 60):
    num_let = 5

  elif (number == 11 or number == 12 \
    or number == 20 or number == 30 or number == 80 or number == 90):
    num_let = 6

  elif (number == 15 or number == 16 or number == 70):
    num_let = 7

  elif (number == 13 or number == 14 or number == 18 or number == 19):
    num_let = 8

  elif (number == 17):
    num_let = 9

  return num_let



if __name__ == "__main__":
  main()