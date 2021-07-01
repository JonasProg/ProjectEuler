def paper_strip_game(Kettenlänge):
    Person_2_win_counter = 0
    Person_1_win_counter = 0
    for y in range (1, Kettenlänge +1):
        Kettenlänge = y
        Person_1 = True # Person 1 fängt immer an!
        Person_2 = True
        while Person_1 == True and Person_2 == True:
            if Kettenlänge >= 2:
                Kettenlängencounter = Kettenlänge
                high = True
                for x in range (0, Kettenlängencounter +1):
                    if Kettenlänge % (4*x+2) == 0:
                        high = False
                for z in range (0, Kettenlängencounter +1):
                    if Kettenlänge % (4*z +3) ==0:
                        high = False
                if high == False:
                    Kettenlänge = Kettenlänge - 2
                else:
                    Kettenlänge = Kettenlänge - 4
                high = True
            else:
                Person_1 = False
            if Kettenlänge >= 2:
                Kettenlängencounter = Kettenlänge
                high2 = True
                for x in range(1, Kettenlängencounter + 1):
                    if Kettenlänge % (4 * x) == 0:
                        high2 = False
                for z in range(0, Kettenlängencounter + 1):
                    if Kettenlänge % (4 * z + 1) == 0:
                        high2 = False
                if high2 == False:
                    Kettenlänge = Kettenlänge - 2
                else:
                    Kettenlänge = Kettenlänge - 4
                high2 = True
            else:
                if Person_1 == True:
                    Person_2 = False
        if Person_1 == False:
            Person_2_win_counter = Person_2_win_counter +1
        if Person_2 == False:
            Person_1_win_counter = Person_1_win_counter +1
    return Person_1_win_counter, Person_2_win_counter
print(paper_strip_game(5))