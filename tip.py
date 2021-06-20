guests = 7;
bill = 200.50;
tipPercentage = 10;

#amout to pay per each person (withouth the tip)
def totalToPay():
    return round(float(bill / guests),2);

#tip to pay for each person
def tip():
    return round(float((tipPercentage/100) * totalToPay()),2);

#total amout to pay including the tip
def totalPerPerson():
    return round(float(tip() + totalToPay()),2);

print(f'Each guests need to pay: {totalToPay()} Euro, the amount of tip for each guest is {tip()} Euro. The total amount to pay is {totalPerPerson()} Euro'.format())