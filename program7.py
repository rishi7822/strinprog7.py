#program to print uncommon words in the given strings

def UncommonW(A, B):
    #split function
    A = A.split()
    B = B.split()
    
    #empty string
    x = []
    #for loop #if # append
    for i in A:
        if i not in B:
            x.append(i)
    #for loop #if # append
    for i in B:
        if i not in A:
            x.append(i)
    #set() function

    x = list(set(x))
    return x

#strings A and B
A = "Jhalak Dikhla Jaa"
B = "Jhalak dikhla jaa ek bar aa jaa "

#print
print(UncommonW(A, B))
    