#on this file are the exercises from day1

def ex1(self): #Given an integer number, print its last digit
    a = 123456
    return a%10

def ex2(a):#Write a function that takes a number and prints its square
    return a*a
print(ex2(4))
def ex2_2(a):
    return a**2
print(ex2_2(4))
def ex3(b = ""): # Given a three-digit number. Find the sum of its digits.
    t = int(b[0]) + int(b[1]) + int(b[2])
    return t
print(ex3('159'))

def ex4(n):
    h = n // 60
    m = n % 60
    return (h, m)
print(ex4(80))