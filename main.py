import time
import random
import sys

USER_SCORE = 0
USER_INPUT = input("press any key to start and hit return (Enter)")
ANIMALS = ["Lion", "Crocodile", "Snake"]
RANDOM_CHOOSED_ANIMAL = random.choice(ANIMALS)

NO_OF_TURNS = 0


SWITCHER = True
wrong_choices = []

# Handle wining situation


def cong_message():
    print(f"Congratulations You won !!!!!")
    play_again()


# Handle losing situation
def losing_message():
    print_sleep("Sorry you lost the game :|")
    play_again()


def check_continue(score):
    global SWITCHER
    switch_on()
    prompt_message = """Congratulations You won!!
    do you want to complete or end (C/E)"""
    if score >= 3:
        bring_input(prompt_message)
        while SWITCHER:
            if USER_INPUT == "complete" or USER_INPUT == "c":
                switch_off()
                return
            elif USER_INPUT == "end" or USER_INPUT == "e":
                switch_off()
                print_sleep("Ok!")
                play_again()
            else:
                invalid_option(prompt_message)
    elif score <= -2:
        losing_message()
    else:
        return
    switch_on()

# Specify the correct choice


def st_wrong_choices(value):
    global wrong_choices
    wrong_choices = value


# Handling user's answer
def removing_spaces_lower():
    global USER_INPUT
    USER_INPUT = USER_INPUT.lower().replace(" ", "")


# Handle printing

def print_sleep(text):
    time.sleep(1.5)
    print("\n")
    print(text)
    time.sleep(1.5)


# Handling invalid choices
def invalid_option(prompt):
    time.sleep(0.5)
    print_sleep(" Invalid Choice :| , Please stick to the valid choices ! ")
    bring_input(prompt)

# Bringing user choice


def bring_input(prompt):

    global USER_INPUT
    time.sleep(1)
    USER_INPUT = input(prompt)
    removing_spaces_lower()


# Controlling While Loops
def switch_on():
    global SWITCHER
    SWITCHER = True


def switch_off():
    global SWITCHER
    SWITCHER = False


# Handling play again
def play_again():
    global SWITCHER
    global USER_INPUT
    global NO_OF_TURNS
    global USER_SCORE
    print_sleep(f"Your score is {USER_SCORE}")
    NO_OF_TURNS = 0
    prompt_message = "do you want to play again (Y/N)"
    print("\n")
    time.sleep(0.5)
    bring_input(prompt_message)
    switch_on()
    while SWITCHER:

        if USER_INPUT == "y" or USER_INPUT == "yes":
            switch_off()
            print("ok!!")
            time.sleep(1.5)
            main()

        elif USER_INPUT == "n" or USER_INPUT == "no":
            switch_off()
            print_sleep("Ok thank you :||")
            time.sleep(2)
            sys.exit(0)

        else:
            invalid_option(prompt_message)


def increse_no_of_turns():
    global NO_OF_TURNS
    NO_OF_TURNS += 1


