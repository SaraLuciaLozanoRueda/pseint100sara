A=int(input("NUMERO A:  "))
B=int(input("NUMERO B:  "))

if A<B:
    n =A + 1
    for n in range (A+1,B):
        print(n)
elif B< A:
    n=B+1
    for n in range (B-1,A):
        print(n)
        
                

