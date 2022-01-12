import random
def responses(input_text):
  user_message= str(input_text).lower()

  if user_message.split()[0] in ("hello","hey","hi","sup"):
    return "Hi, I am Gamer Bot.\n Type 'game' to start the rock, paper, scissor game"

  if user_message == "game":
    return """Type your response:
    rock
    paper
    scissor
    """
  l=['rock','paper','scissor']
  bot_chosen= l[random.randint(0,2)]
  res="You win"
  if user_message in ("rock","paper","scissor"):
    if user_message==bot_chosen:
      res="It's a tie"

    elif user_message == "scissor":
      if bot_chosen=="rock":
        res="You Lost"

    elif user_message == "rock":
      if bot_chosen=="paper":
        res="You Lost"

    else:
      if bot_chosen=="scissor":
        res="You Lost"
        
    return "{}\n{}".format(bot_chosen,res)
  else:
    return "You gave wrong input :( Try again"
 
      

  

