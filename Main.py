# I - Import necessary libs for the build

import random
import turtle
import string
import sys
import time
import os

# I - This functions are used for crash / error handeling

def bug():
    print("Well something went wrong!, maybe u typed something wrong")
    print("Im restarting the game :)")
    time.sleep(2)
    sg()

def troll():
    print("Ok, thats not funny, stop trolling")
    print("Im restarting the game :)")
    time.sleep(2)
    sg()

# I - This function makes the text look like a typewriter

def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.2)
        time.sleep(.05)

# I - Main function for the snake game

def sk():

    delay = 0.1

    # I - Score

    score = 0
    high_score = 0

    # I - Setting up the Screen
    wn = turtle.Screen()
    wn.title("Snake Game by @CoconutA4")
    wn.bgcolor("orange")
    wn.setup(width=600, height=600)
    wn.tracer(0)  # Turns off the screen updates

    # I - Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    # I- Snake objective (food)
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)

    segments = []

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

    # I - Main function for the snake game

    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    # I - Keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")

    # I - Main game loop
    while True:
        wn.update()

        # Check for a collision with the border
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

            # Check for a collision with the food
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            # Shorten the delay
            delay -= 0.001

            # Increase the score
            score += 10

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

            # Move the end segments first in reverse order
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"

                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # Clear the segments list
                segments.clear()

                # Reset the score
                score = 0

                # Reset the delay
                delay = 0.1

                # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 24, "normal"))

        time.sleep(delay)

    wn.mainloop()

# I - Main function for guessing game (it includes the game modes inside)

def sg():

# I - This function restarts SinglePlayer

    def restart_sp():
        user_input = input("Would you like to play again? Type 'Yes' or 'No'\n\n")

        if user_input.lower() == "no":  # Converts input to lowercase for comparison
            print("It was good while it lasted! Good bye :(")
            exit()
        if user_input.lower() == "yes":
            sp()
        else:
            print("U can only type yes or no")
            restart_sp()

# I - This function restarts AI

    def restart_ai():
        user_input = input("Would you like to play again? Type 'Yes' or 'No'\n\n")

        if user_input.lower() == "no":  # Converts input to lowercase for comparison
            print("It was good while it lasted! Good bye :(")
            exit()
        if user_input.lower() == "yes":
            ai()
        else:
            print("U can only type yes or no")
            restart_ai()

# I - This function restarts MultiPlayer

    def restart_mp():
        user_input = input("Would you like to play again? Type 'Yes' or 'No'\n\n")

        if user_input.lower() == "no":  # Converts input to lowercase for comparison
            print("It was good while it lasted! Good bye :(")
            exit()
        if user_input.lower() == "yes":
            mp()
        else:
            print("U can only type yes or no")
            restart_mp()

# I - This function starts the tutorial

    def tut():
        global modeselector
        tut = input("Would you like to go trough a tutorial? (recommended) [Y/N]\n")

        if tut == "Y" or tut == "y":
            print("I see you chose to go trough the tutorial, nice choice\n")
            time.sleep(1)
            typewriter_simulator("The game is quite simple, you have 3 game modes, SP (playing alone), MP (2 players) and AI (playing against the computer)\n")
            typewriter_simulator("The objective is guessing a random number, generated between a limit (depends on the difficulty)\n")
            typewriter_simulator("Theres 4 dificulties, 1 is from 1-20 (5 tries), 2 is from 1-100 (6 tries), 3 is from 1-250 (10 tries), and 4 from 1-400 (10 tries)\n")
            modeselector = int(input("\n" + myName + " after what u were taught, would you like to play SP (1), PVP (2) or PVC (3)? \n"))
        else:
            print("No tutorial? hm ur harcore. I like it\n")

# NI - Line  -  is pure roleplay, making the game interesting

