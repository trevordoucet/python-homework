answer = int(input("How many numbers? "))

playing = "y"

while playing == "y":
    while answer >= 0: 
        print (answer)
        answer -= 1

    playing = input("Would you like to play again? Enter (y), if not enter (n):  ")
    if playing == "y":
        answer = int(input("How many numbers? "))
    
    elif playing == "n": 
        print("Thanks for playing! ")
    
    
