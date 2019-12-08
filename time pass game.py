import time


options = ['Sleep', 'Watch Anime', 'Watch Movies', 'Code(anything Stupid.....like this one)', 'Watch something naughty(if you know what I mean)', 'Study']


def sleep():
    r = 1
    print('Do you actually feel sleepy(y,n): ')
    ask = input()
    if ask == 'y' or ask == 'Y':
        print('Then sleep na....')
        time.sleep(2)
        print('You moron....')
        time.sleep(2)
    else:
        print('Then why the hell do you choose this option..... ')
        time.sleep(2)
        print('Idiot......')
        time.sleep(2)
        print('Try other one')
        time.sleep(2)
        r = 0
    return r


def anime():
    print('There is no asking.........')
    time.sleep(2)
    print('Go and watch it already.....')
    time.sleep(2)
    return 1


def movies():
    r = 0
    print('Uhhhhh....... ')
    time.sleep(2)
    print('....Now its time to talk....')
    time.sleep(2)
    print('\nHow many movies do you have downloaded: ')
    n = int(input())
    if n > 0:
        print("I mean interesting ones yrr....")
        n = int(input())
        if n > 0:
            print('Are they emotional(y,n)???')
            ask = input()
            if ask == 'y' or ask == 'Y':
                print('Go ahead then....')
                time.sleep(2)
                print('but....')
                time.sleep(2)
                print('Try not to cry remembering your girlfriend.......')
                time.sleep(2)
                print('lol')
            else:
                print('Go ahead then......... See Yaa')
            r = 1
    if not r:
        print('Then why the hell this option came in to your mind, just skip it already')
        time.sleep(2)
    return r


def Code():
    r = 0
    print('Seriously.....')
    time.sleep(2)
    print('Doing coding during your free time like the guy who was the creator of me..........')
    time.sleep(5)
    print('Uhhhhh....')
    time.sleep(2)
    print('I mean seriously')
    time.sleep(2)
    print('You really wanna do this......?????(y/n)')
    ask = input()
    if ask == 'y' or ask == 'Y':
        print('Fine then....')
        time.sleep(2)
        print('Go for it captain.....')
        time.sleep(2)
        print('See yaa at the other side of the World...')
        time.sleep(2)
        print('Most probably....... ', end='')
        time.sleep(2)
        print('hell')
        time.sleep(2)
        r = 1
    else:
        print('Thank God...')
        time.sleep(2)
        print('No such stupid coders would be born like the one who created me....')
        time.sleep(2)
        print('Try some other options..')
        time.sleep(2)
        print('My personal favourite is the 2nd one...')
        time.sleep(3)
    return r


def main():
    time.sleep(1)
    print('Loading', end='')
    time.sleep(1)
    for i in range(0, 10):
        print('.', end='')
        time.sleep(1)

    print('')
    time.sleep(1)
    print('Yoo')
    time.sleep(2)
    print('Welcome')
    time.sleep(2)
    print('This is a TIME-PASS Program')
    time.sleep(2)
    print('Created just because someone was f**k\'n bored and had nothing to do in his life')
    time.sleep(6)
    print('Well......')
    time.sleep(3)
    print('This program deals with a problem called \"WHAT TO DO\"')
    time.sleep(3)
    print('This is the problem of not able to decide what to do in your free time,')
    time.sleep(3)
    print('when you have multiple options,')
    time.sleep(3)
    print('all of them exceptionally amazing,')
    time.sleep(3)
    print('and you have to select only one among them.')
    time.sleep(4)
    for i in range(0, 9):
        print()
        time.sleep(1)
    print('Sooo...')
    time.sleep(3)
    print('To solve this problem...')
    time.sleep(3)
    print('Our research team has analyzed the suggestions of the victims\nfrom every part of the world')
    time.sleep(3)
    print('And came with the very fine options')
    print('For the users')
    time.sleep(3)
    print('Easy to select')
    time.sleep(3)
    print('With an awesome Interface')
    time.sleep(3)
    print('To deal off with it.')
    time.sleep(3)
    for i in range(0, 9):
        print()
        time.sleep(1)
    print('Ok')
    time.sleep(3)
    print('This is it....')
    time.sleep(3)
    print('I am not going to extend it a lot....')
    time.sleep(3)
    print('Sounds a bit of a cliche anime I guess....')
    time.sleep(3)
    print('Whatever man')
    time.sleep(3)
    print('I have few options...')
    time.sleep(3)
    print('Select anything you want...')
    time.sleep(3)
    print('Enjoy the time-pass')
    time.sleep(3)
    r = 0
    while not r:
        print('\n\nTHE OPTIONS: ')
        time.sleep(3)
        for i in range(0, 5):
            print('-> ', options[i])
        x = int(input())
        if x == 1:
            r = sleep()
        elif x == 2:
            r = anime()
        elif x == 3:
            r = movies()
        elif x == 4:
            r = Code()
        else:
            print('Well.....')
            time.sleep(3)
            print('These things are personal naaa....')
            time.sleep(3)
            print('So we don\'t deal with this')
            time.sleep(3)
            print('You Pervert')
            time.sleep(3)
            print('Get lost')
            print()
            time.sleep(3)
            r = 1


main()



