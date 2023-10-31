again = True
def printMenu():
    global userIn
    userIn = input(
        '''
Menu
-------------
1. Encode
2. Decode
3. Quit

Please enter an option: ''')

def encode(password):
    global newPass
    newPass = ""
    for dig in password:
        dig = int(dig)
        dig += 3
        newPass += str(dig)
    return newPass
def main():
    while again == True:
        printMenu()
        if userIn == "1":
            userIn2 = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            encode(userIn2)

        elif userIn == "2":
            print(f"The encoded password is {newPass}, and the original password is {userIn2}.")
        else:
            exit()

if __name__ == "__main__":
    main()