#Integer Factorization Algorithms
import time
import math
from random import randint
from fractions import gcd

#Trial Division
def Trial(N):
    for i in range (2, int(n**0.5)+1):
        if (n%i)==0:
            return i

#Pollard's Rho Algorithm
#Credits to Geek to Geek
def PollardsRho(N):
    #If 2 divids N, then one of the factor is 2
    if N%2==0:
        return 2
    #Using the Birthday Paradox by picking random numbers
    #Pick random number for x and c. Take y equal to x and f(x) = x^2 + c
    x = randint(1, N-1)
    y = x
    c = randint(1, N-1)
    g = 1
    #While a divisor is not found
    while g==1:
        #Toroise Movement (x) from the Floy'd cycle
        x = ((x*x)%N+c)%N
        #Hare Movement (y) from the Floy'd cycle
        y = ((y*y)%N+c)%N
        y = ((y*y)%N+c)%N
        #Check gcd of |x-y| and n
        g = gcd(abs(x-y),N)
    #If gcd is 1 or n, repeat the process with another set of value
    if g==N:
        return PollardsRho(n)
    #Else the gcd is one of the factor
    return g

#Brent's improved vision of Pollard's Rho Algorithm
#Credits to Geek to Geek
def Brent(N):
   #If 2 divids N, then one of the factor is 2
   if N%2==0:
      return 2
   #Function use as the move/step is f(x) = x^2 + c
   #Pick random number for y and c, and step limited up to r
   y = randint(1, N-1)
   c = randint(1, N-1)
   m = randint(1, N-1)
   g = 1
   r = 1
   q = 1
   #While the cycle is not found
   while g==1:
      #Set the Toroise and the Hare at the start
      x = y
      #Start of the step count, and the start off of the Hare
      for i in range(r):
         y = ((y*y)%N+c)%N
      k = 0
      #While the step count is in range of the limit
      while (k<r and g==1):
         ys = y
         #If the Hare did not meet the Toroise
         for i in range(min(m,r-k)):
            #Move the Hare
            y = ((y*y)%N+c)%N
            q = q*(abs(x-y))%N
         #Check if Hare meet the Toroise
         g = gcd(q,N)
         #Increase the step count
         k = k + m
      #Move/teleport Toroise position to Hare's location
      #Reset the step counter, and increase the step limit
      r = r*2
   #If the Hare meet the Toroise
   if g==N:
      #Cycle is found
      while True:
         ys = ((ys*ys)%N+c)%N
         #Check the gcd with N
         g = gcd(abs(x-ys),N)
         #If is 1, then repeat the process for another set of value
         if g!=1 and g!=N:
            break
   #Else the gcd is one of the factor
   return g

#Fermat's factorization method
#N should be an odd interger
def Fermat(N):
    #Try various values of x, solving for y
    #Hope that x^2 - N = y^2. y2 is a square
    x = math.ceil(math.sqrt(N))
    y2 = x**2 - N
    #While y2 is not a perfect square, then add 1 to x and retry
    while int(y2**0.5)**2 != y2:
    	x += 1
    	y2 = x**2 - N
    #Else, x+y, x-y are the factors
    return int(x + y2**0.5), int(x - y2**0.5)

ans = "y"
while ans == "y":

    n = int(input("\nEnter a positive integer:"))
    M = input("Choose an factorization algorithm: (t)rial division, (p)ollard's Rho, (b)rent, (f)ermat")
    start = time.perf_counter()
    
    if M == "t":
        i = Trial(n)
    elif M == "p":
        i = PollardsRho(n)        
    elif M == "b":
        i = Brent(n)
    elif M == "f":
        i,j = Fermat(n)
    else :
        print("That is a valid option")

    print(i,"is a factor of",n)
    print(int(n/i),"is the other factor of",n)
    end = time.perf_counter()
    print ("Time taken: ",end - start, "seconds.")

    ans = input("Would you like to make another calculation? (y)es (n)o?")
        
