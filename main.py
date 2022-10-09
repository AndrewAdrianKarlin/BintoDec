allowed = "01"
while True:
    myNumber = str(input('What is your binary number?'))
    if not len(myNumber) <= 8:
        print("please keep your entry 8 digits or less")
        continue
    if not all(dig in allowed for dig in myNumber):
        print("You input something other than 0 or 1. Please only input a binary number.")
        continue
    else:
        break

myElements = list(myNumber)
myElements = list(map(int, myElements))
myElements.reverse()
myNumber = 0
n = -1

for element in myElements:
    n = n+1
    myNumber = myNumber + element * 2 ** n

print(myNumber)
