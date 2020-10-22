#Easy Problems

#1
def factorial(n):
    if n == 1: #base case is 1
        return n
    else:
        return n * factorial(n-1) #multiplied by prior factorial

#print(factorial(int(input('number to be factorialed: '))))

#2
def bunnyears(n):
    if n == 0: #0 bunnies is zero ears
        return n
    else:
        return bunnyears(n-1) + 2 #2 for each bunny

#print(bunnyears(int(input('number of bunny ears: '))))

#3
def fibonacci(n):
    if n == 0 or n == 1:
        return n #0 and 1 are base cases
    else:
        return fibonacci(n-1) + fibonacci(n-2) #sum of prior 2

#print(fibonacci(int(input('nth term of fibonacci sequence: '))))

#6
def digsum(n):
    if n < 10:
        return n #less than 10 means the sum is the same
    else:
        return n%10 + digsum(int(n/10)) #removes last digit and adds each time

#print(digsum(int(input('sum of digits: '))))

#7
def countseven(n,c):
    if n < 7:
        return c #if n < 7, no 7s remain
    else:
        if n%10 == 7: #remainder i.e. last digit is 7
            c += 1
        return countseven(int(n/10),c) #see if is 7
    
#print(countseven(int(input('count 7s: ')),0))

#9
def exponent(a,b):
    if b == 0: #a^0 = 1
        return 1
    else:
        return a * exponent(a,b-1) #multiplied by previous exponent until b = 0 when a would be multiplied by 1

#print(exponent(int(input('base: ')),int(input('power: '))))

#10, modified for any letter
def countletter(x,n): #search for x in n, x must be letter
    if len(n) == 1: #last letter
        if x == n:
            return 1 #adds 1 to count
        else:
            return 0 #adds 0 to count
    elif n[:1] == x:
        return 1 + countletter(x,n[1:]) #matches, adds 1
    else:
        return countletter(x,n[1:]) #doesn't match, doesn't add 1

#print(countletter(input('count occurences of this letter: '),input('string: ')))

#11, modified for any string
def countstr(x,n): #search for x in n where x is a string
    if len(n) <= len(x):
        if x == n:
            return 1
        else:
            return 0
    elif n[:len(x)] == x: #removes len(x) letters and compares them
        return 1 + countstr(x,n[len(x):]) 
    else:
        return countstr(x,n[1:]) #removes 1 if doesn't match

#print(countstr(input('count occurences of this string: '), input('string: ')))

#12
def changepi(n,a):
    if len(n) < 2: #n is finished with
        return a
    elif n[:2] == 'pi': #removes first 2 letters if it's pi and adds 3.14 to new string
        a += '3.14'
        return changepi(n[2:],a) #runs again with 2 letters removed
    else:
        a += n[:1] #adds removed letter to a, to be returned later
        return changepi(n[1:],a) #runs again with 1 letter removed

#print(changepi(input('replace pi with 3.14: '),''))

#16
def countabc(n):
    if len(n) <= 3:
        if 'abc' == n or 'aba' == n: #base case is if n is abc or aba
            return 1
        else:
            return 0
    elif n[:3] == 'abc' or n[:3] == 'aba': #removes 3 letters and sees if they are abc or aba
        return 1 + countabc(n[3:])
    else:
        return countabc(n[1:]) #removes 1 if doesn't match

#print(countabc(input('count abc and aba: ')))

#18
def nestparen(n):
    print(n)
    if n == '()': #base case of ()
        return True
    elif n[:1] == '(' and n[-1:] == ')': #checks if first and last characters are ()
        return nestparen(n[1:-1]) #nestparen ran again with first and last character removed
    else:
        return False
        
#print(nestparen(input('see if parentheses are nested properly: ')))

#Hard Problems

#1
def groupsum(l,t): #if any of the recursive runs return true then true is returned
    if t == 0:
        return True #base case 1, if t is 0 then it can be summed to by any integers by simply not using them in the summation
    elif len(l) == 0 or t < 0:
        return False #base case 2, t of 0 is not reached and the list is emptied
    else:
        if groupsum(l[1:],t - l[0]): #subtracts first item from number list from target, first item of list is also removed in the recursive run
            return True #if it returns true it means that t = 0 and true is to be returned
        else:
            return groupsum(l[1:],t) #does not subtract but removed first item from list

#print(groupsum([2,4,8,3],11)) #parameters are list and target

#6
def splitlist(step,l,a,b):
    if step >= len(l):
        return a == b #if true, functions below will rerun in iteration one before the current with a lowered step
    if splitlist(step+1, l, a+l[step], b): #runs splitlist with these parameters where l[step] is added to a each time, when final depth of recursion is reached a False or True will be returned
        return True #returns True if True is returned
    elif splitlist(step+1, l, a, b+l[step]): #same as above but l[step] is added to b instead of a
        return True
    else:
        return False #False if both recursions return false
    
l = [1,2,3,4]
print(splitlist(0,l,0,0)) #step, list, sum of list a and sum of list - step, sum of list a and sum of list b all start at 0
