 grump_votes = 0
  tiden_votes = 0
  while True:
    a = input("Enter who you would like to vote for(G for grump/T for tiden/q to quit): ")
    if a == "G":
      grump_votes+=1
    elif a == "T":
      tiden_votes+=1
    else:
        break
  if grump_votes>tiden_votes:
    print("Grump is leading by ", grump_votes-tiden_votes ,"votes")
  elif tiden_votes>grump_votes:
    print("Tiden is leading by ", tiden_votes-grump_votes, "votes")
  else:
    print("Its a tie")
  print("grump votes =" ,grump_votes)
  print("tiden votes =" ,tiden_votes)
