spam = 0
while spam < 5:
    print("hello world")
    spam = spam + 1
#-------------------------------------------------------------------------------
# name = ""
# while name != "your name":
#     print("please enter your name.")
#     name = input()
# print("thanks")
#-------------------------------------------------------------------------------
spam1 = 0
while spam1 < 5:
    spam1 = spam1 + 1
    if spam1 == 3:
        continue
    print("Spam1 is " + str(spam1))
#-------------------------------------------------------------------------------
print("")
print("My name is")
for i in range(5):
    print("Jimmy fives times "+ str(i))
#-------------------------------------------------------------------------------
total = 0
for num in range(101):
    total = total + num
print(total)

total = 0
for num in range(2, 5):
    total = total + num
print(total)

total = 0
for num in range(1, 10, 2):
    total = total + num
print(total)
#-------------------------------------------------------------------------------