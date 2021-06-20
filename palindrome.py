def is_palindrome(text):
    
    my_list = str(text).lower()
    reversed_list = my_list[::-1].lower()

    if my_list == reversed_list:
        print('It is a palindrome')
    else:
        print('It is not a palindrome')

