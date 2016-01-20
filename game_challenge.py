def get_input_from_player():
    while True:
        try:
            number=int(raw_input("Please enter a positive integer: "))
        except ValueError:
            print "Invalid, ", 
        else:
            if number>0:
                return number
            else:
                print "Invalid, ",
            
def check_if_player_has_repeated_a_number(numbers=[]):
    while True:
        new_number=get_input_from_player()
        if new_number in numbers:
            print "You already entered the number previously, please enter a number you have not yet entered"
        else:
            numbers.append(new_number)
            return new_number
        
if __name__ == '__main__':
    print "The rules"
    print "1.There are two players."
    print "2.Each player writes a number, hidden from the other player. It can be any integer 1 or greater."
    print "3.The players reveal their numbers."
    print "4.Whoever chose the lower number gets 1 point, unless the lower number is lower by only 1, then the player with the higher number gets 2 points."
    print "5.If they both chose the same number, neither player gets a point."
    print "6.This repeats, and the game ends when one player has 5 points."
    points_player1=0
    points_player2=0
    player1_numbers=[]
    player2_numbers=[]
    while True:
        if points_player1>=5 or points_player2>=5:
            print "Game ended!!!"
            print "Player1", points_player1
            print "Player2", points_player2
            break
        print "Player 1"
        player1=check_if_player_has_repeated_a_number(player1_numbers)
        print "Player 2"
        player2=check_if_player_has_repeated_a_number(player2_numbers)
        print "Player 1 entered: ", player1
        print "Player 2 entered: ", player2
        diff=abs(player1-player2)
        if diff==0:
            print "You entered the same numbers no points"
        elif diff==1:
            if player1>player2:
                print "Player 1 gets 2 points"
                points_player1+=2
            elif player2>player1:
                print "Player 2 gets 2 points"
                points_player2+=2
        else:
            if player1<player2:
                print "Player 1 gets 1 point"
                points_player1+=1
            elif player2<player1:
                print "Player 2 gets 1 point"
                points_player2+=1            
