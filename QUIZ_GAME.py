#this is a quiz game

print("Hello! welcome to the quiz program")

playing=input("Heyyy are you interested to play the quiz game:")
if playing.lower()!="yes":
    quit()
else:
    print("Let's start this interesting game....")

score=0
print("question--1")
answer=input("what does the cpu stands for?:")
if answer.lower()=="central processing unit":
    print("correct answer")
    score+=1
else:
    print("wrong answer buddy")

print("question--2")
answer=input("what is the capital of india?:")
if answer.lower()=="delhi":
    print("wow..,right answer")
    score+=1
else:
    print("Incorrect answer")

print("question--3")
answer=input("what is the full form of os?:")
if answer.lower()=="operating system":
    print("correct")
    score+=1
else:
    print("wrong attempt")

print("question--4")
answer=input("what does ram stands for?:")
if answer.lower()=="random access memory":
    print("Heyy,your answer is correct")
    score+=1
else:
    print("wrong answer:)")

print("question--5")
answer=input("what does gpu stands for:?")
if answer.lower()=="graphical processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")

print("you got " + str(score) + " questions correct")
print("you got " + str((score/4)*100) + "%" + " in this quiz")



