def old_man_path():
    global USER_SCORE
    global USER_INPUT
    global SWITCHER
    global wrong_choices
    global NO_OF_TURNS

    if NO_OF_TURNS < 3:
        switch_on()
        print_sleep("Imagine that you are a young man ")
        print_sleep("Hello can you help me !!\n")
        print_sleep("Old man: Hmm a young man \n")
        print_sleep(""" Old man :
        Do You want my advice ?""")
        print_sleep("YESS YESS !!\n")
        print_sleep("""Old man : Ok But first
        You must answer this question to take my advice""")
        print_sleep("ASK!\n")
        print_sleep("""Do you want it
         a) Easy (+1pt)
         b) Medium (+2pts)
         c) Hard  (+3pts)
         (All of them decrease 1 when answering incorrectly
         except for easy it decreases
         2pts when answering incorrectly)
         (when correctly from the first time (question) !!
         second: your score += n - 1
         where n is the initial score added from the first question
         according to the difficulty except easy one)""")
        bring_input("Enter Your choice (a,b,c):")

        while SWITCHER:

            if USER_INPUT == "easy" or USER_INPUT == "a":

                bring_input("""
                f(x) = x^2 + 3x + 4
                then , dy/dx [f(x)] at x = 2
                a) 11
                b) 9
                c) 14
                d) 7
                Enter your answer (a,b,c,d):""")

                st_wrong_choices(["a", "b", "c", "11", "9", "14"])
                while SWITCHER:
                    if USER_INPUT in wrong_choices:
                        USER_SCORE -= 2
                        print_sleep(f"Sorry the answer is incorrect")
                        print_sleep(f"your score is{USER_SCORE}")

                        if USER_SCORE == -2:
                            switch_off()
                            print("Sorry you lost the game \n")
                            play_again()

                        else:
                            print_sleep("You still have a chance")
                            print_sleep("""
                            Answer this question :-
                                Assuming that:
                                person asked someone:
                                ('How many watermelons does you have')
                                he answered (10)
                                then,
                                when he ask him
                                ('How many 3 watermelons does you have')
                                he should answer with ?
                                a) 5/6
                                b) 10
                                c) 10/3
                                d) 3""")
                            bring_input("Enter your answer (a,b,c,d):")
                            st_wrong_choices(["a", "b", "d", "5/6", "3", "10"])
                            while SWITCHER:
                                if USER_INPUT in wrong_choices:
                                    switch_off()
                                    losing_message()

                                elif USER_INPUT == "10/3" or USER_INPUT == "c":
                                    switch_off()
                                    print_sleep("Nice !\nagain but stay alert")
                                    increse_no_of_turns()
                                    old_man_path()
                                else:
                                    invalid_option("Enter your answer:")

                    elif USER_INPUT == "d" or USER_INPUT == "7":
                        switch_off()
                        USER_SCORE += 1
                    else:
                        invalid_option("Enter your answer (a,b,c,d):")

            elif USER_INPUT == "b" or USER_INPUT == "medium":
                bring_input("""
                f(x) = 2 - √x-3 / x²-49
                (note : (x-3) all of it under the square root )
                then lim x → 7 [f(x)]
                a) Undefined
                b) 1/56
                c) - 2/112
                d) Zero
                Enter Your choice:""")
                st_wrong_choices(["a", "b", "d", "0", "zero",
                                  "1/56",
                                  "undefined"])
                while SWITCHER:
                    if USER_INPUT in wrong_choices:
                        print_sleep("Sorry your answer is incorrect :|")
                        USER_SCORE -= 1
                        bring_input("""
                        Take another one and try to compensate:-
                        f(x) = sin(x) - cos(x) / cos(2x)
                        Lim x → π /4 [f(x)]
                        a) -√2
                        b) √2
                        c)  (-1)³ x -√2 / -(-2)
                        d) (-1)² x  -√2 / -(-2)
                        Enter your answer (a,b,c,d): """)
                        st_wrong_choices(["a", "b", "c", "-√2", "√2",
                                          "(-1)³ x -√2 / -(-2)"])
                        while SWITCHER:
                            if USER_INPUT in wrong_choices:
                                switch_off()
                                losing_message()
                            elif USER_INPUT == "d" or \
                                    USER_INPUT == "(-1)²x -√2/-(-2)":
                                switch_off()
                                USER_SCORE += 2
                            else:
                                invalid_option("Enter your answer (a,b,c,d):")

                    elif USER_INPUT == "c" or \
                        USER_INPUT == "-2/112" \
                            or USER_INPUT == "-1/56":
                        switch_off()
                        print_sleep("Good job")
                        USER_SCORE += 2
                    else:
                        invalid_option("Enter your answer (a,b,c,d):")

            elif USER_INPUT == "hard" or USER_INPUT == "c":
                bring_input(""" f(x) = log(x²+2x) base 2
                    Find dy/dx [f(x)] =
                     a) (2x+2) / (x²+2x)(ln(2))
                     b) 1 / ln(2)
                     c) (2x+2) / (x² + 2x) (ln(2)) (2x+2)
                     d) 1/ x² + 2x
                     Enter Your choice (a,b,c,d): """)
                st_wrong_choices(["b", "c", "d",
                                  "1/ln(2)",
                                  "(2x+2)/(x² + 2x)(ln(2))(2x+2)",
                                  "1/x²+2x"])
                while SWITCHER:
                    if USER_INPUT in wrong_choices:
                        USER_SCORE -= 1
                        print_sleep("Sorry your answer is incorrect :||")
                        print_sleep("Don't worry try another one")
                        bring_input("""f(x) = 7^x (7 power x)
                        dy/dx [f(x)] =
                        a) 7^x * ln(7)
                        b) 1/x
                        c) 7^x
                        d) 7x
                        Enter your choice (a,b,c,d):""")
                        st_wrong_choices(["b", "c", "d", "1/x", "7^x", "7x"])
                        while SWITCHER:
                            if USER_INPUT in wrong_choices:
                                switch_off()
                                losing_message()
                            elif USER_INPUT == "a" or \
                                    USER_INPUT == "7^x*ln(7)":
                                switch_off()
                                print_sleep("Nice !!")
                                USER_SCORE += 3
                            else:
                                invalid_option("Enter Your choice (a,b,c,d):")

                    elif USER_INPUT == "a" or \
                            USER_INPUT == "(2x+2)/(x²+2x)(ln(2))":
                        switch_off()
                        USER_SCORE += 3
                        print_sleep(f"Good Job your score is {USER_SCORE}")
                    else:
                        invalid_option("Enter Your choice (a,b,c,d):")
            else:
                invalid_option("Enter Your choice (a,b,c):")

        check_continue(USER_SCORE)

        print_sleep(f"Good Effort Your score is {USER_SCORE}")

        print_sleep("Old man : Bravo! A thing to remember ..... ")

        print_sleep("tell mee tell meee !!!!!!!!!!!")

        print_sleep("Old man : Iam sorry , Do you know Dolphins ?? ")

        print_sleep("Yes I know !")

        print_sleep("Me too hahahahhahahah !!")
        print_sleep("thank you for answering the question Go ahead !")

        print_sleep(" Y3m sit down !!!! Salamo 3leko   ")

        print_sleep("Old Man : 3lykom el salam ya 3sl   10³ salama :) ")

        print_sleep("........ Running into a man who is crying .............")

        bring_input("Help Him (Y/N)")

        while SWITCHER:
            # Handling choices
            if USER_INPUT == "y" or USER_INPUT == "yes":

                prompt_message = """Where do you want to hit him ?
                                  b) his leg
                                  a) his back
                        (Unordered choices is intentional :| )
                                  """
                print_sleep("Why are you crying ??")
                print_sleep("Man: Where is my son ??? where is my son ??? :( ")
                print_sleep(" keep calm keep calm ")
                print_sleep("Man:O....")
                print_sleep("Man:He is there with the evil man there let's go")
                print_sleep("Let's go to save him")
                print_sleep("Man : I think his weakness point is his leg")
                print("try to hit his leg !")
                print_sleep("......... Close to the evil man ...........")

                bring_input(prompt_message +
                            "Enter Your choice (a,b):")
                while SWITCHER:

                    if USER_INPUT == "a" or USER_INPUT == "hisback":
                        switch_off()
                        print_sleep("Don't you  remember man's words ?\n")
                        USER_SCORE -= 1
                        print_sleep(f"Sorry you lost :| ")
                        print_sleep(f"your score is {USER_SCORE}")
                        play_again()

                    elif USER_INPUT == "b" or USER_INPUT == "hisleg":
                        switch_off()
                        print_sleep(".........Evil man defeated ......... ")
                        print_sleep("Man: Alhamdulillah    ")
                        print_sleep("Alhamdulillah  !\n \n")
                        print_sleep("Is your son fine ? \n")
                        print_sleep("Man : Yes :)")
                        print_sleep("Do you need anything ? ")
                        print_sleep("No :)")
                        print_sleep("salamo 3lekom")
                        print_sleep("Man : 3lekom El salam :)")

                        cong_message()

                    else:
                        invalid_option(prompt_message)

            elif USER_INPUT == "n" or USER_INPUT == "no":
                USER_SCORE -= 1
                if USER_SCORE == -2:
                    switch_off()
                    losing_message()

                else:
                    switch_off()
                    print_sleep("Why ??? Go to the main and stay nobel !!! ")
                    main()

            else:
                invalid_option("Help Him (Y/N)")

    else:
        print_sleep("You run out no of turns :|| Sorry")
        losing_message()


