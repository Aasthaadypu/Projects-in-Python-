print("Welcome to my computer quiz!")
playing = input("Do you want to play")
print("Tim is Great!".lower())
if playing.lower() != "yes":
      quit()
print("Okay! Let's play:)")
score = 0
answer = input("What does CPU stands for?")
if answer.lower() == "central processing unit":
       print("Correct!")
        score += 1
        score = score + 1
else:
     print("Incorrect!")
answer = input("What doe GPU stands for?")
if answer.lower() == "Graphics processing unit":
       print("Correct!")
        score += 1
        score = score + 1

else:
     print("Incorrect!")

answer = input("What does API stands for?").lower()
if answer.lower() == "Application Programming Interface":
       print("Correct!")
        score += 1
        score = score + 1

else:
     print("Incorrect!")
answer = input("What does GUI stands for?")
if answer.lower() == "Graphical User Interface":
       print("Correct!")
       score += 1
        score = score + 1

else:
     print("Incorrect!")
answer = input("What does RAM stands for?")
if answer.lower() == "Random Access Memory":
       print("Correct!")
        score += 1
        score = score + 1

else:
     print("Incorrect!")
print("You got" +str(score)+ "questions marked")
print("You got" +str(score/4*100)+ "%")
quit()




