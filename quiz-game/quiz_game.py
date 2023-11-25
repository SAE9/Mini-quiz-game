print ("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("okay! Let's play:)")
score = 0

answer = input("Where's the Eiffel Tower? ")
if answer == "paris":
    print('Correct!')
    score +=1
else:
    print("Incorrect!")

answer = input("Kangaroos and the Opera House, where are they? ")
if answer.lower() == "australia ":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Salsa, sombreros, and tacos—where's the fiesta? ")
if answer.lower() == "mexico":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")


