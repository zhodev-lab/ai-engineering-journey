# variables
cost = 10
txt_percenet = .25

# String formatting
word = "ABC"
print(f"{word}")
# Data Structures | Lists, dictionaries, sets, tuples | `01_data_structures.py` 

Lists = ['apple', 'banana', 'cherry']
tuple(Lists)
# use list() convert tuple back to list type
thisList = list(("apple", "banna", "cherry"))
# insert items
thisList.insert(2, "watermelon") # apple, banna, cherry, watermelon
thisList.append("Orange") # like JS push 

# extend
thisList = ["a", "b", "c"]
thisTuple = ('x', 'y') 
thisList.extend(thisTuple) # ['a', 'b', 'c', 'x', 'y']

# remove list item
thisList = ["a", "b", "c"]
thisList.remove('a')

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")  
thislist = ["apple", "cherry", "banana", "kiwi"]

#  remove specified index 
thislist = ['a', 'b', 'c']
thislist.pop(1)
# ['a', 'c']

del thislist[0]
#['c']
del thislist  # whole thislist will removed 

# clear() will remove all the items
thislist = ['a', 'b', 'c']
thislist.clear()
# thislist -> [];


dictionaries 