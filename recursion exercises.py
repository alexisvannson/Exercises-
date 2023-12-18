# Write your code here :-)
"""1 Write a recursive algorithm to sum the numbers in a list.
• What is the base and the recursive cases?

2 Write an algorithm to check if a word is a palindrome. A word is a palindrome if it reads the same
both forwards and backwards. An example includes level.
• What is the base and the recursive cases?

3 Write a recursive algorithm that computes the sum of squares from 1 to n for any positive
number. For example, given the number 3 it returns 1^2 + 2^2 + 3^14."""

l = [1,5,8,12,2]
def sum_numbers(l):
    if len(l) == 1:
        return l[0]
    else:
        sum = l[0] + sum_numbers(l[1:])
        return sum

#print(sum_numbers(l))

def is_palindrome(word):
    if len(word) == 1:
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False
#print(is_palindrome("level"))

def sum_of_squares(n):
    if n == 1:
        return 1
    else:
        return n**2 + sum_of_squares(n-1)
#print(sum_of_squares(4))


def reverse(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])

#print(reverse("hello"))

def subsequence(s,t):
    if len(s) == 0:
        return True
    if len(t) == 0:
        return False
    else:
        if s[0] == t[0]:
            return subsequence(s[1:],t[1:])
        else:
            return subsequence(s,t[1:])
#print(subsequence("pin","programming"))


"""A man put a pair of rabbits in a place surrounded by a wall. How many pairs of rabbits will be
there in a year if the initial pair of rabbits (male and female) are newborn, and all rabbit pairs are
not fertile during their first month of life but thereafter give birth to one new male/female pair at
the end of every month?
• As a hint, set up an equation expressing the number of rabbits after n months in terms of the number
of rabbits in some previous months."""

def number_of_rabbits(n):
    if n <=2:
        return 1
    else:
        return 2 * number_of_rabbits(n-2) + (number_of_rabbits(n-1)- number_of_rabbits(n-2)) # or number_of_rabbits2(n-1) + number_of_rabbits2(n-2) like Fibonacci

#print(number_of_rabbits(9))

def suba(sub,string):
    if len(sub) == 0:
        return True
    elif len(sub)>len(string):
        return False
    else:
        if sub[0] == string[0]:
            return suba(sub[1:],string[1:])
        else:
            return suba(sub,string[1:])
            
print(suba("singe","springtime"))
    
