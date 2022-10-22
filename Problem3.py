p1 = (input('Player 1:'))
p2 = (input('Player 2:'))
if p1 == 'rock' and p2 == 'scissors':
    print(p1, ' is the winner!')
elif p1 == 'scissors' and p2 == 'rock':
    print(p2, ' is the winner!')
elif p1 == 'paper' and p2 == 'rock':
    print(p1, ' is the winner!')
elif p2 == 'paper' and p1 == 'rock':
    print(p1, ' is the winner!')
elif p1 == 'scissors' and p2 == 'paper':
    print(p1, ' is the winner!')
elif p2 == 'scissors' and p1 == 'paper':
    print(p1, ' is the winner!')