# NI - Using FSymbols.com to make the text

    print("░██████╗░██╗░░░██╗███████╗░██████╗░██████╗")
    print("██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝")
    print("██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░")
    print("██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗")
    print("╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝")
    print("░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░")
    # NI - Credits -> https://github.com/monkeythatprograms
    print("A python based guessing game :) by @CoconutA4")
    myName = input('\nHello! traveller i see you stuped upon my guessing game. First i need to know ur name, yes i know im a stranger, but i really need to know :) \n')
    print("Owwww " + myName + ", you have a interesting name, but enought talking, lets play")

# I - Line  -  Starting the tutorial function

    tut()

# I - SinglePlayer Function

    def sp():
        print("\nWelcome to Single-Player\n")

        level = int(input('Pick a level of difficulty (1 to 4): '))
        if level == 1:
            top = 20
            tries = 5
        elif level == 2:
            top = 100
            tries = 6
        elif level == 3:
            top = 250
            tries = 10
        elif level == 4:
            top = 400
            tries = 10

        # create a '%' formatted string
        sf = "Well, %s, I am thinking of a number between 1 and %d"
        print(sf % (myName, top))

        # pick the random integer
        number = random.randint(1, top)
        print('Try to guess it!.')

        guessesTaken = 0
        while guessesTaken <= tries:
            guess = int(input('Take a guess: '))
            guessesTaken += 1
            if guess < number:
                print('Your guess is too low.')
            if guess > number:
                print('Your guess is too high.')
            if guess == number:
                print("Spot ON! nice guess")
                restart_sp()

        if guess == number:
            # create a '%' formatted string
            sf = "Good job, %s! You guessed my number with %d guesses!"
            print(sf % (myName, guessesTaken))
            restart_sp()

        if guess != number:
            number = str(number)
            art_over = r"""

               $$$$$$\                                           $$$$$$\                                 
               $$  __$$\                                         $$  __$$\                                
               $$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\        $$ /  $$ |$$\    $$\  $$$$$$\   $$$$$$\  
               $$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\       $$ |  $$ |\$$\  $$  |$$  __$$\ $$  __$$\ 
               $$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |      $$ |  $$ | \$$\$$  / $$$$$$$$ |$$ |  \__|
               $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|      $$ |  $$ |  \$$$  /  $$   ____|$$ |      
               \$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\        $$$$$$  |   \$  /   \$$$$$$$\ $$ |      
                \______/  \_______|\__| \__| \__| \_______|       \______/     \_/     \_______|\__|                                                                                         

            """
            print(art_over)
            print('Awf u have no more trys. The number I was thinking of was ' + number, "better luck next time")
            restart_sp()

# I - Ai Function

    def ai():

        print("Hello " + myName + "!")
        print("You chose to play against ai!")
        print("Don't let the computer beat you (hes smart!) Good luck!")

        level = int(input('Pick a level of difficulty (1 to 4): '))

        if level == 1:
            top = 20
            tries = 5
        elif level == 2:
            top = 100
            tries = 6
        elif level == 3:
            top = 250
            tries = 10
        elif level == 4:
            top = 400
            tries = 10

        the_number = random.randint(1, top)
        guess = 0

        # Iniciating the limits that the computer will use
        minPossible = 0
        maxPossible = 400

        # Guessing Game - Player
        while guess != the_number:
            guess = int(input("Please enter a number: \n"))
            if guess > the_number:
                print(myName + ", guess lower...")
                if guess < maxPossible:
                    maxPossible = guess - 1
            elif guess < the_number:
                print(myName + ", guess higher...")
                if guess > minPossible:
                    minPossible = guess + 1
            else:
                art_over = r"""

                   $$$$$$\                                           $$$$$$\                                 
                   $$  __$$\                                         $$  __$$\                                
                   $$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\        $$ /  $$ |$$\    $$\  $$$$$$\   $$$$$$\  
                   $$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\       $$ |  $$ |\$$\  $$  |$$  __$$\ $$  __$$\ 
                   $$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |      $$ |  $$ | \$$\$$  / $$$$$$$$ |$$ |  \__|
                   $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|      $$ |  $$ |  \$$$  /  $$   ____|$$ |      
                   \$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\        $$$$$$  |   \$  /   \$$$$$$$\ $$ |      
                    \______/  \_______|\__| \__| \__| \_______|       \______/     \_/     \_______|\__|                                                                                         

                """
                print(art_over)
                print("Game Over! The number was", the_number, "," + myName + " wins!\n")
                restart_ai()
            guess = random.randint(minPossible, maxPossible)

            # Guessing Game - AI
            if guess > the_number:
                print("Ai, guess lower...\n")
                maxPossible = guess - 1
            elif guess < the_number:
                print("Ai, guess higher...\n")
                minPossible = guess + 1
            else:
                art_over = r"""

                   $$$$$$\                                           $$$$$$\                                 
                   $$  __$$\                                         $$  __$$\                                
                   $$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\        $$ /  $$ |$$\    $$\  $$$$$$\   $$$$$$\  
                   $$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\       $$ |  $$ |\$$\  $$  |$$  __$$\ $$  __$$\ 
                   $$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |      $$ |  $$ | \$$\$$  / $$$$$$$$ |$$ |  \__|
                   $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|      $$ |  $$ |  \$$$  /  $$   ____|$$ |      
                   \$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\        $$$$$$  |   \$  /   \$$$$$$$\ $$ |      
                    \______/  \_______|\__| \__| \__| \_______|       \______/     \_/     \_______|\__|                                                                                         

                """
                print(art_over)
                print("Game Over! The number was", the_number,
                      "The Ai wins!, im telling you, one day they will take over the world!!!!\n")
                restart_ai()

