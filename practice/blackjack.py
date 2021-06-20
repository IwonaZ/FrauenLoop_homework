def blackjack(a,b,c):
    
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif sum([a,b,c]) <= 31 and (a == 11 or b == 11 or c == 11):
        return sum([a,b,c])-10
    else: 
        return 'BUST'