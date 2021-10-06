# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
# if n % 3 == 0:
   #     return n / 3
   # else:
    #    return 0

    d = dict()
    for i in str(n):
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] +1
    return int((max(d, key = d.get)))

# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
    d = dict()
    for i in str(s):
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
        return (max(d, key=d.get))
    #count = 0
    #letter = ''
    #newLongest = ''
    #for i in range(len(s)):
        #if i < len(s)-1 and s[i] == s[i + 1]:
           #count += 1
            #letter = s[i]
    #return letter




# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
    if str(s.lower().replace(" ", "")) == str(s.lower().replace(" ", ""))[::-1]:
        return True
    else:
        return False