# I - MultiPlayer Function

    def mp():
        print("\nWelcome to MultiPlayer\n")
        level = int(input('Pick a level of difficulty (1 to 4): '))
        if level == 1:
            top = 20
            tries = 5
        elif level == 2:
            top = 100
            tries = 6
        elif level == 3:
            top = 250
            tries = 10
        elif level == 4:
            top = 400
            tries = 10

        num = random.randrange(1, top)

        player1PlayCount = 0
        player2PlayCount = 0
        """enter and assign names to players"""
        player1Name = myName
        player2Name = input('Whats the second player name?\n')

        player1 = player1Name

        player2 = player2Name

        player = player1

        print(player1, 'turn')

        while ((player1PlayCount and player2PlayCount) != tries):
            guessNum = int(input("Guess Number: "))

            if guessNum == num:
                print(player, "won")
                restart_mp()
            if guessNum < num:
                print('Your guess is too low.')
            if guessNum > num:
                print('Your guess is too high.')

            elif player == player1:
                player1PlayCount += 1
                player = player2
                print(player2, 'turn')

            elif player == player2:
                player2PlayCount += 1
                player = player1
                print(player1, 'turn')

            else:
                print("Both ", player1, " and ", player2, " lose")
                restart_mp()

# I - Calling the functions to the respective game modes

    modeselector = int(input("\n" + myName + ", would you like to play SP (1), PVP (2) or PVC (3)? \n"))

    if modeselector == 1:
        sp()
    if modeselector == 2:
        mp()
    if modeselector == 3:
        ai()
    else:
        bug()

# I - Main function for exploration game

def ex():

# NI - Starting variables

    a = 1.5
    b = 0.05

# I - Monster Image (fSymbols.com)

    monster_1 = r"""
                              ______________                               
                        ,===:'.,            `-._                           
                            `:.`---.__         `-._                       
                               `:.     `--.         `.                     
                                 \.        `.         `.                   
                         (,,(,    \.         `.   ____,-`.,                
                      (,'     `/   \.   ,--.___`.'                         
                  ,  ,'  ,--.  `,   \.;'         `                         
                   `{D, {    \  :    \;                                    
                     V,,'    /  /    //                                    
                     j;;    /  ,' ,-//.    ,---.      ,                    
                     \;'   /  ,' /  _  \  /  _  \   ,'/                    
                           \   `'  / \  `'  / \  `.' /                     
                            `.___,'   `.__,'   `.__,'  
     """

