import sys
import random
from colorama import Fore, Style
import time

random.seed(time.time())


def choice_yes_no(prompt):
    choice = input(prompt)
    while choice not in ['Yes', 'No', 'yes', 'no']:
        choice = input(f"Please enter only Yes or No.\n{prompt}")
    return choice


def day_passed():
    stats["today"] += 1
    return stats["today"]


def player_name():
    stats["name"] = input("What is your name?\n")
    return stats["name"]


def player_gender():
    stats["gender"] = input("What is your gender?\n")
    while stats["gender"] not in ['male', 'female', 'other']:
        stats["gender"] = input(
            "Your choices are male, female or other.\nPlease choose one of the above.\n")
    return stats["gender"]


def player_age():
    while True:
        age_input = input("How old are you?\n")
        try:
            age = int(age_input)
            if 0 < age < 100:
                stats["age"] = age
                break
            else:
                print("Please be realistic and input an age between 1 and 99.\n")
        except ValueError:
            print("Only numbers allowed.\n")
    return stats["age"]


def menu_choice():
    choice = input("Choose where you want to navigate.\n")
    while choice not in ['Start', 'Description', 'Reset', 'Quit Game']:
        choice = input(
            "Please choose between Start, Description and Quit Game.\n")
    return choice


def events_counter():
    stats["events_seen"] += 1
    print("\nYou have experienced a new event. Congratulations.")
    return stats["events_seen"]


def lucky_money():
    luck = random.choice([1, 2, 3, 4])
    if luck == 1:
        print(f"{Fore.GREEN}This is your lucky day. You found 10 Euros on the floor.",
              Style.RESET_ALL, "\nWill you take them?")
        choice = choice_yes_no("Will you pick them up?\n")
        if choice == 'Yes' or choice == 'yes':
            stats["purse"] += 10
            print(f"{Fore.GREEN}You now have",
                  stats["purse"], "Euros!", Style.RESET_ALL)
        elif choice == 'No' or choice == 'no':
            print(
                "\nYou left the money where you found them, maybe someone else needs them more.")
            if stats["key_events"]["good_samaritan"] == False:
                events_counter()
            stats["key_events"]["good_samaritan"] = True  # nr.4
    elif luck == 2:
        stats["purse"] += 5
        print(f"{Fore.GREEN}\nNot bad, you found 5 Euros forgotten in your jacket!",
              "You now have", stats["purse"], "Euros!", Style.RESET_ALL)
    elif luck == 3:
        print("You tripped and fell down, ripping a hole on your jeans, on the position of the right knee.")
    elif luck == 4:
        print(f"{Fore.RED}Someone bumped into you.", Style.RESET_ALL)
        time.sleep(2)
        print(
            f"{Fore.RED}You check your purse and notice, 5 Euros are missing!", Style.RESET_ALL)
        stats["purse"] -= 5
        print(f"{Fore.RED}You now have",
              stats["purse"], "Euros...", Style.RESET_ALL)


def fortune_choice():
    print(f"{Fore.LIGHTMAGENTA_EX}\nWhat kind of insight into your future would you like to have?", Style.RESET_ALL)
    choice = input(
        f"{Fore.LIGHTMAGENTA_EX}You may choose between Money, Worklife or Lovelife.\n{Style.RESET_ALL}")
    while choice not in ['Money', 'money', 'Worklife', 'worklife', 'Lovelife', 'lovelife']:
        choice = input(
            "You may ONLY choose between Money, Worklife or Lovelife.\n")
    if choice == 'Money' or choice == 'money':
        return fortune_money()
    elif choice == 'Worklife' or choice == 'worklife':
        return fortune_work()
    elif choice == 'Lovelife' or choice == 'lovelife':
        return fortune_love()


def fortune_love():
    luck = random.choice([1, 2, 3, 4, 5])
    global death
    global skip
    if luck == 1:
        print(f"{Fore.LIGHTMAGENTA_EX}\nIt looks like someone, who's interested in you will make a move soon.", Style.RESET_ALL)
    elif luck == 2:
        if stats["age"] < 50:
            print(
                f"{Fore.LIGHTMAGENTA_EX}\nIt seems you are walking down the right path young one", Style.RESET_ALL)
        else:
            print(
                f"{Fore.LIGHTMAGENTA_EX}\nIt seems you are walking down the right path old one", Style.RESET_ALL)
    elif luck == 3:
        print(f"{Fore.LIGHTMAGENTA_EX}\nThings aren't looking good for you. Maybe try a different aproach.", Style.RESET_ALL)
    elif luck == 4:
        print(
            f"{Fore.LIGHTMAGENTA_EX}\nMaybe you are destined to die alone...", Style.RESET_ALL)
    elif luck == 5:
        print("Oh... What have you brought here... Nooooo!\n")
        time.sleep(3)
        print(
            f"{Fore.RED}A car crashes inside the tent, killing you both instantly. A demon smiles...{Style.RESET_ALL}\n")
        if stats["key_events"]["smiling_demon"] == False:
            events_counter()
        stats["key_events"]["smiling_demon"] = True  # nr.2
        death = True
        skip = True
        stats["deaths"] += 1
    if stats["key_events"]["love_fortune"] == False:
        events_counter()
    stats["key_events"]["love_fortune"] = True  # nr.5
    return stats["key_events"]["love_fortune"], death, skip, stats["deaths"]


