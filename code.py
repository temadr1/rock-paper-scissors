import random


def playerturn(x):
    """your turn def"""
    if x == 'scissors':
        a = 1
        return a
    elif x == 'paper':
        a = 2
        return a
    elif x == 'rock':
        a = 3
        return a
    else:
        pass


def aiturn():
    """randomise bot turn"""
    y = random.randint(1, 3)
    if y == 1:
        print("Computer choose scissors")
    elif y == 2:
        print('Computer choose paper')
    elif y == 3:
        print("Computer choose rock")
    return y


def whowins(a, y):
    """returns who is winner text"""
    q = ''
    try:
        if y == a+1 or y == a-2:
            q = 'You win!'
        elif a == y+1 or a == y-2:
            q = 'You lose'
        elif a == y:
            q = 'Draw'
    except TypeError:
        return 'Неверно введены данные'
    return q


def statistic(u, s):
    """gives statistic about last games"""
    print(f"""_____Statistic_____
You played {s} games 
You have {u[0]} wins
You have {u[1]} draws
You have {u[2]} loses""")


def realiser():
    x = input('Print rock, paper or scissors. To end the game print 0>>')
    u = [0, 0, 0]
    s = 0
    while True:
        a = playerturn(x)
        y = aiturn()
        print(whowins(a, y))
        if whowins(a, y) == 'Draw':
            u[1] += 1
            s += 1
        elif whowins(a, y) == 'You win!':
            u[0] += 1
            s += 1
        elif whowins(a, y) == 'You lose':
            u[2] += 1
            s += 1
        x = input('Next game, to stop print 0>>')
        if x == '0':
            break
    statistic(u, s)


realiser()