# I - Necessary functions

    def slow_text(start_text, end_text, speed):
        print(start_text, end="")
        for character in end_text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(speed)
        print()

    def text_time(text, speed):
        print(text)
        time.sleep(speed)

# I - This function starts the introduction

    def intro():
        print()
        text_time("(Let our story begin!)", 2)
        print()
        slow_text("Date: ", "January 25rd 1893", b)
        time.sleep(a)
        print()
        text_time("(EVERYTHING IS DARK)", a)
        text_time("You feel around, using your hands to see.", a)
        text_time("The ground is cold, hard, and you hear footsteps.", a)
        text_time("The footsteps get closer.", a)
        text_time("You feel around and pick up a rock. Preparing yourself for whoever is approaching.", a)
        text_time("A loud THUD.", a)
        text_time("Light begins flooding in.", a)
        print()
        slow_text("Captain Alves: ", "Ahoy!!", b)
        slow_text("Captain Alves: ", "Look who\'s up", b)
        print()
        time.sleep(a)
        text_time("You look around! You're on a boat!", a)
        print()
        slow_text("Captain Alves: ", "Me bucko don't worry, ye be safe wit' me crew", b)
        slow_text("Captain Alves: ", "Wha's yer name? we found ye marooned at sea", b)
        print()
        text_time("You release the rock. Still confused and on edge.", a)
        print()
        slow_text("Captain Alves: ", "Are ye jus' goin't' sit thar? I dont reckon he talks Hash", b)
        print()
        text_time("You stand up slowly.", a)
        text_time("Reaching around for something to hold you upright.", a)
        text_time("You look around and calmly you say.", a)
        print()
        slow_text(name, f": My name is {name}", b)
        slow_text(name, ": My ship was sunk by some monster....this thing it destroyed everything", b)
        print()
        text_time("Two paths are revealed:", a)
        print()
        print('Path #1: "Please we have to go save my crew! They\'re out there alone!"')
        print('Path #2: "I appreciate you saving me, but when do we reach land?"')
        print()
        first_path = input("Which path will you choose? (1/2): ")
        if first_path == '1':
            print()
            path_1()
        elif first_path == '2':
            print()
            path_2()
        else:
            text_time("You did not choose a proper path. As punishment start over.", 3)

