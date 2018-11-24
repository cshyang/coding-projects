
'''
Shyang = {
    'Apple': 5
    'Banana': 10}

Mo = {
    'Banana': 2
    'Avocado': 3
    'JunkFood': 10
}
Ann = {
    'Apple': 1
    'Salad': 3  
    'Chicken Rice': 4
}

Peggy = {
    'Coffee': 4
}
'''
Shyang = {
    'Apple': 5,
    'Banana': 10}

people = {'Shyang': {'Apple': 5, 'Banana': 10},
          'Mo': {'Banana': 2, 'Avocado': 3, 'JunkFood': 10},
          'Ann': {'Apple': 1, 'Salad': 3, 'Chicken Rice': 4},
          'Peggy': {'Coffee': 4}
          }

# take in dictionary, print out items in dictionary
# for each item in dictionary, print out name of item and value in dictionary
def printFruits(x):
    for k,v in x.items():
        print(v,k)

def fruitCounter(x):
    for k,v in x.items():
        print(k)
        printFruits(v)

# iterate over the dictionary get the unique food and store it into new foodList
# iterate over the dictionary, get value of the keys, look up keys in foodList and sum up the value

foodList = {}
def uniqueFood(x):
    for k,v in x.items():
        for i, j in v.items():
            if i not in foodList:
                foodList[i] = j
            else:
                foodList[i] += j
uniqueFood(people)
print(foodList)

'''
iterate acroos keys and find item name 'Apple'
Get the number for 'Apple'
Sum up 'Apple'
Print Sum

'''



