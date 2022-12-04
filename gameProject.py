import time
import random
import randomItems

location = randomItems.locations[random.randint(0, 2)]
randomNumber = random.randint(0, 2)
weapon = randomItems.weaponsToFind[randomNumber]
artWeapon = randomItems.articulatedWeapons[randomNumber]
creature = randomItems.creatures[random.randint(0, 2)]


def printPause(message):
    print(message)
    time.sleep(2)


def introStory():
    printPause(f'You find yourself {location}.')
    printPause('It looks like there is only two possible ways.')
    printPause('Which way do you want to go?')


def validInput(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            printPause('Please select a valid option:')
    return response


def getWeapon():
    printPause("Looks like there is something on the ground.")
    printPause(f'You notice right there waiting for you {weapon}.')
    printPause(f'You get {artWeapon} and off you go.')


def creatureBattle():
    printPause("wait a minute, what is that?")
    printPause(f'NOOO!!, That {creature} cuts your way!!')
    printPause('What do you want to do now?')
    response = validInput(
        'You can fight (1) or run away (2). \n',
        '2', '1')
    if response == '2':
        printPause('GAME OVER \nA chicken would be more brave, You lost!')
    elif response == '1':
        printPause(f'You take out {artWeapon}.')
        printPause(f'When the {creature} sees '
                   f'{artWeapon} it get scared and runs crying.')
        printPause('NICE MOVE! \nYou win!!!')
    playAgain()


def theAction(path, attribute):
    printPause(f'You go to the {path} and something {attribute} happens.')
    getWeapon()
    creatureBattle()


def playerChoices():
    response = validInput('Enter L to go for the left side. \n'
                          'Enter R to go for the right side. \n',
                          'l', 'r')
    if response == 'l':
        theAction('left', 'strange')
    elif response == 'r':
        theAction('right', 'incredible')


def playAgain():
    # del location, weapon, artWeapon, creature
    response = validInput('Do you want to play again? (y/n)\n', 'y', 'n')
    if response == 'y':
        # del location, weapon, artWeapon, creature
        playGame()
    elif response == 'n':
        printPause(f'Take care, the {creature} could be chasing you...')
        printPause(f'I think you should run away now, '
                   '{creature} is coming for you!')
        printPause('3...')
        printPause('2...')
        printPause('1...')
        printPause('BOO! \nHope you enjoyed the game, see you next time!')


def playGame():
    # del location
    # getRandomItems()
    introStory()
    playerChoices()


playGame()