# I - Functions for each path

    def path_1():
        slow_text(name, ": Please we have to go save my crew! They\'re out there alone!", b)
        print()
        text_time("You look around and realize everyone is laughing.", a)
        text_time("This is serious...why are they laughing!?", a)
        print()
        slow_text("Captain Alves: ", "Look here matey. Wha's in it fer us? we be pirates after all", b)
        print()
        text_time("Captain Alves grins and gets closer.", a)
        text_time("His breath reeks of alcohol.", a)
        text_time("His teeth stained yellow.", a)
        text_time("Yet you understand...he's not to be messed with.", a)
        print()
        slow_text(name, ": I...I can lead you to treasure!", b)
        slow_text(name, ": You take me there and the treasure is all yours", b)
        print()
        time.sleep(1)
        path_3()

    def path_2():
        slow_text(name, ": I appreciate you saving me, but when do we reach land?", b)
        print()
        text_time("You look around and realize everyone is laughing.", a)
        print()
        slow_text("Captain Alves: ", "Land!! ye hear that lads bucko here wants to go to land", b)
        time.sleep(a)
        print()
        text_time("Captain Alves grins and gets closer.", a)
        print()
        slow_text("Captain Alves: ", "Ye weren't jus' marooned at sea fer naught...wha' do ye know", b)
        slow_text("Captain Alves: ", "Either ye tell me or ye walk the plank!", b)
        time.sleep(a)
        print()
        text_time("You start to tremble.", a)
        text_time("You can't go back...not to that thing. It'll kill you this time for sure.", a)
        text_time("Take a deep breathe in.", a)
        slow_text("", "1", a)
        slow_text("", "2", 2)
        slow_text("", "3", 2)
        print()
        slow_text(name, ": Treasure...i can take you there", b)
        slow_text(name, ": But...but if we find my crew we bring them back safe", b)
        print()
        path_3()

    def path_3():
        slow_text("Captain Alves: ", "Now ye're talkin' me language...show me this map", b)
        time.sleep(a)
        print()
        text_time("Captain Alves glances at the map.", a)
        text_time("He turns to his parrot Hash.", a)
        text_time("A grin on his face as you see the excitement lit his eyes.", a)
        print()
        slow_text("Captain Alves: ", "Looks like we got ourselves a big one boys", b)
        slow_text("Captain Alves: ", "Prep the decks, raise the sails...we're gon be rich lads!", b)
        slow_text("Captain Alves: ", f"And you {name}, it's because of yer beauty!", b)
        time.sleep(a)
        print()
        text_time("Captain Alves begins to laugh as he takes a sip of whiskey.", a)
        text_time("The crew mates begin preparing the ship.", a)
        text_time("Everyone is in high spirits...but are they ready for what's to come?", a)
        text_time("The crew mates begin preparing the ship.", 3)
        print()
        os.system('cls')
        slow_text("", "A WEEK LATER", b)
        time.sleep(3)
        print()
        print()
        text_time("The sky is calm. The ship sailed smoothly.", a)
        text_time("Nevertheless, there's tension in the air.", a)
        text_time("You pray that thing isn't still there.", a)
        print()
        slow_text("Captain Alves: ", f"Com'er {name} that's it! We found it!", b)
        slow_text("Captain Alves: ", "Lower the anchors!!", b)
        time.sleep(a)
        print()
        text_time("The boat begins to shake.", a)
        text_time("Fear.", a)
        text_time("You begin to feel fear.", a)
        text_time("It's here. That thing is still here.", a)
        print()
        slow_text(name, ": We have to go back. NOW!", b)
        time.sleep(a)
        print()
        text_time("Before you could even finish it appears.", a)
        text_time(f"The legendary {monster}.", 2)
        print()
        for index in range(25):
            os.system('cls')
            time.sleep(0.05)
            for i in range(index):
                print()
            print(monster_1)
            time.sleep(0.05)
        for index in range(25, 0, -1):
            os.system('cls')
            time.sleep(0.05)
            for i in range(index):
                print()
            print(monster_1)
            time.sleep(0.05)
        time.sleep(2)
        print()
        slow_text("Captain Alves: ", "What in the F*ck!!", b)
        print()
        time.sleep(2)
        print("Two paths are revealed:")
        print()
        print('Path #1: Attack the monster!')
        print('Path #2: Run away!')
        print()
        second_path = input("Which path will you choose? (1/2): ")
        if second_path == '1':
            print()
            path_4()
        elif second_path == '2':
            print()
            path_5()
        else:
            text_time("You did not choose a proper path. As punishment start over.", 3)

    def path_4():
        print()
        text_time("Without hesitation you look around.", a)
        text_time(f"You see a {weapon}!", a)
        text_time("PERFECT!", a)
        text_time(f"You charge towards the {monster}.", a)
        print()
        slow_text(name, f": You're dead {monster}", b)
        print()
        time.sleep(a)
        text_time(f"You throw the {weapon}. A DIRECT HIT.", a)
        text_time("It did nothing. Not even a scratch", a)
        text_time(f"The {monster} SCREAMS.", a)
        text_time("The sounds are deafening and your ears start ringing.", a)
        text_time("You take a step back.", a)
        text_time("Off balance you trip and fall.", a)
        text_time("For some reason you aren't shivering anymore.", 2)
        text_time("As you lay there you aren't scared.", 2)
        text_time("You take a deep breath and close your eyes.", a)
        time.sleep(2)
        os.system('cls')
        path_end()

    def path_5():
        print()
        text_time("Without hesitation you begin to run.", a)
        text_time("You're scared. Tripping over yourself as you head for the life raft.", a)
        print()
        slow_text("Captain Alves: ", f"{name.upper()}!!!!!", b)
        slow_text("Captain Alves: ", "WHERE ARE YOU GOING COWARD", b)
        time.sleep(a)
        print()
        text_time("You ignore everything and run.", a)
        text_time("As fast as you've ever ran before.", a)
        text_time("You reach the edge of the boat.", a)
        text_time("You look up and...", 2)
        os.system('cls')
        print(monster_1)
        time.sleep(0.5)
        os.system('cls')
        path_end()

