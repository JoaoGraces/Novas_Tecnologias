# input
A, B, C = map(float, input().split())

#  delta
delta = B**2 - 4*A*C

if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    # raízes
    raiz1 = (-B + (delta ** 0.5)) / (2*A)
    raiz2 = (-B - (delta ** 0.5)) / (2*A)
    
    # print
    print(f'R1 = {raiz1:.5f}')
    print(f'R2 = {raiz2:.5f}')
