import random

words = 'metasploit virtualbox honeypot computing wireshark forensics'.split()

def instruction():
    print(' * ' * 20)
    print('                  H A N G M A N                           ')
    print(' * ' * 20)
    print("           Welcome to Cybersecurity Hangman game          ")
    print(' ~ ' * 20)
    print('Instructions on how to play: ')
    print('Guess one letter at a time.  If the letter is in the word,')
    print('you will fill the blank(s).  If the letter is not in the word,')
    print('you lose a try, and a part of the hangman is drawn.  Good luck!')
