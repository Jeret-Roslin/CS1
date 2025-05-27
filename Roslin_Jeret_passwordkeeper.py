'''
Author: Jeret Roslin
Sources: Ms. Marciano, CS Google Classroom
Description: Lets a user store data for websites and can be stored in a CSV file
Date: 5/22/25
Challenges: CSV, change_entry, delete_entry
Bugs: None
'''
import csv

def add_entry(websites, usernames, passwords):
    '''
    Adds data from a website
    Args:
        Websites (list): given list of websites 
        Usernames (list): given list of usernames
        Passwords (list): given list of passwords
    Returns
        Index: Index with the website username and password
    '''
    website = input('What website would you like to add? ')
    username = input('What username would you like to add? ')
    password = input('What password would you like to add? ')
    websites.append(website)
    usernames.append(username)
    passwords.append(password)
def print_entry(website, username, password):
    '''
    prints data for a website
    Args:
        Website (list): prints given website
        Username (list): prints given username
        Password (list): prints given password
    Returns
        int: Index for data entry
    '''
    print (f"\033[1m Website: {website} Username: {username} Password:  {password}\033[0m")
def get_index(websites):
    '''
    Prints all data
    Args:
        websites (list): prints all website data
    Returns
        print: All data
    '''
    while True:
        web = input("Which website would you like to see? ")
        if web in websites:
            return websites.index(web)                                          #returns the index of all websites
        else:
            print("This data is not stored please enter a different website")
def change_entry(websites, usernames, passwords):
    '''
    Lets the user change the data of a website entry
    Args:
        websites (list): changes given data for a website in a list
        usernames (list): changes given data for a username in a list
        passwords (list): changes given data for a password in a list
    Returns
        updates data
    '''
    index = get_index(websites)
    usernames[index] = input("What is your new username? ")
    passwords[index] = input ("What is your new password? ")
def delete_entry(websites, usernames, passwords):
    '''
    Lets a user delete a website
    Args:
        websites  (list): deletes a website entry
        usernames (list): deletes a username for a website entry
        passwords (list): deletes a password for a website entry
    Returns: 
        deletes entry
    '''
    index = get_index (websites)
    websites.pop(index)
    usernames.pop(index)
    passwords.pop(index)
def export_to_csv(filename, headers, *arrays):
    '''
    Exports parallel arrays to a CSV file.

    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    '''
    if not arrays:
        raise ValueError("At least one array must be provided.")
    
    num_rows = len(arrays[0])

    for arr in arrays:
        if len(arr) != num_rows:
            raise ValueError("All arrays must have the same length.")
    
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)

        for i in range(num_rows):
            row = [arr[i] for arr in arrays]
            csvwriter.writerow(row)
def main():
    websites = []
    usernames = []
    passwords = []

    while True:
        print ("\033[31m Welcome to the password keeper\033[0m")
        print ("\033[31m When entering data it will be automatically stored put in 3 or 4 to see your data after you add it\033[0m")
        option = input('''What choice would you like'  please put in a number
1. quit
2. add a website
3. Print data for a specific website 
4. Print all data
5. Change data for a website
6. Delete a website
7. Export data from a website into a CSV file  ''')

        if option == '1':
            break
        elif option == '2':
            add_entry(websites, usernames, passwords)
        elif option == "3":
            index = get_index(websites)
            print_entry(websites[index], usernames[index], passwords[index])
        elif option == "4":
            for index in range(len(websites)):
                print_entry(websites[index], usernames[index], passwords[index])
        elif option == "5":
            change_entry(websites, usernames, passwords)
        elif option == "6":
            delete_entry(websites, usernames, passwords)
        elif option == "7":
            filename = input('Enter a filename: ')
            export_to_csv(filename+".csv", ["Website", "Username", "Password"], websites, usernames, passwords)
            print(f'File successfully exported to {filename}.csv')
main()