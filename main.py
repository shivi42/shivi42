import random
name = input ("Hello, what's your name? \n")
number = random.randint(1,10)
print(number)
Guessed_number = int(input("Welcome," + name + " \nGuess a number in between 1 to 10.\n"))
if  Guessed_number > number :
    print("ohh " + name + " you need to think little low!")
if Guessed_number < number :
    print("ohh " + name + " you need to think high!")
if Guessed_number == number :
    print("Congo, " + name  + " you guessed right!")

confirmation = str(input("Want to try again Y/N"))
if confirmation == 'Y':
    import Test
if confirmation == 'N':
    print("No worries, " + name + " Good Luck!")