# I - This function ends the game

    def path_end():

        # NI - This is the end art

        art_end = r"""

        $$$$$$$$\ $$\                       $$$$$$$$\                 $$\ 
        \__$$  __|$$ |                      $$  _____|                $$ |
           $$ |   $$$$$$$\   $$$$$$\        $$ |      $$$$$$$\   $$$$$$$ |
           $$ |   $$  __$$\ $$  __$$\       $$$$$\    $$  __$$\ $$  __$$ |
           $$ |   $$ |  $$ |$$$$$$$$ |      $$  __|   $$ |  $$ |$$ /  $$ |
           $$ |   $$ |  $$ |$$   ____|      $$ |      $$ |  $$ |$$ |  $$ |
           $$ |   $$ |  $$ |\$$$$$$$\       $$$$$$$$\ $$ |  $$ |\$$$$$$$ |
           \__|   \__|  \__| \_______|      \________|\__|  \__| \_______|
                                                            by CoconutA4

             """

        time.sleep(5)
        print()
        print()
        print(art_end)
        print()
        time.sleep(10)
        print()

# NI - Advt game art

    art_ex = r"""
        .=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
        |                     ______                     |
        |                  .-"      "-.                  |
        |                 /            \                 |
        |     _          |              |          _     |
        |    ( \         |,  .-.  .-.  ,|         / )    |
        |     > "=._     | )(__/  \__)( |     _.=" <     |
        |    (_/"=._"=._ |/     /\     \| _.="_.="\_)    |
        |           "=._"(_     ^^     _)"_.="           |
        |               "=\__|IIIIII|__/="               |
        |              _.="| \IIIIII/ |"=._              |
        |    _     _.="_.="\          /"=._"=._     _    |
        |   ( \_.="_.="     `--------`     "=._"=._/ )   |
        |    > _.="                            "=._ <    |
        |   (_/         Adrift at sea              \_)   |
        |                     by CoconutA4               |
        '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='

     """

    print(art_ex)
    time.sleep(1)
    print()

# I - Start of the Adventure game

    startGame = input("Welcome! Are you ready to begin this adventure? (Y/N): ")

    if startGame == "n" or startGame == "N":
        text_time("Tragic!, maybe later!", 3)
    elif startGame == "y" or startGame == "Y":
        name = input("What is your name?: ")
        weapon = input("Choose any weapon of choice (any object): ")
        monster = input("Type a word of something u love: ")
        intro()
    else:
        text_time("You did not choose a proper path. As punishment you start over.", 3)

# NI - Start choice var

choice = 0

# I - Loop waiting for an answer

art_start = r"""
           __________                                 
         .'----------`.                              
         | .--------. |                             
         | |########| |       __________              
         | |########| |      /__________\             
.--------| |########| |------| --=--    |-------------.
.--------| `--------' |------|    --=-- |-------------.
|        `----,-.-----'      |o ======  |             | 
|       ______|_|_______     |__________|             | 
|      /  %%%%%%%%%%%%  \    Welcome to Spax          | 
|     /  %%%%%%%%%%%%%%  \      MultiGame Platform    | 
|     ^^^^^^^^^^^^^^^^^^^^           -> by CoconutA4  | 
+-----------------------------------------------------+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

 """

print(art_start)
while choice !=1 or choice !=2 or choice !=3:

    choice = input("Would you like to play Guess (1), Snaky (2), or Explorer (3)? \n\n")
    if choice == "1":
        sg()
    if choice == "2":
        sk()
    if choice == "3":
        ex()
    else:
        print("U need to choose 1,2 or 3 :)")
