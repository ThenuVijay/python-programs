#mind=43
#guess=0
#while guess!=mind:
#    guess=int(input("Tell me your guess"))
 #   if guess==mind:
 #       print("Wow super")
 #   elif guess>mind:
  #      print("No,Your guess is greater")
  #  else:
  #      print("No,too little")



mark=int(input("Enter your mark"))
while mark!=0:
    if mark<500:
        tamil=int(input("Enter your tamil mark"))
        if tamil>80:
           print("very good")
        else:  
           print("Nice")
    else:        
        print("mark should not exceed 500")
        mark=int(input("Enter your mark"))
        