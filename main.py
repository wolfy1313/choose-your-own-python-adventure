def wrong_answer():
  print("That is not a choice, you seem tired, drink some tea and read the question again")

def begin_game():
  print('Are you at your breaking point? Y or N')
  answer=input().lower()
  match answer:
    case "y":
      breakingPointYes()
    case "n":
      breakingPointNo()
    case _:
      wrong_answer()
      begin_game()

def breakingPointYes():
    print("totally understandable, would you care to have a massage or be hit in the face with a fish? Type M or F")
    answer=input().lower()
    match answer:
      case "m":
        massageYes()
      case "f":
        fishYes()
      case _:
        wrong_answer()
        breakingPointYes()

def breakingPointNo():
    print("Wow that's great. GA Modules or JS challenges? Type G or J")
    answer=input().lower()
    match answer:
      case "g":
        fishYes()
      case "j":
        js_challenges()
      case _:
        wrong_answer()
        breakingPointNo()

def massageYes():
  print("The massage parlor is closed, we still have fish though. Or you could always go for the mystery box. Type F or M")
  answer=input().lower()
  match answer:
    case "f":
      fishYes()
    case "m":
      mystery_box()
    case _:
      wrong_answer()
      massageYes()

def fishYes():
  print("wonderful choice to be hit in the face with a fish which is what you chose. match that emotional pain with some physical pain. Cod or Salmon? Type C or S")
  answer=input().lower()
  match answer:
    case "c":
      cod()
    case "s":
      salmon()
    case _:
      wrong_answer()
      fishYes()

def cod():
  print("fish oil is good for you would you like to add some hot sauce or lime? Type H or L")
  answer=input().lower()
  match answer:
    case "h":
      restart_game("yum yum. would you like to play this cool game again or not? Type Y or N", "vaya con dios!")
    case "l":
      restart_game("he put the lime in the coconut he drink em both up. play again? Type Y or N", "he put the lime in the coconut and mixed them both together, the lime in the coconut then you feel better!")
    case _:
      wrong_answer()
      cod()

def salmon():
  print("oh okay li'l bougie bubba. you have dysentary and cholera now. would you like to go to the doctor or the funeral parlor? Type D or F")
  answer=input().lower()
  match answer:
    case "d":
      restart_game("the doctor is out. you ded. would you like to play again? Type Y or N", "ool enjoy not having to turn anything in ever again")
    case "f":
      print("finally some rest. goodnight sweet yung royal")
      begin_game()
    case _:
      wrong_answer()
      salmon()

def mystery_box():
  print("This box has two things inside. Did you think either would be good? Hot or Cold? Type H or C")
  answer=input().lower()
  match answer:
    case "h":
      restart_game(
        "It sure is hot ain't it? Take a break for now. You win or lose or something. Life does not consist of absolutes. Would you like to play again?",
        "Well...bye"
      )
    case "c":
      restart_game(
        "it's dark and hell is hot. ruff! ruff! told you it was a mystery. you lose. do you want to play again? Type Y or N",
        "sure is cold out here on the mesa ain't it. adios pardner"
      )
    case _:
      wrong_answer()
      mystery_box()


def js_challenges():
  print("You open the js challenges and the test won't run. What will you do instead, sleep or bake? Type S or B")
  answer=input().lower()
  match answer:
    case "s":
      print("sleep is so great. good luck going to sleep thinking about how you didn't do your js challenges yet")
      restart_game(
        "since you're still here, would you care to play again or end this game? Type P or E",
        "best decision you've made so far",
        "p",
        "e"
      )
    case "b":
      print("you gonna burn the house down. would you like cookies or brownies? Type C or B")
      answer=input().lower()
      match answer:
        case "c":
          restart_game("you have cookies to eat on your way to the hospital. play again? Type Y or N", "careful on them roads")
        case _:
          wrong_answer()
          js_challenges()
    case _:
      wrong_answer()
      js_challenges()

def restart_game(play_again_message, signoff_message, yes="y", no="n"):
  print(play_again_message)
  answer=input().lower()
  if answer == yes:
    begin_game()
  else:
    print(signoff_message)


begin_game()