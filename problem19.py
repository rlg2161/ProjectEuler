# How many Sundays fell on the first of the month during the 20th Century 
# (1 Jan 1901 - 31 Dec 2000)?

# Sun = 0, Mon = 1, Tues = 2, Wed = 3, Thurs = 4, Fri = 5, Sat = 6




def main():
  
  days = ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat']
  months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

  year = 1901
  month = 0
  leap = False
  day_index = 2 # Jan 1 1901 was a Tuesday
  count = 0

  while (year < 2001):
    leap = False
    #print str(year) + " " + months[month] + " " + days[day_index]
    if (year % 4 == 0):
      leap = True
    elif (year % 100 == 0):
      leap = False
    elif (year % 400 == 0):
      leap = True

    day_index = dayAtFirstofNextMonth(month, leap, day_index)
    if (day_index == 0):
      count = count + 1
    month = (month + 1) % 12
    if (month == 0):
      #print str(year) + " " + str(count)
      year = year + 1

  print count


  
  

def dayAtFirstofNextMonth(month_index, leap, day_index):

  days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  days_in_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  if (leap):
    dim = days_in_month_leap[month_index]
  else:
    dim = days_in_month[month_index]

  day = (day_index + (dim %7)) % 7
  
  return day 



if __name__ == "__main__":
  main()