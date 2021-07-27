# List == ['cat', 'dog', 'rat']
#list[0] will call the value cat

#list2 = [['cat', 'dog'], [1,2,3,4,5]]
#the above is a list within a list so when a index call presents as a 2d array (list2[1][4]), it is in this case actaully telling you that you need to go
# to the second list in list2 and then the 5th index in list2, so the output would be 5

## List == ['cat', 'bird', 'dog', 'rat']
#list[-1] would spit out the word rat
#list[-2] would spit out the word dog

#can also call a slice, list [1:2] which returns the value
# ['bird', 'dog'] as it took all the values from index 1 to 2 and returned them

#by leaving one side oif the slice blank, the computer will realize that the slice either starts or ends with the starting
# or ending value index depending on which is left out
# ex) list1[:2] starts from index 0 and goes to index 2

# del list[2] is the code to delte index 2

#in and not in operators used to search through list
# 'dog' in ['dog', 'cat', 'rat']
#this returns true bc it is in the list
# 'dog' in ['bird', 'cat', 'rat']
#returns false
#'dog' not in ['dog', 'cat', 'rat']
#returns false due to it being in the listr

#===========================================================================================================================================================


#list() funtion can list out items in a range
#ex list(range(4)) will lsit out [0,1,2,3]

#ex list(range(0, 100, 2)) means start at zero, go to 100, and skip every 2nd number, thereby listing the even numbers from zero to 100

# cat = ['fat','orange', 'loud']
#normally we do  this: size = cat[0], color = cat[1], etc
#but this will assign all the indexes in that order to the order of the list: size, color, noise = cat
#same thing works as: size, color, noise = 'skinny', 'black', 'quiet'


#===========================================================================================================================================================
#methods

#list =[ 'a','b','c','d','e']
#list.index('d') will return 3 since that is the index e is at

#append() and insert() methods will add a value to the end of a list or to insert a value at any index
#list.append('f')
#or
#list.insert(0, 'A') --> this means it will insert at index 0 the new value, or 'A'

#list.remove('b') will remove the value at any index, while the del operator will only remove by index

#list = [2,3,5,6,23,7,8,6]
#list.sort() will sort the numbers, and will also work with words or letters.
#spam.sort(reverse=True) --> will reverse the order

#===========================================================================================================================================================
#this is an example of a mutable list causing problems

def eggs(someParameter):
    someParameter.append("Hello")
spam = [1,2,3]
eggs(spam)
print(spam)
