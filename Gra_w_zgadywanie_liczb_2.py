def start():
    print('Pomyśl liczbę od 1 do 1000, a ja zgadnę ją w max 10 próbach!')
    return
'''
Return instruction. 
'''


def guess_number():
'''
Main function for our program
'''
    start()
    min = 0
    max = 1000
    user_opction_list = []
    error_list = [2, 2, 2]
    for user in range(10):
        guess = int((max - min) / 2) + min
        print("Zgaduję ", str(guess), "!")
        user_opction = int(input("Wpisz odpowiedź! \n 1 - za duża! \n 2 - za mało \n 3 - Zgadłeś!\n"))
        user_opction_list.append(user_opction)
        if error_list == user_opction_list[-3::]:
            print("Nie oszukuj!")
            continue
        if user_opction == 3:
            print("Wygrałeś!")
            break
        elif user_opction == 1:
            max = guess
        elif user_opction == 2:
            min = guess


guess_number()