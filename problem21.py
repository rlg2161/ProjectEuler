# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide
# evenly into n). If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55, 110 - d(220) = 284
# The proper divisors of 284 are 1, 2, 4, 71 and 142 - d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000

import problem12 as p12 

def main():
  
  d_list = getDList(10001)
  
  print d_list
  am_list = []

  for x in range(0, len(d_list)):

    test = d_list[x]


    if (test >= len(d_list)):
      continue

    else:

      target = d_list[test]
      print str(x) + "  " + str(test) + "  " + str(target)
      if (x == target and x != test and (am_list.count(test) == 0)):
        am_list.append(x)
        am_list.append(test)


  am_sum = 0
  print am_list
  while(len( am_list) > 0):
    am_sum = am_sum + am_list.pop()

  print am_sum

  

def getDList(num):

  d_list = []
  d_list.append(0)
  d_list.append(0)

  for x in range(2, num+1):
    lf = p12.listFactors(x)
    lf = lf[0:len(lf)-1]
    sumList = 0
    for y in range(0, len(lf)):
      sumList = sumList + lf[y]

    
   
    #d_tuple = (x, sumList, lf)
    #print d_tuple
    d_list.append(sumList)

  return d_list




if (__name__ == "__main__"):
  main()