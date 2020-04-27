myUniqueList = []
myLeftovers = []

def addToList(thing):
    if thing in myUniqueList:
        addToLeftovers(thing)
        return False
    else:
        myUniqueList.append(thing)
        return True

def addToLeftovers(thing):
  myLeftovers.append(thing)

# Test the addToList function
print(myUniqueList) # []
print(addToList("dog")) # Returns True
print(myUniqueList) # ['dog']
print(myLeftovers) # []
# Adding the element that already exists
print(addToList("dog")) # Returns False
print(myUniqueList) # ['dog']
print(myLeftovers) # ['dog']
# Adding a new element
print(addToList("cat")) # Returns True
print(myUniqueList) # ['dog', 'cat']
print(myLeftovers) # ['dog']