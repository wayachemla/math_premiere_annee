#conversion du décimal au binaire:
a = int(input("Un nombre entier inférieur à 256"))
q1=a//2
r1=a%2
q2=q1//2
r2=q1%2
q3=q2//2
r3=q2%2
q4=q3//2
r4=q3%2
q5=q4//2
r5=q4%2
q6=q5//2
r6=q5%2
q7=q6//2
r7=q6%2
q8=q7//2
r8=q7%2

print(r8,r7,r6,r5,r4,r3,r2,r1)
