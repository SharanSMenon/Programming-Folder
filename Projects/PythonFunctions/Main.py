from SFunctions.NFunctions.lists import *
from SFunctions.NFunctions.numbers import *
from SFunctions.NFunctions.strings import *
import numpy


def print_instructions():
    print("Welcome")
    print("0 - Print instructions")
    print("1 - Choose a number function")
    print("2 - Choose a string function")
    print("3 - Exit the program")


def print_number_instructions():
    print("These are instructions for the number functions")
    print("0 - Print Instructions")
    print("1 - Find Gamma using law of cosines")
    print("2 - Find length of side c using law of cosines")
    print("3 - Find nth fibonacci number")
    print("4 - Check is number is even")
    print("5 - Use Pythagorean theorem to find hypotenuse")


def number_handler():
    print_number_instructions()
    choice = int(input("Choose an option: "))
    if choice == 0:
        print_number_instructions()
    elif choice == 1:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        print("Gamma: " + str(law_of_cosines_gamma(a, b, c)))
    elif choice == 2:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        gamma = float(input("Enter gamma: "))
        print("Gamma: " + str(law_of_cosines_normal(a, b, gamma)))
    elif choice == 3:
        n = int(input("Enter n: "))
        print("nth fibonacci number: " + str(fib(n)))
    elif choice == 4:
        e = int(input("Enter your number: "))
        print("Answer: " + str(is_even(e)))
    elif choice == 5:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        print("Answer: " + str(pythagorean_theorem(a, b)))
    else:
        print("Not a valid choice")


def print_string_instructions():
    print("0 - Print Instructions")
    print("1 - Encrypt a string")
    print("2 - Decrypt a string")
    print("3 - Check if string is a palindrome")
    print("4 - Reverse a string")


def string_handler():
    print_string_instructions()
    choice = int(input("Enter your choice: "))
    default_cipher = "qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM0987654321"
    if choice == 0:
        print_string_instructions()
    elif choice == 1:
        str_to_encrypt = input("Enter your string: ")
        print("Enter 1 to use default cipher.")
        cipher = input("Enter your cipher: ")
        if cipher == "1":
            print("Encrypted string: " + encrypt(str_to_encrypt, default_cipher))
        else:
            print("Encrypted string: " + encrypt(str_to_encrypt, cipher))
    elif choice == 2:
        str_to_decrypt = input("Enter your string: ")
        print("Enter 1 to use default cipher.")
        cipher = input("Enter your cipher: ")
        if cipher == "1":
            print("Decrypted string: " + decrypt(str_to_decrypt, default_cipher))
        else:
            print("Decrypted string: " + decrypt(str_to_decrypt, cipher))
    elif choice == 3:
        str_to_check = input("Enter your string: ")
        print("Answer: " + check_palindrome(str_to_check))
    elif choice == 4:
        str_to_reverse = input("Enter string: ")
        print("Reversed string: " + reverse(str_to_reverse))
    else:
        print("Not a valid choice")


quit_ = False

while not quit_:
    choice = int(input("Choose an option: "))
    if choice == 0:
        print_instructions()
    elif choice == 1:
        number_handler()
    elif choice == 2:
        string_handler()
    else:
        print("Bye")
        quit(0)
