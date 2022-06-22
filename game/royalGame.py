import random
from graphics import *
win = GraphWin()
win.setCoords(0, 0, 4, 8)
win.setBackground("purple")


def odd(playerdistance, beforedistance, playerdistancelistfriendly, playerdistancelistenemy):
    odddictionary = {   # the function calculates the odds of the unit being eaten
        1: 4/16,
        2: 6/16,      # the dictionary transforms the rolls of the cubes into their odds of possibility
        3: 4/16,
        4: 1/16
    }
    t_or_f8 = False
    t_or_f4 = False
    for b in playerdistancelistenemy:
        if b == 4:
            t_or_f4 = True
    for t in playerdistancelistfriendly:
        if t == 8:
            t_or_f8 = True
    if beforedistance == 8:
        t_or_f8 = False
    for y in playerdistancelistenemy:
        if y == 8:
            t_or_f8 = True
    checked_distance = []
    if 13 > playerdistance > 4 and playerdistance != 8:
        oddcount = 0
        for i in playerdistancelistenemy:
            checked = i in checked_distance
            if i < playerdistance and not checked:
                if playerdistance - i <= 4:
                    oddcount += odddictionary[playerdistance - i]
                if i < 8:
                    if playerdistance < 8 and i < 4 and not t_or_f4:
                        oddcount += odddictionary[4-i]*odddictionary[playerdistance-4]
                    elif 4 < i and playerdistance > 8 and not t_or_f8:
                        oddcount += odddictionary[8-i]*odddictionary[playerdistance-8]
                    elif not t_or_f8 and i < 4 and playerdistance > 8:
                        oddcount += odddictionary[4-i]*odddictionary[4]*odddictionary[playerdistance-8]
                checked_distance.append(i)
        return oddcount
    else:
        return 0


def possible(playerdistance, playerdistancelistfriendly, playerdistancelistenemy):
    possibility = True
    if playerdistance <= 16:  # the function calculates if moving the player is possible
        for i in playerdistancelistfriendly:
            if i == playerdistance and playerdistance != 16:
                possibility = False
        for d in playerdistancelistenemy:
            if d == playerdistance and d == 8:
                possibility = False
    else:
        possibility = False
    return possibility


def randomnum():# the function generate a random number in the terms of the game
    distancecounter = 0
    for y in range(4):
        ran = random.randint(0, 1)
        if ran == 1:
            distancecounter += 1
    if distancecounter < 1:
        distancecounter = 1
    return distancecounter


def eating(playerdistance, playerdistancelistenemy, playerdistancelistenemyscreen):
    newlist = []
    counter = 0
    for i in playerdistancelistenemy:
        if 13 > playerdistance > 4 and playerdistance == i:
            newlist.append(0)
            playerdistancelistenemyscreen[counter].undraw()
        else:
            newlist.append(i)
        counter += 1
    return newlist


def update_rect(playerdistance, white_or_not):
    sh = Rectangle(Point(0, 0), Point(0, 0))
    black = 0
    if not white_or_not:
        black = 2
    if playerdistance <= 4:
        sh = Rectangle(Point(1 + black, 4 - playerdistance), Point(black, 5 - playerdistance))
    elif 4 < playerdistance <= 12:
        sh = Rectangle(Point(2, playerdistance-5), Point(1, playerdistance-4))
    elif 12 < playerdistance <= 15:
        sh = Rectangle(Point(1+black, 20 - playerdistance), Point(black, 21 - playerdistance))
    return sh





