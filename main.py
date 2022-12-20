def wrong_answer():
  print("That is not a choice, you seem tired, drink some tea and read the question again")

def begin_game():
  print('Are you at your breaking point? Y or N')
  answer=input()
  if answer.lower()=="y":
    breakingPointYes()
  elif answer.lower()=="n":
    breakingPointNo()
  else:
    wrong_answer()
    begin_game()


def breakingPointYes():
    print("totally understandable, would you care to have a massage or be hit in the face with a fish? Type M or F")
    answer=input()
    if answer.lower()=="m":
      massageYes()
    elif answer.lower()=="f":
      fishYes()
    else:
      wrong_answer()
      breakingPointYes()

def breakingPointNo():
    print("Wow that's great. GA Modules or JS challenges? Type G or J")
    answer=input()
    if answer.lower()=="g":
      fishYes()
    elif answer.lower()=="j":
      js_challenges()
    else:
      wrong_answer()
      breakingPointNo()

def massageYes():
  print("The massage parlor is closed, we still have fish though. Or you could always go for the mystery box. Type F or M")
  answer=input()
  if answer.lower()=="f":
    fishYes()
  elif answer.lower()=="m":
    mystery_box()
  else:
    wrong_answer()
    massageYes()

def fishYes():
  print("wonderful choice to be hit in the face with a fish which is what you chose. match that emotional pain with some physical pain. Cod or Salmon? Type C or S")
  answer=input()
  if answer.lower()=="c":
    cod()
  elif answer.lower()=="s":
    salmon()
  else:
    wrong_answer()
    fishYes()

def cod():
  print("fish oil is good for you would you like to add some hot sauce or lime? Type H or L")
  answer=input()
  if answer.lower()=="h":
    print("yum yum. would you like to play this cool game again or not? Type Y or N")
    answer=input()
    if answer.lower()=="y":
      begin_game()
    else:
      print("vaya con dios!")
  elif answer.lower()=="l":
    print("he put the lime in the coconut he drink em both up. play again? Type Y or N")
    if answer.lower()=="y":
      begin_game()
    else:
      print("he put the lime in the coconut and mixed them both together, the lime in the coconut then you feel better!")
  else:
    wrong_answer()
    cod()

def salmon():
  print("oh okay li'l bougie bubba. you have dysentary and cholera now. would you like to go to the doctor or the funeral parlor? Type D or F")
  answer=input()
  if answer.lower()=="d":
    print("the doctor is out. you ded. would you like to play again? Type Y or N")
    answer=input()
    if answer.lower()=="y":
      begin_game()
    else:
      print("cool enjoy not having to turn anything in ever again")
  elif answer.lower()=="f":
    print("finally some rest. goodnight sweet yung royal")
    begin_game()
  else:
    wrong_answer()
    salmon()

def mystery_box():
  print("This box has two things inside. Did you think either would be good? Hot or Cold? Type H or C")
  answer=input()
  if answer.lower()=="h":
    print("It sure is hot ain't it? Take a break for now. You win or lose or something. Life does not consist of absolutes. Would you like to play again?")
    answer=input()
    if answer.lower()=="y":
      begin_game()
    elif answer.lower()=="n":
      print("Well...bye")
    else:
      wrong_answer()
      mystery_box()
  elif answer.lower()=="c":
    print("it's dark and hell is hot. ruff! ruff! told you it was a mystery. you lose. do you want to play again? Type Y or N")
    answer=input()
    if answer.lower()=="y":
      begin_game()
    elif answer.lower()=="n":
      print("sure is cold out here on the mesa ain't it. adios pardner")
    else:
      print("you don't get to play again because you can't type sorry not sorry lol momboss")
  else:
    wrong_answer()
    mystery_box()

def js_challenges():
  print("You open the js challenges and the test won't run. What will you do instead, sleep or bake? Type S or B")
  answer=input()
  if answer.lower()=="s":
    print("sleep is so great. good luck going to sleep thinking about how you didn't do your js challenges yet")
    print("since you're still here, would you care to play again or end this game? Type P or E")
    answer=input()
    if answer.lower()=="p":
      begin_game()
    elif answer.lower()=="e":
      print("best decision you've made so far")
  elif answer.lower()=="b":
    print("you gonna burn the house down. would you like cookies or brownies? Type C or B")
    answer=input()
    if answer.lower()=="c":
      print("you have cookies to eat on your way to the hospital. play again? Type Y or N")
      if answer.lower()=="y":
        begin_game()
      elif answer.lower()=="n":
        print("careful on them roads")
      else:
        wrong_answer()
        js_challenges()
  else:
    wrong_answer()
    js_challenges()

begin_game()