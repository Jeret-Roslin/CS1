'''
Author: Jeret Roslin
Sources: Ms. Marciano CS Google Classroom, Google
Description: prints a variety of functions based on user's choice
Date 5/5/25
Challenges: Get initials function
Bugs: None
'''


import random

def chorus():
    '''
    prints a chorus for a song
    Args:
        none 
    Returns:
        print: chorus
    '''
    print("it's the eye of the tiger, it's the thrill of the fight")
    print("Rising up to the challenge of our rival")
    print("And the last known survivor stalks his prey in the night")
    print("And he's watching us all with the eye of the tiger") 
def sing_song():
    '''
    prints a verse of a song
    Args:
       none
    Returns:
        print: verse
     '''
    print('Risin up, back on the street')
    print ('Did my time, took my chances')
    print('Went the distance, now Im back on my feet')
    print('Just a man and his will to survive')
    print('So many times it happens too fast')
    print('You trade your passion for glory')
    print('Dont lose your grip on the dreams of the past')
    print('You must fight just to keep them alive')
    chorus()
    print('Face to face, out in the heat')
    print('Hangin tough, stayin hungry')
    print('They stack the odds till we take to the street')
    print('For the kill with the skill to survive')
def add(a, b):
    '''
    Takes two numbers and adds them together
    Args:
        a (int): first number
        b (int): second number
    Returns:
        print: sum of a and b
    '''
    print(a + b)

def print_list(array):
    '''
    Prints a given list individually
    Args:
        array (list): list to print
    Returns:
        print: each element in array
    '''
    for element in array:
        print(element)
    
def in_list(array, element):
    '''
    checks if a element is in a list
    Args:
      array (list): given list
      element (any): element to check
    Returns:
        bool: True/False based on if element is in array
    '''
    return element in array
    
def get_integer(order):
    '''
    Args:
    Returns:
    Raises:
        ValueError: if number is not an integer type
    '''
    while True:
        try:
            num = int(input(f"What's your {order} number? "))
            return num
        except ValueError:
            print('Enter an integer!')

def get_integers():
    '''
    Get two integers via user input
    Args:
        None
    Returns:
        int: two integers from the user
    '''
    a = get_integer('first')
    b = get_integer('second')
    return a, b
def get_random():
    '''
    generates a random integer based on two numbers
    Args:
        None
    Returns:
        print: random integer in between two numbers
    '''
    num1, num2 = get_integers()
    print(random.randint(num1, num2))
    
def count_vowels(string):
    '''
    counts the number of vowels in a string/word
    Args:
        string (str): string to count vowels in
    Returns:
        int: the number of vowels
   '''
    count = 0
    for character in string:
        if character in ['a','e','i','o','u']:
            count += 1
    return count
def reverse_string(string):
    '''
    takes a string and reverses it
    Args:
        string: takes user's string and returns reverse version
    Returns:
      Str:  string  reverse string
    '''
    return string[::-1]
def is_palindrome(string):
    '''
    Checks if something is a palindrome
    Args:
        string: checks if user string is a palindrome
    Returns:
        str: returns the string
    '''
    return string == reverse_string(string)
def get_initials(fullname):
    '''
    returns initials based on name
    Args:
       fullname (str): gets first character of each string
    Returns:
        str: initals from the full name
    '''
    names = fullname.split(" ")
    initials = ''

    for name in names:
        initials += name[0]
    return initials

def main():
    while True:
        option = input('Which would you like? 1. Sing song, 2. Add two numbers, 3. Print a list, 4. Check if element is in a list, 5. Check if something is an integer, 6. Get a random integer ')
        pets = ['dog','cat','fish','lizard','snake','hamster','bird']
        if option == '1':
            sing_song()
        elif option == '2':
            first_number, second_number = get_integers()
            add(first_number, second_number)
        elif option == '3':
            print_list(pets)
        elif option == '4':
             element = input('What would you like to check for? ')
             print(in_list(pets, element))
        elif option == '5':
            get_random()
        elif option == '6':
            string = input('Enter a word or phrase: ')
            print(count_vowels(string))
        elif option =='7':
            name = input("what is your name? ")
            print(get_initials(name))
        elif option =='8':
            string = input("What word would you like to use? ")
            print (reverse_string(string))
        elif option =='9':
            string = input("Enter string to reverse: ")
            print (reverse_string(string))
            print (is_palindrome(string))
        else:
            print('Invalid')
main()



            