def fortune_work():
    luck = random.choice([1, 2, 3, 4, 5])
    global death
    global skip
    if luck == 1:
        print(
            f"{Fore.LIGHTMAGENTA_EX}\nIt looks like a huge promotion will happen soon.", Style.RESET_ALL)
    elif luck == 2:
        print(f"{Fore.LIGHTMAGENTA_EX}\nYou will get a salary raise soon. Stick to what you are doing.", Style.RESET_ALL)
    elif luck == 3:
        print(f"{Fore.LIGHTMAGENTA_EX}\nA coworker will try to put problems before you, be cautious and keep your cool.", Style.RESET_ALL)
    elif luck == 4:
        print(f"{Fore.LIGHTMAGENTA_EX}\nI would start applying myself soon if I were you...", Style.RESET_ALL)
    elif luck == 5:
        print("Oh... What have you brought here... Nooooo!\n")
        time.sleep(3)
        print(
            f"{Fore.RED}A car crashes inside the tent, killing you both instantly. A demon smiles...{Style.RESET_ALL}\n")
        if stats["key_events"]["smiling_demon"] == False:
            events_counter()
        stats["key_events"]["smiling_demon"] = True  # nr.2
        death = True
        skip = True
        stats["deaths"] += 1
        if stats["key_events"]["work_fortune"] == False:
            events_counter()
    stats["key_events"]["work_fortune"] = True  # nr.7
    return stats["key_events"]["work_fortune"], death, skip, stats["deaths"]


def fortune_money():
    luck = random.choice([1, 2, 3, 4, 5])
    global death
    global skip
    global jackpot
    if luck == 1:
        print(f"{Fore.LIGHTMAGENTA_EX}\nLooks like you will be rich very soon! Do not forget this old Fortune Teller...", Style.RESET_ALL)
        jackpot = luck
    elif luck == 2:
        print(f"{Fore.LIGHTMAGENTA_EX}\nI would look under the spare wheel in the car you inherited.", Style.RESET_ALL)
    elif luck == 3:
        print(f"{Fore.LIGHTMAGENTA_EX}\nI would maybe move my money to a different bank if I were you.", Style.RESET_ALL)
    elif luck == 4:
        print(
            f"{Fore.LIGHTMAGENTA_EX}\nRiches aren't everything, right?...", Style.RESET_ALL)
    elif luck == 5:
        print("Oh... What have you brought here... Nooooo!\n")
        time.sleep(3)
        print(
            f"{Fore.RED}A car crashes inside the tent, killing you both instantly. A demon smiles...{Style.RESET_ALL}\n")
        if stats["key_events"]["smiling_demon"] == False:
            events_counter()
        stats["key_events"]["smiling_demon"] = True  # nr.2
        death = True
        skip = True
        stats["deaths"] += 1
        if stats["key_events"]["money_fortune"] == False:
            events_counter()
    stats["key_events"]["money_fortune"] = True  # nr.6
    return stats["key_events"]["money_fortune"], death, skip, stats["deaths"]


stats = {
    "name": "someone",
    "gender": "something",
    "age": 2,
    "purse": 15,
    "today": 0,
    "deaths": 0,
    "events_seen": 0,
    "true_ending": False,
    "key_events": {
            "walk_away": False,  # nr.1 exists * 2
            "smiling_demon": False,  # nr.2 exists * 3
            "deadly_luck": False,  # nr.3 exists * 1
            "good_samaritan": False,  # nr.4 exists * 1
            "love_fortune": False,  # nr.5 exists * 1
            "money_fortune": False,  # nr.6 exists * 1
            "work_fortune": False,  # nr.7 exists * 1
            "sleeper": False,  # nr.8 exists * 1
            "the_undecisive": False,  # nr.9 exists * 1
            "the_loop": False,  # nr.10 exists * 1
            "jackpot": False  # nr. 11 exists * 1
    }
}


