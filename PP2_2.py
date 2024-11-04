

def q1(): 
  #Write Assignment code here
  num = input ('Input a number: ')
  if num == "5":
    print ("The number is Five")
  else:
    print ("The number is not Five")

def q2(): 
  #Write Assignment code here
  num = int(input ("Input a number: "))
  if num > 0:
    print("Positive")
  else:
    print("Negative")

  #q3

  num = int(input ("Input an integer: "))
  if num % 2 == 0:
    print ("Your number is even")
  else:
    print ("Your number is odd")
  # q4

  word = input ("Type the word Hello: ")
  if word == "Hello":
    print ("The word is Hello")
  else:
    print ("The word is not Hello")

#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
