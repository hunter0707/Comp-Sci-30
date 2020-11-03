max = 0
min = 0

while max <= min or min <= 0: #max cannot be less then or equal to min and min cannot be 0 or less
    h = input("enter maximum height and minimum height separated by a space: ").split()
    max = float(h[0]) #converts first number to float
    min = float(h[1]) #converts 2nd to float

def bounceBall(max,min):
    n = 0
    while max > min:
        n += 1 #bounces
        max = max * (2/3) #max multiplied by 2/3
        print('Bounce ' + str(n) + ': ' + str(max)) #prints which bounce its on
    return(str(n) + ' bounces.') #returns number of bounces

print(bounceBall(max,min)) 