import random                                       # import random library
def colored_text(text, color_name):                 # function that shows color name
    color_codes = {                                 # codes for all colors you can call upon
        'black': "\033[0;30m",                      # black code
        'red': "\033[0;31m",                        # red code
        'green': "\033[0;32m",                      # green code
        'yellow': "\033[0;33m",                     # yellow code
        'blue': "\033[0;34m",                       # blue code
        'magenta':"\033[0;35",                      # magenta code
        'cyan':"\033[0;36",                         # cyan code
        'white':"\033[0;37",                        # white code
        'reset': "\033[0;30m"                       # default color
    }
    return color_codes[color_name] + text + "\033[0m"   # if it is glitching show default colored text

print(colored_text('hello', 'red'), colored_text('and', 'blue'),colored_text('welcome', 'green'))   # displays message with red, blue and green text
name = input("What is your name? ")                                                                 # user is asked a question and displays message
print(f'''Hello, {name}!                                                                             
Please read these directions
In order to win the game you need to say which color the line of text is in front of you.
If you guess the correct color, You win!
make sure to type the color, not word
''')

colors = ['black','red','green','yellow','blue','magenta','cyan','white']                           # list of all colors

while True:                                                                                         # forever loop
    text_color = random.choice(colors)                                                              # text color = random color
    print_color = random.choice(colors)                                                             # print color = random color
    print(colored_text(text_color, print_color))                                                    # displays random text color and printed color

    user_color = input("What is the correct color? ")                                               # ask's user a question
    if user_color == print_color:                                                                   # user color is the same as print color
        print("That's correct!")                                                                    # displays message
    else:                                                                                           # happens when other option is not correct
        print("Thats incorrect")                                                                    # displays message
        
    while True:                                                                                     # forever loop
        play_again=input("want to play again? ")                                                    # asks users a question
        if play_again == ("yes"):                                                                   # user chooses to play again
            break                                                                                   # terminates code
        elif play_again == ("no"):                                                                  # happens when user doesn't want to play again
            exit()                                                                                  # exits/ends code
        else:                                                                                       # happens when user says something different than yes or no
            print("Invalid response")                                                               # user response is invalid
    