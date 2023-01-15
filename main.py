import random

series = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e"]
winner_ticket = []
for i in range(4):
    winner_ticket.append(random.choice(series))
print(f"the winner ticket is {winner_ticket} \n "
      f"any ticket matching these 4 numbers or letters wins a prize")