menu = True
game = True
first_tent_encounter = False


player_name()
player_gender()
player_age()


while game == True:
    menu = True
    play = False
    jackpot = 0

    while menu == True:
        print("="*40, "Menu", "="*40)
        print("Start\nDescription\nReset\nQuit Game\n")
        choice = menu_choice()
        if choice == 'Start':
            play = True
            menu = False
        elif choice == 'Description':
            print(f"{Fore.LIGHTCYAN_EX}This is a small text based game about a person, their luck, a shady fortune teller and a cookie.", Style.RESET_ALL)
            time.sleep(5)
        elif choice == 'Reset':
            choice = choice_yes_no(
                f"{Fore.RED}Would you like to reset your achievements?\n{Style.RESET_ALL}")
            if choice == 'Yes' or choice == 'yes':
                choice = choice_yes_no(
                    f"{Fore.RED}Are you sure?\n{Style.RESET_ALL}")
                if choice == 'Yes' or choice == 'yes':
                    for key in stats["key_events"]:
                        stats["key_events"][key] = False
                        stats["true_ending"] = False
                    print("Achievements reset.\n")
                    time.sleep(3)
                elif choice == 'No' or choice == 'no':
                    print(f"{Fore.YELLOW}Achievements kept.\n", Style.RESET_ALL)
            else:
                print(f"{Fore.YELLOW}Achievements kept.\n", Style.RESET_ALL)
        elif choice == 'Quit Game':
            game = False
            menu = False

    while play == True:
        death = False
        skip = False

        choice = choice_yes_no("Would you like to see your stats?\n")

        if choice == 'Yes' or choice == 'yes':
            for key, value in stats.items():
                print(f"{Fore.CYAN}{key}: {Fore.YELLOW}{value}{Style.RESET_ALL}")
        elif choice == 'No' or choice == 'no':
            print("If you don't want to...\n")
            time.sleep(3)
        day_passed()
        print("="*40, "Day", stats["today"], "="*40)
        time.sleep(3)
        print(" ")
        print(" ")
        print(" ")
        print(" ")

        print("="*40, "Apartment", "="*40)
        time.sleep(3)

        choice = choice_yes_no("Will you get out of bed today?\n")

        if choice == 'Yes' or choice == 'yes':
            print("You get off the bed and get ready.\n")
            time.sleep(3)
            print("Your purse has", stats["purse"], "Euros inside.\n")
            print("You grab your keys and walk out the door.\n")
            time.sleep(3)
        else:
            print("You decided to stay in bed today.")
            time.sleep(3)
            skip = True
            if stats["key_events"]["sleeper"] == False:
                events_counter()
            stats["key_events"]["sleeper"] = True  # nr.8

        if skip == False:
            print("="*40, "Town", "="*40)
            time.sleep(3)
            lucky_money()

        if first_tent_encounter == False and skip == False:
            print("You see a dark, creepy Tent on the side of the road. On its sign, you can read 'Fortune Teller'.\n")
            time.sleep(3)
            choice = choice_yes_no("Do you wish to enter the tent?\n")
            first_tent_encounter = True
            if choice == 'Yes' or choice == 'yes':
                print("You decide to spare sometime and enter the tent.")
                time.sleep(3)
            elif choice == 'No' or choice == 'no':
                print("You decided to just continue your walk.")
                time.sleep(3)
                if stats["key_events"]["walk_away"] == False:
                    events_counter()
                stats["key_events"]["walk_away"] = True  # nr.1
                skip = True
        elif first_tent_encounter == True and skip == False:
            print("You see the familiar dark tent once more.\n")
            time.sleep(3)
            choice = choice_yes_no("Will you enter the tent this time?\n")
            if choice == 'Yes' or choice == 'yes':
                print("You decide to give it a shot.\n")
            elif choice == 'No' or choice == 'no':
                print("\nYou get a bad vibe from this place. You walk away.\n")
                time.sleep(3)
                if stats["key_events"]["walk_away"] == False:
                    events_counter()
                stats["key_events"]["walk_away"] = True  # nr.1
                skip = True

        if skip == False:
            print("="*40, "The Tent", "="*40)
            time.sleep(3)
            print("\nInside, you feel an eary aura. The tent is simply decorated and on the center, you see a table with a crystal ball.\n",
                  "On the other side of the table, you notice a creepy, old lady smiling.\n")
            time.sleep(3)
            print(
                f"{Fore.LIGHTMAGENTA_EX}Hello, {Fore.CYAN}{stats["name"]}, {Fore.LIGHTMAGENTA_EX}")
            choice = choice_yes_no(
                "\nWould you like your fortune to be told?\n")
            print(Style.RESET_ALL)
            if choice == 'Yes' or choice == 'yes':
                print("\nThe Fortune Teller hints you to show her your palm.")
                time.sleep(3)
                choice = choice_yes_no(
                    "\nYou feel uneasy. Will you show the Fortune Teller your palm?\n")
                if choice == 'Yes' or choice == 'yes':
                    print("\nThe Fortune Teller studies your palm.")
                    time.sleep(3)
                    fortune_choice()
                elif choice == 'No' or choice == 'no':
                    print("\nYou decided to leave. Even as you exited the tent, the Fortune Teller still had that creepy smile.\nWas this the right choice?\n")
                    time.sleep(3)
                    if stats["key_events"]["the_undecisive"] == False:
                        events_counter()
                    stats["key_events"]["the_undecisive"] = True  # nr.9
                    skip = True
            elif choice == 'No' or choice == 'no':
                print(f"{Fore.LIGHTMAGENTA_EX}Then, what do you want?")
                time.sleep(3)
                print(f"{Fore.BLUE}Nothing...", Style.RESET_ALL)
                time.sleep(3)
                print("The Fortune Teller seemed unamused as your conciousness faided and you woke up in your bed.\nWas this a dream?\n")
                time.sleep(3)
                death = True
                skip = True
                if stats["key_events"]["the_loop"] == False:
                    events_counter()
                stats["key_events"]["the_loop"] = True  # nr.10
                stats["deaths"] += 1

        if death == False and skip == False:
            print("The Fortune Teller did you a service.\nYou have",
                  stats["purse"], "Euros in your purse.\n")
            time.sleep(3)
            choice = choice_yes_no("Will you pay the Fortune Teller?\n")
            if choice == 'Yes' or choice == 'yes':
                stats["purse"] -= 5
                print(f"{Fore.LIGHTMAGENTA_EX}Thank you kind soul.",
                      Style.RESET_ALL)
                time.sleep(3)
            if choice == 'No' or choice == 'no':
                print("You decided the Fortune Teller wasn't worth your money, so you ran away.\nYou could here the Fortune Teller cursing you, as you faded in the distance.\n")
                print(f"{Fore.RED}Just as you thought you ran away, a car loses control and runs you over.\nJust as you are about to pass out, you feel the same eary feeling as you felt when you entered that tent, and then you wake up in your bed. Was this a dream?\n", Style.RESET_ALL)
                time.sleep(3)
                if stats["key_events"]["deadly_luck"] == False:
                    events_counter()
                stats["key_events"]["deadly_luck"] = True  # nr.3
                death = True
                skip = True
                stats["deaths"] += 1

            if skip == False:
                print("="*40, "Town", "="*40)
                time.sleep(3)
                print("You get outside the tent and continue your walk.")
                time.sleep(3)

            if jackpot == 1 and skip == False:
                print(
                    "After a while, you find a suitcase next to a bus stop, but no one is around.\n")
                time.sleep(3)
                choice = choice_yes_no("Will you take the suitcase?\n")
                if choice == 'Yes' or choice == 'yes':
                    print("You grabbed the suitcase and headed straight home. You open it and found",
                          f"{Fore.GREEN}100.000 Euros!\n", Style.RESET_ALL)
                    time.sleep(3)
                    stats["purse"] += 100000
                    if stats["key_events"]["jackpot"] == False:
                        events_counter()
                    stats["key_events"]["jackpot"] = True  # nr.11
                    print("You slept well tonight.\n")
                    time.sleep(3)
                else:
                    print(
                        "You decided to leave the suitcase as is, you don't want to get mixed into anything weird.\n")
                    print("You walked home and slept.\n")
                    time.sleep(3)

        if death == True:
            print("It seems like you died. Would you like another chance?\n")
            time.sleep(3)
            choice = choice_yes_no(
                "Type Yes to play again or No to quit the game.\n")
            if choice == 'Yes' or choice == 'yes':
                play = True
                print("A new day dawns.\n")
                time.sleep(3)
            else:
                print("Thank you for playing!\n")
                play = False

        if death == False:
            choice = choice_yes_no(
                "Would you like to play again? You might have missed something.\n")
            time.sleep(3)
            if choice == 'Yes' or choice == 'yes':
                play = True
                print("A new day dawns.\n")
                time.sleep(3)
            else:
                print("Thank you for playing!")
                play = False

        if all(stats["key_events"].values()):
            print(
                "Congratulations! You finished the whole game! Thank you for your time!\n")
            print("You earned a chocolate-chip cookie.\n")
            stats["true_ending"] = True
