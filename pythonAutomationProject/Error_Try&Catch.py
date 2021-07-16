


def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: you tried to divide by 0")

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

#-------------------------------------------------------------------------------

print(" How many ctas you got?")
numCats = input()
try:
    if int(numCats) >= 4:
        print("That's a lot of cats")
    else:
        print("That's not a lot of cats")
except ValueError:
    print("You did not enter a numerical number.")