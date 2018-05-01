from SFunctions.NFunctions.lists import *
from SFunctions.NFunctions.numbers import *
from SFunctions.NFunctions.strings import *
import numpy
# Tests
# Lists
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("List " + str(l))
print("Sum of l: " + str(addList(l)))
print("All elements in l sqared: " + str(squareList(l)))
lSort = list(list(numpy.random.randint(low=0, high=10, size=(1, 10)))[0])
print("Random list to sort: " + str(lSort))
print("Sorted: " + str(sort(lSort)))
print("-----")
# Numbers
print("5 is prime: " + str(is_prime(5)))
print("10 is prime: " + str(is_prime(10)))
print("5 is even: " + str(is_even(5)))
print("10 is even: " + str(is_even(10)))
print("5 is odd: " + str(is_odd(5)))
print("10 is odd: " + str(is_odd(10)))
print("10 - 5 = " + str(subtract(10, 5)))
print("10 * 5 = " + str(multipliy(10, 5)))
print("10 / 5 = " + str(divide(10, 5)))
print("Circle of Numbers for n = 10 and firstNumber = 2: " + str(circle_of_numbers(10, 2)))
print("Perimeter of rectangle with side length 10 and 8: " + str(perimeter_of_rectangle(10, 8)))
print("Area of rectangle with side length 10 and 8: " + str(area_of_rectangle(10, 8)))
print("Area of circle with radius 5: " + str(area_of_circle(radius=5)))
print("Area of circle with diameter 20: " + str(area_of_circle(diameter=20)))
print("Area of square with side 10: " + str(area_of_square(10)))
print("Perimeter of square with side 10: " + str(perimeter_of_square(10)))
print("Circumference of circle with radius 5: " + str(circumference(radius=5)))
print("Circumference of circle with diameter 7: " + str(circumference(diameter=7)))
print("Hypotenuse for right triangle legs 3 and 4: " + str(pythagorean_theorem(3, 4)))
print("Law of cosines for a, b = 10 and C = 25: " + str(law_of_cosines_normal(10, 10, 25)))
print("Calculating C with law of cosines when a = 5, b = 4, and c = 6: " + str(law_of_cosines_gamma(5, 4, 6)))
# print("423th fibonacci number: " + str(fib(423)))
print("-----")
print("String tests")
print("Check if 'civic' is a palindrome: " + str(check_palindrome("civic")))
print("Check if 'hello' is a palindrome: " + str(check_palindrome("hello")))
print("'Hello world' reversed: " + reverse("Hello world"))
print("Most common character in string 'Hello World': " + find_most_common_character("Hello World"))
cipher = "qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM0987654321"
print("Encrypt 'Hello world 45' with cipher '" + cipher + "': " + encrypt("Hello world 45", cipher))
print("Decrypt 'Itssg vgksr 76' with cipher '" + cipher + "': " + decrypt("Itssg vgksr 76", cipher))
