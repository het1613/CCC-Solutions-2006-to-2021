num=int(input('Number of votes: '))
vote_sequence=input('Enter sequence of votes: ')

##METHOD 1
##A_votes=0
##B_votes=0

##for current_vote in vote_sequence:
##    if current_vote=='A':
##        A_votes+=1
##    elif current_vote=='B':
##        B_votes+=1

##METHOD 2
A_votes=vote_sequence.count('A')
B_votes=vote_sequence.count('B')

if (A_votes>B_votes):
    winner='A'
elif A_votes<B_votes:
    winner='B'
else:
    winner='Tie'

print(winner)
