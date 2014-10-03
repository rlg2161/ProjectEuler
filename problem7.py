import problem3 as p3 

def main():
  counter = 1 # set to one b/c start testing at 3
  test = 2

  while (counter < 10001):
    test +=1
    print counter
    if(p3.isPrime(test)):
      counter += 1 

  print test


if __name__ == "__main__":
  main()