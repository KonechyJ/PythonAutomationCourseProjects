#Regular Expression ----- Long version example
#
# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False #not a phone number size
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False #no area code
#         if text[3] != '-':
#             return False # missing dash
#         for i in range(4, 7):
#             if not text[i].isdecimal():
#                 return False #missing first three digits
#         if text[7] != "-":
#             return False #missing second dash
#         for i in range(8, 12):
#             if not text[i].isdecimal():
#                 return False #missing last 4 digits
#         return True
#
# print(isPhoneNumber("415-516-6516"))
#
# print(isPhoneNumber("415-516-656"))
#
# print(isPhoneNumber("phone number"))
#
# message = "Call me at 415-516-6516 today or tomorrow."
# foundNumber = False
# for i in range(len(message)):
#     chunk = message[i:i + 12]
#     if isPhoneNumber(chunk):
#         print("phone number found!")
#         foundNumber = True
#     if not foundNumber:
#         print("no phone numbers.")
#=======================================================================================
#Regular Expression ----- Short version example
#
# import re
#
# message = "Call me at 415-516-6516 today or tomorrow. Again my number is 415-516-6516"
# phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# mo = phoneNumRegex.search(message)
# print(mo.group())
#
# print(phoneNumRegex.findall(message))

#=======================================================================================
#Regular Expression ----- groups and pipes

# import re
#
# phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")
# mo = phoneNumRegex.search("My number is 324-235-2352")
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group(3))
#
# phoneNumRegex = re.compile(r"\(\d\d\d\)-\d\d\d-\d\d\d\d")
# mo = phoneNumRegex.search("My number is (324)-255-2352")
# print(mo.group())
#
# #pipes
# batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
# mo = batRegex.search("Batmobile vs the batcopter")
# print(mo.group())
# print(mo.group(1))

#=======================================================================================
#Regular Expression ----- Repetition in Regex Patterns and Greedy/Nongreedy

# import re
# #? --> can be either or of the combo; ie batman or batwoman
# batRegex = re.compile(r"Bat(wo)?man")
# mo = batRegex.search(("The adventures of Batman"))
# print(mo.group())
# mo2 = batRegex.search(("The adventures of Batwoman"))
# print(mo2.group())
#
# phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
# mo3 = phoneRegex.search("My phone number is 555-1234. Call me tomorrow.")
# print(mo3.group())
# #* --> () item can appear as many times as it wants; ie batwowowowowowoman is fair but so it batwoman
# batRegex = re.compile(r"Bat(wo)*man")
# mo4 = batRegex.search(("The adventures of Batwowowowowowoman"))
# print(mo4.group())
#
# # + --> () must appear atleast once; ie batwowowowowowoman is fair but so it batwoman
# batRegex = re.compile(r"Bat(wo)+man")
# mo5 = batRegex.search(("The adventures of Batwowoman"))
# print(mo5.group())
#
# regex = re.compile(r"\+\*\?")
# print(regex.search("I learned about +*? regex syntax"))
#
# regex = re.compile(r"(\+\*\?)+")
# print(regex.search("I learned about +*?+*?+*?+*?+*?+*? regex syntax"))
#
# haRegex = re.compile(r"(Ha){3}")
# print(haRegex.search("He said HaHaHa"))
#
# phoneRegex2 = re.compile(r"((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}") #0r  re.compile(r"((\d\d\d-)?\d\d\d-\d\d\d\d(,)?) ((\d\d\d-)?\d\d\d-\d\d\d\d(,)?) ((\d\d\d-)?\d\d\d-\d\d\d\d(,)?)")
# print(phoneRegex2.search("My numbers are 423-234-6345,523-265-8755,223-455-4355"))
#
# haRegex2 = re.compile(r"(Ha){3,5}") # leaving the comma and five blank will leave the string unbounded or limitless
# print(haRegex2.search("He said HaHaHa"))
# print(haRegex2.search("He said HaHaHaHaHa"))
# print(haRegex2.search("He said Ha"))
#
# digitRegex = re.compile(r"(\d){3,5}") # ---> greedy match as it goes to the largest cap of 5
# print(digitRegex.search("1234567890"))
#
# digitRegex = re.compile(r"(\d){3,5}?") # ---> non greedy match as it goes to the smallest cap of 3
# print(digitRegex.search("1234567890"))

#=======================================================================================
#Regular Expression ----- Regex Character Classes and the findall() Method

import re
#findall returns a list of all compatiable matches while search returns the first match
phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
phones = "324-423-2424, 534-534-7866, 854-264-7457"
print(phoneRegex.findall(phones))

phoneRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
phones = "324-423-2424, 534-534-7866, 854-264-7457"
print(phoneRegex.findall(phones))

vowelRegex = re.compile(r"[aeiouAEIOU]")
print(vowelRegex.findall("Its the end of the world as we know it."))
#{} will speicify how long you want the string to continue to qualify
vowelRegex = re.compile(r"[aeiouAEIOU]{2}")
print(vowelRegex.findall("Go do that voodoo that you do so well."))

# ^ carret will return opposite
vowelRegex = re.compile(r"[^aeiouAEIOU]")
print(vowelRegex.findall("Go do that voodoo that you do so well."))


#comnent