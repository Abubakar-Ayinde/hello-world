A = int(input("Input A: ")) 
B = int(input("Input B: ")) 
C = int(input("Input C: ")) 
 
if A  > B > C: 
    print([A, B, C])
elif A > C > B:
    print([A, C, B]) 
elif B > A > C: 
    print([B, A, C]) 
elif C > B > A: 
    print([C, B, A]) 
elif B > C > A:
    print([B, C, A]) 
elif C > A > B:
    print([C, A, B])

else:
    print("life is good")