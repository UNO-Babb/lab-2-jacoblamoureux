#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour + 6) % 12
  currentMinute = now.minute

  #TODO:
  #Ask user for hours
  morehour = int(input('Enter number of hours:'))
  futurehour = (currentHour + morehour) % 12

  #Ask user for minute
  moremins = int(input('Enter number of minutes:'))
  futuremins = (currentMinute + moremins ) % 60
  extrahour = (currentMinute + moremins) // 60
  bighour = (futurehour + extrahour) % 12
  
  print("Future time is", bighour,":",futuremins)
  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
