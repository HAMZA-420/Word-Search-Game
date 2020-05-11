def game():
    
    import random

    #A subroutine to replace all "-" (empty characters) with a random letter
    def randomFill(wordsearch):
        LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for row in range(0,12):
            for col in range(0,12):
                if wordsearch[row][col]=="-":
                    randomLetter = random.choice(LETTERS)
                    wordsearch[row][col]=randomLetter

        #A subroutine to output the wordsearch on screen    
    def displayWordsearch(wordsearch):
        print(" _________________________")
        print("|                         |")
        for row in range(0,12):
            line="| "
            for col in range(0,12):
                line = line + wordsearch[row][col] + " "
            line = line + "|"
            print(line)
        print("|_________________________|")  
    
    #A subroutine to add a word to the wordsearch at a random position
    def addWord(word,wordsearch):
        row=random.randint(0,11)
        col=0
        for i in range(0,len(word)):
            wordsearch[row][col+i]=word[i]
        
        # ----Randomly decide where the word will start
        # ----Decide if the word will be added horizontally, vertically or diagonally
        # ----Check that the word will fit in (within the 12 by 12 grid)
        # ----Check that the word will not overlap with existing letters/words in the wordsearch
  

    #Create an empty 12 by 12 wordsearch (list of lists)
    wordsearch = []
    for row in range(0,12):
        wordsearch.append([])
        for col in range(0,12):
            wordsearch[row].append("-")


    print("\nWELCOME TO WORD SEARCH GAME!")
    
    print("\n1. Easy\n2. Medium\n3. Hard")
    mode = eval(input("\nPlease select game mode\nSr No: "))



    if mode==1:
        #Adding words to our wordsearch
        addWord("PYTHON",wordsearch)
        addWord("ALGORITHM",wordsearch)
        addWord("CODING",wordsearch)
        addWord("PROGRAM",wordsearch)
        addWord("HELLO",wordsearch)
        #All unused spaces in the wordsearch will be replaced with a random letter
        randomFill(wordsearch)
        #Display the fully competed wordseach on screen
        displayWordsearch(wordsearch)
    
    
        print("\nYou have three Chances:\n")

        print("Game will Starts in 5 Seconds: ")


        count = 0

        while count<=3:
            
            if count == 1:
                import winsound
                import sys
                import time
                timeLoop = True

                # Variables to keep track and display
                Sec = 0

                # Begin Process

                while timeLoop:
                    while Sec!=5:
                        Sec += 1
                        sys.stdout.write(str(Sec) + "'s,  ")
                        frequency = 300  # Set Frequency To 300 Hertz
                        duration = 1000  # Set Duration To 1000 ms == 1 second
                
                        winsound.Beep(frequency, duration)
                
                        time.sleep(1)
                
                        if Sec==5:
                            print("\n\nLets Start Now!")
                            first_chance= input("\nEnter your word: ")
                            if first_chance ==  "PYTHON" or first_chance =="ALGORITHM" or first_chance =="CODING" or first_chance =="PROGRAM" :
                                print("You Won first Chance, HURRAH!")
                            else:
                                print("You lost your 1st chance")
                            break
                    break
                    
            
        
            if count == 2:
                randomFill(wordsearch)
                displayWordsearch(wordsearch)
                print("\n2nd Chance")
                print("\nPlease Enter any Word other than 1st Input")
                print("\nGame will starts after 3 seconds")
       
        
        
                import winsound
                import sys
                import time
                timeLoop = True

                # Variables to keep track and display
                Sec = 0
  
                # Begin Process

                while timeLoop:
                    while Sec!=3:
                        Sec += 1
                        sys.stdout.write(str(Sec) + "'s,  ")
                        frequency = 300  # Set Frequency To 300 Hertz
                        duration = 1000  # Set Duration To 1000 ms == 1 second
                
                        winsound.Beep(frequency, duration)
                
                        time.sleep(1)
                
                        if Sec==3:
                            print("\n\nLets Start Now!")
                            second_chance = input("\nEnter your word: ")
                            if second_chance==first_chance:
                                print("\nYou've already entered this word\n find another one")
                                second_chance = input("\nEnter your word: ")
                            if second_chance ==  "PYTHON" or second_chance =="ALGORITHM" or second_chance =="CODING" or second_chance =="PROGRAM":
                                print("You Won 2nd Chance, HURRAH!")
                            else:
                               print("You lost your 2nd chance")
                            break
                    break
                    
                    
            if count == 3:
                randomFill(wordsearch)
                displayWordsearch(wordsearch)
        
                print("\n3rd Chance")   
                print("\nPlease Enter any Word other than 1st and 2nd Input")
                print("\nGame will starts after 3 seconds")
        
                import winsound
                import sys
                import time
                timeLoop = True

                # Variables to keep track and display
                Sec = 0

                # Begin Process

                while timeLoop:
                    while Sec!=3:
                        Sec += 1
                        sys.stdout.write(str(Sec) + "'s,  ")
                        frequency = 300  # Set Frequency To 300 Hertz
                        duration = 1000  # Set Duration To 1000 ms == 1 second
                 
                        winsound.Beep(frequency, duration)
                
                        time.sleep(1)
                
                        if Sec==3:
                            print("\n\nLets start Now!")
                            Third_chance = input("\nEnter your word: ")
                            if Third_chance==first_chance or Third_chance==second_chance:
                                print("\nYou've already entered this word\n find another one")
                                Third_chance = input("\nEnter your word: ")
                            if Third_chance ==  "PYTHON" or Third_chance =="ALGORITHM" or Third_chance =="CODING" or Third_chance =="PROGRAM":
                                print("You Won 3rd Chance, HURRAH!")
                            else:
                                print("You lost your 3rd chance")
                                
                            def player_choice():                   #Ask Player whether he wants to restart game or exit
                                print("\nWhats you like!")
                                print("1.Restart\n2.Exit")
                                Ask_Player = eval(input("Enter Here: "))
                                if Ask_Player == 1:
                                    game()
                                elif Ask_Player ==2:
                                    print("\nThank You for Being Here\n     Good Bye")
                                    sys.exit()
                                else:
                                    print("Please select from given options")
                                    player_choice()
                            player_choice()
                                
                            
                        break
                break
            
            count+=1

    
    
    
    
    
    
    
    if mode==2:
        addWord("ALGORITHM",wordsearch)
        addWord("PROGRAM",wordsearch)
        addWord("CODING",wordsearch)
        addWord("MICROSOFT",wordsearch)
    
        randomFill(wordsearch)
        displayWordsearch(wordsearch)
        
        
    
        print("\nYou have three Chances:\n")

        print("Game will Starts in 5 Seconds: ")


        count = 0

        while count<=3:
            if count == 1:
                import winsound
                import sys
                import time
                timeLoop = True

                # Variables to keep track and display
                Sec = 0

                # Begin Process

                while timeLoop:
                    while Sec!=5:
                        Sec += 1
                        sys.stdout.write(str(Sec) + "'s,  ")
                        frequency = 300  # Set Frequency To 300 Hertz
                        duration = 1000  # Set Duration To 1000 ms == 1 second
                
                        winsound.Beep(frequency, duration)
                
                        time.sleep(1)
                
                        if Sec==5:
                            print("\n\nLets Start Now!")
                            first_chance= input("\nEnter your word: ")
                            
                            if first_chance =="ALGORITHM" or first_chance =="CODING" or first_chance =="PROGRAM" :
                                print("You Won first Chance, HURRAH!")
                            else:
                                print("You lost your 1st chance")
                            break
                    break
                    
            
        
            if count == 2:
                randomFill(wordsearch)
                displayWordsearch(wordsearch)
                print("\n2nd Chance")
                print("\nPlease Enter any Word other than 1st Input")
                print("\nGame will starts after 3 seconds")
       
        
        
                import winsound
                import sys
                import time
                timeLoop = True

                # Variables to keep track and display
                Sec = 0
  
                # Begin Process

                while timeLoop:
                    while Sec!=3:
                        Sec += 1
                        sys.stdout.write(str(Sec) + "'s,  ")
                        frequency = 300  # Set Frequency To 300 Hertz
                        duration = 1000  # Set Duration To 1000 ms == 1 second
                
                        winsound.Beep(frequency, duration)
                
                        time.sleep(1)
                
                        if Sec==3:
                            print("\n\nLets Start Now!")
                            second_chance = input("\nEnter your word: ")
                            if second_chance==first_chance:
                                print("\nYou've already entered this word\n find another one")
                                second_chance = input("\nEnter your word: ")
                           
                            if second_chance =="ALGORITHM" or second_chance =="CODING" or second_chance =="PROGRAM" :
                                print("You Won 2nd Chance, HURRAH!")
                            else:
                               print("You lost your 2nd chance")
                            break
                    break
                    
                    
            if count ==3:
                randomFill(wordsearch)
                displayWordsearch(wordsearch)
        
                print("\n3rd Chance")   
                print("\nPlease Enter any Word other than 1st and 2nd Input")
                print("\nGame will starts after 3 seconds")
        
                import winsound
                import sys
                import time
                timeLoop = True

                # Variables to keep track and display
                Sec = 0

                # Begin Process

                while timeLoop:
                    while Sec!=3:
                        Sec += 1
                        sys.stdout.write(str(Sec) + "'s,  ")
                        frequency = 300  # Set Frequency To 300 Hertz
                        duration = 1000  # Set Duration To 1000 ms == 1 second
                 
                        winsound.Beep(frequency, duration)
                
                        time.sleep(1)
                
                        if Sec==3:
                            print("\n\nLets start Now!")
                            Third_chance = input("\nEnter your word: ")
                            if Third_chance==first_chance or Third_chance==second_chance:
                                print("\nYou've already entered this word\n find another one")
                                Third_chance = input("\nEnter your word: ")
                            
                            if Third_chance == "ALGORITHM" or Third_chance == "CODING" or Third_chance ==  "PROGRAM":
                                print("You Won 3rd Chance, HURRAH!")
                            else:
                                print("You lost your 3rd chance")
                                
                                
                            def player_choice():                   #Ask Player whether he wants to restart game or exit
                                print("\nWhats you like!")
                                print("1.Restart\n2.Exit")
                                Ask_Player = eval(input("Enter Here: "))
                                if Ask_Player == 1:
                                    game()
                                elif Ask_Player ==2:
                                    print("\nThank You for Being Here\n      Good Bye")
                                    sys.exit()
                                else:
                                    print("Please select from given options")
                                    player_choice()
                            player_choice()
                                
                                
                        break
                break
            
            count+=1

    
    
    
    
    
    
    
    
    
    if mode==3:
        addWord("PROGRAM",wordsearch)
        addWord("CODING",wordsearch)
        addWord("JAVA",wordsearch)
    
        randomFill(wordsearch)
        displayWordsearch(wordsearch)
        print("\nYou have three Chances:\n")

        print("Game will Starts in 5 Seconds: ")
        
        
        count = 0

        while count<=3:
            if count == 1:
                import winsound
                import sys
                import time
                timeLoop = True

                # Variables to keep track and display
                Sec = 0

                # Begin Process

                while timeLoop:
                    while Sec!=5:
                        Sec += 1
                        sys.stdout.write(str(Sec) + "'s,  ")
                        frequency = 300  # Set Frequency To 300 Hertz
                        duration = 1000  # Set Duration To 1000 ms == 1 second
                
                        winsound.Beep(frequency, duration)
                
                        time.sleep(1)
                
                        if Sec==5:
                            print("\n\nLets Start Now!")
                            first_chance= input("\nEnter your word: ")
                            
                            
                            if first_chance =="CODING" or first_chance =="PROGRAM" or first_chance == "JAVA":
                                print("You Won first Chance, HURRAH!")
                            else:
                                print("You lost your 1st chance")
                            break
                    break
                    
            
        
            if count == 2:
                randomFill(wordsearch)
                displayWordsearch(wordsearch)
                print("\n2nd Chance")
                print("\nPlease Enter any Word other than 1st Input")
                print("\nGame will starts after 3 seconds")
       
        
        
                import winsound
                import sys
                import time
                timeLoop = True

                # Variables to keep track and display
                Sec = 0
  
                # Begin Process

                while timeLoop:
                    while Sec!=3:
                        Sec += 1
                        sys.stdout.write(str(Sec) + "'s,  ")
                        frequency = 300  # Set Frequency To 300 Hertz
                        duration = 1000  # Set Duration To 1000 ms == 1 second
                
                        winsound.Beep(frequency, duration)
                
                        time.sleep(1)
                
                        if Sec==3:
                            print("\n\nLets Start Now!")
                            second_chance = input("\nEnter your word: ")
                            if second_chance==first_chance:
                                print("\nYou've already entered this word\n find another one")
                                second_chance = input("\nEnter your word: ")
                           
                            
                            if second_chance =="CODING" or second_chance =="PROGRAM" or second_chance == "JAVA":
                               print("You Won 2nd Chance, HURRAH!")
                            else:
                               print("You lost your 2nd chance")
                            break
                    break
                    
                    
            if count ==3:
                randomFill(wordsearch)
                displayWordsearch(wordsearch)
        
                print("\n3rd Chance")   
                print("\nPlease Enter any Word other than 1st and 2nd Input")
                print("\nGame will starts after 3 seconds")
        
                import winsound
                import sys
                import time
                timeLoop = True

                # Variables to keep track and display
                Sec = 0

                # Begin Process

                while timeLoop:
                    while Sec!=3:
                        Sec += 1
                        sys.stdout.write(str(Sec) + "'s,  ")
                        frequency = 300  # Set Frequency To 300 Hertz
                        duration = 1000  # Set Duration To 1000 ms == 1 second
                 
                        winsound.Beep(frequency, duration)
                
                        time.sleep(1)
                
                        if Sec==3:
                            print("\n\nLets start Now!")
                            Third_chance = input("\nEnter your word: ")
                            if Third_chance==first_chance or Third_chance==second_chance:
                                print("\nYou've already entered this word\n find another one")
                                Third_chance = input("\nEnter your word: ")
                            
                            
                            if Third_chance == "CODING" or Third_chance ==  "PROGRAM" or Third_chance == "JAVA":
                                print("You Won 3rd Chance, HURRAH!")
                            else:
                                print("You lost your 3rd chance")
                                
                                
                            def player_choice():                   #Ask Player whether he wants to restart game or exit
                                print("\nWhats you like!")
                                print("1.Restart\n2.Exit")
                                Ask_Player = eval(input("Enter Here: "))
                                if Ask_Player == 1:
                                    game()
                                elif Ask_Player ==2:
                                    print("\nThank You for Being Here\n      Good Bye")
                                    sys.exit()
                                else:
                                    print("Please select from given options")
                                    player_choice()
                            player_choice()
                                    
                            
                        break
                break
            
            count+=1

    
    
    else:
        print("\nWrong input\nPlease Enter given Sr No")
        game()

game()






