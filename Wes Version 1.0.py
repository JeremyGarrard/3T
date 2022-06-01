



L1=["-","-","-"]

L2=["-","-","-"]

L3=["-","-","-"]

L4=["-","-","-"]

Grid=[L1,L2,L3,L4]



print (Grid [0])

print (Grid [1])

print (Grid [2])





counter=0

turn = "x"





while counter<9:

    y = (int)(input ("Type x coordinate of your move: "))

    x = (int)(input ("Type y coordinate of your move: "))

    x=x-1

    y=y-1

    if (x>=3 or x<0):

        print("Error make y coordinate less than two and greater than -1")

        continue

    if (y>=3 or y<0):

        print("Error make x coordinate less than two and greater than -1")

        continue

    if turn=="x" and Grid[x][y]=="-":

        Grid[x][y]="x"

        turn="y"

        

    elif turn=="y"and Grid[x][y]=="-":

        Grid[x][y]="o"

        turn="x"

    else:

        counter=counter-1

    print (Grid [0])

    print (Grid [1])

    print (Grid [2])

    counter=counter+1



print ("Winner!")
