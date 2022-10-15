
# tuple1 = (10,20,30)

# del tuple1

# print(tuple1)

# unpack a tuple
# in python, we can extract the values into diff varibales. This is unpacking

# numbers = (10,20,30) #packing

# (num1, num2, num3) = numbers # num of variables should match number of items in tuple

# print(num1)
# print(num2)
# print(num3)

numbers = (100,220,330,440,550,660,770,880,990) #packing

# (num1, num2, *num3) = numbers # num of variables should match number of items in tuple

(num1, *num2, num3) = numbers # num of variables should match number of items in tuple

print(num1)
print(num2)
print(num3) #rest of the values are stored in a list

# Loop Through Tuples

# for loop

myTuple = ('kivies', 'banana', 'mangoes')
# for x in myTuple:
#     print(x)

# looping through index numbers

# for i in range(len(myTuple)):
#     print(myTuple[i])


# Joining tuples

tuple1 = (60,70,80,90)
tuple2 = (50,40,30,20,10)

tuple3 = tuple1 + tuple2

# print(tuple3)

# multiplcation of tuples

myTuple = ["kivies", "mangoes", "banana"]

multipliedTuple = myTuple * 3

print(multipliedTuple)






# Sets

# It is also used to store multiple items in a single variable
# here we use curly brackets to denote a set
# Sets are unordered, unindexed, unchangeable and can only store unique values i.e. no duplicates allowed
# Still we can add and remove new items
# It can have multiple data types

# mySet = {10,20,30,40}

# mySet = {10,20,30,40, 10,20}

# print(len(mySet))

# mySet = {'aksdnjk', 40, 'hello', True, 50, False}

# print(mySet)

mySet = set((110,220,330,440))

print(mySet)



# Access the items in a set

# We cannot use index or a key to access items as they are unordered

# we can loop through that if the value is present or not
# we can use in keyword to check if the item is present or not



# mySet = {10,20,30,30}

# for x in mySet:
#     print(x)

# print(200 in mySet)



# Once the set is created, we cannot change the items but we can definitely add the items 


# mySet = {'John', 'peter', 'Aj'}

# mySet.add(10)
# mySet.add('abc')

# print(mySet)

# Add items from one set to another
# update() can take any iterable object

set1 = {110,220,330,440}
# set2 = {550,660}
list1 = [550,660]

# set1.update(set2)
set1.update(list1)


print(set1)


# Remove Item

# mySet = {10,20,30}

# # mySet.remove(200)

# # mySet.discard(200)

# # x = mySet.pop()


# # print(x)

# del mySet

# print(mySet)

# # 

# mySet = {10,20,30}

# for i in mySet:
#     print(i)

# Join the sets

# set1 = {'a', 'b', 'c', 'c', 'b'}

# set2 = {10,20,30, 10,20}

# # set3 = set1.union(set2)

# set1.update(set2)

# print(set1)
# print(set2)



# x = {10,20,30,40,50}
# y = {40,50,60,70}
# x.intersection_update(y) #modifying the set x in this case

# print(x)

# z =  x.intersection(y)

# print(x)
# print(y)
# print(z)


x = {110,220,330,440,550}
y = {440,550,660,770}

# x.symmetric_difference_update(y)

# print(x) #modifying the x in this case
# print(y)

z = x.symmetric_difference(y)

print(x)
print(y)
print(z)
