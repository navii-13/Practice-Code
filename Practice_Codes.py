#given an array of numbers, to order them depending to their color, in this case
#0 = red, 1 = white, 2 = green
def flag_sort(nums):
    colors = [0,1,2]
    count = [0,0,0]
    idx = 0
    for i in nums:
        if i == colors[0]:
            count[0] += 1
        if i == colors[1]:
            count[1] += 1
        if i == colors[2]:
            count[2] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            nums[idx] = colors[i]
            idx += 1
# radix sort^^^
# next code to reverse an array
def rev_array(nums):
    l = []
    for i in range(len(nums)):
        l.append(nums.pop())
    print(l)

def double_stuff(x):
    if x:
        return x * 2
    else:
        return 0

def decon(x):
    if len(x) == 1:
        print(x)
        return
    num = 0
    idx = 0
    s = ""
    while x[idx] != "[":
        num = int(x[idx])
        idx += 1
    idx += 1
    while x[idx] != "]":
        '''if int(x[idx]):
            decon(x[idx:])
        else:'''
        s += x[idx]
        idx += 1
    idx += 1
    for i in range(num):
        print(s, end= "")
    if idx == len(x):
        return
    else:
        decon(x[idx:])
#given an array, to count all even numbers.
def countEvens(x):
    if len(x) == 0:
        return 0
    if abs(x[0]) % 2 == 0:
        return 1 + countEvens(x[1:])
    else:
        return countEvens(x[1:])
#given a int variable, to find out if it is a palindrome(be able to read the same way in reverse).
def palindrome(x):
    s = str(x)
    for i in range(len(s)):
        if len(s) == 0:
            return True
        if len(s) == 1:
            return True
        elif s[0] == s[-1]:
            s = s[1:-1]
    return False
def palindrome_2(x):
    s = str(x)
    c = 0
    l = x
    while l > 0:
        l = l //10**x
        c += 1
    print(c)

def fizzbuzz(num):
    for i in range(1,num+1):
        if i % 5 == 0 and i % 3 == 0:
            print(str(i) + ":FizzBuzz")
        elif i % 5 == 0:
            print(str(i) + ":Buzz")
        elif i % 3 == 0:
            print(str(i) +":Fizz")
        else:
            print(i)

def steps(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    return steps(n - 2) + steps(n - 1)

def a_string(string):
    count = 0
    for i in range(len(string)):
        if string[i] == 'a' or string[i] == 'A':
            count += 1
    return count


def a_stringrec(string,k):
    if len(string) == k:
        return 0
    if string[k] == 'a' or string[k] == 'A':
        return 1 + a_stringrec(string, k+1)
    return a_stringrec(string, k+1)





#
#
#Below are the testing of the problems/methods
#
#

#print(double_stuff(3))
#decon("3[abc]4[ab]c")
#decon("2[3[a]b]")
#countEvens([-1,-2,0,1,2])
palindrome_2(75657)