def animals_path():
    global RANDOM_CHOOSED_ANIMAL
    global NO_OF_TURNS
    if NO_OF_TURNS != 3:
        print_sleep("I love courage")
        print_sleep(f"but why do you want to go to {RANDOM_CHOOSED_ANIMAL} :)")
        losing_message()
    else:
        print_sleep("You run out no of turns :| sorry")
        losing_message()


def house_path():
    switch_on()

    global USER_SCORE
    global USER_INPUT
    global SWITCHER
    global wrong_choices
    global NO_OF_TURNS

    # Handling no of turns
    if NO_OF_TURNS != 3:
        prompt_message = """Stay for Help or return to the main
                                    a) Escape
                                    b) Stay \n Enter your answer(a,b)"""
        switch_on()
        print_sleep("Imagine")
        print_sleep(".......Running to the house..........")
        print_sleep("Young Boy:Can you help us ?!!")
        print("There is a thief in the house")
        print_sleep("....... He might have been shocked.........")
        print_sleep("""Young boy : I think he is trying to open the door
                    if he opens it he might hurt us
                    (2nd condition :) )""")
        print_sleep("Young boy : Try to stop him from opening the door")
        print(" and don't open it !!! ")
        print_sleep("............Getting close to the door...............")
        print_sleep("""To follow the young boy's advice
        If We assume that the theif pushes the door
         with a Force of magnitude 100√3 N
        which inclined to the vertical with angle (60 degree)
        Find : What is the magnitude of the force
        do you need to push with at the middle of the door
        to  Implement boy's advice ?
         a) 50√3 N
         b) 150 N
         c) 100√3 N
         d) 150√3 N""")

        bring_input("Enter your answer (a,b,c,d):")

        st_wrong_choices(["a", "c", "d", "150√3", "100√3", "50√3"])

        # Handling situations
        while SWITCHER:
            if USER_INPUT in wrong_choices:
                USER_SCORE -= 1
                print_sleep("Sorry The answer is incorrect ")
                print(f"your new score is {USER_SCORE}")
                if USER_SCORE == -2:
                    switch_off()
                    losing_message()

                print_sleep("..........Door Opened...........")

                bring_input(prompt_message)

                while SWITCHER:
                    if USER_INPUT == "a" or USER_INPUT == "escape":
                        switch_off()
                        print_sleep("Not a nobel behaviour :|")
                        main()
                    elif USER_INPUT == "b" or USER_INPUT == "return":
                        quad_msg = """Solve for x this to get back
                        to the beginning of the path
                                2x² - 3x + 21  = -x² + 4x + 5
                        X ∈
                        a) {3,2}
                        b) {2}
                        c) X has no solution in R
                        d) {3,4}
                        Enter your answer (a,b,c,d):"""
                        bring_input(quad_msg)
                        st_wrong_choices(["a", "b", "d", "{3,2}", "{2}",
                                          "{3,4}"])
                        while SWITCHER:
                            if USER_INPUT in wrong_choices:
                                losing_message()
                                if USER_SCORE == -2:
                                    switch_off()
                                    losing_message()
                            elif USER_INPUT == "c":
                                switch_off()
                                print_sleep("Good job !!")
                                print("Retry the path again stay Alert!!")
                                increse_no_of_turns()
                                print_sleep(f"no of turns is {NO_OF_TURNS}")
                                print("Max : 3")
                                house_path()

                            else:
                                invalid_option(quad_msg)

                    else:
                        invalid_option(prompt_message)

            elif USER_INPUT == "150n" or USER_INPUT == "b":
                USER_SCORE += 1
                print_sleep("Good Effort !\n")
                print_sleep(".......... Stopping pushing ........\n")
                print_sleep("Young Boy : He is there Runnn !")
                print_sleep("Ok Let's Goo ")
                bring_input("""If We assume that he will have escaped
                after 1 min  and you was at rest and begin to run
                     with velocity of 18 km/h and with acceleration 3m/s
                    Assume he is (at stationary state)
                    and  he was at a displacement 5700.1 m away
                    from you then can you catch him or he will escape ?
                a) Yes, Catching him is possible even if he was more 10cm away
                b) NO, Catching him is probably not possible more10m is needed
                c) NO, Catching him is probably not possible more10cm is needed
                d) Yes, Catching him is possible even
                if he was more 779.9 m away\n
                Enter your answer (a,b,c,d)\n
                """)
                st_wrong_choices(["a", "b", "d"])
                if USER_INPUT in wrong_choices:
                    USER_SCORE -= 1
                    print_sleep("Sorry your answer is incorrect :||")
                    print_sleep("""
                    Take another question you still have a chance :-
                    Given : 9x² = 25y² + 20y + 4
                     then:
                             8^x / 32^y = ?
                (8 raise to power x over 32 raised to the power y ?),
                     a) 4
                     b) 2x
                     c) (1/4)^(x-y)
                     d) 8
                     """)
                    bring_input("Enter your choice(a,b,c,d) :")
                    st_wrong_choices(["b", "c ", "d", "2x", "8",
                                      "(1/4)^(x-y)"])
                    while SWITCHER:
                        if USER_INPUT in wrong_choices:
                            switch_off()
                            losing_message()
                        elif USER_INPUT == "4" or USER_INPUT == "a":
                            switch_off()
                            USER_SCORE += 1
                            print_sleep("Good effort again but stay alert!! ")
                            increse_no_of_turns()
                            house_path()
                        else:
                            invalid_option("Enter your choice(a,b,c,d) :")

                elif USER_INPUT == "c":
                    switch_off()
                    print_sleep("Young boy:Yes we did alhamdulillah !!! ")
                    print_sleep("Yes , Alhamdulillah !!!")
                    cong_message()
                else:
                    invalid_option("Enter your answer (a,b,c,d):")
            else:
                invalid_option("Enter your answer (a,b,c,d):")
    else:
        print_sleep("Sorry you run out of turns :|")
        losing_message()


