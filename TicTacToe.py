from random import randint

board = [0,1,2,3,4,5,6,7,8]
listaVerificare = []
listaVerificare2 = []
pornire = True
WIN_COMBINATIONS = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

def Print():
    print str(board[0]) + " | " + str(board[1]) + " | " + str(board[2])
    print "----------"
    print str(board[3]) + " | " + str(board[4]) + " | " + str(board[5])
    print "----------"
    print str(board[6]) + " | " + str(board[7]) + " | " + str(board[8])

Print()


while pornire == True:
    input = raw_input("Selectati un numar: ")
    input  = int(input)

    if input != "x" and input != "o":
        board[input] = "x"
        opponent = randint(0,8)
        listaVerificare.append(input)
        if opponent != input:
            board[opponent] = "o"
            listaVerificare2.append(opponent)
            Print()
            for z in WIN_COMBINATIONS:
                if set(z) <= set(listaVerificare):
                    print "Ai castigat"
                    pornire = False
                elif set(z) <= set(listaVerificare2):
                    print "Ai pierdut"
                    pornire = False








