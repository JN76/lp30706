def knap(W,wt,val,n):
    K=[[0 for x in range(W+1)]for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0 :
                K[i][w] =0 
            elif wt[i-1]<=w:
                K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
            else:
                K[i][w]=K[i-1][w]
    return K[n][W]

n=int(input('Enter no. of items : '))
value=input('Enter the values of the {} item(s) in order : '.format(n)).split()
value = [int(v) for v in value ]
weight=input('Enter the positive weights of the {} item(s) in order : '.format(n)).split()
weight = [int(w) for w in weight ]
capacity=int(input('Enter maximum weight : '))

max_value= knap(capacity,weight,value,n)
print('The maximum value of items that can be carried : ',max_value)
