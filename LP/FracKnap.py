def fracknap(value,wgt,capacity):
    index=list(range(len(value)))
    ratio=[v/w for v,w in zip(value,wgt)]
    index.sort(key=lambda i:ratio[i],reverse=True)

    max_value=0
    fractions=[0]*len(value)
    for i in index :
        if wgt[i]<=capacity:
            fractions[i]=1
            max_value+=value[i]
            capacity-=wgt[i]
        else :
            fractions[i]=capacity/wgt[i]
            max_value+=value[i]*capacity/wgt[i]
            break
    return max_value,fractions

n=int(input('Enter no. of items : '))
value=input('Enter the values of the {} item(s) in order : '.format(n)).split()
value = [int(v) for v in value ]
weight=input('Enter the positive weights of the {} item(s) in order : '.format(n)).split()
weight = [int(w) for w in weight ]
capacity=int(input('Enter maximum weight : '))

max_value,fractions = fracknap(value,weight,capacity)
print('The maximum value of items that can be carried : ',max_value)
print('The fraction in which the items should be taken : ',fractions)
Structure for an item which stores weight and
corresponding value of Item
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


# Main greedy function to solve problem
def fractionalKnapsack(W, arr):
    # Sorting Item on basis of ratio
    arr.sort(key=lambda x: (x.value / x.weight), reverse=True)

    # Result(value in Knapsack)
    finalvalue = 0.0

    # Looping through all Items
    for item in arr:

        # If adding Item won't overflow,
        # add it completely
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value

        # If we can't add current Item,
        # add fractional part of it
        else:
            finalvalue += item.value * W / item.weight
            break

    # Returning final value
    return finalvalue


# Driver Code
if __name__ == "__main__":
    W = int(input("weight: "))
    arr = [Item(60, 20), Item(100, 40), Item(120, 50)]

    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(max_val)
