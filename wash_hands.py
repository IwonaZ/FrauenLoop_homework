def wash_hands(N, nM):
    time_to_wash = 21 
    number_of_washes = (N * 30) * nM
    sec = number_of_washes * time_to_wash
    minutes = sec // 60
    seconds = sec % 60
    return print(f'{minutes} minutes and {seconds} seconds')