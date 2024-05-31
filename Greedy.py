class Food:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.calories = weight

    def get_value(self):
        return self.value
    
    def get_cost(self):
        return self.calories
    
    def density(self):
        return self.get_value()/self.get_cost()
    
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ': <' + str(self.calories) + '>' 
    
# function to BuildMenu
def buildMenu(names, values, calories):
        """names, values, claories lists of the same length.
           name a list of strings
           values and calories lists of numbers
           returns list of foods"""
        menu = []
        for i in range(len(values)):
            menu.append(Food(names[i], values[i], calories[i]))
        return menu
        
def greedy(items, maxCost, keyFunction):
            """Assumes items in a list, maxCost >= 0, 
                keyFunction map elements of items to numbers"""
            itemsCopy = sorted(items, key = keyFunction, reverse = True)
            result = []
            totalValue, totalCost = 0.0, 0.0

            for i in range(len(itemsCopy)):
                if(totalCost+itemsCopy[i].get_cost() <= maxCost):
                    result.append(itemsCopy[i])
                    totalCost += itemsCopy[i].get_cost()
                    totalValue += itemsCopy[i].get_value()

            return(result, totalValue)

# using greedy
def testGreedy(items, constraint, keyFunction):
        taken, val = greedy(items, constraint, keyFunction)
        print('Total value of items taken =', val)
        for item in taken:
            print('  ', item)

def testGreedys(foods, maxUnits):
        print('Use greedy ba value to allocate', maxUnits, 'calories')
        testGreedy(foods, maxUnits, Food.get_value)
        print('\nUse greedy by cost to allocate', maxUnits, 'calories')
        testGreedy(foods, maxUnits,
                   lambda x: 1/Food.get_cost(x))
        print('\nUse greedy by density to allocate', maxUnits, 'calories')
        testGreedy(foods, maxUnits, Food.density)
names =["wine","beer","pizza","fries","burger","soda","apple","cake"]
values = [89,90,95,150,90,78,54,20]
calories = [124,368,256,345,365,150,90,200]
foods = buildMenu(names, values, calories)
testGreedys(foods, 800)