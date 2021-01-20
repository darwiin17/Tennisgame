import player


def read_data():  #skapar en funktion read_data som kollar hur monga spelare som finns i filen och returnerar verdet
    player_list = []  #skapar en lista
    file = open("data.txt", "r")  #leser in textfilen och leser
    lines = file.read().splitlines()  #delar antal rader som kolumner
    file.close()

    line_count = 0
    for l in lines:
        line_count = line_count + 1
        count=0
    while count < line_count:  #Ansetter varje players attribut ett index
        name = lines[count]
        chance = float(lines[count + 1])
        wins = int(lines[count + 2])
        played = int(lines[count + 3])
        player1 = player.player(name, chance, wins, played)  #Distributerar attribut till varje spelare som behovs och I detta fall er attributerna skapade med fyra stegs mellanrum
        player_list.append(player1)
        count = count + 4
        return player_list

def write_data(player_list):
    file = open("data.txt","w")  # Oppnar textfilen och skriver ut den
    for player in player_list:  #programmet skriver ut alla attribut for alla spelare i spelet
        name = player.name
        chance = player.chance
        wins = player.wins
        played = player.played
        file.write(name + '\n')
        file.write(str(chance) + '\n') 
        file.write(str(wins)+ '\n')
        file.write(str(played)+ '\n')
        file.close()
#Funktioner for matchen skapas

#def show_table(name, chance, wins, played):
    #file = open("data.txt", "r")
   # player_list = read_data()
   # for player in player_list:
        #print (player)
    
        print("; Plac ; Namn ; Andel vunna ; Vinster ; Spelade ")
        print(";",name, " "*(4-len(name)), ";", wins, " "*(7-len(wins)), ";", played, " "*(7-len(played)),";", chance, " "*(10-len(chance)),";")


def main():
    player_list = read_data()

    print("* Welcome to tennis game *") #skriver meny metod
    print("1. New Game\n2. Show Table\n3. Exit")
    while True:
        try:
            x = input()
            x = int(x)
            if x == 1:
                new_game(player_list)
                break
            elif x == 2:
                #show_table(name, chance, wins, played)
                write_data(player_list)
                print("Here is the current table")
                break
            elif x == 3:
                write_data(player_list)
                print("Thanks for playing!")
                exit()
            else:
                print("Number must be between 1 and 3!")
        except ValueError:
            print("Input was incorrect! Pleas try again")

def new_game(player_list):
    print("* Choose two antagonists *")
    print("1. Choose player 1\n2. Choose player 2\n3. Choose player 3\n4. Choose player 4\n5. Choose player 5\n6. Choose player 6\n7. Exit program")
    while True:
        try:
            x = input()
            x = int(x)
            if x == 1:
                print("You have chosen player 1, please choose another player")
                third_menu(player_list)
                break
            elif x == 2: 
                print("You have chosen player 2")
                fourth_menu(player_list)
                break
            elif x == 3:
                print("Thanks for playing!")
                exit()
            else:
                print("Number must be between 1 and 3!")
        except ValueError:
            print("Input was incorrect! Pleas try again")

def third_menu(player_list):
    print("* Choose another antagonist *")
    print("1. Choose player 2\n2. Exit program") 
    while True:
        try:
            x = input()
            x = int(x)
            if x == 1:
                print("You have chosen player 2, Let's begin game!")
                fourth_menu(player_list)
                break
            elif x == 2:
                print("Thanks for playing!")
                exit()
            else:
                print("Number must be between 1 and 3!")
        except ValueError:
            print("Input was incorrect! Pleas try again")

def fourth_menu(player_list):
    print("* Choose another antagonist *")
    print("1. Choose player 1\n2. Exit program")
    while True:
        try:
            x = input()
            x = int(x)
            if x == 1:
                print("You have chosen player 1, Let's begin game!")
                who_won(player_list)
                break
            elif x == 2:
                print("Thanks for playing!")
                exit()
            else:
                print("Number must be between 1 and 2!")
        except ValueError:
            print("Input was incorrect! Please try again")


def who_won(player_list): #funktionen who_won loter anvandaren velja vem som vinner 
    print ("* Who won the game? *")
    print("1. Player 1\n2. Player 2\n3. Exit program")
    while True:
        try:
            x = input()
            x = int(x)
            if  x == 1:
                print("Player 1 won the game, congratulations!")
                player_list[0].won_game() #spelare 1 vinner
                player_list[1].loose_game() #spelare 2 torskar
                file = open("data.txt", "w")
                for player in player_list:
                    file.write("%s\n" % (player.name))
                    file.write("%s\n" & (str(player.chance)))
                    file.write("%s\n" % (str(player.wins)))
                    file.write("%s\n" % (str(player.played)))
                    file.close()
                    break
            elif x == 2:
                print("Player 2 won the game, congratulations!")
                player_list[1].won_game() # spelare 2 vinner
                player_list[0].loose_game() # spelare 1 torskar
                file = open("data.txt", "w") # programmet oppnar textfilen for att uppdatera resultatet
                for player in player_list:
                    file.write("%s\n" % (player.name))
                    file.write("%s\n" & (str(player.chance)))
                    file.write("%s\n" % (str(player.wins)))
                    file.write("%s\n" % (str(player.played)))
                    file.close()
                    break
            elif x == 3:
                print("Thanks for playing!")
                exit()
            else:
                print("Number must be between 1 and 3!")
        except ValueError:
            print("Input was incorrect! Please try again")
main()
