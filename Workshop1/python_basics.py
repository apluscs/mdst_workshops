"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    num = int(input("Enter a number: "))
    print("even" if num % 2 == 0 else "odd")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    ans = random.randint(1, 9)
    while True:
        num = input("Guess a number: ")
        if num == "exit":
            return
        num = int(num)
        if num == ans:
            print("You guessed exactly right.")
        elif num < ans:
            print("You guessed too low.")
        else:
            print("You guessed too high.")

def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    str = input("Enter a string: ")
    if str[::-1] == str:
        print("Is palindrome.")
    else:
        print("Is not palindrome.")

def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    u_bytes = base64.b64encode(username.encode('ascii'))
    p_bytes = base64.b64encode(password.encode('ascii'))

    f = open(filename, "w")
    f.write(u_bytes.decode('ascii')+"\n")
    f.write(p_bytes.decode('ascii')+"\n")

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    f = open(filename, "r")
    lines = f.readlines()
    u_bytes = base64.b64decode(lines[0].encode('ascii'))   ## lines[0] is ascii string, convert into bytes
    p_bytes = base64.b64decode(lines[1].encode('ascii'))   

    print(u_bytes.decode('ascii'))
    print(p_bytes.decode('ascii'))

    if password == None :
        part4a(filename, u_bytes.decode('ascii'), p_bytes.decode('ascii'))  # old u and p
    else:
        part4a(filename, u_bytes.decode('ascii'), password)

if __name__ == "__main__":
##    part1(3)  # odd!
##    part1(4)  # even!
##    part2()
##    part3("ratrace")  # False
##    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
