#collatz sequence
#Write a function named collatz() that has one parameter named number. If
#number is even, then collatz() should print number // 2 and return this value.
#If number is odd, then collatz() should print and return 3 * number + 1.
#Then write a program that lets the user type in an integer and that keeps
#calling collatz() on that number until the function returns the value 1.
#(Amazingly enough, this sequence actually works for any integer—sooner
#or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t
#sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)

def collatz(num):
    if num % 2 == 0:
        num = num // 2
        print(num)
        return num
    else:
        num = 3 * num + 1
        print(num)
        return num


print('enter number:')
try:
    number = int(input())
    num = collatz(number)
    while num != 1:
       num = collatz(num)
except ValueError:
    print('Input error: Must enter an integer')



