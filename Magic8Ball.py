#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  question = input("Ask a question, any question! As long as it is in yes/no format! ")
  #Prompt the user for their question.
  answers = ["As I see it, yes.", "Ask again later, MOM", "Better not tell you now.", "Wouldn't you like to know.", "You wish buddy.",
           "Don’t count on it.", "Oh for sure.", "Most likely.", "My sources say nah bruh.", "yessir.", "Signs point to probably, I think.",
           "Very doubtful.", "Bruh idk.", "Yes.", "No.", "I wouldn't count on it, boss."]
  #Answer question randomly with one of the options from your earlier list.
  length = len(answers)
  r = random.random() * length
  r = int(r)
  
  response = answers[r]
  print(response)

if __name__ == '__main__':
  main()
