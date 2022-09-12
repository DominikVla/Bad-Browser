# library imports
import webbrowser
import pywhatkit
from random import randint
from random import choice
from time import sleep
import ctypes

# ascii art logo because low budget
print("""



BBBBBBBBBBBBBBBBB               AAA               DDDDDDDDDDDDD             BBBBBBBBBBBBBBBBB   RRRRRRRRRRRRRRRRR        OOOOOOOOO     WWWWWWWW         good luck         WWWWWWWW   SSSSSSSSSSSSSSS EEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR   
B::::::::::::::::B             A:::A              D::::::::::::DDD          B::::::::::::::::B  R::::::::::::::::R     OO:::::::::OO   W::::::W                           W::::::W SS:::::::::::::::SE::::::::::::::::::::ER::::::::::::::::R  
B::::::BBBBBB:::::B           A:::::A             D:::::::::::::::DD        B::::::BBBBBB:::::B R::::::RRRRRR:::::R  OO:::::::::::::OO W::::::W                           W::::::WS:::::SSSSSS::::::SE::::::::::::::::::::ER::::::RRRRRR:::::R 
BB:::::B     B:::::B         A:::::::A            DDD:::::DDDDD:::::D       BB:::::B     B:::::BRR:::::R     R:::::RO:::::::OOO:::::::OW::::::W                           W::::::WS:::::S     SSSSSSSEE::::::EEEEEEEEE::::ERR:::::R     R:::::R
  B::::B     B:::::B        A:::::::::A             D:::::D    D:::::D        B::::B     B:::::B  R::::R     R:::::RO::::::O   O::::::O W:::::W           WWWWW           W:::::W S:::::S              E:::::E       EEEEEE  R::::R     R:::::R
  B::::B     B:::::B       A:::::A:::::A            D:::::D     D:::::D       B::::B     B:::::B  R::::R     R:::::RO:::::O     O:::::O  W:::::W         W:::::W         W:::::W  S:::::S              E:::::E               R::::R     R:::::R
  B::::BBBBBB:::::B       A:::::A A:::::A           D:::::D     D:::::D       B::::BBBBBB:::::B   R::::RRRRRR:::::R O:::::O     O:::::O   W:::::W       W:::::::W       W:::::W    S::::SSSS           E::::::EEEEEEEEEE     R::::RRRRRR:::::R 
  B:::::::::::::BB       A:::::A   A:::::A          D:::::D     D:::::D       B:::::::::::::BB    R:::::::::::::RR  O:::::O     O:::::O    W:::::W     W:::::::::W     W:::::W      SS::::::SSSSS      E:::::::::::::::E     R:::::::::::::RR  
  B::::BBBBBB:::::B     A:::::A     A:::::A         D:::::D     D:::::D       B::::BBBBBB:::::B   R::::RRRRRR:::::R O:::::O     O:::::O     W:::::W   W:::::W:::::W   W:::::W         SSS::::::::SS    E:::::::::::::::E     R::::RRRRRR:::::R 
  B::::B     B:::::B   A:::::AAAAAAAAA:::::A        D:::::D     D:::::D       B::::B     B:::::B  R::::R     R:::::RO:::::O     O:::::O      W:::::W W:::::W W:::::W W:::::W             SSSSSS::::S   E::::::EEEEEEEEEE     R::::R     R:::::R
  B::::B     B:::::B  A:::::::::::::::::::::A       D:::::D     D:::::D       B::::B     B:::::B  R::::R     R:::::RO:::::O     O:::::O       W:::::W:::::W   W:::::W:::::W                   S:::::S  E:::::E               R::::R     R:::::R
  B::::B     B:::::B A:::::AAAAAAAAAAAAA:::::A      D:::::D    D:::::D        B::::B     B:::::B  R::::R     R:::::RO::::::O   O::::::O        W:::::::::W     W:::::::::W                    S:::::S  E:::::E       EEEEEE  R::::R     R:::::R
BB:::::BBBBBB::::::BA:::::A             A:::::A   DDD:::::DDDDD:::::D       BB:::::BBBBBB::::::BRR:::::R     R:::::RO:::::::OOO:::::::O         W:::::::W       W:::::::W         SSSSSSS     S:::::SEE::::::EEEEEEEE:::::ERR:::::R     R:::::R
B:::::::::::::::::BA:::::A               A:::::A  D:::::::::::::::DD        B:::::::::::::::::B R::::::R     R:::::R OO:::::::::::::OO           W:::::W         W:::::W          S::::::SSSSSS:::::SE::::::::::::::::::::ER::::::R     R:::::R
B::::::::::::::::BA:::::A                 A:::::A D::::::::::::DDD          B::::::::::::::::B  R::::::R     R:::::R   OO:::::::::OO              W:::W           W:::W           S:::::::::::::::SS E::::::::::::::::::::ER::::::R     R:::::R
BBBBBBBBBBBBBBBBBAAAAAAA                   AAAAAAADDDDDDDDDDDDD             BBBBBBBBBBBBBBBBB   RRRRRRRR     RRRRRRR     OOOOOOOOO                 WWW             WWW             SSSSSSSSSSSSSSS   EEEEEEEEEEEEEEEEEEEEEERRRRRRRR     RRRRRRR
""")

running = True
while running == True:

    # Main program

    search = input("What are you looking for today?")
    search = search.lower()

    if search == 'stop running':
        quit()

    # Blocking other search engines, why use them when you have this... thing... that uses them...
    if search == 'google' or search == 'bing':
        print("Loading...")
        sleep(10)
        print("Hang on this will take a few seconds...")
        sleep(18)
        print("Recalculating...")
        print("Loading, this will take approximately.... 1 year")
        count = 0
        while count != 52:
            sleep(604800)
            count = count + 1
        quit()

    # deciding conditions
    if search == 'test(1)':
        conditions = 1
    elif search == 'test(2)':
        conditions = 2
    elif search == 'test(3)':
        conditions = 3
    elif search == 'test(4)':
        conditions = 4
    else:
        conditions = randint(1, 4)

    # adding function to the conditions
    if conditions == 3:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    elif conditions == 4:
        word_list = ['apple', 'banana', 'cherry', 'dates', 'etc', 'absorb', 'abuse', 'academic', 'accept', 'access',
                     'accident', 'accompany', 'accomplish', 'according', 'account', 'accurate', 'become', 'bed',
                     'bedroom', 'beer', 'before', 'begin', 'beginning', 'behavior', 'behind', 'being', 'belief',
                     'believe', 'bell', 'belong', 'below', 'belt', 'bench', 'bend', 'beneath', 'benefit', 'beside',
                     'besides', 'best', 'bet', 'better', 'between', 'beyond', 'Bible', 'big', 'bike', 'bill', 'billion',
                     'bind', 'biological', 'bird', 'birth', 'birthday', 'bit', 'bite', 'black', 'blade', 'blame',
                     'blanket', 'blind', 'block', 'blood', 'blow', 'blue', 'board', 'boat', 'body', 'bomb', 'bombing',
                     'bond', 'bone', 'book', 'boom', 'conclusion', 'concrete', 'condition', 'conduct', 'conference',
                     'confidence', 'confident', 'confirm', 'conflict', 'confront', 'confusion', 'Congress',
                     'congressional', 'connect']
        research = choice(word_list)
        pywhatkit.search(research)
    elif conditions == 1:
        pywhatkit.search(search)
    else:
        webbrowser.open('https://t4.ftcdn.net/jpg/03/17/05/39/360_F_317053936_O2grehTc0hFvxhbTbRoAS6nYInVQlDmz.jpg')