def main():
    switch_on()
    global USER_SCORE
    global USER_INPUT
    global SWITCHER
    global RANDOM_CHOOSED_ANIMAL
    global NO_OF_TURNS
    USER_SCORE = 0
    increse_no_of_turns()
    print_sleep(f"Your number of turns is {NO_OF_TURNS} \n Max: 3 ")
    if NO_OF_TURNS != 3:
        print_sleep(" ALL OF THESE STORY'S SITUATION ARE FAKE \n")
        print("They are not real!")
        print("ALL of these are imagination !!!!!")
        print_sleep(" Imagine you are a ")
        print("young man  in a dark forest")
        print_sleep("Looking Behind you !! You saw an old man \n")
        print_sleep(f"Looking to your right !!")
        print(f"You saw a {RANDOM_CHOOSED_ANIMAL}\n")
        print_sleep("Looking to your left !! You saw an abandoned house\n")
        print_sleep(" Before you choose take a preparatory question :)\n")
        print_sleep("""        How many Surahs in the  Holy Quran?
                a) 30
                b) 114
                c) 100
                d) 112 """)
        bring_input("Enter Your answer(a,b,c,d):")
        st_wrong_choices(["a", "d", "c", "100", "112", "30"])
        # Handling the first question answer :)
        while SWITCHER:
            if USER_INPUT in wrong_choices:
                if USER_INPUT == "a" or USER_INPUT == "30":
                    print_sleep("stay Alert !! I wrote Suhras not parts :)")
                switch_off()
                USER_SCORE -= 1
                print_sleep(f"Sorry the answer is incorrect")
                print(f"Your score is {USER_SCORE} ")
                print_sleep("The correct is 114 :)")

            elif USER_INPUT == "b" or USER_INPUT == "114":
                USER_SCORE += 1
                print_sleep(f"Allah bless you,Your answer is correct")
                print(f"Your new score is {USER_SCORE} \n Keep Going !!!")
                switch_off()

            else:
                invalid_option("Enter Your answer(a,b,c,d):")

        switch_on()
        # ----------------------------------------------------------------------------------------------

        print_sleep("Now Let's Choose the path you want to choose !!!!")
        print_sleep(f"""  Select the path :-
        a) Going to the old man
        b) Going to the {RANDOM_CHOOSED_ANIMAL}
        c) Going to the abandoned house
        """)
        # Handling Choosing path
        bring_input("Enter Your choice(a,b,c) :")
        while SWITCHER:
            if USER_INPUT == "a":
                old_man_path()
                switch_off()
            elif USER_INPUT == "b":
                animals_path()
                switch_off()

            elif USER_INPUT == "c":
                house_path()
                switch_off()
            else:
                invalid_option("Enter Your answer(a,b,c):")

    else:
        losing_message()
    switch_on()


main()

# Done Alhamdulillah
# Sorry for making the python code in a single file
# Sorry for using global variables in the function but
# the code will run smoothly insha'Allah
# AI tools for bringing symbols and
# ensuring the answers of some questions
# and also search engines , articles , websites
# and videos for expanding knowledge and knowing
# new modules
# :),:)
