#Het Patel
#J2 CCC 2021
#17/02/20

num=int(input())

highest_bid=0

for i in range(num):
    name=input()
    bid=int(input())

    if bid>highest_bid:
        highest_bid=bid
        highest_bidder=name

print(highest_bidder)
