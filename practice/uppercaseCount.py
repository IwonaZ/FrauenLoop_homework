def up_low(s):
    uppercase = 0
    lowercase = 0
    
    for char in s:
        if char.isupper()== True:
            uppercase += 1
        elif char.islower() == True:
            lowercase +=1
        else:
            pass
        
    print(f'Original String: {s}')
    print(f'No. of Upper case characters : {uppercase}')
    print(f'No. of Lower case Characters :  {lowercase}')