def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code
    playerdistancelistwhite = [0, 0, 0, 0, 0, 0, 0]
    playerdistancelistblack = [0, 0, 0, 0, 0, 0, 0]
    end1 = Text(Point(0.5, 4.5), "WHITE_END")
    end1.draw(win)
    end1.setTextColor("white")
    cube1 = Text(Point(3.5, 5.5), "you rolled")
    cube1.draw(win)
    cube1.setTextColor("white")
    cube2 = Text(Point(3.5, 4.5), "roll")
    cube2.draw(win)
    cube2.setTextColor("white")
    cubebl1 = Text(Point(3.5, 3.5), "black rolled")
    cubebl1.draw(win)
    cubebl3 = Text(Point(3.5, 3.3), "before you")
    cubebl3.draw(win)
    cubebl2 = Text(Point(3.5, 2.5), "")
    cubebl2.draw(win)
    end2 = Text(Point(2.5, 4.5), "BLACK_END")
    end2.draw(win)
    end2.setTextColor("black")
    playerdistancelistwhitescreen = [Rectangle(Point(0, 0), Point(0, 0)), Rectangle(Point(0, 0), Point(0, 0)), Rectangle(Point(0, 0), Point(0, 0)), Rectangle(Point(0, 0), Point(0, 0)), Rectangle(Point(0, 0), Point(0, 0)), Rectangle(Point(0, 0), Point(0, 0)), Rectangle(Point(0, 0), Point(0, 0))]
    playerdistancelistblackscreen = [Rectangle(Point(0, 0), Point(0, 0)), Rectangle(Point(0, 0), Point(0, 0)), Rectangle(Point(0, 0), Point(0, 0)), Rectangle(Point(0, 0), Point(0, 0)), Rectangle(Point(0, 0), Point(0, 0)), Rectangle(Point(0, 0), Point(0, 0)), Rectangle(Point(0, 0), Point(0, 0))]
    for b in playerdistancelistblackscreen:
        b.draw(win)
    for f in playerdistancelistwhitescreen:
        f.draw(win)
    winwhite = 0
    winblack = 0
    turn = True
    print("the game has started, " + "white list distances is " + str(playerdistancelistwhite) + "black list distances is " + str(playerdistancelistblack))
    while winwhite != 7 and winblack != 7:
        distance = randomnum()
        if turn:
            cube2.setText(str(distance))
            if distance != 0:
                counter = 0
                for b in playerdistancelistwhite:
                    counter += 1
                    if possible(b+distance, playerdistancelistwhite, playerdistancelistblack):
                        print("UNIT " + str(counter) + "   " + str(b) + " " + str(b+distance) + " " + str(odd(b+distance, b, playerdistancelistwhite, playerdistancelistblack)))
            print("you can move " + str(distance) + ", pick the unit from the list above")
            picked = input()
            if possible(playerdistancelistwhite[int(picked)-1]+distance, playerdistancelistwhite, playerdistancelistblack):
                playerdistancelistwhite[int(picked)-1] += distance
                playerdistancelistwhitescreen[int(picked) - 1].undraw()
                playerdistancelistwhitescreen[int(picked) - 1] = update_rect(playerdistancelistwhite[int(picked)-1], True)
                playerdistancelistwhitescreen[int(picked) - 1].draw(win)
                playerdistancelistwhitescreen[int(picked) - 1].setFill("white")
            playerdistancelistblack = eating(playerdistancelistwhite[int(picked)-1], playerdistancelistblack, playerdistancelistblackscreen)
            if playerdistancelistwhite[int(picked)-1] == 4 or playerdistancelistwhite[int(picked)-1] == 8:
                turn = True
            else:
                turn = False
        else:
            cubebl2.setText(str(distance))
            lowest = 1
            picked = 0
            counter = 0
            if distance != 0:
                for w in playerdistancelistblack:
                    if possible(w+distance, playerdistancelistblack, playerdistancelistwhite) and odd(w+distance, w, playerdistancelistblack, playerdistancelistwhite) < lowest:
                        lowest = odd(w+distance, w, playerdistancelistblack, playerdistancelistwhite)
                        picked = counter
                    counter += 1
            if possible(playerdistancelistblack[picked] + distance, playerdistancelistblack, playerdistancelistwhite):
                playerdistancelistblack[picked] += distance
                playerdistancelistblackscreen[int(picked)].undraw()
                playerdistancelistblackscreen[int(picked)] = update_rect(playerdistancelistblack[int(picked)], False)
                playerdistancelistblackscreen[int(picked)].draw(win)
                playerdistancelistblackscreen[int(picked)].setFill("black")
                playerdistancelistblackscreen[int(picked)].setOutline("blue")
            playerdistancelistwhite = eating(playerdistancelistblack[picked], playerdistancelistwhite, playerdistancelistwhitescreen)
            if playerdistancelistblack[picked] == 4 or playerdistancelistblack[picked] == 8:
                turn = False
            else:
                turn = True
        print("white list distances is " + str(playerdistancelistwhite) + "black list distances is " + str(playerdistancelistblack))
        winwhite = 0
        winblack = 0
        for i in playerdistancelistwhite:
            if i == 16:
                winwhite += 1
        for d in playerdistancelistblack:
            if d == 16:
                winblack += 1
    if winwhite == 7:
        winner = "white"
        t = Text(Point(2, 4.5), "Player white has won")
        t.draw(win)
        t.setTextColor("white")
        t.setSize(14)
    else:
        winner = "black"
        t = Text(Point(2, 4.5), "Player black has won")
        t.draw(win)
        t.setSize(14)
    print("the game has ended, player " + winner + " has won")
    end1.undraw()
    end2.undraw()
    for b in playerdistancelistblackscreen:
        b.undraw()
    for f in playerdistancelistwhitescreen:
        f.undraw()
    cube1.undraw()
    cube2.undraw()
    cubebl1.undraw()
    cubebl3.undraw()
    cubebl2.undraw()
    win.getMouse()
    win.close()

#bruh
if __name__ == '__main__':
    main()